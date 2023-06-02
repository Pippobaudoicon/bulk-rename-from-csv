import os
import glob
import csv

verses = []
folder_path = 'C:/Users/hontr/Downloads/bulk dailyverse/bulk dailyverse'

def sort_key(filepath):
    # Extract the number from the filepath
    filename = os.path.basename(filepath)
    number = int(filename.replace('.mp4', ''))
    return number

with open('daily-verses.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Skip the first row
    for row in reader:
        parts = row[-1]
        verse = parts.replace(':','-')
        verses.append(verse)


# print(verses)

for i, old_path in enumerate(sorted(glob.glob(os.path.join(folder_path, '*.mp4')), key=sort_key)):
    new_path = os.path.join(folder_path, verses[i]+'.mp4')
    j = 1
    while os.path.exists(new_path):
        new_name = f'{verses[i]} ({j}).mp4'
        new_path = os.path.join(folder_path, new_name)
        j += 1
    os.rename(old_path, new_path)



