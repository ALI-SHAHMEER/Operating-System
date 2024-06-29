import os
import subprocess
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QStackedWidget


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("welcome.ui",self)
        self.file_management.clicked.connect(self.goto_file_management)
        self.file_modification.clicked.connect(self.goto_file_modification)
        self.application.clicked.connect(self.goto_application)
        self.process_management.clicked.connect(self.goto_process_management)
        self.power_management.clicked.connect(self.goto_power_management)

    def goto_file_management(self):
        file_management = File_management()
        stacked_widget.addWidget(file_management)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def goto_file_modification(self):
        file_modification = File_modification()
        stacked_widget.addWidget(file_modification)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def goto_application(self):
        application = Application()
        stacked_widget.addWidget(application)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def goto_process_management(self):
        process_management = Process_management()
        stacked_widget.addWidget(process_management)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def goto_power_management(self):
        power_management = Power_management()
        stacked_widget.addWidget(power_management)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)
import subprocess



class Power_management(QDialog):
    def __init__(self):
        super(Power_management,self).__init__()
        loadUi("power_management.ui",self)
        self.lock.clicked.connect(self.run_lock)
        self.reboot.clicked.connect(self.run_reboot)
        self.exit.clicked.connect(self.close_application)
    def run_lock(self):
        # Path to your bash script (replace with the actual path)
        bash_script_path = "/home/wolf/OS_Project/lock.sh"
        # Option 1: Using subprocess.run() for flexibility
        subprocess.run([bash_script_path])
        # os.system("xlock")
    def run_reboot(self):
        os.system("xlock")
    def close_application(self):
        QApplication.instance().quit()


class Process_management(QDialog):
    def __init__(self):
        super(Process_management,self).__init__()
        loadUi("process_management.ui",self)
        self.lspci.clicked.connect(self.run_lspci)
        self.df.clicked.connect(self.run_df)
        self.lsblk.clicked.connect(self.run_lsblk)
        self.free.clicked.connect(self.run_free)
    def run_lspci(self):
        os.system("lspci")
    def run_df(self):
        pass
    def run_lsblk(self):
        os.system("lsblk -l")
    def run_free(self):
        os.system("free")

class Application(QDialog):
    def __init__(self):
        super(Application,self).__init__()
        loadUi("application.ui",self)
        self.firefox.clicked.connect(self.run_firefox)
        self.vlc.clicked.connect(self.run_vlc)
        self.exit.clicked.connect(self.close_application)

    def run_firefox(self):
        url = "https://www.google.com"
        subprocess.run(["xdg-open", url])
        # subprocess.call(['sh','./fire.sh'])
        # os.popen("sh","./fire.sh")
    def run_vlc(self):
        subprocess.run(["xdg-open","1.mp4"])
        # os.popen("sh" ,"./vlc.sh")
    def close_application(self):
        QApplication.instance().quit()


class File_modification(QDialog):
    def __init__(self):
        super(File_modification,self).__init__()
        loadUi("file_modification.ui",self)
        self.change.clicked.connect(self.change_mode)
        self.exit.clicked.connect(self.close_application)
    def close_application(self):
        QApplication.instance().quit()

    def change_mode(self):
        name = self.name_field.text()
        mode = self.mode_field.text()
        permission = 0
        if mode == "r" or mode == "R":
            permission = 0o644
        elif mode == "w" or mode == "W":
            permission = 0o642
        elif mode == "x" or mode == "X":
            permission = 0o641
        if os.path.exists(name):
            os.chmod(name,permission)
            self.result.setText("File Mode Change Successfuly!")
        else:
            self.result.setText("File not Found")


class File_management(QDialog):
    def __init__(self):
        super(File_management,self).__init__()
        loadUi("file_management.ui",self)
        self.folder.clicked.connect(self.goto_folder)
        self.file.clicked.connect(self.goto_file)

    def goto_folder(self):
        add = Folder()
        stacked_widget.addWidget(add)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def goto_file(self):
        add = File()
        stacked_widget.addWidget(add)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

class Folder(QDialog):
    def __init__(self):
        super(Folder,self).__init__()
        loadUi("folder.ui",self)
        self.exit.clicked.connect(self.close_application)
        self.generate.clicked.connect(self.create_folder)
    
    def create_folder(self):
        name = self.name_field.text()
        if os.path.exists(name):
            self.result.setText("Folder Already Exist")
        else:
            os.mkdir(name)
            self.result.setText("Folder Created!")

    def close_application(self):
        QApplication.instance().quit()


class File(QDialog):
    def __init__(self):
        super(File,self).__init__()
        loadUi("file.ui",self)
        self.exit.clicked.connect(self.close_application)
        self.generate.clicked.connect(self.create_file)
    
    def create_file(self):
        name = self.name_field.text()
        if os.path.exists(name):
            self.result.setText("File Already Exist")
        else:
            with open(name, "w") as file:
                file.write("File created successfully")
            self.result.setText("File Created Successfuly!")
            file.close()
    def close_application(self):
        QApplication.instance().quit()





app = QApplication(sys.argv)
welcome = WelcomeScreen()
stacked_widget = QStackedWidget()
stacked_widget.addWidget(welcome)
stacked_widget.setFixedHeight(800)
stacked_widget.setFixedWidth(1200)
stacked_widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")