from typing import List
from pdf2image import convert_from_path
import pytesseract


def extract_text_from_pdf(
    pdf_path: str,
    lang: str = "spa",
    dpi: int = 200
) -> List[str]:
    """
    Convierte un PDF escaneado en texto usando OCR.

    :param pdf_path: Ruta del archivo PDF
    :param lang: Idioma para Tesseract (default: spa)
    :param dpi: Resolución de conversión (default: 200)
    :return: Lista de textos por página
    """

    pages = convert_from_path(pdf_path, dpi=dpi)

    extracted_text = []

    for page in pages:
        text = pytesseract.image_to_string(page, lang=lang)
        extracted_text.append(text)

    return extracted_text