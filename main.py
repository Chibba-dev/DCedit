from PyQt5 import QtWidgets, uic
import sys
from ui_main import Ui

# with open(pathToFile) as f:
#     data = json.load(f)


# with open(pathToFile, 'w') as outfile:
#     json.dump(data, outfile)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()