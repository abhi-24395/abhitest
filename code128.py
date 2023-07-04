from barcode import Code128

from barcode.writer import ImageWriter

number = 'CFT360_00001'

my_code = Code128(number, writer=ImageWriter())

my_code.save("new_code2")
