from PyQt6 import QtCore, QtGui, QtWidgets
from main import *


class Ui_QuineMcCluskey(object):
    def setupUi(self, QuineMcCluskey):
        QuineMcCluskey.setObjectName("QuineMcCluskey")
        QuineMcCluskey.resize(1000, 720)

        self.centralwidget = QtWidgets.QWidget(QuineMcCluskey)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.valtozokinput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valtozokinput.sizePolicy().hasHeightForWidth())

        self.valtozokinput.setSizePolicy(sizePolicy)
        self.valtozokinput.setObjectName("valtozokinput")
        self.gridLayout.addWidget(self.valtozokinput, 17, 0, 1, 1)

        self.PrimImplikansTabla = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrimImplikansTabla.sizePolicy().hasHeightForWidth())
        self.PrimImplikansTabla.setSizePolicy(sizePolicy)
        self.PrimImplikansTabla.setObjectName("PrimImplikansTabla")
        self.gridLayout.addWidget(self.PrimImplikansTabla, 13, 1, 8, 2)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 20, 0, 1, 1)
        self.pushButton_2.clicked.connect(self.csodalgoritmus)

        self.valtozokszama = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.valtozokszama.setFont(font)
        self.valtozokszama.setObjectName("valtozokszama")

        self.gridLayout.addWidget(self.valtozokszama, 16, 0, 1, 1)
        self.mintermekinput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mintermekinput.sizePolicy().hasHeightForWidth())

        self.mintermekinput.setSizePolicy(sizePolicy)
        self.mintermekinput.setObjectName("mintermekinput")
        self.gridLayout.addWidget(self.mintermekinput, 19, 0, 1, 1)

        self.mintermekszama = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.mintermekszama.setFont(font)
        self.mintermekszama.setObjectName("mintermekszama")
        self.gridLayout.addWidget(self.mintermekszama, 18, 0, 1, 1)

        self.MintermTabla = QtWidgets.QTableWidget(self.centralwidget)
        self.MintermTabla.setMinimumSize(QtCore.QSize(0, 3))
        self.MintermTabla.setObjectName("MintermTabla")
        self.MintermTabla.setColumnCount(0)
        self.MintermTabla.setRowCount(0)
        self.gridLayout.addWidget(self.MintermTabla, 12, 1, 1, 1)

        self.EredmenyekLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.EredmenyekLabel.setFont(font)
        self.EredmenyekLabel.setText("")
        self.EredmenyekLabel.setObjectName("EredmenyekLabel")
        self.gridLayout.addWidget(self.EredmenyekLabel, 12, 0, 1, 1)
        QuineMcCluskey.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(QuineMcCluskey)
        self.statusbar.setObjectName("statusbar")
        QuineMcCluskey.setStatusBar(self.statusbar)

        self.retranslateUi(QuineMcCluskey)
        QtCore.QMetaObject.connectSlotsByName(QuineMcCluskey)

    def retranslateUi(self, QuineMcCluskey):
        _translate = QtCore.QCoreApplication.translate
        QuineMcCluskey.setWindowTitle(_translate("QuineMcCluskey", "Quine-McCluskey"))
        self.pushButton_2.setText(_translate("QuineMcCluskey", "Mintermek egyszerusitese"))
        self.valtozokszama.setText(_translate("QuineMcCluskey", "Változók száma:"))
        self.mintermekszama.setText(_translate("QuineMcCluskey", "Mintermek (decimális formában), pl: 1,2,3"))
        self.statusbar.showMessage("Szabo Ferenc, BO5Z8D")

    def show_first_table_please(self,mintermColumns):

        firstTable = firstTableData(mintermColumns)
        colCount = len(mintermColumns[0])
        rowCount = 0
        rows = []
        for i in firstTable:
            rowCount += 1
            if type(i) == int and i <= 1:
                rows.append(rowCount)
                rowCount = 0

        xNum = 0
        yNum = 0
        largestX = 0
        self.MintermTabla.setColumnCount(colCount)
        self.MintermTabla.setRowCount(max(rows))
        self.MintermTabla.verticalHeader().setVisible(False)


        for item in range(len(firstTable)):

            if type(firstTable[item]) == int:

                if firstTable[item] >= largestX:
                    largestX = firstTable[item]
                    rowCount = largestX
                else:
                    largestX = 0
                    yNum = yNum + 1
                    xNum = 0

            if type(firstTable[item]) == int:
                actualNumber = QtWidgets.QTableWidgetItem("___________ "+str(firstTable[item]))
            else:
                binDiff = " "
                if type(firstTable[item]) != str:
                    binDiff = str(binary_difference(tuple(firstTable[item])))

                actualNumber = QtWidgets.QTableWidgetItem(str(binary_to_decimal(firstTable[item]))+" "+binDiff)

            self.MintermTabla.setItem(xNum,yNum,actualNumber)

            xNum += 1

    def show_second_table_please(self,mintermColumns):

        abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        primeImplicants = unused_minterms(mintermColumns)
        primeImpTableSide, primeImpTable = prime_implicant_table(primeImplicants)
        primeImpTableHeader = list(primeImpTable.keys())

        self.PrimImplikansTabla.setColumnCount(len(primeImpTableHeader)+1)
        self.PrimImplikansTabla.setRowCount(len(primeImpTableSide)+1)
        self.PrimImplikansTabla.verticalHeader().setVisible(False)
        self.PrimImplikansTabla.horizontalHeader().setVisible(False)


        actualCell = ""
        for i1 in range(len(primeImpTableSide)):

            actualCell = QtWidgets.QTableWidgetItem(primeImpTableSide[i1])
            self.PrimImplikansTabla.setItem(i1+1,0,actualCell)

        for i1 in range(len(primeImpTableHeader)):

            actualCell = QtWidgets.QTableWidgetItem(str(primeImpTableHeader[i1]))
            self.PrimImplikansTabla.setItem(0, i1+1, actualCell)

        for i1 in primeImpTable:
            if len(primeImpTable[i1]) > 1:
                for i2 in primeImpTable[i1]:
                    self.PrimImplikansTabla.setItem(abc.index(i2)+1, primeImpTableHeader.index(i1)+1 ,QtWidgets.QTableWidgetItem("X"))

            else:
                self.PrimImplikansTabla.setItem(abc.index(primeImpTable[i1]) + 1, primeImpTableHeader.index(i1) + 1,QtWidgets.QTableWidgetItem("X"))

    def user_input(self):

            try:
                varC = int(self.valtozokinput.text())
                minN2 = list(self.mintermekinput.text().split(","))
                minN = []

                for i1 in minN2:
                    minN.append(int(i1))

                return varC, minN

            except:
                print("Nem jól adta meg a változók számát, vagy a mintermeket")

                varC = "ERROR"
                minN = "ERROR"
                return  varC,minN

    def csodalgoritmus(self):

        variableInput, mintermInput = self.user_input()

        if variableInput == "ERROR" or len(mintermInput) <= 1:

            print("Hibás adatok!")

        else:
            mintermColumns = minterm_grouping(variableInput, mintermInput)
            self.show_first_table_please(mintermColumns)
            self.show_second_table_please(mintermColumns)
            primeImplicants = unused_minterms(mintermColumns)
            eredmenyek = final_outcome(primeImplicants)


            if eredmenyek[-1] == "*":
                eredmenyek = eredmenyek[0:-1]
            self.EredmenyekLabel.setText(eredmenyek)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QuineMcCluskey = QtWidgets.QMainWindow()
    ui = Ui_QuineMcCluskey()
    ui.setupUi(QuineMcCluskey)
    QuineMcCluskey.show()
    sys.exit(app.exec())
