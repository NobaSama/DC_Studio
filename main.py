import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel


app = QApplication(sys.argv)

ventana = QLabel("Bienvenido a DC Studio")

ventana.resize(500, 300)

ventana.setWindowTitle("DC Studio")

ventana.show()

sys.exit(app.exec())