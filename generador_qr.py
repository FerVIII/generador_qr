import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk

# crear ventana principal
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.configure(bg="#f0f4f7")

# URL input
label_url = ttk.Label(root, text="Enter URL:", background="#f0f4f7")
label_url.pack(pady=10)
entry_url = ttk.Entry(root, font=("Helvetica", 12), width=40)
entry_url.pack(pady=20)

# boton generador
button_generate = ttk.Button(root,text="Generador de QR", command=None)
button_generate.pack(pady=20)

# etiqueta para mostrar el QR
qr_label = ttk.Label(root, background="#f0f4f7")
qr_label.pack(pady=10)

# Funcion de genereración de QR
def generate_qrcode():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Error", "por favor ingrese una URL válida")
        return


    # generar godigo QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # <--- este es el nombre correcto
        box_size=6,
        border=2,
    )

    qr.add_data(url)
    qr.make(fit=True)
    
    # Crear y guardar la imagen del código QR
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("qrcode.png")
 
    # imagen del código QR
    qr_image_tk = ImageTk.PhotoImage(Image.open("qrcode.png"))
    qr_label.config(image=qr_image_tk)
    qr_label.image = qr_image_tk
    messagebox.showinfo("Éxito", "Codigo QR generado con éxito")

# Asignar la función al botón
button_generate.config(command=generate_qrcode)

# Ejecutar la aplicación
root.mainloop()