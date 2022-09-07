from tkinter.ttk import Style
from PyQt5 import QtCore, QtGui, QtWidgets
from ascii_functions import *
from PIL import Image
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)

        self.width_ = 0 # по началу сделаем такими
        self.height_ = 0

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.tabWidget.setObjectName("tabWidget")

        self.form = QtWidgets.QWidget()
        self.form.setObjectName("form")

        self.label_way = QtWidgets.QLabel(self.form)
        self.label_way.setGeometry(QtCore.QRect(50, 130, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)

        self.label_way.setFont(font)
        self.label_way.setObjectName("label_way")

        self.contast_slider = QtWidgets.QSlider(self.form)
        self.contast_slider.setGeometry(QtCore.QRect(310, 205, 640, 25))
        self.contast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contast_slider.setObjectName("contast_slider")
        self.contast_slider.setMinimum(0)
        self.contast_slider.setMaximum(2)

        self.way_to_art = QtWidgets.QPlainTextEdit(self.form)
        self.way_to_art.setGeometry(QtCore.QRect(310, 140, 640, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.way_to_art.setFont(font)
        self.way_to_art.setObjectName("way_to_art")

        self.label_contrast = QtWidgets.QLabel(self.form)
        self.label_contrast.setGeometry(QtCore.QRect(50, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_contrast.setFont(font)
        self.label_contrast.setObjectName("label_contrast")

        self.readyButton = QtWidgets.QPushButton(self.form)
        self.readyButton.setGeometry(QtCore.QRect(420, 630, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.readyButton.setFont(font)
        self.readyButton.setObjectName("readyButton")
        #self.readyButton.setEnabled(False)

        self.label_change_size = QtWidgets.QLabel(self.form)
        self.label_change_size.setGeometry(QtCore.QRect(50, 250, 231, 121))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_change_size.setFont(font)
        self.label_change_size.setWordWrap(True)
        self.label_change_size.setObjectName("label_change_size")

        self.label_width = QtWidgets.QLabel(self.form)
        self.label_width.setGeometry(QtCore.QRect(320, 250, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_width.setFont(font)
        self.label_width.setWordWrap(True)
        self.label_width.setObjectName("label_width")

        self.label_height = QtWidgets.QLabel(self.form)
        self.label_height.setGeometry(QtCore.QRect(640, 250, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_height.setFont(font)
        self.label_height.setWordWrap(True)
        self.label_height.setObjectName("label_height")

        self.width = QtWidgets.QPlainTextEdit(self.form)
        self.width.setGeometry(QtCore.QRect(320, 330, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.width.setFont(font)
        self.width.setObjectName("width")

        self.height = QtWidgets.QPlainTextEdit(self.form)
        self.height.setGeometry(QtCore.QRect(640, 330, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.height.setFont(font)
        self.height.setObjectName("height")

        self.checkBox_grayify = QtWidgets.QCheckBox(self.form)
        self.checkBox_grayify.setGeometry(QtCore.QRect(50, 440, 350, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.checkBox_grayify.setFont(font)
        self.checkBox_grayify.setObjectName("checkBox_grayify")

        self.checkBox_ascii_art = QtWidgets.QCheckBox(self.form)
        self.checkBox_ascii_art.setGeometry(QtCore.QRect(480, 440, 350, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.checkBox_ascii_art.setFont(font)
        self.checkBox_ascii_art.setObjectName("checkBox_ascii_art")

        self.checkBox_ascii_art = QtWidgets.QCheckBox(self.form)
        self.checkBox_ascii_art.setGeometry(QtCore.QRect(480, 440, 350, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.checkBox_ascii_art.setFont(font)
        self.checkBox_ascii_art.setObjectName("checkBox_ascii_art")
        

        self.tabWidget.addTab(self.form, "")

        self.res = QtWidgets.QWidget()
        self.res.setObjectName("res")

        self.label_image = QtWidgets.QLabel(self.res)
        self.label_image.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")

        self.tabWidget.addTab(self.res, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions() # add_functions отвечает за привязку функций к кнопкам / ползункам / чекбоксам..

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_way.setText(_translate("MainWindow", "Путь до изображения:"))
        self.label_contrast.setText(_translate("MainWindow", "Контрастность:"))
        self.readyButton.setText(_translate("MainWindow", "Готово!"))
        self.label_change_size.setText(_translate("MainWindow", "Изменение размеров изображения:"))
        self.label_width.setText(_translate("MainWindow", "Ширина (в пикселях):"))
        self.label_height.setText(_translate("MainWindow", "Высота (в пикселях):"))
        self.checkBox_grayify.setText(_translate("MainWindow", "Сделать изображение ч/б"))
        self.checkBox_ascii_art.setText(_translate("MainWindow", "Сделать ASCII_Art"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.form), _translate("MainWindow", "Настройки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.res), _translate("MainWindow", "Результат"))

    def add_functions(self):
        self.readyButton.clicked.connect(self.results) # срабатывает все при нажатии кнопки "Готово!"

    def results(self):
        try:
            image = Image.open(self.way_to_art.toPlainText())
        except:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Путь до изображения некорректен")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            pass
        else:
            self.width_, self.height_ = image.size

            if self.width.toPlainText() != "":
                self.width_ = int(self.width.toPlainText())
            if self.height.toPlainText() != "":
                self.height_ = int(self.height.toPlainText())
            
            if not self.checkBox_ascii_art.isChecked() and not self.checkBox_grayify.isChecked():
                resized_image = resize_image_user_tools(image, self.width_*10, self.height_*10)
                pixmap = QPixmap.fromImage(ImageQt(resized_image))
                self.label_image.setPixmap(pixmap)
            if self.checkBox_ascii_art.isChecked():
                self.label_image.setText(do_ascii_art(resize_image_user_tools(image, self.width_, self.height_), 1, self.width_, self.height_))
            elif self.checkBox_grayify.isChecked():
                resized_image = resize_image_user_tools(image, self.width_*10, self.height_*10)
                pixmap = QPixmap.fromImage(ImageQt(grayify(resized_image)))
                self.label_image.setPixmap(pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
