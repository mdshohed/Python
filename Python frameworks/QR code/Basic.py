#pip install qrcode
#pip install Pillow


import qrcode
img = qrcode.make("Hello World!")
img.save("code.png")
