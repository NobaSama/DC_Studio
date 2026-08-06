from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QStatusBar,
    QToolBar,
    QFileDialog,
    QMenuBar,
    QMenu
)

from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DC Studio")
        self.resize(1000, 700)

        self.etiqueta = QLabel("Bienvenido a DC Studio")
        self.etiqueta.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.etiqueta)

        self.barra_estado = QStatusBar()
        self.barra_estado.showMessage("Listo")
        self.setStatusBar(self.barra_estado)
        barra_menu = self.menuBar()
        self.menu_archivo = barra_menu.addMenu("Archivo")
        self.menu_editar = barra_menu.addMenu("Editar")
        self.menu_imagen = barra_menu.addMenu("Imagen")
        self.menu_filtros = barra_menu.addMenu("Filtros")
        self.menu_ver = barra_menu.addMenu("Ver")
        self.menu_ayuda = barra_menu.addMenu("Ayuda")

        # Barra de herramientas
        barra_herramientas = QToolBar("Principal")
        self.addToolBar(barra_herramientas)

        accion_nuevo = QAction("Nuevo", self)
        accion_abrir = QAction("Abrir", self)
        accion_guardar = QAction("Guardar", self)

        accion_abrir.triggered.connect(self.abrir_archivo)

        barra_herramientas.addAction(accion_nuevo)
        barra_herramientas.addAction(accion_abrir)
        barra_herramientas.addAction(accion_guardar)

    def abrir_archivo(self):

        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp);;Todos los archivos (*)"
        )
        if archivo:
            imagen = QPixmap(archivo)
            self.etiqueta.setPixmap(imagen)
            self.etiqueta.setScaledContents(True)
            self.statusBar().showMessage(f"Imagen cargada: {archivo}")