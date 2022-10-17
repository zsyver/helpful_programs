import os
import glob
import shutil

source = 'DESKTOP_DIRECTORY'
destination = 'DESTINATION_DIRECTORY'
#
# Move the files with the specified file type
allfiles = glob.glob(os.path.join(source, '*.png'), recursive=True)
print("Files to move", allfiles)

# Moves every file and prints in terminal exactly what was moved
for file_path in allfiles:
	dst_path = os.path.join(destination, os.path.basename(file_path))
	shutil.move(file_path, dst_path)
	print(f"Moved {file_path} -> {dst_path}")