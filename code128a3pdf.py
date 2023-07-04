import os
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw

# Set the dimensions of the A3 sheet in pixels (assuming 300 DPI)
A3_WIDTH = 3508
A3_HEIGHT = 4961

# Set the number of barcodes per row and column
BARCODES_PER_ROW = 8
BARCODES_PER_COLUMN = 11

# Set the spacing between barcodes in pixels
BARCODE_SPACING = 50

# Set the starting position of the first barcode
START_X = 100
START_Y = 100

# Set the folder path to save the barcodes
folder_path = 'barcodes'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Calculate the width and height of each barcode based on the A3 dimensions and spacing
barcode_width = (A3_WIDTH - (BARCODES_PER_ROW + 1) * BARCODE_SPACING) // BARCODES_PER_ROW
barcode_height = (A3_HEIGHT - (BARCODES_PER_COLUMN + 1) * BARCODE_SPACING) // BARCODES_PER_COLUMN

# Create a new A3-sized image
sheet = Image.new('RGB', (A3_WIDTH, A3_HEIGHT), color='white')
draw = ImageDraw.Draw(sheet)

# Generate and place barcodes on the sheet
count = 0
for row in range(BARCODES_PER_COLUMN):
    for col in range(BARCODES_PER_ROW):
        if count >= 88:
            break

        number = f'CFT360_{count + 1:05}'
        barcode = Code128(number, writer=ImageWriter())
        filename = f"barcode_{count + 1:05}.png"
        file_path = os.path.join(folder_path, filename)
        barcode.save(file_path)

        barcode_image = Image.open(file_path)
        barcode_image = barcode_image.resize((barcode_width, barcode_height), Image.ANTIALIAS)

        x = START_X + col * (barcode_width + BARCODE_SPACING)
        y = START_Y + row * (barcode_height + BARCODE_SPACING)

        sheet.paste(barcode_image, (x, y))

        count += 1

    if count >= 88:
        break

# Save the final A3 sheet containing the barcodes
sheet.save(os.path.join(folder_path, 'barcode_sheet.png'))
