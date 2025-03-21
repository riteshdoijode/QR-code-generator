import qrcode

# Load generated links
with open(r"Windows URL (Path) of the saved folder.", "r") as f:
    links = f.readlines()

# Create QR codes for each link
for i, link in enumerate(links):
    qr = qrcode.make(link.strip())  # Generate QR code
    qr.save(f"C:\\Users\\rites\\Desktop\\temp\\QR\\qr_code_{i+1}.png")

print("✅ QR Codes generated for all files!")