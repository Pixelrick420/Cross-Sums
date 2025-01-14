import cv2
import pytesseract
import numpy as np

# Set up Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image
image_path = "zmatrix.jpg"  # Update this with the correct path
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to load the image. Check the file path.")
    exit()

# Preprocessing: Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Increase contrast for better OCR recognition
gray = cv2.equalizeHist(gray)

# Thresholding: Convert to binary image
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours to locate grid cells
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by position (top-to-bottom, left-to-right)
contours = sorted(contours, key=lambda c: (cv2.boundingRect(c)[1], cv2.boundingRect(c)[0]))

# Extract grid cells while ignoring the top row and leftmost column
grid = []
cell_size = 0  # To approximate the size of grid cells
filtered_contours = []

for c in contours:
    x, y, w, h = cv2.boundingRect(c)

    # Skip small contours (noise or artifacts)
    if w < 10 or h < 10:
        continue

    # Initialize cell size from the first detected contour
    if cell_size == 0:
        cell_size = max(w, h)

    # Skip cells in the top row or leftmost column
    if y < cell_size or x < cell_size:
        continue

    filtered_contours.append((x, y, w, h))

# Extract numbers from the filtered contours
for x, y, w, h in filtered_contours:
    # Crop each grid cell
    cell_roi = binary[y:y + h, x:x + w]

    # Resize to improve OCR accuracy
    cell_roi = cv2.resize(cell_roi, (cell_size * 2, cell_size * 2), interpolation=cv2.INTER_LINEAR)

    # OCR to extract the number
    number = pytesseract.image_to_string(cell_roi, config="--psm 10 digits")

    try:
        grid.append(int(number.strip()))
    except ValueError:
        grid.append(0)  # Use 0 if OCR fails

# Convert the grid list to an n*n matrix
n = int(len(grid) ** 0.5)  # Assume a square matrix
matrix = np.array(grid).reshape(n, n)

# Display the extracted matrix
print("Extracted Matrix:")
print(matrix)
