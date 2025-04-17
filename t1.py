import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, Label
import cv2

# Function to preprocess the image
def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    return Image.fromarray(image)

# Function to detect Tamil text from image
def detect_tamil_text_from_image(image_path):
    image = preprocess_image(image_path)
    text = pytesseract.image_to_string(image, lang='tam', config='--psm 6')
    return text

# Function to open file dialog and process the selected image
def browse_image():
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg;.jpeg;*.png")])
    if image_path:
        tamil_text = detect_tamil_text_from_image(image_path)
        result_label.config(text=tamil_text)

# Creating the main window
root = tk.Tk()
root.title("Tamil Text Detection from Image")
root.geometry("600x400")

browse_button = tk.Button(root, text="Select Image", command=browse_image)
browse_button.pack(pady=20)

result_label = Label(root, text="", wraplength=500, justify="left")
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
