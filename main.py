__author__ = "Egor Mironov @ved3v"

import locale

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

    def createNewTimetable(self):
        pass

    def initMainPage(self):
        # menu

        # create menu
        self.mainMenu = tkinter.Menu(self.root)

        # config root to use menu
        self.root.config(menu=self.mainMenu)

        # add File button to menu
        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=False, background=self.mainColor)
        self.mainMenu.add_cascade(label="File", menu=self.fileMenu)

        self.fileMenu.add_command(label="New", command=self.createNewTimetable, background=self.mainColor)
        self.fileMenu.add_command(label="Open Recent", command=self.openRecentTimetable, background=self.mainColor)
        self.fileMenu.add_command(label="Open...", command=self.openTimetable, background=self.mainColor)
        self.fileMenu.add_command(label="Save", command=self.saveTimetable, background=self.mainColor)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exitProgram, background=self.mainColor)

        # TODO: add Edit button to menu

        # welcome page
        # TODO: add welcome page

    def packMainPage(self):
        pass

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
        self.mainFont = tkinter.font.Font(family="Helvetica", size=self.WIDTH // 100, weight="bold")

        self.titleFont = tkinter.font.Font(family="Helvetica", size=self.WIDTH // 60, weight="bold")

        # styles
        # self.mainStyle = tkinter.ttk.Style()
        # print(self.mainStyle.theme_names())
        # self.mainStyle.theme_use("winnative")
        # self.mainStyle.configure("TButton", padding=0, background=self.mainColor, width=10)

    def rootConfig(self):
        self.WIDTH = self.root.winfo_screenwidth()
        self.HEIGHT = self.root.winfo_screenheight()
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.state("zoomed")
        self.root.resizable(False, True)

    def __init__(self):
        self.root = tkinter.Tk()

        self.root.title("School Timetable Desktop")

        self.rootConfig()

        self.config()

        self.root.config(bg=self.mainColor)

        """
        
        Page names:
        
        main
        create new timetable
        settings
        guide
        
        """

        # get OS language
        windll = ctypes.windll.kernel32
        self.LANGUAGE = locale.windows_locale[windll.GetUserDefaultUILanguage()] # format: en_US

        self.mainPage()

        # root events

        # handling close event
        self.root.protocol("WM_DELETE_WINDOW", self.askExit)

        self.root.mainloop()


if __name__ == "__main__":
    app = App()
