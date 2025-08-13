#!/usr/bin/env python3
import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import qrcode

def setup_demo_assets():
    """Setup demo assets for the Harmony website"""
    
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    print("🎨 Setting up demo assets for Harmony website...")
    
    # 1. Copy APK if it exists
    apk_source = os.path.join(os.path.dirname(__file__), '..', 'debug', 'composeApp-debug.apk')
    apk_dest = os.path.join(static_dir, 'harmony-app.apk')
    
    if os.path.exists(apk_source):
        shutil.copy2(apk_source, apk_dest)
        print(f"✅ Copied APK: {apk_dest}")
    else:
        print(f"⚠️  APK not found at {apk_source}")
        print("   Build your app first: ./gradlew assembleDebug")
    
    # 2. Generate QR code
    generate_qr_code(static_dir)
    
    # 3. Create placeholder screenshots if they don't exist
    create_placeholder_screenshots(static_dir)
    
    # 4. Create app icon
    create_app_icon(static_dir)
    
    print("🎉 Asset setup complete!")
    print(f"📁 Assets created in: {static_dir}")

def generate_qr_code(static_dir):
    """Generate QR code for APK download"""
    
    # Your actual Azure website URL
    download_url = "https://cts-vibeappau6113-4.azurewebsites.net/download"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    qr.add_data(download_url)
    qr.make(fit=True)
    
    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code
    qr_path = os.path.join(static_dir, 'qr-code.png')
    qr_img.save(qr_path, 'PNG')
    
    print(f"✅ Generated QR code: {qr_path}")

def create_placeholder_screenshots(static_dir):
    """Create placeholder screenshots for demo"""
    
    screenshots = [
        ('app-screenshot.png', 'Harmony\nAI Chat', '#667eea'),
        ('screenshot-1.png', 'Dashboard\nView', '#764ba2'),
        ('screenshot-2.png', 'AI Chat\nInterface', '#667eea'),
        ('screenshot-3.png', 'Goal\nTracking', '#6bcf7f')
    ]
    
    for filename, text, color in screenshots:
        filepath = os.path.join(static_dir, filename)
        
        if not os.path.exists(filepath):
            # Create a 300x600 placeholder image
            img = Image.new('RGB', (300, 600), color)
            draw = ImageDraw.Draw(img)
            
            # Try to use a nice font, fallback to default
            try:
                font = ImageFont.truetype("Arial", 36)
            except:
                font = ImageFont.load_default()
            
            # Calculate text position (center)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            x = (300 - text_width) // 2
            y = (600 - text_height) // 2
            
            # Draw text
            draw.text((x, y), text, fill='white', font=font, align='center')
            
            # Save image
            img.save(filepath, 'PNG')
            print(f"✅ Created placeholder: {filename}")

def create_app_icon(static_dir):
    """Create a simple app icon"""
    
    icon_path = os.path.join(static_dir, 'harmony-icon.png')
    
    if not os.path.exists(icon_path):
        # Create a 256x256 icon
        img = Image.new('RGB', (256, 256), '#667eea')
        draw = ImageDraw.Draw(img)
        
        # Draw a simple harmony symbol (circle with lines)
        # Outer circle
        draw.ellipse([40, 40, 216, 216], fill='white')
        
        # Inner design - simplified harmony symbol
        draw.ellipse([80, 80, 176, 176], fill='#667eea')
        draw.ellipse([100, 100, 156, 156], fill='white')
        
        # Add "H" in the center
        try:
            font = ImageFont.truetype("Arial", 48)
        except:
            font = ImageFont.load_default()
        
        draw.text((115, 110), 'H', fill='#667eea', font=font)
        
        img.save(icon_path, 'PNG')
        print(f"✅ Created app icon: {icon_path}")

if __name__ == "__main__":
    setup_demo_assets()
