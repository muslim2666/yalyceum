import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.load_data()
    
    def load_data(self):
        connection = sqlite3.connect("../data/coffee.sqlite")
        cursor = connection.cursor()
        
        cursor.execute("""
        SELECT * FROM cofee
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
