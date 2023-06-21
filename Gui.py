from tkinter import *
import customtkinter #tkinkter assister
from tkinter import messagebox
from customtkinter import CTkToplevel

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
        newwin.geometry('500x500+{:d}+{:d}'.format(
            newwin.winfo_screenwidth() // 2 - 250,
            newwin.winfo_screenheight() // 2 - 250
        ))
        newwin.config(bg="#242320")
        newwin.title("Waka-ama")
        newwin.resizable(0, 0)

        # Label
        wellabel = customtkinter.CTkLabel(newwin, text="Welcome to results", font=self.font2, text_color="#FFFFFF",
                                        width=100, height=100)
        wellabel.place(x=85, y=0)

        # File location entry
        file_label = customtkinter.CTkLabel(newwin, text="File Location:", font=self.font1, text_color="#FFFFFF")
        file_label.place(x=15, y=100)
        file_entry = customtkinter.CTkEntry(newwin, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                            border_color="#FFFFFF", text_color="#000000", width=200)
        file_entry.place(x=150, y=101.912831241924)

        # Keyword entry
        keyword_label = customtkinter.CTkLabel(newwin, text="Keyword:", font=self.font1, text_color="#FFFFFF")
        keyword_label.place(x=15, y=150)
        keyword_entry = customtkinter.CTkEntry(newwin, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                            border_color="#FFFFFF", text_color="#000000", width=200)
        keyword_entry.place(x=150, y=151.912831241924)

        # Year entry
        year_label = customtkinter.CTkLabel(newwin, text="Year:", font=self.font1, text_color="#FFFFFF")
        year_label.place(x=15, y=200)
        year_entry = customtkinter.CTkEntry(newwin, fg_color="#FFFFFF", bg_color="#000000", font=self.font1,
                                            border_color="#FFFFFF", text_color="#000000", width=200)
        year_entry.place(x=150, y=201.912831241924)

        # Start the new window
        newwin.mainloop()


app = apps()

