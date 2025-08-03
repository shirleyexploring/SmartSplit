import pytesseract
from PIL import Image

def extract_text_from_image(image_path: str) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_total_amount(text: str) -> str:
    import re
    matches = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d{2})\b', text)
    return matches[-1] if matches else "Not found"
