from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit


class QlineE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLinseEdit')
        # Componente QLineEdit
        linea_texto = QLineEdit()
        # Establecemos el máximo de caracteres a capturar
        linea_texto.setMaxLength(15)
        # Establecemos un texto de ayuda
        linea_texto.setPlaceholderText('Introduce tu nombre:')
        # Solo lectura
        # linea_texto.setReadOnly(True)
        # Evento enter, cambio seleccion texto, cambio texto
        linea_texto.returnPressed.connect(self.enter_presionado)
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        linea_texto.textChanged.connect(self.cambio_texto)

        # Publicamos este componente
        self.setCentralWidget(linea_texto)

    def enter_presionado(self):
        print('Se presionó el enter')
        self.centralWidget().setText('Juan Perez!')

    def cambio_seleccion(self):
        print('Selección de texto')
        print(self.centralWidget().selectedText())

    def cambio_texto(self, nuevo_texto):
        print('Cambio en el texto')
        print(nuevo_texto)

if __name__ == '__main__':
    app = QApplication([])
    ventana = QlineE()
    ventana.show()
    app.exec()