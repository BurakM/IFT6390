# coding=utf-8
#!/Users/Mikael/anaconda/bin/anaconda

from os import walk, path, fork, getcwd, mkdir # Load files (I'm using os.walk)

def load_images_in_folder(folder):

	file_list = []

	for files in folder:

		#From the folder, acquire the file(s) that will be tested.
		for dirpath, dirnames, filenames in walk(files): # Load the files in the path.
			for filename in filenames:
				if not ".ds_store" in filename.lower(): # Remove ds_store files form OSX.
					file_list.append(path.join(dirpath,filename)) # Uses the os package. 

	return file_list