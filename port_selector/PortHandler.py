from PyQt6 import QtCore, QtGui, QtWidgets
from googletrans import Translator
from port_interface import Ui_Dialog as interface_Dialog
from error_display import Ui_Form as error_interface
import serial.tools.list_ports
import os, sys

ser = serial.Serial()


class error_dialog(QtWidgets.QWidget):
    def __init__(self, error_msg, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.error_dialog = error_interface()
        self.error_dialog.setupUi(self)
        translator = Translator()
        translated_error_msg = translator.translate(str(error_msg), src='en', dest='th')
        self.show_an_error(error_eng=error_msg, error_thai=translated_error_msg.text)
        self.error_dialog.pushButton.clicked.connect(lambda: self.close())
    def show_an_error(self,error_eng, error_thai):
        self.error_dialog.textEdit.setHtml(QtCore.QCoreApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(error_eng)+"</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(error_thai)+"</p></body></html>"))


class Port_list(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        self.avalible_bandRate = [4800,9600,115200,250000]
        QtWidgets.QWidget.__init__(self, parent)
        self.portUI = interface_Dialog()
        self.portUI.setupUi(self)
        self.update_port_data()
        self.list_port()
        self.portUI.reload_button.clicked.connect(self.reflesh_port)
        self.portUI.buttonBox.accepted.connect(self.connection_Handler)
    def update_port_data(self):
        for port, desc, hwid in sorted(serial.tools.list_ports.comports()):
            self.portUI.Port_list.addItem(port)
    def reflesh_port(self):
        self.portUI.Port_list.clear()
        for port, desc, hwid in sorted(serial.tools.list_ports.comports()):
            self.portUI.Port_list.addItem(port)
    def list_port(self):
        for bandrate in sorted(self.avalible_bandRate):
            self.portUI.Bandrate_list.addItem(str(bandrate))
    def connection_Handler(self):
        try:
            ser.bandrate = self.portUI.Bandrate_list.currentText()
            ser.port = self.portUI.Port_list.currentText()
            ser.timeout = 1
            ser.open()
            if (ser.is_open):
                self.switch_window.emit()       #check connect and change display
        except serial.SerialException as err:
            print(err)
            self.show_error = error_dialog(error_msg=err)
            self.show_error.show()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Port_list()
    controller.show()
    sys.exit(app.exec())