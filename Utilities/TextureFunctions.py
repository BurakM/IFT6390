import dicom
import pylab
from matplotlib import pyplot as plt
import numpy as np
from skimage import feature, data, exposure
import scipy
from os import walk, path, getcwd, mkdir, makedirs

def GetTextureMaps(patient_mask,patient_image,sl,PATCH_SIZE,TEXTURES,N_GRAY_LEVELS):

    print "Creating textures..."
    lung_patches = [] # This will include a neighborhood of each lung location.

    # Identify the couples (y,x) in the slice where we have lung :
    AllPerm = np.argwhere(patient_mask[:,:,sl]>0)

    lung_locations = AllPerm.tolist()
    #locations are [(y,x)]. y are the lines in the image, and x are the rows.

    for loc in lung_locations:
        lung_patches.append(patient_image[loc[0]-PATCH_SIZE:loc[0]+PATCH_SIZE,loc[1]-PATCH_SIZE:loc[1]+PATCH_SIZE,sl[loc[2]]])

    glcm_textures_list = ['contrast','dissimilarity','homogeneity','ASM','energy','correlation']
    general_textures_list = ['kurtosis','skewness','variance']

    full_texture_list = list()

    for texture in TEXTURES:
      
        current_texture_list = list()
      
        if (texture in glcm_textures_list): # If you have a GLCM texture.
          
            k = 0
            for patch in lung_patches: # Loop over all pixel patches and get the texture.
                glcm = feature.greycomatrix(patch.astype(np.uint8), [5], [0], N_GRAY_LEVELS, symmetric=True, normed=True)
                current_texture_list.append(feature.greycoprops(glcm,texture)[0,0])
                k+=1
          
        if (texture in general_textures_list): # If you have a general texture.
          
            k = 0
            for patch in lung_patches: # Loop over all pixel patches and get the texture.
                patch_1d = np.ndarray.flatten(patch.astype(np.uint8))
          
                # Now, it's either variance, skewness or kurtosis.
                if texture == 'variance':
                    current_texture_list.append(np.var(patch_1d))
                elif texture == 'skewness':
                    current_texture_list.append(scipy.stats.skew(patch_1d))    
                elif texture == 'kurtosis':
                    current_texture_list.append(scipy.stats.kurtosis(patch_1d))
              
        # Append this to another list. We end up with a list of lists.
        full_texture_list.append(current_texture_list)
        print(str(texture) + ' done.')
      
    ####################################################################################
    # PRINT TEXTURES TO ARRAY
    ####################################################################################

    # Create an empty array that will store texture maps.
    texture_maps = np.zeros([patient_image.shape[0],patient_image.shape[1],patient_image.shape[2],len(TEXTURES)])

    for i in range(len(TEXTURES)): # For each texture, score the value in the correct location.
        cpt = 0
        for loc in lung_locations:
            texture_maps[loc[0],loc[1],sl[loc[2]],i] = full_texture_list[i][cpt]
            cpt += 1    
      
    print "Done." 

    return texture_maps