#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from deep_translator import GoogleTranslator
from language import *

#Class
class Home(QWidget):
    #Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()

    #App object and Design
    def initUI(self):
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.btn_reverse = QPushButton("Reverse")
        self.btn_reset = QPushButton("Reset")
        self.submit = QPushButton("Translate Now!")
        self.input_option = QComboBox()
        self.output_option = QComboBox()
        self.title = QLabel("Language Translator")

        self.master = QHBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        self.input_option.addItems(values)
        self.output_option.addItems(values)

        col1.addWidget(self.title)
        col1.addWidget(self.input_option)
        col1.addWidget(self.output_option)
        col1.addWidget(self.submit)
        col1.addWidget(self.btn_reset)

        col2.addWidget(self.input_box)
        col2.addWidget(self.btn_reverse)
        col2.addWidget(self.output_box)

        self.master.addLayout(col1, 20)
        self.master.addLayout(col2, 80)

        self.setLayout(self.master)

        #Button signals
        self.submit.clicked.connect(self.translate_click)
        self.btn_reset.clicked.connect(self.reset_app)
        self.btn_reverse.clicked.connect(self.reverse_translation)

    #App settings
    def settings(self):
        self.setWindowTitle("Language Translator")
        self.setGeometry(200, 200, 800, 500)

    #Translate click
    def translate_click(self):
        value_to_key1 = self.input_option.currentText()
        value_to_key2 = self.output_option.currentText()

        key_to_value1 = [k for k, v in LANGUAGES.items() if v == value_to_key1]
        key_to_value2 = [k for k, v in LANGUAGES.items() if v == value_to_key2]

        if key_to_value1 and key_to_value2:
            result = self.translate_text(
                self.input_box.toPlainText(),
                key_to_value2[0],
                key_to_value1[0]
            )
            self.output_box.setText(result)

    #Reset App
    def reset_app(self):
        self.input_box.clear()
        self.output_box.clear()

    #Translate Text (Google)
    def translate_text(self, text, dest_language, source_language):
        translation = GoogleTranslator(source=source_language, target=dest_language).translate(text)
        return translation

    #Reverse Translation
    def reverse_translation(self):
        l1 = self.input_option.currentText()
        l2 = self.output_option.currentText()

        t1 = self.input_box.toPlainText()
        t2 = self.output_box.toPlainText()

        self.input_box.setText(t2)
        self.output_box.setText(t1)

        self.input_option.setCurrentText(l2)
        self.output_option.setCurrentText(l1)


#Main Run
if __name__ == "__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()