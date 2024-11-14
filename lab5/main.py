from PyQt5 import QtWidgets, uic
from swarm_algorithm import initialize_particles, algorithm, func
from copy import deepcopy
import pyqtgraph as pg



class GeneticAlgorithmGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GeneticAlgorithmGUI, self).__init__()
        uic.loadUi("ui.xml", self)
        self.setStyleSheet(
            """
            background-color: #D8D8D8; 
            color: #000000; 

            QPushButton {
                background-color: #D8D8D8; 
                color: #000000; 
            }

            QPushButton:hover {
                background-color: #D8D8D8; 
            }
            """
        )

        # Подключение функций к кнопкам
        self.pushButton.clicked.connect(self.calculate_particles)
        self.pushButton_2.clicked.connect(self.calculate)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Значение", "x1", "x2"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )

        self.particles = []
        self.funcQLE.setText("4 * ((x1 - 5) ** 2) + (x2 - 6) ** 2")
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(10000)
        self.spinBox_4.setMinimum(0)
        self.spinBox_4.setMaximum(10000)
        self.spinBox_5.setMinimum(0)
        self.spinBox_5.setMaximum(100000)
        self.spinBox_6.setMinimum(-10000)
        self.spinBox_6.setMaximum(10000)
        self.spinBox_7.setMinimum(-10000)
        self.spinBox_7.setMaximum(10000)
        self.spinBox.setValue(30)
        self.spinBox_4.setValue(0)
        self.spinBox_5.setValue(1)
        self.spinBox_6.setValue(4)
        self.spinBox_7.setValue(7)
        self.checkBox_2.setChecked(True)
        self.plotWidget = pg.PlotWidget()

        self.plotWidget.setParent(self.findChild(QtWidgets.QWidget, "plotWidget"))
        self.plotWidget.show() 

    def calculate_particles(self):
        n = self.spinBox.value()
        lower_bound = self.spinBox_6.value()
        upper_bound = self.spinBox_7.value()
        area = (lower_bound, upper_bound)
        self.particles = initialize_particles(area, n)

    def calculate(self):
        if not self.particles:
            self.calculate_particles()
        func_str = self.funcQLE.text()

        previous_iterations = self.spinBox_4.value()
        total_iterations = self.spinBox_5.value()

        shown_iterations = previous_iterations + total_iterations
        previous_iterations = max(previous_iterations, total_iterations)
        self.spinBox_4.setValue(shown_iterations)

        if self.checkBox_2.isChecked():
            result = algorithm(
                True, deepcopy(self.particles), shown_iterations, func_str
            )
        else:
            result = algorithm(
                False, deepcopy(self.particles), shown_iterations, func_str
            )

        self.display_particles_in_table(result[-1])
        self.display_best_val(result[-1])

        self.particles = result[-1]


    def display_particles_in_table(self, contents):
        self.tableWidget.setRowCount(0)
        lower_bound = self.spinBox_6.value()
        upper_bound = self.spinBox_7.value()

        self.plotWidget.clear()
        self.plotWidget.resize(220, 220)

        x_values = []
        y_values = []
        z_values = []

        for _, gene in enumerate(contents):
            func_str = self.funcQLE.text()
            position = (gene["x1"], gene["x2"])
            value = func(func_str, *position)

            # Добавляем новую строку в таблицу
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

            # Заполняем ячейки таблицы
            self.tableWidget.setItem(
                row_position, 1, QtWidgets.QTableWidgetItem(str(position[0]))
            )
            self.tableWidget.setItem(
                row_position, 2, QtWidgets.QTableWidgetItem(str(position[1]))
            )
            self.tableWidget.setItem(
                row_position, 0, QtWidgets.QTableWidgetItem(str(value))
            )

            x_values.append(position[0])
            y_values.append(position[1])
            z_values.append(value)

        self.plotWidget.plot(x_values, y_values, pen=None, symbol='o', symbolSize=5)
        self.plotWidget.showGrid(x = True, y = True)
        self.plotWidget.addLegend()

        self.plotWidget.setXRange(lower_bound, upper_bound)
        self.plotWidget.setYRange(lower_bound, upper_bound)    
 
        self.plotWidget.setLabel('left', 'X2')
        self.plotWidget.setLabel('bottom', 'X1')

        self.plotWidget.show()

    def display_best_val(self, genes):
        best_gene = (genes[0]["x1"], genes[0]["x2"])
        func_str = self.funcQLE.text()
        value = func(func_str, *best_gene)
        result_text = f"Значение: {value},\n x1: {best_gene[0]},\n x2: {best_gene[1]}"
        self.plainTextEdit.setPlainText(result_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = GeneticAlgorithmGUI()
    window.show()
    app.exec_()
