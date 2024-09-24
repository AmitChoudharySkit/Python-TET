import os

path = 'ecommerce_data'

obj = os.scandir(path)

print("Files and Directories in '% s':" % path)
for entry in obj :
	if entry.is_dir() or entry.is_file():
		print(entry.name)


obj.close()


