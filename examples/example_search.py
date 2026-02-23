from pdf_ocr_finder.search import search_in_pdf

result = search_in_pdf(
    pdf_path="/home/hugo/Descargas/DECRETO 5311 PGN 2026.pdf",
    pattern=r"Presupuesto"
)

print(result)