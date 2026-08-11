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

        self.configurar_ventana()
        self.crear_barra_de_estado()
        self.crear_area_imagen()
        self.crear_menu()
        self.crear_acciones()
        self.crear_barra_herramientas()

    def configurar_ventana(self):
        self.setWindowTitle("DC Studio")
        self.resize(1000, 700)    

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

    def nuevo_archivo(self):

            self.etiqueta.clear()
            self.etiqueta.setText("Nuevo proyecto")
            self.barra_estado.showMessage("Nuevo proyecto creado")
  
    def crear_barra_de_estado(self):

        self.barra_estado = QStatusBar()
        self.setStatusBar(self.barra_estado)
        self.barra_estado.showMessage("Listo") 

    def crear_menu(self):

        barra_menu = self.menuBar()

        self.menu_archivo = barra_menu.addMenu("Archivo")
        self.menu_editar = barra_menu.addMenu("Editar")
        self.menu_imagen = barra_menu.addMenu("Imagen")
        self.menu_filtros = barra_menu.addMenu("Filtros")
        self.menu_ver = barra_menu.addMenu("Ver")
        self.menu_ayuda = barra_menu.addMenu("Ayuda")

    def crear_area_imagen(self):
        self.etiqueta = QLabel("Bienvenido a DC Studio")
        self.etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.etiqueta)

    def crear_acciones(self):

        self.accion_nuevo = QAction("Nuevo", self)
        self.accion_abrir = QAction("Abrir", self)
        self.accion_guardar = QAction("Guardar", self)

        self.accion_abrir.triggered.connect(self.abrir_archivo)
        self.accion_nuevo.triggered.connect(self.nuevo_archivo)

        self.menu_archivo.addAction(self.accion_nuevo)
        self.menu_archivo.addAction(self.accion_abrir)
        self.menu_archivo.addAction(self.accion_guardar)

    def crear_barra_herramientas(self):

        barra = QToolBar("Principal")

        self.addToolBar(barra)

        barra.addAction(self.accion_nuevo)
        barra.addAction(self.accion_abrir)
        barra.addAction(self.accion_guardar)

    def nuevo_archivo(self):

        self.etiqueta.clear()
        self.etiqueta.setText("Nuevo proyecto")
        self.barra_estado.showMessage("Nuevo proyecto creado")