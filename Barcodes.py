# Import the EAN13 barcode format from the barcode package
# Import the ImageWriter class from the barcode.writer module
from barcode import EAN13
from barcode.writer import ImageWriter

numberOfBarcodes = int(input("How many Barcodes do you need?\n"))
numbers = range(numberOfBarcodes)

for i in numbers:
    id = input("Give 12- Digit numbers for your barcode ID:\n")

    # Create a new EAN13 barcode instance with the given ID and an ImageWriter instance for writing the barcode image.
    my_code = EAN13(id, writer = ImageWriter())     
    name = input("Give name to save Barcodes:\n")

    my_code.save(name)


