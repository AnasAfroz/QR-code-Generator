
---

# QR Code Generator

This Python-based QR Code Generator allows users to input a string (text or URL) and generates a corresponding QR code image, which is saved as a PNG file in a specified folder.

## Features

- **Input any text or URL**: Enter any text or URL, and the script will generate a QR code.
- **Customizable Output Folder**: The QR code image is saved in a specific folder of your choice.
- **Error Handling**: Handles missing folder creation automatically.

## Requirements

- Python 3.6 or higher
- `pyqrcode` library for generating QR codes
- `pypng` library for saving QR codes as PNG files

## Installation

### Step 1: Install Dependencies

Before running the script, you need to install the required Python libraries. Run the following command to install both dependencies:

```bash
pip install pyqrcode pypng
```

### Step 2: Clone or Download the Repository

Clone or download the project repository to your local machine.

```bash
git clone <repository_url>
```

Or, simply download the project as a ZIP and extract it.

## Usage

### Step 1: Customize the Folder Path

In the script, the QR code image is saved to a folder specified by the `folder_path` variable. Make sure to update the path if needed. For example:

```python
folder_path = r'C:\Users\User\Downloads\PYTHON PROJECTS'
```

### Step 2: Run the Script

To generate a QR code, run the Python script:

```bash
python QR-CODE-GENERATOR.py
```

You will be prompted to enter the text or URL for the QR code. After entering the input, the script will create the QR code and save it as a PNG file in the specified folder.

Example input:

```
Enter the text or URL for the QR code: https://example.com
```

The QR code will be saved in the folder as `my_qrcode3.png`.

### Step 3: Check the Output

The generated QR code will be saved in the folder you've specified, and a message will confirm the successful creation of the QR code.

Example message:

```
QR Code saved successfully at C:\Users\User\Downloads\PYTHON PROJECTS\my_qrcode3.png!
```

## Troubleshooting

- **ModuleNotFoundError: No module named 'png'**: If you see this error, install the `pypng` module by running:

  ```bash
  pip install pypng
  ```

- **Folder Not Created**: If the folder doesn't exist, the script will automatically create it. If you encounter issues, ensure you have the necessary permissions to write to the specified folder.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Feel free to open issues or pull requests if you encounter any bugs or have suggestions for improvements!

---
