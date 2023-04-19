import pytesseract
import cv2
import pandas as pd

# Load the image
image = cv2.imread("./invoice.jpeg")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to convert the image to black and white
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Perform OCR using Tesseract
text = pytesseract.image_to_string(thresh)

# Print the extracted text
print(text)

data = text

# Define the data as a list of dictionaries
'''
depend on the file make a split on ur choice and data you want 
in your case i have 1000 of files i use the dict
'''


# Create a DataFrame from the data
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel("receipt_data.xlsx", index=False)
