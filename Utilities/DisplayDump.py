# SOME DUMMY CODE ON HOW TO DISPLAY IMAGES. JUST COPY PASTE THIS IN _MAIN.ipynb.

# Display if you want.
dpi = 100 # Arbitrary. The number of pixels in the image will always be identical
height, width = np.array(texture_maps[:,:,sl[0],0].shape, dtype=float) / dpi
imfr = 0.031

SLSLSL = 1

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],0], interpolation='none', vmin=0,vmax=2000)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[0])
plt.show()
fig.savefig('lung_pat3sl203_CONTRAST1286.tif', dpi=dpi,bbox_inches='tight')

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],1], interpolation='none', vmin=0,vmax=50)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[1])
plt.show()
fig.savefig('lung_pat3sl203_DISSIMILARITY1286.tif', dpi=dpi,bbox_inches='tight')

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],2], interpolation='none', vmin=0,vmax=0.6)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[2])
plt.show()
fig.savefig('lung_pat3sl203_HOMOGENEITY1286.tif', dpi=dpi,bbox_inches='tight')

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],3], interpolation='none', vmin=0,vmax=0.05)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[3])
plt.show()
fig.savefig('lung_pat3sl203_ASM1286.tif', dpi=dpi,bbox_inches='tight')

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],4], interpolation='none', vmin=0,vmax=.3)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[4])
plt.show()
fig.savefig('lung_pat3sl203_ENERGY1286.tif', dpi=dpi,bbox_inches='tight')

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],5], interpolation='none', vmin=-.5,vmax=.5)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[5])
plt.show()
fig.savefig('lung_pat3sl203_CORRELATION1286.tif', dpi=dpi,bbox_inches='tight')

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],6], interpolation='none', vmin=-1,vmax=5)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[6])
plt.show()
fig.savefig('lung_pat3sl203_KURTOSIS1286.tif', dpi=dpi,bbox_inches='tight')

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],7], interpolation='none', vmin=0,vmax=3.5)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[7])
plt.show()
fig.savefig('lung_pat3sl203_SKEWNESS1286.tif', dpi=dpi,bbox_inches='tight')

fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
im = ax.imshow(texture_maps[80:280,150:450,sl[SLSLSL],8], interpolation='none', vmin=0,vmax=1000)
fig.colorbar(im,fraction=imfr, pad=0.04)
plt.title(TEXTURES[8])
plt.show()
fig.savefig('lung_pat3sl203_VARIANCE1286.tif', dpi=dpi,bbox_inches='tight')


#SLICE = 203
# Print figures to .tiff format.
#dpi = 200 # Arbitrary. The number of pixels in the image will always be identical
#data = pat1[:,:,SLICE]
#height, width = np.array(data.shape, dtype=float) / dpi
#fig = plt.figure(figsize=(width, height), dpi=dpi)
#ax = fig.add_axes([0, 0, 1, 1])
#ax.axis('off')
#ax.imshow(data, interpolation='none',cmap=plt.cm.bone)
#fig.savefig('lung_masked_pat3sl203.tif', dpi=dpi)

#fig = plt.figure(figsize=(width, height), dpi=dpi)
#ax = fig.add_axes([0, 0, 1, 1])
#ax.axis('off')
#ax.imshow(pat1_mask[:,:,SLICE], interpolation='none',cmap=plt.cm.bone)
#fig.savefig('lung_classes_pat3sl203.tif', dpi=dpi)





    
