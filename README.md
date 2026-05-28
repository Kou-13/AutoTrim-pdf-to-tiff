# AutoTrim PDF to TIFF

This Python script reads each page of a PDF file as an image, automatically trims the white margins, and saves the result as rectangular TIFF images. It can be used on both Windows and macOS.

## Features

This script performs the following processes.

1. Read each page of the PDF as an image.
2. Automatically detect white margins, trim the image into a rectangular shape, and save it in TIFF format.
3. If the PDF has multiple pages, save each page as a sequentially numbered TIFF image.
4. An output folder is automatically created in the same location as the input PDF.

## Required Libraries

The required Python libraries are listed in `requirements.txt`.

Before using this script, install the libraries listed in `requirements.txt`.

Usually, run the following command.

```bash
pip install -r requirements.txt
```

If you use multiple Python environments, specify the Python interpreter used to run this script when installing the libraries.

```bash
(Python path) -m pip install -r requirements.txt
```

You can check the path of the currently used Python interpreter by running the following in Python.

```python
import sys
print(sys.executable)
```

This README does not explain how to install Python itself or how to set up development environments such as Spyder.

## How to Use

Open `AutoTrim_pdf_to_tiff.py` and edit the `Settings` section at the top of the file before running the script.

The main settings to change are the following four items.

1. `PDF_PATH`
2. `OUTPUT_FOLDER_NAME`
3. `TARGET_DPI`
4. `FILE_PREFIX`

### 1. PDF_PATH

Enter the path of the PDF file you want to convert inside `" "`.

Important: Do not remove the `r` in `Path(r"...")`.

Keeping `r` allows the path to be used on both Windows and macOS.

If `r` is removed, `\` included in Windows paths may not be handled correctly, which may cause an error.

### 2. OUTPUT_FOLDER_NAME

Specify the folder name where the output images will be saved.

This folder is automatically created in the same directory as the input PDF.

### 3. TARGET_DPI

Specify the resolution of the output images.

A larger value produces higher-resolution images.

Usually, use a value around 250-300. If higher resolution is required, use 600 as a guideline. Please note that a higher resolution also increases the image file size.

### 4. FILE_PREFIX

Specify the prefix of the output image file names.

If the PDF has multiple pages, the images are saved with sequential numbers in page order.

Example:

```python
FILE_PREFIX = "Fig_"
```

Output examples:

```text
Fig_1.tif
Fig_2.tif
Fig_3.tif
```

## Preparing the PDF

Even if the resolution is specified in this script, if the original PDF has a low resolution, only the image file size will increase and the visual quality will not improve.

Therefore, when converting figures created in PowerPoint into a PDF, it is recommended to create the PDF using the print function instead of the export function in PowerPoint.

In addition, configuring PowerPoint settings to avoid image compression and preserve high resolution can help save cleaner images.

## Notes

- If an output file with the same name already exists, it will be overwritten.
- The input PDF itself is not modified.
- `WHITE_THRESHOLD` is an internal setting used to detect white margins. Usually, do not change it.

## Troubleshooting

### If the PDF cannot be found

Check whether `PDF_PATH` is correct.

Especially on Windows, do not remove the `r` in `Path(r"...")`.

### If a library cannot be found

The following errors may occur.

```text
ModuleNotFoundError: No module named 'fitz'
ModuleNotFoundError: No module named 'PIL'
```

In this case, the required libraries are not installed in the Python environment currently used to run the script.

Install the libraries listed in `requirements.txt`.

### If the output image is rough

Increase the value of `TARGET_DPI`, configure PowerPoint to preserve high resolution, or create the PDF using the print function.

### If margin trimming does not work well

This script detects white backgrounds as margins.

If the background is not completely white, it will be recognized as content and will not be trimmed.

## License

This project is released under the MIT License.