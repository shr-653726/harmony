#!/usr/bin/env python3
import qrcode
from PIL import Image, ImageDraw
import os

def generate_qr_code():
    # Your actual Azure website URL
    download_url = "https://cts-vibeappau6113-4.azurewebsites.net/download"
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data
    qr.add_data(download_url)
    qr.make(fit=True)
    
    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code directly
    final_img = qr_img
    
    # Save the QR code
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    qr_path = os.path.join(static_dir, 'qr-code.png')
    final_img.save(qr_path, 'PNG', quality=95)
    
    print(f"QR code generated successfully: {qr_path}")
    print(f"QR code points to: {download_url}")
    
    return qr_path

if __name__ == "__main__":
    generate_qr_code()
