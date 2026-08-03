from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QStatusBar,
    QToolBar,
    QMenuBar,
    QMenu
)
from PySide6.QtGui import QAction

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

        # Barra de herramientas
        barra_herramientas = QToolBar("Principal")
        self.addToolBar(barra_herramientas)

        accion_nuevo = QAction("Nuevo", self)
        accion_abrir = QAction("Abrir", self)
        accion_guardar = QAction("Guardar", self)

        barra_herramientas.addAction(accion_nuevo)
        barra_herramientas.addAction(accion_abrir)
        barra_herramientas.addAction(accion_guardar)
