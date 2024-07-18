import pypdf


def pdf_input(filename):
    text = ""
    with open(filename, "rb") as pdf_file:
        reader = pypdf.PdfReader(pdf_file)
        for i, page in enumerate(reader.pages, start=0):
            text += page.extract_text()
    return text
