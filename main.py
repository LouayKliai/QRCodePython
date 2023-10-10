import pyqrcode
link =input("Enter a link or a text : ")
url =pyqrcode.create(link)
url.png("QRCODE.png",scale=6)
print("QR Code generated successfully!")