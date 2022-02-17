from pdfminer.high_level import extract_text

with open("extracted_7000.txt", mode="w", encoding="utf-8") as f:
    txt = extract_text("1552438563395h2EQgNj0.pdf")
    f.write(txt)
