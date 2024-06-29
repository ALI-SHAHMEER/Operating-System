import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QStackedWidget
import mysql.connector

data = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="314287",
    database = "test"
)
cursor = data.cursor(buffered=True)
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("welcome.ui",self)
        self.admin.clicked.connect(self.goto_admin)
        self.instructor.clicked.connect(self.goto_instructor)
        self.student.clicked.connect(self.goto_student)

    def goto_admin(self):
        admin_login = Admin_Login()
        stacked_widget.addWidget(admin_login)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)


    def goto_instructor(self):
        instructor_login = Instructor_Login()
        stacked_widget.addWidget(instructor_login)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)


    def goto_student(self):
        student_login = Student_Login()
        stacked_widget.addWidget(student_login)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)


class Search_Screen(QDialog):
    def __init__(self):
        super(Search_Screen,self).__init__()
        loadUi("search.ui",self)
        self.exit.clicked.connect(self.close_application)
        self.add.clicked.connect(self.add_function)
        self.remove.clicked.connect(self.remove_function)
        self.update_data.clicked.connect(self.update_function)
        self.search.clicked.connect(self.serach_function)
    
    def close_application(self):
        QApplication.instance().quit()

    def add_function(self):
        add = Add_Screen()
        stacked_widget.addWidget(add)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def remove_function(self):
        remove = Remove_Screen()
        stacked_widget.addWidget(remove)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def update_function(self):
        update = Update_Screen()
        stacked_widget.addWidget(update)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def serach_function(self):
        id = self.id_field.text()
        if len(id) == 0:
            self.message.setText("Please input all field")
        else:
            query = f"SELECT * FROM student WHERE student_id ='{id}'"
            cursor.execute(query)
            result = cursor.fetchone()
            # result = cursor.execute(query)
            print(type(result))
            if result is None:
                self.message.setText("No Record Found")
            else:
                print("Student Record Found")
                self.message.setText("Student Record Found")
            
            


class Update_Screen(QDialog):
    def __init__(self):
        super(Update_Screen,self).__init__()
        loadUi("update.ui",self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.exit.clicked.connect(self.close_application)
        self.add.clicked.connect(self.add_function)
        self.remove.clicked.connect(self.remove_function)
        self.update_data.clicked.connect(self.update_function)
        self.search.clicked.connect(self.serach_function)
    
    def close_application(self):
        QApplication.instance().quit()

    def add_function(self):
        add = Add_Screen()
        stacked_widget.addWidget(add)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def remove_function(self):
        remove = Remove_Screen()
        stacked_widget.addWidget(remove)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def update_function(self):
        id = self.id_field.text()
        password = self.password_field.text()
        if len(id) == 0 and len(password) == 0:
            self.message.setText("Please input all field")
        else:
            query = f"SELECT * FROM student WHERE student_id ='{id}'"
            cursor.execute(query)
            result = cursor.fetchone()
            # result = cursor.execute(query)
            print(type(result))
            if result is None:
                self.message.setText("No Record Found")
            else:
                query_update = f"UPDATE student SET password = '{password}' WHERE student_id = '{id}'"
                cursor.execute(query_update)
                print("Record Update")
                self.message.setText("Record Update")

    def serach_function(self):
        search = Search_Screen()
        stacked_widget.addWidget(search)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)


class Remove_Screen(QDialog):
    def __init__(self):
        super(Remove_Screen,self).__init__()
        loadUi("remove.ui",self)
        self.exit.clicked.connect(self.close_application)
        self.add.clicked.connect(self.add_function)
        self.remove.clicked.connect(self.remove_function)
        self.update_data.clicked.connect(self.update_function)
        self.search.clicked.connect(self.serach_function)
    
    def close_application(self):
        QApplication.instance().quit()

    def add_function(self):
        add = Add_Screen()
        stacked_widget.addWidget(add)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def remove_function(self):
        id = self.id_field.text()
        query = f"DELETE FROM student WHERE student_id = '{id}'"
        cursor.execute(query)

        # Get the number of rows deleted (affected rows)
        deleted_rows = cursor.rowcount

        if deleted_rows > 0:
            print(f"Record with ID {id} deleted successfully!")
            self.message.setText("Record have been deleted")
        else:
            print(f"No record found with ID {id}.")
            self.message.setText("No Record Found")


    def update_function(self):
        update = Update_Screen()
        stacked_widget.addWidget(update)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def serach_function(self):
        search = Search_Screen()
        stacked_widget.addWidget(search)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

