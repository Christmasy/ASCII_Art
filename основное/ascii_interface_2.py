from os import error
from PyQt5 import QtCore, QtGui, QtWidgets
from ascii_functions import *
from PIL import Image
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 850)

        self.width_ = 0 # по началу сделаем такими
        self.height_ = 0

        self.correct_width = True
        self.correct_height = True

        self.not_zero_width = True
        self.not_zero_height = True

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1070, 5000))
        self.tabWidget.setObjectName("tabWidget")

        self.form = QtWidgets.QWidget()
        self.form.setObjectName("form")

        self.label_way = QtWidgets.QLabel(self.form)
        self.label_way.setGeometry(QtCore.QRect(60, 130, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)

        self.label_way.setFont(font)
        self.label_way.setObjectName("label_way")

        self.contast_slider = QtWidgets.QSlider(self.form)
        self.contast_slider.setGeometry(QtCore.QRect(330, 205, 670, 25))
        self.contast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contast_slider.setObjectName("contast_slider")

        self.way_to_art = QtWidgets.QPlainTextEdit(self.form)
        self.way_to_art.setGeometry(QtCore.QRect(330, 140, 670, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.way_to_art.setFont(font)
        self.way_to_art.setObjectName("way_to_art")

        self.label_contrast = QtWidgets.QLabel(self.form)
        self.label_contrast.setGeometry(QtCore.QRect(60, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_contrast.setFont(font)
        self.label_contrast.setObjectName("label_contrast")

        self.readyButton = QtWidgets.QPushButton(self.form)
        self.readyButton.setGeometry(QtCore.QRect(455, 660, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.readyButton.setFont(font)
        self.readyButton.setObjectName("readyButton")

        self.label_change_size = QtWidgets.QLabel(self.form)
        self.label_change_size.setGeometry(QtCore.QRect(60, 250, 231, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_change_size.setFont(font)
        self.label_change_size.setWordWrap(True)
        self.label_change_size.setObjectName("label_change_size")

        self.label_width = QtWidgets.QLabel(self.form)
        self.label_width.setGeometry(QtCore.QRect(340, 260, 251, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_width.setFont(font)
        self.label_width.setWordWrap(True)
        self.label_width.setObjectName("label_width")

        self.label_height = QtWidgets.QLabel(self.form)
        self.label_height.setGeometry(QtCore.QRect(720, 260, 231, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_height.setFont(font)
        self.label_height.setWordWrap(True)
        self.label_height.setObjectName("label_height")

        self.width = QtWidgets.QPlainTextEdit(self.form)
        self.width.setGeometry(QtCore.QRect(340, 330, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.width.setFont(font)
        self.width.setObjectName("width")

        self.height = QtWidgets.QPlainTextEdit(self.form)
        self.height.setGeometry(QtCore.QRect(720, 330, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.height.setFont(font)
        self.height.setObjectName("height")

        self.radBut_without = QtWidgets.QRadioButton(self.form)
        self.radBut_without.setGeometry(QtCore.QRect(60, 540, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radBut_without.setFont(font)
        self.radBut_without.setObjectName("radBut_without")

        self.radBut_graify = QtWidgets.QRadioButton(self.form)
        self.radBut_graify.setGeometry(QtCore.QRect(330, 540, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radBut_graify.setFont(font)
        self.radBut_graify.setObjectName("radBut_graify")

        self.radBut_ascii = QtWidgets.QRadioButton(self.form)
        self.radBut_ascii.setGeometry(QtCore.QRect(710, 540, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radBut_ascii.setFont(font)
        self.radBut_ascii.setObjectName("radBut_ascii")

        self.label = QtWidgets.QLabel(self.form)
        self.label.setGeometry(QtCore.QRect(60, 440, 900, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.form, "")

        self.res = QtWidgets.QWidget()
        self.res.setObjectName("res")

        self.label_image = QtWidgets.QLabel(self.res)
        self.label_image.setGeometry(QtCore.QRect(100, 10, 1070, 850))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.tabWidget.addTab(self.res, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
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
        self.radBut_without.setText(_translate("MainWindow", "Без обработки"))
        self.radBut_graify.setText(_translate("MainWindow", "Сделать изображение ч/б"))
        self.radBut_ascii.setText(_translate("MainWindow", "Перевести в ASCII Art"))
        self.label.setText(_translate("MainWindow", "Пожалуйста, выберите одну из обработок изображения:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.form), _translate("MainWindow", "Настройки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.res), _translate("MainWindow", "Результат"))

    def add_functions(self):
        self.readyButton.clicked.connect(self.results) # все срабатывает при нажатии кнопки "Готово!"

    def results(self):
        try:
            image = Image.open(self.way_to_art.toPlainText())
        except:
            self.createError("Путь до изображения некорректен")
        else:
            self.width_, self.height_ = image.size

            if self.width.toPlainText() != "":
                try:
                    self.width_ = int(self.width.toPlainText())
                except:
                    self.createError("Некорректная ширина")
                    self.correct_width = False
                else:
                    self.correct_width = True

            if self.width.toPlainText() != "":
                try:
                    self.height_ = int(self.height.toPlainText())
                except:
                    self.createError("Некорректная высота")
                    self.correct_height = False
                else:
                    self.correct_height = True

            if self.width_ == 0:
                self.createError("Ширина не может быть равна 0")
                self.not_zero_width = False
            else:
                self.not_zero_width = True
                
            if self.height_ == 0:
                self.createError("Высота не может быть равна 0")
                self.not_zero_height = False
            else:
                self.not_zero_height = True
            
            if self.correct_width and self.correct_height and self.not_zero_height and self.not_zero_width:
                if self.radBut_without.isChecked():
                    
                    resized_image = resize_image_user_tools(image, self.width_, self.height_)
                    pixmap = QPixmap.fromImage(ImageQt(resized_image))
                    self.label_image.setPixmap(pixmap)
                    self.formulate_ready_message()
                elif self.radBut_graify.isChecked():
                    resized_image = resize_image_user_tools(image, self.width_, self.height_)
                    pixmap = QPixmap.fromImage(ImageQt(grayify(resized_image)))
                    self.label_image.setPixmap(pixmap)
                    self.formulate_ready_message()
                elif self.radBut_ascii.isChecked():
                    resized_image = resize_image_user_tools(image, self.width_, self.height_)
                    self.label_image.setText(do_ascii_art(resized_image, 1, self.width_, self.height_))
                    self.formulate_ready_message()
                else:
                    self.createError("Пожалуйста, выберите одну из настроек!")


    def createError(self, error_text):
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText(error_text)
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def formulate_ready_message(self):
        ready_message = QMessageBox()
        ready_message.setWindowTitle("Готово")
        ready_message.setText("Ваше изображение обработано! \nРезультат можно посмотреть на соседней вкладке :)")
        ready_message.setIcon(QMessageBox.NoIcon)
        ready_message.setStandardButtons(QMessageBox.Ok)
        ready_message.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
