import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
import pyodbc
import os

class ImageUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Devolución Payless")

        # Configuración de la base de datos
        self.conn_str = (
            r"DRIVER={SQL Server};"
            r"SERVER=DESKTOP-9J5JKGT;"
            r"DATABASE=devolucion;"
            r"Trusted_Connection=yes;"
        )

        # Configuración de la apariencia
        ctk.set_appearance_mode("System")  # Opciones: "System", "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Cambiar el tema de color

        # Marco principal
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Título
        self.title_label = ctk.CTkLabel(self.main_frame, text="Sistema de Devolución Payless", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Etiqueta de ejemplo
        self.example_label = ctk.CTkLabel(self.main_frame, text="Ejemplo de cómo debe subir la foto:", font=("Arial", 16, "bold"))
        self.example_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        # Marcos para las imágenes de ejemplo
        self.example_frame1 = ctk.CTkFrame(self.main_frame, width=150, height=150, corner_radius=10, bg_color="white")
        self.example_frame1.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.example_frame2 = ctk.CTkFrame(self.main_frame, width=150, height=150, corner_radius=10, bg_color="white")
        self.example_frame2.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Configurar las columnas para que se ajusten y centren
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)  # Asegurar que la fila 2 se expanda

        # Cargar imágenes de ejemplo
        self.load_example_images()

        # Etiqueta de "Subir imagen"
        self.upload_label = ctk.CTkLabel(self.main_frame, text="Subir una imagen", font=("Arial", 12))
        self.upload_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        # Botón para buscar imagen
        self.upload_button = ctk.CTkButton(self.main_frame, text="Cargar una imagen", command=self.open_image)
        self.upload_button.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

        # Marco para la imagen cargada
        self.uploaded_frame = ctk.CTkFrame(self.main_frame, width=250, height=250, corner_radius=10, bg_color="white")
        self.uploaded_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=5)
        self.uploaded_frame.grid_propagate(False)

        # Placeholder para la imagen cargada
        self.uploaded_image_label = ctk.CTkLabel(self.uploaded_frame)
        self.uploaded_image_label.pack(expand=True)

        # Etiqueta para seleccionar el tipo de calzado
        self.type_label = ctk.CTkLabel(self.main_frame, text="Seleccionar tipo de calzado:", font=("Arial", 12))
        self.type_label.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

        # ComboBox para el tipo de calzado
        self.shoe_type_var = ctk.StringVar()
        self.shoe_type_combobox = ctk.CTkComboBox(self.main_frame, variable=self.shoe_type_var, values=("sandalias", "tenis", "zapatos", "tacos", "botas"), width=200)
        self.shoe_type_combobox.grid(row=7, column=0, columnspan=3, padx=10, pady=5)
        self.shoe_type_combobox.set("sandalias")  # Seleccionar la primera opción por defecto

        # Botón para aceptar
        self.accept_button = ctk.CTkButton(self.main_frame, text="Solicitar la devolución", command=self.accept_image)
        self.accept_button.grid(row=8, column=2, padx=10, pady=10)

        # Etiqueta para mostrar la predicción
        self.prediction_label = ctk.CTkLabel(self.main_frame, text="", text_color="blue", font=("Arial", 10))
        self.prediction_label.grid(row=9, column=0, columnspan=3, padx=10, pady=5)

        self.uploaded_image_path = None  # Variable para almacenar la ruta de la imagen cargada

    def load_example_images(self):
        # Cargar y mostrar las imágenes de ejemplo
        example_image1 = Image.open("zapatoej.webp")
        example_image1 = example_image1.resize((200, 200), Image.LANCZOS)
        self.example_image1_tk = ImageTk.PhotoImage(example_image1)

        # Mostrar la primera imagen
        example_label1 = ctk.CTkLabel(self.example_frame1, image=self.example_image1_tk, text="", text_color="white")
        example_label1.pack(expand=True, fill='both')  # Expandir y llenar el marco

        example_image2 = Image.open("tacosej.webp")
        example_image2 = example_image2.resize((200, 200), Image.LANCZOS)
        self.example_image2_tk = ImageTk.PhotoImage(example_image2)

        # Mostrar la segunda imagen
        example_label2 = ctk.CTkLabel(self.example_frame2, image=self.example_image2_tk, text="", text_color="white")
        example_label2.pack(expand=True, fill='both')  # Expandir y llenar el marco

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            self.uploaded_image_path = file_path
            uploaded_image = Image.open(file_path)
            uploaded_image = uploaded_image.resize((250, 250), Image.LANCZOS)
            self.uploaded_image_tk = ImageTk.PhotoImage(uploaded_image)
            self.uploaded_image_label.configure(image=self.uploaded_image_tk)
            self.uploaded_image_label.configure(text="")

    def clear_fields(self):
        self.uploaded_image_label.configure(image='')
        self.uploaded_image_path = None
        self.prediction_label.configure(text="")
        self.shoe_type_combobox.set("sandalias")  # Reiniciar la selección del ComboBox al valor por defecto

    def save_to_database(self, tipo_calzado, image_path):
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        # Obtener el ID del tipo de calzado
        cursor.execute("SELECT TipoCalzadoID FROM TiposCalzado WHERE Descripcion = ?", tipo_calzado)
        result = cursor.fetchone()
        if result:
            tipo_calzado_id = result[0]
        else:
            messagebox.showerror("Error", "Tipo de calzado no encontrado en la base de datos.")
            conn.close()
            return

        # Insertar la solicitud de devolución en la base de datos
        cursor.execute("""
            INSERT INTO SolicitudesDevolucion (TipoCalzadoIndicadoID, Imagen)
            VALUES (?, ?)
        """, tipo_calzado_id, image_path)
        conn.commit()
        conn.close()

    def accept_image(self):
        if self.uploaded_image_path:
            # Enviar la imagen a la API de Azure Custom Vision
            endpoint = "https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/f5370cb0-618e-484f-b464-25e50be5f7d7/classify/iterations/Payless%20IA/image"
            prediction_key = "f5459a728f35422496aeae33dd4c573f"
            content_type = "application/octet-stream"

            with open(self.uploaded_image_path, "rb") as image_file:
                image_data = image_file.read()

            headers = {
                "Prediction-Key": prediction_key,
                "Content-Type": content_type
            }

            response = requests.post(endpoint, headers=headers, data=image_data)

            if response.status_code == 200:
                predictions = response.json()

                if predictions['predictions']:
                    # Obtener la predicción con mayor probabilidad
                    top_prediction = max(predictions['predictions'], key=lambda p: p['probability'])
                    predicted_type = top_prediction['tagName'].lower()  # Convertir a minúsculas para una comparación insensible a mayúsculas
                    selected_type = self.shoe_type_var.get().lower()  # Convertir a minúsculas para una comparación insensible a mayúsculas

                    print(f"Predicción: {predicted_type}, Selección del usuario: {selected_type}")  # Mensaje de depuración

                    if predicted_type == selected_type:
                        self.save_to_database(selected_type, os.path.basename(self.uploaded_image_path))
                        messagebox.showinfo("Éxito", "La devolución se ha realizado con éxito.")
                        self.clear_fields()  # Limpiar campos después de guardar
                    else:
                        messagebox.showerror("Error", "No coincide. Intentelo de nuevo.")
                        self.clear_fields()
                else:
                    self.prediction_label.configure(text="No se encontraron predicciones.")
            else:
                messagebox.showerror("Error", f"Error: {response.status_code}, {response.text}")
                self.clear_fields()
        else:
            messagebox.showwarning("Advertencia", "Por favor, sube una imagen antes de aceptar.")

if __name__ == "__main__":
    root = ctk.CTk()
    app = ImageUploaderApp(root)
    root.mainloop()
