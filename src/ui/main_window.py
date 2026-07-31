from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QStatusBar,
    QMenuBar,
    QMenu
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DC Studio")
        self.resize(1000, 700)

        etiqueta = QLabel("Bienvenido a DC Studio v0.0.2")
        self.setCentralWidget(etiqueta)

        barra_estado = QStatusBar()
        barra_estado.showMessage("Listo")
        self.setStatusBar(barra_estado)
        barra_menu = self.menuBar()
        menu_archivo = barra_menu.addMenu("Archivo")
        menu_editar = barra_menu.addMenu("Editar")
        menu_imagen = barra_menu.addMenu("Imagen")
        menu_filtros = barra_menu.addMenu("Filtros")
        menu_ver = barra_menu.addMenu("Ver")
        menu_ayuda = barra_menu.addMenu("Ayuda")