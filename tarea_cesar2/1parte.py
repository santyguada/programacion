import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        
        # Crear layout de cuadrícula
        layout = QGridLayout()
        self.setLayout(layout)
        
        # Título del formulario (grande y centrado)
        titulo = QLabel("Formulario de Afiliación")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(titulo, 0, 0, 1, 2)  # Ocupa dos columnas
        
        # Campos del formulario
        campos = [
            ("Nombre", 1),
            ("Apellido", 2),
            ("DNI", 3),
            ("Fecha de nacimiento", 4)
        ]
        
        #se agrega aparte para uso posterior sin complicaciones
        for texto, fila in campos:
            # Crear etiqueta
            label = QLabel(texto + ":")
            layout.addWidget(label, fila, 0)
            
            # Crear campo de entrada
            entrada = QLineEdit()
            layout.addWidget(entrada, fila, 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_form = VentanaFormulario()
    ventana_form.show()
    sys.exit(app.exec_())