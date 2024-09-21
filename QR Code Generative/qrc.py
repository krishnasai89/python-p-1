import qrcode
data = "https://github.com/vellampallikrishnasaigifhub"
qr = qrcode.make(data)
qr.save("githud.png")
print("QR code generated and saved as 'github.png'")