from PyQt5 import QtCore, QtGui, QtWidgets
from main import *


class Ui_QuineMcCluskey(object):
    def setupUi(self, QuineMcCluskey):

        QuineMcCluskey.setObjectName("QuineMcCluskey")
        QuineMcCluskey.resize(1000, 720)

        self.centralwidget = QtWidgets.QWidget(QuineMcCluskey)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cluck)

        self.gridLayout.addWidget(self.pushButton_2, 14, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.egyszerusitesitablazat = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.egyszerusitesitablazat.sizePolicy().hasHeightForWidth())
        self.egyszerusitesitablazat.setSizePolicy(sizePolicy)
        self.egyszerusitesitablazat.setObjectName("egyszerusitesitablazat")
        self.gridLayout.addWidget(self.egyszerusitesitablazat, 0, 0, 1, 4)

        self.tablazattablazat = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablazattablazat.sizePolicy().hasHeightForWidth())
        self.tablazattablazat.setSizePolicy(sizePolicy)
        self.tablazattablazat.setObjectName("tablazattablazat")
        self.gridLayout.addWidget(self.tablazattablazat,9,2,6,3)

        self.valtozokinput = QtWidgets.QLineEdit(self.centralwidget)
        self.valtozokinput.setObjectName("valtozokinput")
        self.gridLayout.addWidget(self.valtozokinput, 11, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.mintermekinput = QtWidgets.QLineEdit(self.centralwidget)
        self.mintermekinput.setObjectName("mintermekinput")
        self.gridLayout.addWidget(self.mintermekinput, 13, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)

        self.mintermekszama = QtWidgets.QLabel(self.centralwidget)
        self.mintermekszama.setObjectName("mintermekszama")
        self.gridLayout.addWidget(self.mintermekszama, 12, 0, 1, 1)

        self.valtozokszama = QtWidgets.QLabel(self.centralwidget)
        self.valtozokszama.setObjectName("valtozokszama")
        self.gridLayout.addWidget(self.valtozokszama, 10, 0, 1, 1)

        QuineMcCluskey.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QuineMcCluskey)
        self.statusbar.setObjectName("statusbar")
        QuineMcCluskey.setStatusBar(self.statusbar)

        self.retranslateUi(QuineMcCluskey)
        QtCore.QMetaObject.connectSlotsByName(QuineMcCluskey)

    def retranslateUi(self, QuineMcCluskey):
        _translate = QtCore.QCoreApplication.translate
        QuineMcCluskey.setWindowTitle(_translate("QuineMcCluskey", "Quine-McCluskey"))
        self.pushButton_2.setText(_translate("QuineMcCluskey", "GO!"))
        self.mintermekszama.setText(_translate("QuineMcCluskey", "Mintermek (decimális formában) pl: 1,2,4,6:"))
        self.valtozokszama.setText(_translate("QuineMcCluskey", "Változók száma:"))

    def showFirstTablePlease(self,mintermColumns):

        firstTable = firstTableData(mintermColums)

        colCount = len(mintermColums[0])
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

        self.egyszerusitesitablazat.setColumnCount(colCount)
        self.egyszerusitesitablazat.setRowCount(max(rows))
        self.egyszerusitesitablazat.verticalHeader().setVisible(False)



        for item in range(len(firstTable)):

            if type(firstTable[item]) == int:

                if firstTable[item] > largestX:
                    largestX = firstTable[item]
                    rowCount = largestX
                else:
                    largestX = 0
                    yNum = yNum + 1
                    xNum = 0

            if type(firstTable[item]) == int:
                actualNumber = QtWidgets.QTableWidgetItem("_______________ "+str(firstTable[item]))
            else:

                actualNumber = QtWidgets.QTableWidgetItem(str(binary_to_decimal(firstTable[item])))

            self.egyszerusitesitablazat.setItem(xNum,yNum,actualNumber)

            xNum += 1

    def showSecondTablePlease(self,mintermColumns):

        abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        primeImplicants = unused_minterms(mintermColums)
        primeImpTableSide, primeImpTable = prime_implicant_table(primeImplicants)
        primeImpTableHeader = list(primeImpTable.keys())

        self.tablazattablazat.setColumnCount(len(primeImpTableHeader)+1)
        self.tablazattablazat.setRowCount(len(primeImpTableSide)+1)
        self.tablazattablazat.verticalHeader().setVisible(False)
        self.tablazattablazat.horizontalHeader().setVisible(False)

        actualCell = ""

        for i1 in range(len(primeImpTableSide)):

            actualCell = QtWidgets.QTableWidgetItem(primeImpTableSide[i1])
            self.tablazattablazat.setItem(i1+1,0,actualCell)

        for i1 in range(len(primeImpTableHeader)):

            actualCell = QtWidgets.QTableWidgetItem(str(primeImpTableHeader[i1]))
            self.tablazattablazat.setItem(0, i1+1, actualCell)

        for i1 in primeImpTable:
            if len(primeImpTable[i1]) > 1:
                for i2 in primeImpTable[i1]:
                    self.tablazattablazat.setItem(abc.index(i2)+1, primeImpTableHeader.index(i1)+1 ,QtWidgets.QTableWidgetItem("X"))

            else:
                self.tablazattablazat.setItem(abc.index(primeImpTable[i1]) + 1, primeImpTableHeader.index(i1) + 1,QtWidgets.QTableWidgetItem("X"))

    def user_input(self):


            try:
                varC = int(self.valtozokinput.text())
                minN = list(self.mintermekinput.text().split(","))

                return varC, minN

            except:
                variableCount3 = 0
                print("Nem jól adta meg a változók számát, vagy a mintermeket")

                varC = "ERROR"
                minN = "ERROR"
                return varC,minN



    def cluck(self):

        variableCount3,mintermNumbers3 = self.user_input()

        if variableCount3 == "ERROR" or len(mintermNumbers3) <= 1:

            print("Hibás adatok!")

        else:

            mintermColums = minterm_simplification(variableCount, mintermNumbers)

            self.showFirstTablePlease(mintermColums)
            self.showSecondTablePlease(mintermColums)

            print(mintermColums)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QuineMcCluskey = QtWidgets.QMainWindow()
    ui = Ui_QuineMcCluskey()
    ui.setupUi(QuineMcCluskey)
    QuineMcCluskey.show()
    sys.exit(app.exec_())
