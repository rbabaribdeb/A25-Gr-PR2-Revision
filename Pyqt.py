import sys
from PyQt6.QtWidgets import QApplication, QWidget

# create a PyQt5 application
app = QApplication(sys.argv)

# create a QWidget object
win = QWidget()

# Make a window title
win.setWindowTitle("This is a first PyQt5 app !")

# define a geometry of the window
win.setGeometry(100, 100, 500, 400)

# apply the show method to view the window
win.show()

sys.exit(app.exec())


