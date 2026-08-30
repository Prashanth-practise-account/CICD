import re
from pathlib import Path

from pypdf import PdfReader


class DocumentLoader:
    def __init__(self):
        self.pdf_path = Path(__file__).with_name("Prashanth_Resume_6yrs.pdf")
    def loader(self):
        try:
            if not self.pdf_path.exists():
                raise FileNotFoundError(f"PDF file not found: {self.pdf_path}")

            reader = PdfReader(str(self.pdf_path))
            text_parts = []

            for page in reader.pages:
                page_text = page.extract_text() or ""
                cleaned = re.sub(r"\s+", " ", page_text)
                cleaned = re.sub(r"[^\w\s.,@+#()/:-]", " ", cleaned)
                cleaned = cleaned.strip()

                if cleaned:
                    text_parts.append(cleaned)

            output = "\n".join(text_parts)
            print(output if output else "No text found in the PDF.")

        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
        except (OSError, ValueError) as e:
            print(f"An error occurred: {e}")