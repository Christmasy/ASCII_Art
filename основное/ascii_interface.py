# сторонний импорт в алфавитном порядке
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox

# локальный импорт
from ascii_functions import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 850)

        self.way = ''  # путь до файла

        self.width_ = 0  # по началу сделаем такими
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

        self.label_enter_ascii = QtWidgets.QLabel(self.form)
        self.label_enter_ascii.setGeometry(QtCore.QRect(60, 190, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_enter_ascii.setFont(font)
        self.label_enter_ascii.setObjectName("label_enter_ascii")

        self.scale = QtWidgets.QLineEdit(self.form)
        self.scale.setGeometry(QtCore.QRect(330, 200, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.scale.setFont(font)
        self.scale.setStyleSheet('background-color: rgb(255,255,255)')

        self.label_way = QtWidgets.QLabel(self.form)
        self.label_way.setGeometry(QtCore.QRect(400, 60, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_way.setFont(font)
        self.label_way.setObjectName("label_way")

        self.label_contrast_values = QtWidgets.QLabel(self.form)
        self.label_contrast_values.setGeometry(QtCore.QRect(392, 245, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        self.label_contrast_values.setFont(font)
        self.label_contrast_values.setObjectName("label_contrast_values")

        self.contast_slider = QtWidgets.QSlider(self.form)
        self.contast_slider.setGeometry(QtCore.QRect(330, 270, 670, 25))
        self.contast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contast_slider.setObjectName("contast_slider")
        self.contast_slider.setValue(10)  # 10 - контрастность не менялась
        self.contast_slider.setMinimum(0)  # 0 - изображение сплошное серое
        self.contast_slider.setMaximum(100)
        self.contast_slider.setTickPosition(1)  # разметка

        self.way_to_art_button = QtWidgets.QPushButton(self.form)
        self.way_to_art_button.setGeometry(QtCore.QRect(60, 70, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.way_to_art_button.setFont(font)
        self.way_to_art_button.setObjectName("way_to_art_button")

        self.label_contrast = QtWidgets.QLabel(self.form)
        self.label_contrast.setGeometry(QtCore.QRect(60, 260, 231, 41))
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
        self.label_change_size.setGeometry(QtCore.QRect(60, 320, 231, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_change_size.setFont(font)
        self.label_change_size.setWordWrap(True)
        self.label_change_size.setObjectName("label_change_size")

        self.label_width = QtWidgets.QLabel(self.form)
        self.label_width.setGeometry(QtCore.QRect(340, 320, 251, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_width.setFont(font)
        self.label_width.setWordWrap(True)
        self.label_width.setObjectName("label_width")

        self.label_height = QtWidgets.QLabel(self.form)
        self.label_height.setGeometry(QtCore.QRect(720, 320, 231, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_height.setFont(font)
        self.label_height.setWordWrap(True)
        self.label_height.setObjectName("label_height")

        self.width = QtWidgets.QPlainTextEdit(self.form)
        self.width.setGeometry(QtCore.QRect(340, 390, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.width.setFont(font)
        self.width.setObjectName("width")

        self.height = QtWidgets.QPlainTextEdit(self.form)
        self.height.setGeometry(QtCore.QRect(720, 390, 230, 40))
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

        self.label_set_tool = QtWidgets.QLabel(self.form)
        self.label_set_tool.setGeometry(QtCore.QRect(60, 460, 900, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label_set_tool.setFont(font)
        self.label_set_tool.setObjectName("label_set_tool")
        self.tabWidget.addTab(self.form, "")

        self.res = QtWidgets.QWidget()
        self.res.setObjectName("res")

        self.label_image = QtWidgets.QLabel(self.res)
        self.label_image.setFont(QtGui.QFont('Courier New', 10))
        self.label_image.setGeometry(QtCore.QRect(100, 10, 1070, 850))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.tabWidget.addTab(self.res, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()  # привязка функций к кнопкам / ползункам..

    def retranslateUi(self, MainWindow):
        _t = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_t("MainWindow", "ASCII Art"))
        self.label_contrast_values.setText(_t("MainWindow", "☟"))
        self.label_contrast.setText(_t("MainWindow", "Контрастность:"))
        self.label_enter_ascii.setText(_t("MainWindow", "ASCII-символы:"))
        self.scale.setText(_t("MainWindow", "@#S%?*+;:,."))
        self.way_to_art_button.setText(_t("MainWindow", "Путь к изображению"))
        self.readyButton.setText(_t("MainWindow", "Готово!"))
        change_size_text = "Изменение размеров изображения:"
        self.label_change_size.setText(_t("MainWindow", change_size_text))
        self.label_width.setText(_t("MainWindow", "Ширина (в пикселях):"))
        self.label_height.setText(_t("MainWindow", "Высота (в пикселях):"))
        self.radBut_without.setText(_t("MainWindow", "Без обработки"))
        self.radBut_graify.setText(_t("MainWindow", "Сделать изображение ч/б"))
        self.radBut_ascii.setText(_t("MainWindow", "Перевести в ASCII Art"))
        set_tool_text = "Пожалуйста, выберите одну из обработок изображения:"
        self.label_set_tool.setText(_t("MainWindow", set_tool_text))
        index = self.tabWidget.indexOf
        set_tab_text = self.tabWidget.setTabText
        set_tab_text(index(self.form), _t("MainWindow", "Настройки"))
        set_tab_text(index(self.res), _t("MainWindow", "Результат"))

    def add_functions(self):
        self.readyButton.clicked.connect(self.results)
        self.way_to_art_button.clicked.connect(self.way_to_art_handler)

    def way_to_art_handler(self):
        filename = QFileDialog.getOpenFileName()
        self.way = filename[0]
        split_way = self.way.split('/')
        _t = QtCore.QCoreApplication.translate
        self.label_way.setText(_t("MainWindow", split_way[len(split_way)-1]))

    def results(self):
        try:
            image = Image.open(self.way)  # работаю с открытием файла по имени
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

            if self.height.toPlainText() != "":
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

            correct_h_w = self.correct_width and self.correct_height
            not_zero_h_w = self.not_zero_height and self.not_zero_width

            if correct_h_w and not_zero_h_w:
                w = self.width_
                h = self.height_
                resized_im = resize_image_user_tools(image, w, h)
                contr_im = contrast(resized_im, self.contast_slider.value()/10)
                if self.radBut_without.isChecked():
                    self.set_non_text_image(modify_image_to_P_mode(contr_im))
                elif self.radBut_graify.isChecked():
                    self.set_non_text_image(grayify(contr_im))
                elif self.radBut_ascii.isChecked():
                    ASCII_chars = list(self.scale.text())
                    if len(ASCII_chars) == 0:
                        self.createError("Введите, пожалуйста, ASCII-имволы")
                    else:
                        if len(ASCII_chars) == 1:
                            warning_mes = QMessageBox()
                            warning_mes.setWindowTitle("Предупреждение")
                            one_symb = "Один символ?.. ну ладно :)"
                            warning_mes.setText(one_symb)
                            warning_mes.setIcon(QMessageBox.NoIcon)
                            warning_mes.setStandardButtons(QMessageBox.Ok)
                            warning_mes.exec()
                        set_text = self.label_image.setText
                        set_text(do_ascii_art(contr_im, 1, ASCII_chars, w, h))
                        self.formulate_ready_message()
                else:
                    create_err = self.createError
                    create_err("Пожалуйста, выберите одну из обработок ниже!")

    def set_non_text_image(self, processed_image):
        pixmap = QPixmap.fromImage(ImageQt(processed_image))
        self.label_image.setPixmap(pixmap)
        self.formulate_ready_message()

    def createError(self, error_text):
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText(error_text)
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def formulate_ready_message(self):
        ready_mes = QMessageBox()
        ready_mes.setWindowTitle("Готово")
        im_ready_text = "Изображение обработано!"
        res_text = "Результат на соседней вкладке :)"
        ready_mes.setText(im_ready_text + '\n' + res_text)
        ready_mes.setIcon(QMessageBox.NoIcon)
        ready_mes.setStandardButtons(QMessageBox.Ok)
        ready_mes.exec()
