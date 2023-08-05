import cv2
import pytesseract

# Set the path to the Tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def read_label(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale image
    extracted_text = pytesseract.image_to_string(gray_image)

    return extracted_text.strip()

if __name__ == "__main__":
    # Specify the path to the image containing the label
    image_path = "12.png"

    # Read the label using OCR
    extracted_text = read_label(image_path)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("No text was extracted.")
