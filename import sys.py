import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel,
    QLineEdit, QRadioButton, QComboBox, QPushButton, QButtonGroup
)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Registration Form")
        self.setGeometry(100, 100, 400, 300)  
        
        main_layout = QVBoxLayout()

        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama: Muhammad Daffa Dzaki Ahnaf"))
        identity_layout.addWidget(QLabel("NIM: F1D022142"))
        identity_layout.addWidget(QLabel("Kelas: C"))
        main_layout.addLayout(identity_layout)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        main_layout.addLayout(nav_layout)

        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()

        form_layout.addRow("Full Name:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Phone:", self.phone_input)

        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")

        self.gender_group = QButtonGroup()
        self.gender_group.addButton(self.male_radio)
        self.gender_group.addButton(self.female_radio)

        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        form_layout.addRow("Gender:", gender_layout)

        self.country_combo = QComboBox()
        countries = ["Select Country", "Indonesia", "Malaysia", "Singapore", "Thailand", "Philippines"]
        self.country_combo.addItems(countries)
        form_layout.addRow("Country:", self.country_combo)

        main_layout.addLayout(form_layout)

        action_layout = QHBoxLayout()
        self.submit_button = QPushButton("Submit")
        self.cancel_button = QPushButton("Cancel")

        self.submit_button.clicked.connect(self.submit_form)
        self.cancel_button.clicked.connect(self.close)

        action_layout.addWidget(self.submit_button)
        action_layout.addWidget(self.cancel_button)
        main_layout.addLayout(action_layout)

        self.setLayout(main_layout)

    def submit_form(self):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        gender = "Male" if self.male_radio.isChecked() else "Female" if self.female_radio.isChecked() else "Not Selected"
        country = self.country_combo.currentText()

        print(f"Full Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Gender: {gender}")
        print(f"Country: {country}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
