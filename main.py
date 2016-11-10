import dicom
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from skimage import feature, data
import scipy
from os import walk, path, fork, getcwd, mkdir, makedirs
from Utilities import DCM,Maths # Import utilities.


# We now have up to 3 patients. Specify mask 'a', 'b' or '' if there are multiple contours.
PATIENT = 1
MASK = 'a'
sl = 173 # Example slice to display and calculate textures for now.

## Create 3D maps of the masks - uncomment if you have not created the dicom files.
# Example :DCM.CreatePatientMask('P1a',368) # 368

## Create lists with paths for each patients.
base_path = getcwd() 
DicomFiles_Pat1 = list() 
DicomFiles_Pat1_Mask = list()

# I'm using my own local path as we're not gonna upload the images on github - everyone should change this to their own local path.
MikaelPath = "/Users/Mikael/Dropbox/PhD/Classes/IFT6390/Data_Project/" # This is my base path.

DicomFiles_Pat1.append(MikaelPath + "patient" + str(PATIENT) +"_images_anon")# Create full path of patient.
DicomFiles_Pat1_Mask.append(base_path + '/Structures/Dicom/' + 'P' + str(PATIENT) + MASK)# Create full path of patient mask.

# # Load 3D volume with CT data.
pat1 = DCM.import_patient(DicomFiles_Pat1)

# Load 3D volume mask.
pat1_mask = DCM.import_patient(DicomFiles_Pat1_Mask)
# Get the mask                : pat1_mask>0
# Get the fibrosis voxels     : pat1_mask==2
# Get the non-fibrosis voxels : pat1_mask==1

# Display example slice.
fig, ax = plt.subplots(2, 2)
ax[0,0].set_title("Patient 1, slice " + str(sl))
ax[0,0].imshow(pat1[:,:,sl], cmap=plt.cm.bone)
ax[0,1].imshow(pat1_mask[:,:,sl], cmap=plt.cm.bone)
ax[1,0].imshow(np.multiply(pat1[:,:,sl],pat1_mask[:,:,sl]), cmap=plt.cm.bone)
plt.show()

########################################################################
# 					TEXTURE ANALYSIS
########################################################################
print "Texture analysis..."
# Calculate the texture of 1 slice.
# based on http://scikit-image.org/docs/dev/auto_examples/plot_glcm.html

# # Say we test centered at the following locations : should be generalized
# # to ALL pixels of interest. Also for now fixed at one slice.

lung_patches = [] # This will include a neighborhood of each lung location.

# Define the neighborhood of each location : for now, a square region of size PATCH_SIZE around the voxel.
PATCH_SIZE = 5 # We could test a circular region or whatever...

# Identify the couples (y,x) in the slice where we have lung :
AllPerm = np.argwhere(pat1_mask[:,:,sl]>0)

lung_locations = AllPerm.tolist()
#locations are [(y,x)]. y are the lines in the image, and x are the rows.

for loc in lung_locations:
 	lung_patches.append(pat1[loc[0]-PATCH_SIZE:loc[0]+PATCH_SIZE,loc[1]-PATCH_SIZE:loc[1]+PATCH_SIZE,sl])

# Calculate some GLCM properties for each patch.
diss = []
corr = []
ASM = []
energy = []
k = 0
for patch in lung_patches:
 	# Other choices : 
 	# 'contrast','dissimilarity','homogeneity','ASM','energy','correlation'
 	glcm = feature.greycomatrix(patch.astype(np.uint8), [5], [0], 256, symmetric=True, normed=True)
 	diss.append(feature.greycoprops(glcm,'dissimilarity')[0,0])
 	corr.append(feature.greycoprops(glcm,'correlation')[0,0])
 	energy.append(feature.greycoprops(glcm,'energy')[0,0])
 	ASM.append(feature.greycoprops(glcm,'ASM')[0,0])
 	k += 1

dissimilarity_image = np.zeros([512,512])
correlation_image = np.zeros([512,512])
ASM_image = np.zeros([512,512])
energy_image = np.zeros([512,512])

cpt = 0
for loc in lung_locations:
 	dissimilarity_image[loc[0],loc[1]] = diss[cpt]
 	correlation_image[loc[0],loc[1]] = corr[cpt]
 	ASM_image[loc[0],loc[1]] = ASM[cpt]
 	energy_image[loc[0],loc[1]] = energy[cpt]
 	cpt += 1


fig, ax = plt.subplots(2, 2)
ax[0,0].set_title("Dissimilarity")
ax[0,0].imshow(dissimilarity_image, cmap=plt.cm.bone)
ax[0,1].set_title("Correlation")
ax[0,1].imshow(correlation_image, cmap=plt.cm.bone)
ax[1,0].set_title("Energy")
ax[1,0].imshow(energy_image, cmap=plt.cm.bone)
ax[1,1].set_title("ASM")
ax[1,1].imshow(ASM_image, cmap=plt.cm.bone)

plt.show()





