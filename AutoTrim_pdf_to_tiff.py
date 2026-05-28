# AutoTrim PDF to TIFF.
# Compatible with Windows and macOS.

from pathlib import Path

import fitz  # PyMuPDF
import numpy as np
from PIL import Image


# ==========================================
# Settings
# ==========================================

# PDF file path
# Note:
# How to write PDF path of Windows and Mac can be used.
# But don't delete "r".
PDF_PATH = Path(r" ")

# Output folder name
# The folder will be created in the same folder as the PDF file.
OUTPUT_FOLDER_NAME = "Test"

# Resolution setting (dpi)
TARGET_DPI = 250

# Output file name prefix (ex: Fig_, Table_)
FILE_PREFIX = "Fig_"




# White threshold (you shouldn't change this value.)
WHITE_THRESHOLD = 250

# ==========================================
# Path handling
# ==========================================

def build_paths():
    """
    Build OS-independent input and output paths.
    """

    pdf_path = PDF_PATH.expanduser().resolve()
    output_dir = pdf_path.parent / OUTPUT_FOLDER_NAME

    return pdf_path, output_dir


# ==========================================
# PDF rendering
# ==========================================

def render_pdf_page_to_pil(page, dpi):
    """
    Render one PDF page to a PIL image using PyMuPDF.
    """

    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)

    pix = page.get_pixmap(
        matrix=matrix,
        alpha=False
    )

    image = Image.frombytes(
        "RGB",
        (pix.width, pix.height),
        pix.samples
    )

    return image


# ==========================================
# Image processing
# ==========================================

def crop_white_background(image, threshold=WHITE_THRESHOLD):
    """
    Automatically crop white background from an image.
    """

    image = image.convert("RGB")
    img_array = np.array(image)

    is_content = np.any(img_array < threshold, axis=2)
    coords = np.argwhere(is_content)

    if coords.size == 0:
        print("  -> No content found. Skipped.")
        return None

    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    cropped_image = image.crop((x_min, y_min, x_max + 1, y_max + 1))

    return cropped_image


# ==========================================
# Main process
# ==========================================

def main():
    pdf_path, output_dir = build_paths()

    if not pdf_path.exists():
        print("PDF file was not found.")
        print(f"Expected path: {pdf_path}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    print("=== PDF Auto Trim and TIFF Export ===")
    print(f"PDF: {pdf_path}")
    print(f"Output folder: {output_dir}")
    print(f"DPI: {TARGET_DPI}")
    print(f"White threshold: {WHITE_THRESHOLD}")
    print("PDF renderer: PyMuPDF")
    print("")

    try:
        pdf_doc = fitz.open(str(pdf_path))
        total_pages = len(pdf_doc)

        print(f"Total pages: {total_pages}")

        for page_index in range(total_pages):
            page_num = page_index + 1
            filename = f"{FILE_PREFIX}{page_num}.tif"
            save_path = output_dir / filename

            print(f"Processing page {page_num} ...", end="")

            page = pdf_doc[page_index]
            img = render_pdf_page_to_pil(page, TARGET_DPI)

            cropped_img = crop_white_background(
                img,
                threshold=WHITE_THRESHOLD
            )

            if cropped_img is not None:
                cropped_img.save(
                    str(save_path),
                    format="TIFF",
                    compression="tiff_lzw",
                    dpi=(TARGET_DPI, TARGET_DPI)
                )

                print(f" saved: {filename} size={cropped_img.size}")
            else:
                print(" skipped.")

        pdf_doc.close()

        print("")
        print("=== Completed ===")
        print(f"Saved to: {output_dir}")

    except Exception as e:
        print("")
        print("Error occurred:")
        print(e)


if __name__ == "__main__":
    main()