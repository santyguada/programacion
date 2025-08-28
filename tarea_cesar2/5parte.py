
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout, 
                             QPushButton, QVBoxLayout, QMessageBox)
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
        titulo.setStyleSheet("color: black; color:red ")        
        layout.addWidget(titulo, 0, 0, 1, 2)  # Ocupa dos columnas
        
        # Campos del formulario (guardamos referencias para acceder luego)
        self.campos = {}
        campos_config = [
            ("Nombre", 1),
            ("Apellido", 2),
            ("DNI", 3),
            ("Fecha de nacimiento", 4)
        ]
        
        for texto, fila in campos_config:
            # Crear etiqueta
            label = QLabel(texto + ":")
            layout.addWidget(label, fila, 0)
            
            # Crear campo de entrada y guardar referencia
            entrada = QLineEdit()
            layout.addWidget(entrada, fila, 1)
            self.campos[texto] = entrada
    
    def obtener_datos(self):
        """Obtiene los datos ingresados en el formulario"""
        datos = {}
        for campo, widget in self.campos.items():
            datos[campo] = widget.text()
        return datos

class VentanaHerramientas(QWidget):
    def __init__(self, ventana_formulario):
        super().__init__()
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        self.ventana_formulario = ventana_formulario  # Guardar referencia al formulario
        
        # Crear layout vertical
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Botones de herramientas con sus funciones
        boton_guardar = QPushButton("Guardar")
        boton_guardar.setStyleSheet("background-color: red; color: white;")
        boton_guardar.clicked.connect(self.mostrar_datos)
        layout.addWidget(boton_guardar)
        
        boton_abrir = QPushButton("Abrir")
        boton_abrir.setStyleSheet("background-color: white; color: black;")
        # Por ahora no implementamos funcionalidad para Abrir
        layout.addWidget(boton_abrir)
        
        boton_buscar = QPushButton("Buscar")
        boton_buscar.setStyleSheet("background-color: black; color: white;")
        # Por ahora no implementamos funcionalidad para Buscar
        layout.addWidget(boton_buscar)
        
        boton_salir = QPushButton("Salir")
        boton_salir.setStyleSheet("background-color: red; color: white;")
        boton_salir.clicked.connect(self.cerrar_ventanas)
        layout.addWidget(boton_salir)
    
    def mostrar_datos(self):
        """Muestra un mensaje con los datos del formulario"""
        datos = self.ventana_formulario.obtener_datos()
        mensaje = f"Datos del formulario:\n\n" \
                 f"Nombre: {datos['Nombre']}\n" \
                 f"Apellido: {datos['Apellido']}\n" \
                 f"DNI: {datos['DNI']}\n" \
                 f"Fecha de nacimiento: {datos['Fecha de nacimiento']}"
        
        QMessageBox.information(self, "Datos del Formulario", mensaje)
    
    def cerrar_ventanas(self):
        """Cierra ambas ventanas"""
        self.ventana_formulario.close()
        self.close()

if __name__ == '__main__':
    # Crear aplicación
    app = QApplication(sys.argv)
    
    # Crear ventana de formulario
    ventana_form = VentanaFormulario()
    
    # Crear ventana de herramientas pasando referencia al formulario
    ventana_herr = VentanaHerramientas(ventana_form)
    
    # Mostrar ambas ventanas simultáneamente
    ventana_form.show()
    ventana_herr.show()
    
    # Ejecutar aplicación
    sys.exit(app.exec_())