from os import walk, path, fork, getcwd, mkdir # Load files (I'm using os.walk)
import dicom
import numpy as np

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
		pat[:,:,ct] = ds_temp.pixel_array
		ct += 1


	return pat		


