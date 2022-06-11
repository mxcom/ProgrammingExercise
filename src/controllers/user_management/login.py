import re, sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6 import QtCore

from src.controllers.user_management.user_management import get_user
from src.views.user_management.WndLogin import Ui_WndLogin
from src.controllers.primary.primary import PrimaryWindow
from src.controllers.user_management.registration import RegistrationWindow
from src.controllers.cryptography.cryptography import compare_passwd

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class LoginWindow(QMainWindow, Ui_WndLogin):
    """
    Class provides functionalities to interact with ui for login
    """

    def __init__(self, parent=None):
        """
        Used to setup the ui and connect widgets with methods
        """
        super(LoginWindow, self).__init__(parent)
        self.mw = None
        self.ui = Ui_WndLogin()
        self.ui.setupUi(self)

        # Settings for GUI
        self.ui.leEmail.textChanged.connect(self.validate_email)
        self.ui.btnLogin.clicked.connect(self.validate_login)

        # Change Window
        self.ui.btnSignup.clicked.connect(self.switch_to_registration)

    def switch_to_registration(self):
        self.destroy()
        self.mw = RegistrationWindow()
        self.mw.show()

    def validate_email(self):
        """
        Validate email based on regex

        Return
        ------
        bool
            True if regex and input correspond
            False if regex and input don't correspond
        """
        email = self.ui.leEmail.text()
        if re.fullmatch(regex, email):
            self.ui.leEmail.setStyleSheet("color: black;")
            return True
        else:
            self.ui.leEmail.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_passwd(self):
        """
        validates password

        Return
        ------
        bool
            True if password is >= 8 chars
            False if password is > 8 chars
        """
        passwd = self.ui.lePassword.text()

        if len(passwd) < 8:
            return False
        else:
            return True

    def validate_login(self):
        """
        Validates user login credentials using obove validate methods
        """
        if self.validate_email() and self.validate_passwd() == True:
            try:
                email = self.ui.leEmail.text()
                passwd = self.ui.lePassword.text()

                user = get_user('mxprivate@protonmail.com')

                if compare_passwd(self.ui.lePassword.text(), user.get_passwd()):
                    self.destroy()
                    self.mw = PrimaryWindow(user)
                    self.mw.show()
                else:
                    print("wrong email or password")
            except Exception as e:
                print(e)
        else:
            print("could not validate")
