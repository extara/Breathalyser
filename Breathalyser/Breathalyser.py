from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtGui import QDoubleValidator, QValidator
import ctypes

sex = 0
wage = 0.0
ml_drank = 0
percentage = 0

class Ui_Breathalyser(object):
    def setupUi(self, Breathalyser):
        Breathalyser.setObjectName("Breathalyser")
        Breathalyser.resize(600, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("breath.png"))
        Breathalyser.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Breathalyser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setMouseTracking(False)
        self.check_button.setObjectName("check_button")
        self.gridLayout.addWidget(self.check_button, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 3, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.ml_drink = QtWidgets.QLineEdit(self.centralwidget)
        self.ml_drink.setText("0")
        self.ml_drink.setObjectName("ml_drink")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ml_drink)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.proc = QtWidgets.QSpinBox(self.centralwidget)
        self.proc.setObjectName("proc")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.proc)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.Male_check = QtWidgets.QCheckBox(self.centralwidget)
        self.Male_check.setObjectName("Male_check")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Male_check)
        self.FMale_check = QtWidgets.QCheckBox(self.centralwidget)
        self.FMale_check.setObjectName("FMale_check")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.FMale_check)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.wage = QtWidgets.QLineEdit(self.centralwidget)
        self.wage.setText("0")
        self.wage.setObjectName("wage")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.wage)
        self.gridLayout_2.addLayout(self.formLayout, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 5, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 2, 1, 1)
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setObjectName("result")
        self.gridLayout_2.addWidget(self.result, 5, 2, 1, 1)
        self.smart_info = QtWidgets.QLabel(self.centralwidget)
        self.smart_info.setObjectName("smart_info")
        self.gridLayout_2.addWidget(self.smart_info, 5, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 5, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 5, 0, 1, 1)
        Breathalyser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Breathalyser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        self.menuta = QtWidgets.QMenu(self.menubar)
        self.menuta.setObjectName("menuta")
        Breathalyser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Breathalyser)
        self.statusbar.setObjectName("statusbar")
        Breathalyser.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuta.menuAction())

        self.retranslateUi(Breathalyser)
        QtCore.QMetaObject.connectSlotsByName(Breathalyser)

    def retranslateUi(self, Breathalyser):
        _translate = QtCore.QCoreApplication.translate
        Breathalyser.setWindowTitle(_translate("Breathalyser", "Breathalyser"))
        self.label_4.setText(_translate("Breathalyser", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#64ff03;\">Detailed informations:</span></p></body></html>"))
        self.check_button.setText(_translate("Breathalyser", "CHECK ME !"))
        self.label_5.setText(_translate("Breathalyser", "<html><head/><body><p align=\"center\">Tell me how much did you drink <span style=\" font-weight:600;\">(in ml)</span></p></body></html>"))
        self.label_6.setText(_translate("Breathalyser", "<html><head/><body><p align=\"center\">And what was the percentage of this drink ? <span style=\" font-weight:600;\">(in %)</span></p></body></html>"))
        self.label.setText(_translate("Breathalyser", "Please choose your sex:"))
        self.Male_check.setText(_translate("Breathalyser", "Male"))
        self.FMale_check.setText(_translate("Breathalyser", "Female"))
        self.label_2.setText(_translate("Breathalyser", "Please input your wage (in kg)"))
        self.label_3.setText(_translate("Breathalyser", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff0000;\">Results:</span></p></body></html>"))
        self.result.setText(_translate("Breathalyser", ""))
        self.smart_info.setText(_translate("Breathalyser", ""))

        #Connect stuff
        self.check_button.clicked.connect(self.equation)
        self.Male_check.clicked.connect(self.checkboxes)
        self.FMale_check.clicked.connect(self.checkboxes)
    #Define stuff


    def checkboxes(self):
        global sex
        if self.Male_check.isChecked() == True:
            sex = 0.7
        if self.FMale_check.isChecked() == True:
            sex = 0.6
        if self.Male_check.isChecked() == True and self.FMale_check.isChecked() == True:
            ctypes.windll.user32.MessageBoxW(0, "Please choose only one sex!", "Error encountered", 0x10)
            self.FMale_check.setChecked(False)
            self.Male_check.setChecked(False)
    def input_validation(self):
        rule = QtGui.QDoubleValidator(0, 10000, 0)
        print(rule.validate(self.text(), 14))
        if rule.validate(self.text(), 14) == QValidator.Acceptable:
            self.setFocus()
        else:
            ctypes.windll.user32.MessageBoxW(0, "Please choose only one sex!", "Error encountered", 0x10)

    def equation(self):
        global ml_drank
        global percentage
        global wage
        ml_drank = self.ml_drink.text()
        percentage = self.proc.text()
        percentage_dec = (int(percentage)) / 100
        cag = (float(ml_drank) * float(percentage_dec) * float(0.8))
        wage = self.wage.text()
        bot = (float(wage) * float(sex))
        print(bot, cag)
        if bot and cag >= 0.2:
            just_var = cag / bot
            promil_rounded = round(just_var, 2)
            if promil_rounded >= 0.2:
                print(promil_rounded)
                self.result.setText(f"<html><head/><body><p><span style=\" font-weight:600; color:#941713;\">your score in </span><span style=\" font-family:\'arial\',\'sans-serif\'; font-size:14px; font-weight:600; color:#941713; background-color:#ffffff;\">{promil_rounded}‰</span></p></body></html>")
                self.smart_info.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#5e7859;\">Did you know that currently alcohol...</span></p><p align=\"center\"><span style=\" font-size:8pt; font-weight:300; color:#5e7859;\">"
                                        f"- interferes your memory and learning skills"
                                        f"<br> - increases the likelihood that you will use other drugs."
                                        f"<br> - increases your risk of developing cancer."
                                        f"<br> - increases depression and anxiety.</span></p>"
                                        f"<p align=\"center\"><span style=\" font-size:8pt; font-weight:300; color:#5e7859;\">Please remember <br> about the fact that alcohol will never solve your problems,<br> never drink under heavy emotional situations<br> and... DRINK WITH LIMITS !</span></p></body></html>")
            elif promil_rounded <= 0.2:
                self.result.setText(f"<html><head/><body><p><span style=\" font-weight:600; color:#941713;\">your score in </span><span style=\" font-family:\'arial\',\'sans-serif\'; font-size:14px; font-weight:600; color:#941713; background-color:#ffffff;\">{promil_rounded}‰</span></p></body></html>")
                self.smart_info.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#5e7859;\">You are still sober.</span></p></body></html>")
            if promil_rounded >= 10:
                self.result.setText(f"<html><head/><body><p><span style=\" font-weight:600; color:#941713;\">your score in </span><span style=\" font-family:\'arial\',\'sans-serif\'; font-size:14px; font-weight:600; color:#941713; background-color:#ffffff;\">{promil_rounded}‰</span></p></body></html>")
                self.smart_info.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#5e7859;\">If what you telling me, its true...<br> Please visit hospital<br> or at least contact doctor as soon as possible.</span></p></body></html>")

        if bot == 0 and cag == 0:
            ctypes.windll.user32.MessageBoxW(0, "Please correct your wage and ml/percentage inputs !",
                                             "Error encountered", 0x10)
        elif cag == 0:
            ctypes.windll.user32.MessageBoxW(0, "Please correct ml or percentage inputs !", "Error encountered", 0x10)
            self.result.setText("")
            self.smart_info.setText("")
        elif bot == 0:
            ctypes.windll.user32.MessageBoxW(0, "Please correct your wage input !", "Error encountered", 0x10)
            self.result.setText("")
            self.smart_info.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Breathalyser = QtWidgets.QMainWindow()
    ui = Ui_Breathalyser()
    ui.setupUi(Breathalyser)
    Breathalyser.show()
    sys.exit(app.exec())
