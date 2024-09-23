import qrcode
data = input("Enter your URL: ")
qr = qrcode.make(data)
qr.save("QRcode.png")
print("QR code generated and saved as 'github.png'")