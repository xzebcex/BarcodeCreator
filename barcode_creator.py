# Barcode Generator

from barcode import EAN13 # import EAN13 from barcode module


from barcode.writer import ImageWriter # import ImageWriter to generate an image file


number = '123456789' # Make sure to pass the number as string

 """Now, let's create an object of EAN13 class and
 pass the number with the ImageWriter() as the
 writer"""
my_code = EAN13(number, writer=ImageWriter())


my_code.save("new_code1") # Our barcode is ready. Let's save it.
