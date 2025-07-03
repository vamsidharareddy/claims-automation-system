import os
import pdfplumber

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"❌ Error reading TXT file: {e}")
        return ""

def read_pdf_file(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            return text.strip()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return ""

def load_claim_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.txt':
        return read_text_file(file_path)
    elif ext == '.pdf':
        return read_pdf_file(file_path)
    else:
        raise ValueError(f"❌ Unsupported file type: {ext}")
