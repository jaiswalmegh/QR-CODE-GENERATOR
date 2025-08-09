import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
import os

# Function to generate QR
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Required", "Please enter text or URL.")
        return

    # Create QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save & show QR Code
    img_path = "generated_qr.png"
    img.save(img_path)
    img_display = Image.open(img_path)
    img_display = img_display.resize((250, 250))
    qr_img = ImageTk.PhotoImage(img_display)

    qr_label.config(image=qr_img)
    qr_label.image = qr_img  # prevent garbage collection

# UI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.configure(bg="#e0f7fa")

tk.Label(root, text="Enter text or URL:", font=("Arial", 14), bg="#e0f7fa").pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Generate QR", command=generate_qr, font=("Arial", 12),
          bg="#00796b", fg="white").pack(pady=10)

qr_label = tk.Label(root, bg="#e0f7fa")
qr_label.pack(pady=20)

root.mainloop()
