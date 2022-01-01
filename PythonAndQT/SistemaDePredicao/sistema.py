# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistema.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import sys
from os.path import dirname, realpath, join
import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AutoReg

from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_arquivo = QtWidgets.QPushButton(self.centralwidget)
        self.bt_arquivo.setGeometry(QtCore.QRect(660, 40, 71, 31))
        self.bt_arquivo.setObjectName("bt_arquivo")
        self.bt_predizer = QtWidgets.QPushButton(self.centralwidget)
        self.bt_predizer.setGeometry(QtCore.QRect(610, 390, 131, 51))
        self.bt_predizer.setObjectName("bt_predizer")
        self.txt_predicao = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_predicao.setGeometry(QtCore.QRect(20, 417, 571, 21))
        self.txt_predicao.setObjectName("txt_predicao")
        self.lb_predicaoFaturamento = QtWidgets.QLabel(self.centralwidget)
        self.lb_predicaoFaturamento.setGeometry(QtCore.QRect(20, 30, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lb_predicaoFaturamento.setFont(font)
        self.lb_predicaoFaturamento.setObjectName("lb_predicaoFaturamento")
        self.txt_totalFaturado = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_totalFaturado.setGeometry(QtCore.QRect(430, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_totalFaturado.setFont(font)
        self.txt_totalFaturado.setText("")
        self.txt_totalFaturado.setObjectName("txt_totalFaturado")
        self.lb_totalFaturado = QtWidgets.QLabel(self.centralwidget)
        self.lb_totalFaturado.setGeometry(QtCore.QRect(430, 20, 111, 16))
        self.lb_totalFaturado.setObjectName("lb_totalFaturado")
        self.sb_colunas = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_colunas.setGeometry(QtCore.QRect(610, 50, 42, 22))
        self.sb_colunas.setObjectName("sb_colunas")
        self.lb_tipoPredicao = QtWidgets.QLabel(self.centralwidget)
        self.lb_tipoPredicao.setGeometry(QtCore.QRect(620, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_tipoPredicao.setFont(font)
        self.lb_tipoPredicao.setObjectName("lb_tipoPredicao")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(610, 110, 140, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_media = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_media.setChecked(True)
        self.rb_media.setObjectName("rb_media")
        self.verticalLayout.addWidget(self.rb_media)
        self.rb_desvioPadrao = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_desvioPadrao.setObjectName("rb_desvioPadrao")
        self.verticalLayout.addWidget(self.rb_desvioPadrao)
        self.rb_mediaPonderada = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_mediaPonderada.setObjectName("rb_mediaPonderada")
        self.verticalLayout.addWidget(self.rb_mediaPonderada)
        self.rb_segregacaoDados = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_segregacaoDados.setObjectName("rb_segregacaoDados")
        self.verticalLayout.addWidget(self.rb_segregacaoDados)
        self.rb_regressaoLinear = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_regressaoLinear.setObjectName("rb_regressaoLinear")
        self.verticalLayout.addWidget(self.rb_regressaoLinear)
        self.rb_seriesTemporais = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_seriesTemporais.setObjectName("rb_seriesTemporais")
        self.verticalLayout.addWidget(self.rb_seriesTemporais)
        self.tb_faturamento = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_faturamento.setGeometry(QtCore.QRect(20, 80, 571, 321))
        self.tb_faturamento.setObjectName("tb_faturamento")
        self.tb_faturamento.setColumnCount(3)
        self.tb_faturamento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_faturamento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_faturamento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_faturamento.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_arquivo.setText(_translate("MainWindow", "Arquivo"))
        self.bt_predizer.setText(_translate("MainWindow", "Predizer"))
        self.lb_predicaoFaturamento.setText(_translate("MainWindow", "Predição de faturamento"))
        self.lb_totalFaturado.setText(_translate("MainWindow", "Total faturado"))
        self.lb_tipoPredicao.setText(_translate("MainWindow", "Tipo de predição"))
        self.rb_media.setText(_translate("MainWindow", "Média"))
        self.rb_desvioPadrao.setText(_translate("MainWindow", "Desvio padrão"))
        self.rb_mediaPonderada.setText(_translate("MainWindow", "Média ponderada"))
        self.rb_segregacaoDados.setText(_translate("MainWindow", "Segregação de dados"))
        self.rb_regressaoLinear.setText(_translate("MainWindow", "Regressão Linear"))
        self.rb_seriesTemporais.setText(_translate("MainWindow", "Séries temporais"))
        item = self.tb_faturamento.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ano"))
        item = self.tb_faturamento.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mes"))
        item = self.tb_faturamento.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Faturamento"))

        self.bt_arquivo.clicked.connect(self.openFile)
        self.bt_predizer.clicked.connect(self.predicao)

    def openFile(self):
        # Localiza o caminho do arquivo
        Tk().withdraw()
        path = askopenfilename()
        self.all_data = pd.read_csv(path)

        # Carrega o arquivo na tabela tb_faturamento
        numColumn = self.sb_colunas.value()
        if numColumn == 0:
            numRows = len(self.all_data.index)
        else:
            numRows = numColumn
        self.tb_faturamento.setColumnCount(len(self.all_data.columns))
        self.tb_faturamento.setRowCount(numRows)
        self.tb_faturamento.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_faturamento.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tb_faturamento.resizeColumnsToContents()
        self.tb_faturamento.resizeRowsToContents

        # Soma do faturamento
        soma_faturamento = str('R$%0.02f' %sum(self.all_data['Faturamento']))
        self.txt_totalFaturado.setText(soma_faturamento)


    def predicao(self):
        df = self.all_data
        ### Média ###
        if self.rb_media.isChecked() == True:
            media = df['Faturamento'].mean()
            predicao = 'Nos proximos meses sera faturado R$ ' + str('%0.02f' %media) + '/mes em media.'
            self.txt_predicao.setText(predicao)
        ### Desvio Padrão ###
        elif self.rb_desvioPadrao.isChecked() == True:
            media = df['Faturamento'].mean()
            desvpad = df['Faturamento'].std()
            coe_var = (desvpad / media) * 100
            predicao = 'Predição de R$ ' + str('%0.02f' %media) + '/mes podendo variar em torno de ' + str('%0.02f' %coe_var) + '%'
            self.txt_predicao.setText(predicao)
        ### Media Ponderada ###
        elif self.rb_mediaPonderada.isChecked() == True:
            lista = np.transpose((np.array([df['Faturamento'].tail(), np.arange(1,6)])))
            pesos = np.arange(1,6)
            df_ult = pd.DataFrame(lista, columns = ['Ultimos', 'Pesos'])
            df_ult['Ponderado'] = df_ult['Ultimos'] * df_ult['Pesos']
            med_pond = df_ult['Ponderado'].sum() / df_ult['Pesos'].sum()
            predicao = 'Predição ponderada de R$ ' + str('%0.02f' %med_pond) + ' para os próximos meses.'
            self.txt_predicao.setText(predicao)
        ### Segregação dos Dados ###
        elif self.rb_segregacaoDados.isChecked() == True:
            df_janeiro = df.loc[df['Mes'] == 1]
            med_seg = df_janeiro['Faturamento'].mean()
            predicao = 'Predição segregada de R$ ' + str('%0.02f' %med_seg) + ' para janeiro.'
            self.txt_predicao.setText(predicao)
        ### Regressão Linear ###
        elif self.rb_regressaoLinear.isChecked() == True:
            coefficients = np.polyfit(df.index, df['Faturamento'], 1)
            a = coefficients[0]
            b = coefficients[1]
            jan_reta = a * 36 + b
            predicao = 'Predição por regressão de R$ ' + str('%0.02f' %jan_reta) + ' para janeiro.'
            self.txt_predicao.setText(predicao)
        ### Series temporais ###
        elif self.rb_seriesTemporais.isChecked() == True:
            model = AutoReg(df['Faturamento'], lags=1, old_names=True) #old_names só foi utilizado por conta de um aviso da próxima versão
            model_fit = model.fit()
            yhat = model_fit.predict(len(df['Faturamento']), len(df['Faturamento'])+2)
            pred = np.array(yhat)
            predicao = 'Predição por serie temporal de R$ ' + str('%0.02f' %pred[0]) + ' para janeiro e R$ ' + str('%0.02f' %pred[1]) + ' para fevereiro.'
            self.txt_predicao.setText(predicao)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())