## Method 1: Qr code while setting its dimesion and bg and fill color.
import qrcode

qr= qrcode.QRCode(version=1,error_correction= qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://github.com/AyushJaggii")
img = qr.make_image(fill_color = "black", back_color = "white")
img.save("Ayush_github.png")


### Alternate simpler method:

## import qrcode as qr
## img = qr.make("www.xyz.com")
## img.save("xyz_Website.png")