from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter as ctk


class apps:
    def __init__(self):
        # Window information
        self.root = ctk.CTk()
        self.root.title("login")
        self.root.geometry("350x200")
        self.root.config(bg='#242320')
        # self.root.eval('tk::PlaceWindow . center')

        # Fonts
        self.font1 = ('Arial', 15, 'bold')
        self.font2 = ('Helvetica', 35, 'bold')

        # Username and password
        self.username = 'J'
        self.password = 'K'

        # Trials
        self.trials = 0

        # Creating the label for username and password
        self.userlabel = ctk.CTkLabel(self.root, text="Username:", font=self.font1, text_color="#FFFFFF")
        self.userlabel.place(x=15, y=25)

        self.passlabel = ctk.CTkLabel(self.root, text="Password:", font=self.font1, text_color="#FFFFFF")
        self.passlabel.place(x=15, y=75)

        # Creating a text box for username and password
        self.userentry = ctk.CTkEntry(self.root, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                      border_color="#FFFFFF", text_color="#000000", width=200)
        self.userentry.place(x=100, y=26)

        self.passentry = ctk.CTkEntry(self.root, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                      border_color="#FFFFFF", text_color="#000000", width=200)
        self.passentry.place(x=100, y=76)

        # Login Button
        self.loginbu = ctk.CTkButton(self.root, text="Login", font=self.font1, text_color="#FFFFFF",
                                     fg_color="#07b527", hover_color="#07b527", command=self.login)
        self.loginbu.place(x=110, y=132.5)

        self.root.mainloop()

        # Login logic

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
            triallabel = ctk.CTkLabel(self.root, text="Too many failed attempts", font=self.font1, text_color="#FFFFFF")
            triallabel.place(x=80, y=132.5)

    def mainwin(self):
        # General information about the window
        newwin = ctk.CTkToplevel(self.root)
        newwin.geometry('500x500+{:d}+{:d}'.format(
            newwin.winfo_screenwidth() // 2 - 250,
            newwin.winfo_screenheight() // 2 - 250
        ))
        newwin.config(bg="#242320")
        newwin.title("Waka-ama")
        newwin.resizable(0, 0)

        # Label
        wellabel = ctk.CTkLabel(newwin, text="Welcome to results", font=self.font2, text_color="#FFFFFF",
                                width=100, height=100)
        wellabel.place(x=85, y=0)

        def select_folder(entry):
            folder_path = filedialog.askdirectory()
            if folder_path:
                entry.delete(0, END)
                entry.insert(0, folder_path)

        # File location entry
        file_label = ctk.CTkLabel(newwin, text="Folder Location:", font=self.font1, text_color="#FFFFFF")
        file_label.place(x=15, y=100)
        file_entry = ctk.CTkEntry(newwin, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                  border_color="#FFFFFF", text_color="#000000", width=300)
        file_entry.place(x=150, y=101)

        # Select folder button
        select_button = ctk.CTkButton(newwin, text="Select Folder", font=self.font1, text_color="#FFFFFF",
                                      fg_color="#07b527", hover_color="#07b527",
                                      command=lambda: select_folder(file_entry))
        select_button.place(x=150, y=130)

        # Find keyword

        kword = ctk.CTkLabel(newwin, text="Enter Keyword:", font=self.font1, text_color="#FFFFFF")
        kword.place(x =15, y = 185)

        # User type

        kkword = ctk.CTkEntry(newwin, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                  border_color="#FFFFFF", text_color="#000000", width=200)
        kkword.place(x=150, y=185 )

        # Another Key word

        Yword = ctk.CTkLabel(newwin, text="Enter year:", font=self.font1, text_color="#FFFFFF")
        Yword.place(x =30, y = 260)

        # User type

        Ykword = ctk.CTkEntry(newwin, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                  border_color="#FFFFFF", text_color="#000000", width=200)
        Ykword.place(x = 150 , y = 260)

        # Give this into a variable 

        def giveinfo():

            keyword = kkword.get()
            year_input = Ykword.get()

            global year, racetype, filelocation

            year = year_input
            racetype = keyword
            filelocation = file_entry.get()

            print("Keyword:", racetype)
            print("Year:", year)
            print("File Location:", filelocation)

        # Download file (broken)

        submit_button = ctk.CTkButton(newwin, text="Submit", font=self.font1, text_color="#FFFFFF",
                                      fg_color="#07b527", hover_color="#07b527",
                                      command=giveinfo)
        submit_button.place(x=220, y=300)


        newwin.mainloop()


app = apps()
