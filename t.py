import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, Label, messagebox

# Function to detect Tamil text from an image
def detect_tamil_text_from_image(image_path):
    """Detects and extracts Tamil text from the given image."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='t')  # Ensure 'tam' is used for Tamil
    return text

# Function to save extracted text to a .txt file
def save_text_to_file(text):
    """Saves the extracted text to a .txt file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        messagebox.showinfo("Success", f"Text saved to {file_path}")

# Function to open file dialog, process the selected image, and save text
def browse_image():
    # Open file dialog to select an image
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg;.jpeg;*.png")])
    if image_path:
        # Extract Tamil text from the selected image
        tamil_text = detect_tamil_text_from_image(image_path)
        # Display the extracted text in the label
        result_label.config(text=tamil_text)
        # Offer to save the text to a file
        save_text_to_file(tamil_text)

# Creating the main window
root = tk.Tk()
root.title("Tamil Text Detection from Image")
root.geometry("700x500")
root.configure(bg='#f0f0f0')  # Set a background color

# Create a title label
title_label = tk.Label(root, text="Tamil Text Detection from Image", font=("Arial", 16, "bold"), bg='#f0f0f0')
title_label.pack(pady=10)

# Create a button to browse and select an image
browse_button = tk.Button(root, text="Select Image", command=browse_image, font=("Arial", 12), bg='#4CAF50', fg='white')
browse_button.pack(pady=20)

# Create a label to display the extracted text
result_label = Label(root, text="", wraplength=600, justify="left", bg='#f0f0f0', font=("Arial", 12), anchor="w")
result_label.pack(pady=20, padx=20, fill="both", expand=True)

# Start the GUI event loop
root.mainloop()
