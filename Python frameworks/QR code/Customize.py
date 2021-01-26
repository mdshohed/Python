import qrcode
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=30,
    border=2,
)
qr.add_data('Hi! I am shohedul Islam')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("code.png")
