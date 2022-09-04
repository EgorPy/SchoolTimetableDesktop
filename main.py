__author__ = "Egor Mironov @ved3v"

"""

This is a School Timetable Desktop Project.

It allows users to create and edit school timetables.

Date of creation: 04.08.22

"""

import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.filedialog
import tkinter.font
import ctypes
import pickle
import locale
from ctypes import windll


class App:
    def askFileToSave(self):
        pass

    def askExit(self):
        # TODO: Complete this function
        self.exitProgram()
        # if self.changesMade:
        #     answer = tkinter.messagebox.askyesnocancel("Save changes", "Save changes?")
        #     if answer == True:
        #         self.askFileToSave()
        #     elif answer == False:
        #         self.exitProgram()
        # else:
        #     self.exitProgram()

    def exitProgram(self):
        # update first launch variable
        self.FIRST_LAUNCH = False

        # save first launch variable
        with open("savedData/firstLaunch.dat", "wb") as file:
            pickle.dump(self.FIRST_LAUNCH, file)

        self.root.destroy()

    def saveTimetable(self):
        pass

    def openTimetable(self):
        pass

    def openRecentTimetable(self):
        pass

    def createTimetable(self):
        pass

    def initMainPage(self):
        # menu

        # create menu
        self.mainMenu = tkinter.Menu(self.root)

        # config root to use menu
        self.root.config(menu=self.mainMenu)

        # add File button to menu
        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=False)
        self.mainMenu.add_cascade(label="File", menu=self.fileMenu)

        self.fileMenu.add_command(label="New", command=self.createTimetable, activebackground=self.sectionBackgroundColor)
        self.fileMenu.add_command(label="Open Recent", command=self.openRecentTimetable, activebackground=self.sectionBackgroundColor)
        self.fileMenu.add_command(label="Open...", command=self.openTimetable, activebackground=self.sectionBackgroundColor)
        self.fileMenu.add_command(label="Save", command=self.saveTimetable, activebackground=self.sectionBackgroundColor)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exitProgram, activebackground=self.sectionBackgroundColor)

        # TODO: add Edit button to menu

        # welcome page
        # TODO: add welcome page

        self.welcomePageFrame = tkinter.Frame(self.root, background=self.mainColor)
        self.mainPageTitleLabel = tkinter.Label(self.welcomePageFrame, text="School Timetable Desktop", background=self.mainColor, font=self.titleFont)
        self.welcomePageLabel = tkinter.Label(self.welcomePageFrame, text="Welcome Page", background=self.mainColor, font=self.subtitleFont)

        self.timetablesFrame = tkinter.Frame(self.welcomePageFrame, background=self.mainColor)
        self.mainPageStartLabel = tkinter.Label(self.timetablesFrame, text="Start", background=self.mainColor, font=self.bigFont)
        self.createTimetableButton = tkinter.Button(self.timetablesFrame, text="New Timetable...", background=self.mainColor, activebackground=self.mainColor,
                                                    foreground=self.buttonColor, activeforeground=self.buttonColor, font=self.mainFont, cursor="hand2", relief="flat", borderwidth=0)
        self.openTimetableButton = tkinter.Button(self.timetablesFrame, text="Open Timetable...", background=self.mainColor, activebackground=self.mainColor,
                                                  foreground=self.buttonColor, activeforeground=self.buttonColor, font=self.mainFont, cursor="hand2", relief="flat", borderwidth=0)

    def packMainPage(self):
        self.welcomePageFrame.pack(anchor="nw", padx=100, pady=100)
        self.mainPageTitleLabel.pack(anchor="nw")
        self.welcomePageLabel.pack(anchor="nw")

        self.timetablesFrame.pack(anchor="nw", pady=50)
        self.mainPageStartLabel.pack(anchor="nw")
        self.createTimetableButton.pack(anchor="nw")
        self.openTimetableButton.pack(anchor="nw")

    def unpackCreateNewTimetablePage(self):
        pass

    def initCreateNewTimetablePage(self):
        pass

    def packCreateNewTimetablePage(self):
        pass

    def unpackCreateNewTimetablePage(self):
        pass

    def initSettingsPage(self):
        pass

    def packSettingsPage(self):
        pass

    def unpackSettingsPage(self):
        pass

    def initGuidePage(self):
        pass

    def packGuidePage(self):
        pass

    def unpackGuidePage(self):
        pass

    def mainPage(self):
        self.PAGE = "main"

        self.initMainPage()
        self.packMainPage()

    def config(self):
        # general

        # load first launch variable
        try:
            with open("savedData/firstLaunch.dat", "rb") as file:
                self.FIRST_LAUNCH = pickle.load(file)
        except FileNotFoundError:
            self.FIRST_LAUNCH = True

        # colors
        self.mainColor = "#FFFFFF"

        self.titleColor = "#3F51B5"
        self.backgroundColor = "#A5E3FF"
        self.sectionBackgroundColor = "#03A9F4"
        self.buttonColor = "#2196F3"
        self.textInputColor = "#000000"
        self.textHintColor = "#555555"

        self.timetableTitleColor = "#555555"
        self.timetableSubjectColumnColor = "#EEEEEE"
        self.timetableClassroomColumnColor = "#FFFFFF"

        # fonts
        self.bigFont = tkinter.font.Font(family="Segoe UI", size=self.WIDTH // 70)
        self.mainFont = tkinter.font.Font(family="Segoe UI", size=self.WIDTH // 100)
        self.titleFont = tkinter.font.Font(family="Segoe UI", size=self.WIDTH // 40)
        self.subtitleFont = tkinter.font.Font(family="Segoe UI", size=self.WIDTH // 60)

        # images
        self.createTimetableImage = tkinter.PhotoImage(file="images/createTimetable.png")

    def rootConfig(self):
        self.WIDTH = self.root.winfo_screenwidth()
        self.HEIGHT = self.root.winfo_screenheight()
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.state("zoomed")
        self.root.resizable(False, True)
        # this line of code needed to get rid of blurred fonts (see https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp)
        windll.shcore.SetProcessDpiAwareness(1)

    def __init__(self):
        self.root = tkinter.Tk()

        self.root.title("School Timetable Desktop")

        self.rootConfig()

        self.config()

        self.root.config(bg=self.mainColor)

        """
        
        Page names:
        
        main
        create timetable
        settings
        guide
        
        """

        # get OS language
        windll = ctypes.windll.kernel32
        self.LANGUAGE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # format: en_US

        self.mainPage()

        # root events

        # handling close event
        self.root.protocol("WM_DELETE_WINDOW", self.askExit)

        self.root.mainloop()


if __name__ == "__main__":
    app = App()
