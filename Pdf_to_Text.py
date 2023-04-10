# Import PyPDF2 module to work with PDF files
import PyPDF2


pdf_file = open("E:\Mtech\Letter.pdf", "rb")     # Open the PDF file in binary mode for reading.
pdf_reader = PyPDF2.PdfReader(pdf_file)          # Create a PdfReader object to read the PDF file.
text = pdf_reader.pages[0].extract_text()        # Extract the text content from the first page of the PDF file.

# Open a text file in write mode
with open("E:\\1. Tech\\Python Projects\\Letter.txt", "w") as text_file:
    # Write the extracted text to the file
    text_file.write(text)

print("Text from File Extracted Successfully")
