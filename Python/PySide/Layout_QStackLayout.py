from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QStackedLayout


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class Layoutt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en PySide')
        # Layout QStackedLayout
        layout = QStackedLayout()
        # Por default solo se visualiza el primer widget agregado
        layout.addWidget(Color('red'))# Indice 0
        layout.addWidget(Color('green'))# Indice 1
        layout.addWidget(Color('yellow'))# Indice 2
        layout.setCurrentIndex(1)
        # Creamos un componente generico para poder publicar el layout
        componente = QWidget()
        componente.setLayout(layout)
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Layoutt()
    ventana.show()
    app.exec()