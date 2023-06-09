import os
import csv


#items to search for items change if want diffent outcomes
year = '2018'
racetype = "Final"
races = []

# Function to read the contents of a file

def read_file(file_path):
    encodings = ['utf-8','latin-1'] # File containing these encoding
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                file_content = file.read()
            return file_content
        except UnicodeDecodeError:
            continue
    
    print(f"Oops! Something went wrong with file: {file_path}")
    return None

# Function to read the contents of a file (year)

def find_folder(year, race, folder_path):
    abs_path = os.path.abspath(folder_path)
    
    # Walk through the directory tree

    for root, dirs, files in os.walk(abs_path):
        for dir in dirs:
            if year in dir:
                dir_path = os.path.join(abs_path, dir)
                find_files(race, dir_path) 

# Function to find files with the given keyword in a folder

def find_files(race, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if race in file:               
                file_path = os.path.join(folder_path, file)
                races.append(read_file(file_path))

# Call the find_folder function to search for files          

find_folder(year, racetype, "resources") 

# Create a function to calculate the points of the races
# If the place is 1, they get 8 points. If they are 2nd, they get 7 points. Points decrease by one until 7th place.
# Any place below 7th will earn 1 point.

def assign_points(place):
    if place == 1:
        return 8 
    elif place == 2:
        return 7
    elif place == 3:
        return 6
    elif place == 4:
        return 5
    elif place == 5:
        return 4
    elif place == 6:
        return 3
    elif place == 7:
        return 2
    else:
        return 1

# Class to hold information about a race entry      

class Info:
    def __init__(self, line):
        entries = [entry.strip() for entry in line.split(',')]

        if len(entries) < 10:
            self.broken = entries
            self.valid = False
            return
        
        self.place = entries[0]
        self.club = entries[4]
        self.points = assign_points(int(self.place))
        self.valid = True

# List to hold the infomation about the race

inlist = []

# Runs the race data

for race in races:
    lines = race.split('\n')

    for line in lines[1:]: # Misses the first line
        line = line.split(',')
        filter_line = ','.join(filter(None, line)) # These 3 lines limits the commas it can have in the data
        race_info = Info(filter_line)

        # If the data is broken as in there is less than 10 it tells us which data is broken
        
        if not race_info.valid:
            # print(f'gone {race_info.broken}') 
            continue
        inlist.append(race_info)

# Create a dictionary to store club names and their total points


# for race_info in inlist:
#     print(race_info.club, race_info.place)  #test

# Create a dictionary to store club names and their total points

club_points = {}

# Loop over the races and process the data

for race in races:
    lines = race.split('\n')
    for line in lines[1:]:
        line = line.split(',')
        filter_line = ','.join(filter(None, line))
        race_info = Info(filter_line)

        # If the data is broken, skip it
        if not race_info.valid:
            continue

        # Check if the club already exists in the dictionary
        if race_info.club in club_points:
            # If it exists, add the points to the existing value
            club_points[race_info.club] += race_info.points
        else:
            # If it doesn't exist, create a new entry in the dictionary
            club_points[race_info.club] = race_info.points

# Print club names and total points
# for club, points in club_points.items():
#     print(f"{club}: {points} points")

# Function to download the results into csv file

def dlcsv():

    # Sorts the data in decending order

    sorted_data = sorted(club_points.items(), key=lambda x: x[1], reverse=True)

    # Write the sorted data into a CSV file 
    with open('finalresult.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for club,points in sorted_data:
            writer.writerow([f'{club}: {points} Points'])

dlcsv()
