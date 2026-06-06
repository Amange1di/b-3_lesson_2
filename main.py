import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Проверка пароля")
        self.resize(350, 180)

        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setPlaceholderText("Введите пароль")
        self.input_password.setGeometry(20, 20, 310, 30)

        self.button_check = QPushButton("Проверить", self)
        self.button_check.setGeometry(20, 60, 310, 30)
        self.button_check.clicked.connect(self.check_password)

        self.label_message = QLabel("", self)
        self.label_message.setGeometry(20, 100, 310, 30)

    def check_password(self):
        password = self.input_password.text()

        if not password:
            self.label_message.setText("Введите пароль")
        elif password == "12345":
            self.label_message.setText("Доступ разрешён")
        else:
            self.label_message.setText("Неверный пароль")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordChecker()
    window.show()
    sys.exit(app.exec())
