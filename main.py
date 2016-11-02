import dicom
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skimage
import scipy
from os import walk, path, fork, getcwd, mkdir
from Utilities import * # Import everything in the file IFT6390_Functions.

# Get base path and make a list of files that need to be treated.

base_path = getcwd() 
DicomFiles = list()

# Say you want to load all dicom images from these two folders : 

DicomFiles.append(base_path + "/Images/Example_Image") # Folder #1.
DicomFiles.append(base_path + "/Images/Example_Image2") # Folder #2.

# This will load all of the files : 
file_list = load_images_in_folder(DicomFiles)

# File list would hold ALL of the .dcm files that are in all folders listed in DicomFiles.

# These calls would give you the dicom information of each file, for example. 
ds = dicom.read_file(file_list[0]) # Here, reading first file
ds1 = dicom.read_file(file_list[1]) # Here, reading second file.

# Now, some examples of what is contained inside the "structure" ds : 

nbpix_row, nbpix_column = ds.pixel_array.shape # Nb of pixels.
row_spacing, column_spacing = ds.PixelSpacing # Px spacing in mm.
I = ds.pixel_array # Image itself.

fig, ax = plt.subplots(1, 1)
ax.set_title("whatever image")
ax.imshow(I, cmap=plt.cm.bone)
plt.show()
