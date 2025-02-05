#school_21_lovejoye

import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from UI.main import Ui_MainWindow
from UI.addEditCoffeeForm import Ui_Dialog 


class CoffeeApp(QMainWindow, Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.load_data()

        self.addButton.clicked.connect(self.add_coffee)

    def load_data(self):
        connection = sqlite3.connect("data/coffee.sqlite")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id, name, stepen, zerno, vkus, price, objem FROM cofee
        """)
        rows = cursor.fetchall()

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Название", "Обжарка", "Молотый/Зерна", "Описание", "Цена", "Объем"
        ])

        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        connection.close()

    def add_coffee(self):
        """Открытие формы добавления кофе"""
        dialog = AddEditCoffeeDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted: 
            self.load_data()  


class AddEditCoffeeDialog(QDialog, Ui_Dialog): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.saveButton.clicked.connect(self.save_coffee)

    def save_coffee(self):
        name = self.nameLineEdit.text()
        stepen = self.stepenLineEdit.text()
        zerno = self.zernoComboBox.currentText()
        vkus = self.vkusPlainTextEdit.toPlainText()
        price = self.priceSpinBox.value()
        objem = self.objemSpinBox.value()

        if not name or not stepen:
            return 

        connection = sqlite3.connect("data/coffee.sqlite")  
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO cofee (name, stepen, zerno, vkus, price, objem) 
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, stepen, zerno, vkus, price, objem))

        connection.commit()
        connection.close()
        self.accept() 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CoffeeApp()
    ex.show()
    sys.exit(app.exec())