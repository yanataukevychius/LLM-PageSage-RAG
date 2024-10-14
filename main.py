from data_preprocessing.data_load import extract_pdf_pages_as_images

PDF_PATH = "/Users/yanatautkevychyus/Desktop/github/LLM-PageSage-RAG/data/IELTS - Vocabulary for IELTS.pdf"
OUTPUT_DIR = "/Users/yanatautkevychyus/Desktop/github/LLM-PageSage-RAG/data/data_images"

extract_pdf_pages_as_images(PDF_PATH, 15, 35, OUTPUT_DIR)