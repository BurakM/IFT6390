from os import walk, path, getcwd, mkdir, makedirs
import dicom, dicom.UID
from dicom.dataset import Dataset, FileDataset
import datetime, time
import numpy as np
from skimage import img_as_ubyte
from scipy import misc

def load_images_in_folder(folder):

	file_list = []

	for files in folder:

		#From the folder, acquire the file(s) that will be tested.
		for dirpath, dirnames, filenames in walk(files): # Load the files in the path.
			for filename in filenames:
				if not ".ds_store" in filename.lower(): # Remove ds_store files form OSX.
					file_list.append(path.join(dirpath,filename)) # Uses the os package. 

	return file_list


# Function to import a patient in a 3D array, from a folder containing all of its slices.
def import_patient(folder):

	file_list_patient = load_images_in_folder(folder)

	# Read the first file to see the pixel size.
	ds_0 = dicom.read_file(file_list_patient[0])
	Nx, Ny = ds_0.pixel_array.shape

	# Create patient
	pat = np.zeros([Nx,Ny,len(file_list_patient)])
	ct = 0

	# Import each image.
	for files in file_list_patient:

		ds_temp = dicom.read_file(files)
		pat[:,:,ct] = ds_temp.pixel_array#*ds_temp.slope
		ct += 1

	# Return the image scaled as a 8 bit integer - required for textures.
	if np.dtype(ds_temp.pixel_array[0,0]) == 'uint8': # if already a uint, return this.
		out = pat
	else:
		out = misc.bytescale(pat)

	return out

def write_dicom_8bit(PIX_ARRAY,filename):
    """
    INPUTS:
    pixel_array: 2D numpy ndarray.  If pixel_array is larger than 2D, errors.
    filename: string name for the output file.
    """

    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = 'Secondary Capture Image Storage'
    file_meta.MediaStorageSOPInstanceUID = '999'
    file_meta.ImplementationClassUID = '999'
    ds = FileDataset(filename, {},file_meta = file_meta,preamble="\0"*128)
    ds.Modality = 'CT'
    ds.ContentDate = str(datetime.date.today()).replace('-','')
    ds.ContentTime = str(time.time()) #milliseconds since the epoch
    ds.StudyInstanceUID =  '999'
    ds.SeriesInstanceUID = '999'
    ds.SOPInstanceUID =    '999'
    ds.SOPClassUID = 'Secondary Capture Image Storage'
    ds.SecondaryCaptureDeviceManufctur = 'Python 2.7.3'

    ## These are the necessary imaging components of the FileDataset object.
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 0
    ds.HighBit = 7
    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.SmallestImagePixelValue = '\\x00\\x00'
    ds.LargestImagePixelValue = '\\xff\\xff'
    ds.Columns = PIX_ARRAY.shape[0]
    ds.Rows = PIX_ARRAY.shape[1]
    if PIX_ARRAY.dtype != np.uint8:
        PIX_ARRAY = PIX_ARRAY.astype(np.uint8)
    ds.PixelData = PIX_ARRAY #.tostring()
    ds.save_as(filename)
    return

def CreatePatientMask(PATIENT_NO,pat_Nsl):

	Npx = 512 # Assume images are all 512x512.

	# Make another test with already preallocated slices.
	mask_pat = np.zeros((Npx,Npx,pat_Nsl))
	base_path = getcwd()

	for ii in range(pat_Nsl):

		with open(base_path + '/Structures/Txt/' + PATIENT_NO + '/' + str(ii+1) + '.txt') as f:

			F = f.readlines() # Read each line. the first line will give 1 or 0 (file is empty or not).

			cpt = 0 # Set counter to zero.

			if int(F[0]) >0.5: # if you have something in the slice, then fill it with new values.

				for line in F:

					if cpt>1:

						splitted_line = line.split()
						mask_pat[:,cpt-2,ii] = [int(i) for i in (splitted_line[0][::2])]

					cpt += 1	

		dicom_file_folder = base_path + '/Structures/Dicom/' + PATIENT_NO + '/' 

		if not path.exists(dicom_file_folder):
			makedirs(dicom_file_folder)

		# make the number
		if len(str(ii+1))==1:
			numero = '00' + str(ii+1)
		elif len(str(ii+1))==2:
			numero = '0' + str(ii+1)
		else:
			numero = str(ii+1)

		filename_write_dicom = dicom_file_folder + PATIENT_NO + '_mask_' + numero + '.dcm'
		write_dicom_8bit(mask_pat[:,:,ii],filename_write_dicom)	


	return		