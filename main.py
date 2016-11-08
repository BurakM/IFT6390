import dicom
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import skimage
import scipy
from os import walk, path, fork, getcwd, mkdir
from Utilities import DCM # Import utilities.

# Create empty lists that will contain the path for all patient images.
base_path = getcwd() 
DicomFiles_Pat1 = list()
DicomFiles_Pat2 = list()
DicomFiles_Pat3 = list()

# I'm using my own local path as we're not gonna upload the images on github. 
MikaelPath = "/Users/Mikael/Dropbox/PhD/Classes/IFT6390/Data_Project/" # This is my base path.

DicomFiles_Pat1.append(MikaelPath + "patient1_images_anon")
DicomFiles_Pat2.append(MikaelPath + "patient2_images_anon")
DicomFiles_Pat3.append(MikaelPath + "patient3_images_anon")

# Load 3D volume for all patients.
pat1 = DCM.import_patient(DicomFiles_Pat1)
pat2 = DCM.import_patient(DicomFiles_Pat2)
pat3 = DCM.import_patient(DicomFiles_Pat3)

# Display one slice of each patient.
sl = 250
fig, ax = plt.subplots(2, 2)
ax[0,0].set_title("Patient 1, slice " + str(sl))
ax[0,0].imshow(pat1[:,:,sl], cmap=plt.cm.bone)
ax[0,1].set_title("Patient 2, slice " + str(sl))
ax[0,1].imshow(pat2[:,:,sl], cmap=plt.cm.bone)
ax[1,0].set_title("Patient 3, slice " + str(sl))
ax[1,0].imshow(pat3[:,:,sl], cmap=plt.cm.bone)
plt.show()

# Code continues here
# and here.