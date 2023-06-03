import os

year = '2018'
racetype = "Final"
races = []


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    except OSError:
        print(f"Oops! Something went wrong with file: {file_path}")
        return None

def find_folder(year, race, folder_path):
    abs_path = os.path.abspath(folder_path)
    
    for root, dirs, files in os.walk(abs_path):
        for dir in dirs:
            if year in dir:
                dir_path = os.path.join(abs_path, dir)
                find_files(race, dir_path) 

def find_files(race, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if race in file:               
                file_path = os.path.join(folder_path, file)
                races.append(read_file(file_path))
            
find_folder(year, racetype, "resources")       


        
def createlane(line):
    entries = line.split(',')
    lane = entries[2]
    uID = entries[3]
    place = entries[4]
    name = entries[5]
    club = entries[6]
    timetaken = entries[7]

    for race in races:
        lines = race.split('\n')

    for line in lines[1:]:
        createlane(line)
        






# Print the contents of each file
# for file_content in file_contents: 
    # print(file_content) 

