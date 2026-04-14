import io
from PyPDF2 import PdfReader
import docx

def extract_text_from_upload(file):
    if file is None:
        return ""
    name = file.name.lower()
    if name.endswith(".txt"):
        return file.read().decode()
    if name.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(file.read()))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if name.endswith(".docx"):
        doc = docx.Document(io.BytesIO(file.read()))
        return "\n".join(p.text for p in doc.paragraphs)
    return ""
