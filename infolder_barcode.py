import os
from barcode import Code128
from barcode.writer import ImageWriter

start_number = 1
total_barcodes = 2000
folder_path = 'barcodes'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for i in range(start_number, start_number + total_barcodes):
    number = f'CFT360_{i:05}'
    my_code = Code128(number, writer=ImageWriter())
    filename = f"barcode_{i:05}.png"
    file_path = os.path.join(folder_path, filename)
    my_code.save(file_path)
