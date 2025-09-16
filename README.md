# Generador de QR en Python 🖤

## Descripción
Aplicación en Python con **interfaz gráfica (Tkinter)** que permite generar códigos QR a partir de cualquier URL.  
Introduce la URL, presiona **Generador de QR**, y el código se mostrará en pantalla y se guardará como `qrcode.png`.

## Vista previa de la aplicación
*Ejemplo de QR generado por el programa que enlaza a la página del máster donde estoy cursando.*
![Generador QR](images/imagen_1.png)

## Requisitos
- Python 3.x
- Librerías:
  - `qrcode`
  - `Pillow`
- Tkinter (incluido en Python estándar)

## Instalación y ejecución
1. Clonar el repositorio:
```bash
git clone git@github.com:FerVIII/generador_qr.git

2. Crear y activar un entorno virtual:

python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias:

pip install -r requirements.txt


4. Ejecutar la aplicación:

python generador_qr.py

## Cómo funciona

Introduce una URL válida en la caja de texto.

Haz clic en Generador de QR.

El QR se mostrará en la ventana y se guardará como qrcode.png.

Aparecerá un mensaje de confirmación de éxito.

## Lo que aprendí

Creación de interfaces gráficas con Tkinter y ttk.

Manejo de imágenes con Pillow (PIL).

Generación de códigos QR dinámicos con la librería qrcode.

Validación de entradas y manejo de errores con messagebox.




