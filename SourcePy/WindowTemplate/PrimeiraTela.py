# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrimeiraTela.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JanelaInicial(object):
    def setupUi(self, JanelaInicial):
        JanelaInicial.setObjectName("JanelaInicial")
        JanelaInicial.resize(750, 261)
        JanelaInicial.setMinimumSize(QtCore.QSize(750, 261))
        JanelaInicial.setMaximumSize(QtCore.QSize(750, 261))
        JanelaInicial.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/bagla.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        JanelaInicial.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(JanelaInicial)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelTentativas = QtWidgets.QLabel(JanelaInicial)
        self.labelTentativas.setEnabled(True)
        self.labelTentativas.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTentativas.setObjectName("labelTentativas")
        self.gridLayout_2.addWidget(self.labelTentativas, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.ImagemBagla = QtWidgets.QLabel(JanelaInicial)
        self.ImagemBagla.setText("")
        self.ImagemBagla.setPixmap(QtGui.QPixmap(":/newPrefix/bagla.png"))
        self.ImagemBagla.setScaledContents(False)
        self.ImagemBagla.setObjectName("ImagemBagla")
        self.gridLayout_2.addWidget(self.ImagemBagla, 0, 0, 1, 1)
        self.botaoNao = QtWidgets.QPushButton(JanelaInicial)
        self.botaoNao.setObjectName("botaoNao")
        self.gridLayout_2.addWidget(self.botaoNao, 2, 2, 1, 1)
        self.widget = QtWidgets.QWidget(JanelaInicial)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.labelTexto = QtWidgets.QLabel(self.widget)
        self.labelTexto.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelTexto.setObjectName("labelTexto")
        self.gridLayout.addWidget(self.labelTexto, 2, 0, 1, 1)
        self.labelTitulo = QtWidgets.QLabel(self.widget)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelTitulo.setObjectName("labelTitulo")
        self.gridLayout.addWidget(self.labelTitulo, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 3)
        self.botaoSim = QtWidgets.QPushButton(JanelaInicial)
        self.botaoSim.setObjectName("botaoSim")
        self.gridLayout_2.addWidget(self.botaoSim, 2, 3, 1, 1)

        self.retranslateUi(JanelaInicial)
        QtCore.QMetaObject.connectSlotsByName(JanelaInicial)

    def retranslateUi(self, JanelaInicial):
        _translate = QtCore.QCoreApplication.translate
        JanelaInicial.setWindowTitle(_translate("JanelaInicial", "Aqui ?? bagla!"))
        self.labelTentativas.setText(_translate("JanelaInicial", "Numero de tentativas: "))
        self.botaoNao.setText(_translate("JanelaInicial", "N??o"))
        self.labelTexto.setText(_translate("JanelaInicial", "<html><head/><body><p><span style=\" font-size:10pt;\"><br/>Voc?? consegue me fechar?</span></p></body></html>"))
        self.labelTitulo.setText(_translate("JanelaInicial", "<html><head/><body><p><span style=\" font-size:16pt;\">Bagla Puzzle</span></p></body></html>"))
        self.botaoSim.setText(_translate("JanelaInicial", "Sim"))
import Resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaInicial = QtWidgets.QWidget()
    ui = Ui_JanelaInicial()
    ui.setupUi(JanelaInicial)
    JanelaInicial.show()
    sys.exit(app.exec_())
