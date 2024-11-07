from PyQt5 import QtWidgets, uic
from genetic_algorithm import initialize_genes, algorithm, func
from copy import deepcopy

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
        self.pushButton.clicked.connect(self.calculate_chromosomes)
        self.pushButton_2.clicked.connect(self.calculate)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Значение", "x1", "x2"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )

        self.genes = []
        self.funcQLE.setText("4 * ((x1 - 5) ** 2) + (x2 - 6) ** 2")
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(10000)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(100)
        self.spinBox_4.setMinimum(0)
        self.spinBox_4.setMaximum(10000)
        self.spinBox_5.setMinimum(0)
        self.spinBox_5.setMaximum(100000)
        self.spinBox_6.setMinimum(-10000)
        self.spinBox_6.setMaximum(10000)
        self.spinBox_7.setMinimum(-10000)
        self.spinBox_7.setMaximum(10000)
        self.spinBox.setValue(30)
        self.spinBox_2.setValue(30)
        self.spinBox_4.setValue(0)
        self.spinBox_5.setValue(50)
        self.spinBox_6.setValue(4)
        self.spinBox_7.setValue(7)
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(True)

    def calculate_chromosomes(self):
        num_genes = self.spinBox.value()
        lower_bound = self.spinBox_6.value()
        upper_bound = self.spinBox_7.value()
        area = (lower_bound, upper_bound)
        if self.checkBox_1.isChecked():
            self.genes = initialize_genes(True, area, num_genes)
        else:
            self.genes = initialize_genes(False, area, num_genes)
        

    def calculate(self):
        if not self.genes:
            self.calculate_chromosomes()
        func_str = self.funcQLE.text()
        mutation_probability = self.spinBox_2.value()

        previous_iterations = self.spinBox_4.value()
        total_iterations = self.spinBox_5.value()
        shown_iterations = previous_iterations + total_iterations
        previous_iterations = max(previous_iterations, total_iterations)
        self.spinBox_4.setValue(shown_iterations)
        lower_bound = self.spinBox_6.value()
        upper_bound = self.spinBox_7.value()
        area = (lower_bound, upper_bound)

        if self.checkBox_2.isChecked():
            result = algorithm(
                True, deepcopy(self.genes), shown_iterations, func_str, mutation_probability, area
            )
        else:
            result = algorithm(
                False, deepcopy(self.genes), shown_iterations, func_str, mutation_probability, area
            )
        self.display_genes_in_table(result[previous_iterations])
        self.display_best_gene(result[-1])

    def display_genes_in_table(self, contents):
        self.tableWidget.setRowCount(0)
        for i, gene in enumerate(contents):
            func_str = self.funcQLE.text()
            value = func(func_str, *gene)
            position = gene

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

    def display_best_gene(self, genes):
        best_gene = genes[0]
        func_str = self.funcQLE.text()
        value = func(func_str, *best_gene)
        result_text = f"Значение: {value},\n x1: {best_gene[0]},\n x2: {best_gene[1]}"
        self.plainTextEdit.setPlainText(result_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = GeneticAlgorithmGUI()
    window.show()
    app.exec_()