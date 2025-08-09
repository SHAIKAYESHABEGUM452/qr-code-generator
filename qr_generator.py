import qrcode  # Import the QR code library

# 1. Ask the user for the data they want to convert into a QR code
data = input("Enter the text or URL for the QR code: ")

# 2. Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 = smallest, 40 = largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border thickness
)

# 3. Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)  # Fit the QR code to the data

# 4. Create the image
img = qr.make_image(fill_color="black", back_color="white")

# 5. Save the image
file_name = "my_qr_code.png"
img.save(file_name)

print(f"QR code successfully created and saved as {file_name}")
