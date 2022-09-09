"""
Simple QRcode generator

Requirements -> pyqrcode, pypng
"""

import pyqrcode
from datetime import datetime

def qrcode_generator(txt: str) -> None:
	"""
	Function to create QR code from the user input

	:parm: String data
	:return: None
	"""
	qr: pyqrcode.QRCode = pyqrcode.create(txt)
	qr.png(f"{datetime.now()}.png", scale=10)


if __name__ == "__main__":
	ip: str = input("Please enter: ")
	qrcode_generator(ip)