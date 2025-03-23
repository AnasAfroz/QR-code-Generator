import pyqrcode
import os

# Define the folder path (make sure it's valid for your system)
folder_path = r"C:\\Users\\User\\Downloads"

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Get user input
h = input("Enter the text or URL for the QR code: ")

# Create the QR code object
qr = pyqrcode.create(h, version=8, error='Q')

# Save the QR code as a PNG file to the folder
qr_file_path = os.path.join(folder_path, 'my_qrcode3.png')
qr.png(qr_file_path, scale=8)

print(f"QR Code saved successfully at {qr_file_path}!")
