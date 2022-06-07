import sys

from PySide6.QtWidgets import QApplication

# from src.controllers.user_management.registration import RegistrationWindow
from src.controllers.user_management.login import LoginWindow
from src.controllers.user_management.email import send_mail


def main():
    print("hello, world")
    # uncomment next line for email (and replace receiver mail)
    # send_mail('reciever@gmail.com')

    # app = QApplication(sys.argv)
    # window = LoginWindow()
    # window.show()
    # sys.exit(app.exec())


if __name__ == "__main__":
    main()
