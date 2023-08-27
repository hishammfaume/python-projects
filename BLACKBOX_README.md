 ```
# Image to Text Converter

This Python script uses the PyTesseract library to convert an image to text. It requires Tesseract-OCR to be installed on your system.

## Step 1: Import the necessary libraries

```
import pytesseract
import os
from PIL import Image
```

## Step 2: Set the Tesseract-OCR path

The PyTesseract library requires the path to the Tesseract-OCR executable. You can set this path using the `tesseract_cmd` attribute of the `pytesseract.pytesseract` module.

```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Step 3: Define the `convert()` function

The `convert()` function is the main function of the script. It opens the image file, converts it to text using the `image_to_string()` function of the `pytesseract` module, and prints the extracted text to the console.

```
def convert():
    img  = Image.open("OIP.jpg")
    text = pytesseract.image_to_string(img)
    print(text)
```

## Step 4: Call the `convert()` function

The `convert()` function is called at the end of the script to convert the image file to text.

```
convert()
```

## Usage

To use the script, save the code in a file named `imgtotxt.py` and run it from the command line.

```
python imgtotxt.py
```

The script will convert the image file `OIP.jpg` to text and print the extracted text to the console.

## Output

The output of the script will be the text extracted from the image file. For example, if the image file contains the text "Hello, world!", the output of the script will be:

```
Hello, world!
```
```

