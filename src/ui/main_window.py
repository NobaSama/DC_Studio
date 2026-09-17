from PySide6.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QToolBar,
    QFileDialog,
    QGraphicsView,
    QGraphicsScene,
    QLabel
)

from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import Qt, QPointF, Signal


class CanvasView(QGraphicsView):

    zoom_cambiado = Signal(float)

    def __init__(self, scene):
        super().__init__(scene)

        self.factor_zoom = 1.15
        self.zoom_minimo = 0.10
        self.zoom_maximo = 10.0

        self.setTransformationAnchor(
            QGraphicsView.NoAnchor
        )

        self.setResizeAnchor(
            QGraphicsView.NoAnchor
        )

    def wheelEvent(self, event):

        posicion_mouse = event.position()

        posicion_escena_antes = self.mapToScene(
            posicion_mouse.toPoint()
        )

        if event.angleDelta().y() > 0:

            factor = self.factor_zoom

        else:

            factor = 1 / self.factor_zoom

        transformacion_actual = self.transform()
        escala_actual = transformacion_actual.m11()

        nueva_escala = escala_actual * factor

        if nueva_escala < self.zoom_minimo:
            factor = self.zoom_minimo / escala_actual

        elif nueva_escala > self.zoom_maximo:
            factor = self.zoom_maximo / escala_actual

        self.scale(factor, factor)

        posicion_escena_despues = self.mapToScene(
            posicion_mouse.toPoint()
        )

        desplazamiento = (
            posicion_escena_despues
            - posicion_escena_antes
        )

        self.translate(
            desplazamiento.x(),
            desplazamiento.y()
        )

        escala_actual = self.transform().m11()
        porcentaje_zoom = escala_actual * 100

        self.zoom_cambiado.emit(porcentaje_zoom)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.configurar_ventana()
        self.crear_barra_de_estado()
        self.crear_indicador_zoom()
        self.crear_area_imagen()
        self.crear_menu()
        self.crear_acciones()
        self.crear_barra_herramientas()

    def configurar_ventana(self):
        self.setWindowTitle("DC Studio")
        self.resize(1000, 700)

    def crear_barra_de_estado(self):

        self.barra_estado = QStatusBar()
        self.setStatusBar(self.barra_estado)
        self.barra_estado.showMessage("Listo")

    def crear_indicador_zoom(self):

        self.indicador_zoom = QLabel("Zoom: 100%")

        self.barra_estado.addPermanentWidget(
            self.indicador_zoom
        )

    def crear_area_imagen(self):

        self.escena = QGraphicsScene()

        self.canvas = CanvasView(self.escena)

        self.canvas.zoom_cambiado.connect(
            self.actualizar_zoom
        )

        self.canvas.setAlignment(Qt.AlignCenter)

        self.canvas.setBackgroundBrush(
            Qt.lightGray
        )

        self.setCentralWidget(self.canvas)

        self.imagen_actual = None
        self.elemento_imagen = None

    def crear_menu(self):

        barra_menu = self.menuBar()

        self.menu_archivo = barra_menu.addMenu("Archivo")
        self.menu_editar = barra_menu.addMenu("Editar")
        self.menu_imagen = barra_menu.addMenu("Imagen")
        self.menu_filtros = barra_menu.addMenu("Filtros")
        self.menu_ver = barra_menu.addMenu("Ver")
        self.menu_ayuda = barra_menu.addMenu("Ayuda")

    def crear_acciones(self):

        self.accion_nuevo = QAction("Nuevo", self)
        self.accion_abrir = QAction("Abrir", self)
        self.accion_guardar = QAction("Guardar", self)

        self.accion_abrir.triggered.connect(
            self.abrir_archivo
        )

        self.accion_nuevo.triggered.connect(
            self.nuevo_archivo
        )

        self.accion_guardar.triggered.connect(
            self.guardar_archivo
        )

        self.menu_archivo.addAction(
            self.accion_nuevo
        )

        self.menu_archivo.addAction(
            self.accion_abrir
        )

        self.menu_archivo.addAction(
            self.accion_guardar
        )

    def crear_barra_herramientas(self):

        barra = QToolBar("Principal")

        self.addToolBar(barra)

        barra.addAction(self.accion_nuevo)
        barra.addAction(self.accion_abrir)
        barra.addAction(self.accion_guardar)

    def abrir_archivo(self):

        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp);;Todos los archivos (*)"
        )

        if archivo:

            self.imagen_actual = QPixmap(archivo)

            self.escena.clear()

            self.elemento_imagen = (
                self.escena.addPixmap(
                    self.imagen_actual
                )
            )

            self.escena.setSceneRect(
                self.elemento_imagen.boundingRect()
            )

            self.canvas.fitInView(
                self.elemento_imagen,
                Qt.KeepAspectRatio
            )

            self.barra_estado.showMessage(
                f"Imagen cargada: {archivo}"
            )

    def nuevo_archivo(self):

        self.escena.clear()

        self.imagen_actual = None
        self.elemento_imagen = None

        self.barra_estado.showMessage(
            "Nuevo proyecto creado"
        )

    def guardar_archivo(self):

        if self.imagen_actual is None:

            self.barra_estado.showMessage(
                "No hay ninguna imagen para guardar"
            )

            return

        archivo, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Imagen",
            "",
            "PNG (*.png);;JPEG (*.jpg *.jpeg);;Todos los archivos (*)"
        )

        if archivo:

            resultado = self.imagen_actual.save(
                archivo
            )

            if resultado:

                self.barra_estado.showMessage(
                    f"Imagen guardada: {archivo}"
                )

            else:

                self.barra_estado.showMessage(
                    "Error al guardar la imagen"
                )
                
    def actualizar_zoom(self, porcentaje):

        self.indicador_zoom.setText(
            f"Zoom: {porcentaje:.0f}%"
        )           