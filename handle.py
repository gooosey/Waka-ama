import os

# Can be edited to change the year and racetype of the races 

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

# Function to read the contents of a file

def find_folder(year, race, folder_path):
    abs_path = os.path.abspath(folder_path)
    
    # Walk through the directory tree

    for root, dirs, files in os.walk(abs_path):
        for dir in dirs:
            if year in dir:
                dir_path = os.path.join(abs_path, dir)
                find_files(race, dir_path) 

# Function to find files with the given race type in a folder

def find_files(race, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if race in file:               
                file_path = os.path.join(folder_path, file)
                races.append(read_file(file_path))

# Call the find_folder function to search for files          

find_folder(year, racetype, "resources")      

# Limits the commas to one instead of many 

for race in races:
    lines = race.split('\n')

    for line in lines[1:]:
        line = line.split(',')
        filter_line = ','.join(filter(None, line))
        print(filter_line)
    
# Class to hold information about a race entry      

class Info:
    def __init__(self, line):
        entries = [entry.strip() for entry in line.split(',')]

        if len(entries) < 10:
            self.broken = entries
            self.valid = False
            return

        self.lane = entries[0]
        self.uID = entries[1]
        self.place = entries[2]
        self.name = entries[3]
        self.club = entries[4]
        self.timetaken = entries[5]
        self.pgain = entries[6]
        self.timetaken2 = entries[7]
        self.pgain2 = entries[8]
        self.pgain3 = entries[9]

for race in races:
    lines = race.split('\n')

for line in lines[1:]:
    line = line.split(',')
    filter_line = ','.join(filter(None, line))
    print(filter_line)

    race_info = Info(filter_line)
    print(f"Lane: {race_info.lane}")
    print(f"uID: {race_info.uID}")
    print(f"place: {race_info.place}")
    print(f"name: {race_info.name}")
    print(f"club: {race_info.club}")
    print(f"timetaken: {race_info.timetaken}")
    print(f"point gain: {race_info.pgain}")
    print(f"timetaken2: {race_info.timetaken2}")
    print(f"point gain: {race_info.pgain2}")
    print(f"point gain: {race_info.pgain3}")


# print club and place 

for race_info in inlist:
    print(race_info.club, race_info.place)

