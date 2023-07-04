import barcode
from barcode import Code39
from barcode.writer import ImageWriter

def generate_barcodes(starting_code, num_barcodes, format_type, filename_prefix):
    # Create a barcode generator object based on the format type
    try:
        barcode_generator = barcode.get_barcode_class(format_type)
    except barcode.errors.BarcodeNotFoundError:
        print(f"Error: Barcode format '{format_type}' is not supported.")
        return

    # Generate and save barcodes for each code
    for i in range(num_barcodes):
        code = f"{starting_code}-{str(i+1).zfill(5)}"
        barcode_value = barcode_generator(code, writer=ImageWriter())
        filename = f"{filename_prefix}_{code}.png"
        barcode_value.save(filename)

        # Print the code and number below the barcode
        print(f"Code: {code}")
        print(f"Number: {i+1}")
        print()

# Example usage
starting_code = 'CFT360'
num_barcodes = 1500
format_type = 'code39'
filename_prefix = 'barcode'
generate_barcodes(starting_code, num_barcodes, format_type, filename_prefix)
