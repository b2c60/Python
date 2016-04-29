
from qrcode import *

qr = QRCode(version=2, error_correction=ERROR_CORRECT_L)
qr.add_data("http://blog.matael.org/")
qr.make() # Generate the QRCode itself

# im contains a PIL.Image.Image object
im = qr.make_image()

# To save it
im.save("filename.png")
