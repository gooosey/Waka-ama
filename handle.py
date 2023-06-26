import os
import csv
from tkinter import *
import customtkinter #tkinkter assister
from tkinter import messagebox
from customtkinter import CTkToplevel



#items to search for items change if want diffent outcomes
year = "2017"
racetype = "Final"
races = []

# Function to read the contents of a file

def read_file(file_path):
    encodings = ['utf-8', 'latin-1', 'utf-16']  # File containing these encodings
    placeholder = "'"  # Placeholder character to replace invalid characters
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding, errors='replace') as file:
                file_content = file.read()
            return file_content.replace('\ufffd', placeholder)
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
                print(file_path)

# Call the find_folder function to search for files          


find_folder(year, racetype, "resources") 


# Create a function to calculate the points of the races
# If the place is 1, they get 8 points. If they are 2nd, they get 7 points. Points decrease by one until 7th place.
# Any place below 7th will earn 1 point.

def assign_points(place):
    points = [0, 8, 7, 6, 5, 4, 3, 2]
    return points[place] if place < len(points) else 1

# Class to hold information about a race entry      

class Info:
    def __init__(self, line):
        entries = [entry.strip() for entry in line.split(',')] #Skips the disqualification data

        if len(entries) < 10: #Only happnes if there is less than 10 entries 
            self.broken = entries
            self.valid = False
            return
        
        self.place = entries[0] if entries[0] else '0'
        self.club = entries[4]
        self.points = assign_points(int(self.place))
        self.valid = True

# List to hold the infomation about the race

inlist = []

# Runs the race data

for race in races:
    lines = race.split('\n')

    for line in lines[1:]:
        entries = [entry.strip() for entry in line.split(',')]
        filter_line = ','.join(filter(None, entries))
        race_info = Info(line)
        #Appeds the data
        inlist.append(race_info)

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

# dlcsv() 

class apps:
    def __init__(self):

        # Window information

        self.root = customtkinter.CTk()
        self.root.title("login")
        self.root.geometry("350x200")
        self.root.config(bg='#242320')
        self.root.eval('tk::PlaceWindow . center')

        # Fonts
        self.font1 = ('Arial', 15, 'bold')
        self.font2 = ('Helvetica', 35, 'bold')

        # Username and password

        self.username = 'J'
        self.password = 'K'

        # Trials
        self.trials = 0

        # Creating the label for username and password

        self.userlabel = customtkinter.CTkLabel(self.root, text="Username:", font=self.font1, text_color="#FFFFFF")
        self.userlabel.place(x=15, y=25)

        self.passlabel = customtkinter.CTkLabel(self.root, text="Password:", font=self.font1, text_color="#FFFFFF")
        self.passlabel.place(x=15, y=75)

        # Creating a text box for username and password

        self.userentry = customtkinter.CTkEntry(self.root, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                                border_color="#FFFFFF", text_color="#000000", width=200)
        self.userentry.place(x=100, y=26.912831241924)

        self.passentry = customtkinter.CTkEntry(self.root, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                                border_color="#FFFFFF", text_color="#000000", width=200)
        self.passentry.place(x=100, y=76.912831241924)

        # Login Button

        self.loginbu = customtkinter.CTkButton(self.root, text="Login", font=self.font1, text_color="#FFFFFF",
                                               fg_color="#07b527", hover_color="#07b527", command=self.login)
        self.loginbu.place(x=110, y=132.5)

        self.root.mainloop()

    def login(self):
        written_user = self.userentry.get()
        written_pass = self.passentry.get()

        if written_user == '' or written_pass == '':
            messagebox.showwarning(title="Error", message="Enter username and password")
        elif written_user == self.username and written_pass == self.password:
            self.mainwin()
        elif (written_user != self.username or written_pass != self.password) and self.trials < 3:
            messagebox.showwarning(title="Error", message="Invalid username or password")
            self.trials += 1
        else:
            self.loginbu.destroy()  # Destroy the login button
            triallabel = customtkinter.CTkLabel(self.root, text="Too many failed attempts", font=self.font1,text_color="#FFFFFF")
            triallabel.place(x=80, y=132.5)

    def mainwin(self):

        # General information about the window

        newwin = CTkToplevel(self.root)
        newwin.geometry("{0}x{1}+0+0".format(newwin.winfo_screenwidth(), newwin.winfo_screenheight()))
        newwin.config(bg="#242320")
        newwin.title("Waka-ama")
        newwin.resizable(0,0)

        # Label

        wellabel = customtkinter.CTkLabel(newwin, text="Welcome to results", font=self.font2 ,text_color="#FFFFFF", width=100, height=100)
        wellabel.place(x=700, y=80)

        # Start the new window

        newwin.mainloop()


app = apps()