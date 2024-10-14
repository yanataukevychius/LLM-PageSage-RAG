"""
PDF Image Extractor

This module provides functionality to extract pages from a PDF as high-resolution images.
It uses PyMuPDF for efficient PDF processing and Pillow for image handling.

Usage:
    from pdf_image_extractor import extract_pdf_pages_as_images
    extract_pdf_pages_as_images('path/to/pdf', 1, 10, 'output/dir')
"""

import os
from typing import Tuple
import fitz
from PIL import Image

def extract_pdf_pages_as_images(pdf_path: str, start_page: int, end_page: int, output_dir: str, dpi: int = 300) -> None:
    """
    Extract a range of pages from a PDF as high-resolution images.

    Args:
        pdf_path (str): Path to the PDF file.
        start_page (int): First page to extract (1-indexed).
        end_page (int): Last page to extract (inclusive).
        output_dir (str): Directory to save extracted images.
        dpi (int, optional): Resolution of extracted images. Defaults to 300.

    Raises:
        ValueError: If the PDF file cannot be opened or if page range is invalid.
    """
    os.makedirs(output_dir, exist_ok=True)

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        raise ValueError(f"Failed to open PDF: {e}")

    start_page, end_page = _validate_page_range(doc, start_page, end_page)
    scale = dpi / 72  # PDF standard is 72 DPI

    for page_num in range(start_page - 1, end_page):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
        img.save(img_path, "PNG")

    print(f"Extracted {end_page - start_page + 1} pages as images.")

def _validate_page_range(doc: fitz.Document, start: int, end: int) -> Tuple[int, int]:
    """Validate and adjust the page range."""
    if start < 1 or end > doc.page_count or start > end:
        raise ValueError(f"Invalid page range. Document has {doc.page_count} pages.")
    return max(1, start), min(doc.page_count, end)