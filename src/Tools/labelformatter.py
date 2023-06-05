import glob

directory_path = '../../data/local/roboflow/Chess Pieces.v24-416x416_aug.yolov8/'
txt_files = glob.glob(directory_path + '**/*.txt', recursive=True)

# source - target
new_indexes = [(0, 10), (1, 4), (2, 8), (3, 2), (4, 11), (5, 5), (6, 7), (7, 1), (8, 12), (9, 6), (10, 9), (11, 3)]

for file_path in txt_files:
	if "README" in file_path:
		continue

	txt_buffer = ""
	with open(file_path, 'r') as file:
		for line in file.readlines():
			values = line.split()
		
			if len(values) >= 1:
				for i1, i2 in new_indexes:
					if values[0] == str(i2):
						values[0] = str(i1)
						break
					
			txt_buffer += ' '.join(values) + '\n'
    
	with open(file_path, 'w') as file:
		file.write(txt_buffer)

	print("Modified contents of " + file_path)