class Add_Screen(QDialog):
    def __init__(self):
        super(Add_Screen,self).__init__()
        loadUi("add.ui",self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.exit.clicked.connect(self.close_application)
        self.add.clicked.connect(self.add_function)
        self.remove.clicked.connect(self.remove_function)
        self.update_data.clicked.connect(self.update_function)
        self.search.clicked.connect(self.serach_function)
    
    def close_application(self):
        QApplication.instance().quit()

    def add_function(self):
        id = self.id_field.text()
        password = self.password_field.text()

        if len(id) == 0 or len(password) == 0:
            self.message.setText("Please input all field")
        else:
            query = f"INSERT INTO student(student_id,password) VALUES('{id}','{password}')"
            cursor.execute(query)
            print("Successfully Logged In")
            self.message.setText("Record Successfully Added")

    def remove_function(self):
        remove = Remove_Screen()
        stacked_widget.addWidget(remove)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def update_function(self):
        update = Update_Screen()
        stacked_widget.addWidget(update)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def serach_function(self):
        search = Search_Screen()
        stacked_widget.addWidget(search)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)


class Admin_panel(QDialog):
    def __init__(self):
        super(Admin_panel,self).__init__()
        loadUi("admin_panel.ui",self)
        self.name_panel.setText('WELCOME')
        self.exit.clicked.connect(self.close_application)
        self.add.clicked.connect(self.add_function)
        self.remove.clicked.connect(self.remove_function)
        self.update_data.clicked.connect(self.update_function)
        self.search.clicked.connect(self.serach_function)
    
    def close_application(self):
        QApplication.instance().quit()

    def add_function(self):
        add = Add_Screen()
        stacked_widget.addWidget(add)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def remove_function(self):
        remove = Remove_Screen()
        stacked_widget.addWidget(remove)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def update_function(self):
        update = Update_Screen()
        stacked_widget.addWidget(update)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def serach_function(self):
        search = Search_Screen()
        stacked_widget.addWidget(search)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)




class Admin_Login(QDialog):
    def __init__(self):
        super(Admin_Login,self).__init__()
        loadUi("admin_login.ui",self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.handle_login)
    def handle_login(self):
        if self.admin_login() == 1:
            self.goto_panel()
        
    def goto_panel(self):
        panel = Admin_panel()
        stacked_widget.addWidget(panel)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

    def admin_login(self):
        id = self.id_field.text()
        password = self.password_field.text()

        if len(id) == 0 or len(password) == 0:
            self.message_label.setText("Please input all field")
        else:
            query = "SELECT * FROM admin WHERE admin_id = %s AND password = %s"
            cursor.execute(query, (id, password))
            result = cursor.fetchone()
            if bool(result):
                print("Successfully Logged In")
                self.message_label.setText("Successfully Logged In")
                print(result[0])
                return 1
            else:
                self.message_label.setText("Invalid Id or Password")

class Instructor_panel(QDialog):
    def __init__(self):
        super(Instructor_panel,self).__init__()
        loadUi("instructor_panel.ui",self)


class Instructor_Login(QDialog):
    def __init__(self):
        super(Instructor_Login,self).__init__()
        loadUi("instructor_login.ui",self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.login.clicked.connect(self.instructor_login)
        self.login.clicked.connect(self.handle_login)
    def handle_login(self):
        if self.instructor_login() == 1:
            self.goto_panel()
        
    def goto_panel(self):
        panel = Instructor_panel()
        stacked_widget.addWidget(panel)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)
    def instructor_login(self):
        id = self.id_field.text()
        password = self.password_field.text()

        if len(id) == 0 or len(password) == 0:
            self.message_label.setText("Please input all field")
        else:
            query = "SELECT * FROM instructor WHERE instructor_id = %s AND password = %s"
            cursor.execute(query, (id, password))
            result = cursor.fetchone()
            if bool(result):
                print("Successfully Logged In")
                self.message_label.setText("Successfully Logged In")
                return 1
            else:
                self.message_label.setText("Invalid Id or Password")

class Student_panel(QDialog):
    def __init__(self):
        super(Student_panel,self).__init__()
        loadUi("student_panel.ui",self)


class Student_Login(QDialog):
    def __init__(self):
        super(Student_Login,self).__init__()
        loadUi("student_login.ui",self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.login.clicked.connect(self.student_login)
        self.login.clicked.connect(self.handle_login)
    def handle_login(self):
        if self.student_login() == 1:
            self.goto_panel()
        
    def goto_panel(self):
        panel = Student_panel()
        stacked_widget.addWidget(panel)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)
    def student_login(self):
        id = self.id_field.text()
        password = self.password_field.text()

        if len(id) == 0 or len(password) == 0:
            self.message_label.setText("Please input all field")
        else:
            query = "SELECT * FROM student WHERE student_id = %s AND password = %s"
            cursor.execute(query, (id, password))
            result = cursor.fetchone()
            if bool(result):
                print("Successfully Logged In")
                self.message_label.setText("Successfully Logged In")
                
                return 1
            else:
                self.message_label.setText("Invalid Id or Password")




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