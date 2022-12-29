from check_arch import check_platform
import os, sys
from upload_display import Ui_Dialog
from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess


class display_feedback(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.displayfeedback = Ui_Dialog()
        self.displayfeedback.setupUi(self)
        self.update_onscreen_data()
        #flash_reciver("/dev/tty.usbmodem4212401")
    def update_onscreen_data(self):
        progress_out = str(subprocess.run("cd upload_tools/upload_handler \n avrdude "+"-c arduino -P "+"/dev/tty.usbmodem4212401"+" -b 115200 -p atmega328p -D -U flash:w:"+"../reciver.hex", shell=True, capture_output=True))
        self.displayfeedback.plainTextEdit.setPlainText(QtCore.QCoreApplication.translate("MainWindow", str(progress_out.find("flash verified"))))



def run_command(command):
    if check_platform() == 'arm macos' or check_platform() == 'macos':
        os.system("cd upload_tools/upload_handler \n avrdude "+str(command))
    elif check_platform() == 'window':
        os.system("cd upload_tools/upload_handler \n avrdude.exe "+str(command))

def flash_reciver(port):
    run_command(command= "-c arduino -P "+port+" -b 115200 -p atmega328p -D -U flash:w:"+"../reciver.hex")

def flash_transiver(port):
    run_command(command= "-c arduino -P "+port+" -b 115200 -p atmega328p -D -U flash:w:"+"../transiver.hex")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    feed = display_feedback()
    feed.show()
    sys.exit(app.exec())