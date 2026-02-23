import re
from typing import List, Dict
from .ocr import extract_text_from_pdf


def search_in_pdf(
    pdf_path: str,
    pattern: str,
    lang: str = "spa"
) -> Dict[str, List[int]]:
    """
    Busca un patrón (regex) dentro de un PDF escaneado.

    :param pdf_path: Ruta del PDF
    :param pattern: Expresión regular a buscar
    :param lang: Idioma OCR
    :return: Diccionario con páginas donde se encontró
    """

    regex = re.compile(pattern, re.IGNORECASE)
    pages_text = extract_text_from_pdf(pdf_path, lang=lang)

    matches = []

    for index, text in enumerate(pages_text):
        if regex.search(text):
            matches.append(index + 1)

    return {
        "pattern": pattern,
        "pages_found": matches,
        "total_matches": len(matches)
    }