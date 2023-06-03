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



for race in races:
    lines = race.split('\n')

    for line in lines[1:]:
        line = line.split(',')
        filter_line = ','.join(filter(None, line))
        print(filter_line)
        
class info:
    def __init__(self, line):
        entries = line.split(',')
        self.lane = entries[0]
        self.uID = entries[1]
        self.place = entries[2]
        self.name = entries[3]
        self.club = entries[4]
        self.timetaken = entries[5]

for race in races:
    lines = race.split('\n')

    for line in lines[1:]:
        line = line.split(',')
        filter_line = ','.join(filter(None, line))
        print(filter_line)

        race_info = info(filter_line)
        print(f"Lane: {race_info.lane}")
        print(f"uID: {race_info.uID}")
        print(f"place: {race_info.place}")
        print(f"name: {race_info.name}")
        print(f"club: {race_info.club}")
        print(f"timetaken: {race_info.timetaken}")


# Print the contents of each file
# for file_content in file_contents: 
    # print(file_content) 

