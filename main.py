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


class App:
    def initMainPage(self):
        pass

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
        self.mainStyle = tkinter.ttk.Style()
        self.mainStyle.theme_use("vista")
        self.mainStyle.configure("TButton", padding=0, background=self.mainColor, width=100)

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

        """
        
        Page names:
        
        main
        create new timetable
        settings
        guide
        
        """

        self.mainPage()

        self.root.mainloop()


if __name__ == "__main__":
    app = App()
