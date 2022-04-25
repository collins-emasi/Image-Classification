"""
Program to sort the training data into the following format


Species_1_folder
    |____image_1, image_2, image_3, ... image_N
Species_2_folder
    |____image_1, image_2, image_3, ..., image_N
    .
    .
    .
Species_K_folder
    |____image_1, image_2, image_3, ... image_N


"""
# Imports
import os
import pandas as pd
from shutil import copy2

# Paths
parent_folder = "/home/snow/Desktop/AI project/"
dsail_porini_folder = os.path.join(parent_folder, 'dataset')
data_folder = os.path.join(parent_folder, 'DATA')
annotation_file = os.path.join(parent_folder, 'camera_trap_dataset_annotation.xlsx')

# Dataframe
df = pd.read_excel(annotation_file)
image_file_names = df["Filename"]
animal_classes = df['Species'].unique()

print("Creating Directories ", end='')
for animal_class in animal_classes:
    data_path = os.path.join(parent_folder, 'DATA', animal_class)
    os.makedirs(data_path)
    print(".", end='')
print(" Successful")

print("Copying files", end='')
for index, image_file_name in enumerate(image_file_names):
    animal_class = df['Species'][index]
    source = os.path.join(dsail_porini_folder, image_file_name)
    destination = os.path.join(data_folder, animal_class)

    if os.path.isfile(source):
        copy2(source, destination)
        print(".", end='')
print("Copied all files")
print("Check ", data_folder)
