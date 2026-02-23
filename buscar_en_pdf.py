import re
from pdf2image import convert_from_path
import pytesseract

# 📌 Define aquí tu archivo
PDF_PATH = "/home/hugo/Descargas/LEY_7609_PGN_2026_OCR.pdf"

# Buscar 16% o 16 %
patron = re.compile(r"16\s*%")

print(f"Procesando: {PDF_PATH}\n")

paginas = convert_from_path(PDF_PATH)

encontrado = False

for i, pagina in enumerate(paginas):
    texto = pytesseract.image_to_string(pagina, lang="spa")

    if patron.search(texto):
        print(f"✅ Encontrado en página {i+1}")
        encontrado = True

if not encontrado:
    print("❌ No se encontró '16%'")