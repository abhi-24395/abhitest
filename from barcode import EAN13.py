from barcode import Code128
from barcode.writer import ImageWriter

start_number = 1
total_barcodes = 2000

for i in range(start_number, start_number + total_barcodes):
    number = f'CFT360_{i:05}'
    my_code = Code128(number, writer=ImageWriter())
    filename = f"barcode_{i:05}.png"
    my_code.save(filename)
