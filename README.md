# Harmony Demo Website

A beautiful, modern landing page to showcase the Harmony AI app for your demo. Features QR code download, app screenshots, and professional presentation.

## 🚀 Quick Deploy to Azure

### Prerequisites
- Azure CLI installed and configured
- Python 3.11+
- Git

### Step 1: Setup Assets
```bash
# Navigate to website directory
cd website

# Install Python dependencies
pip install -r requirements.txt

# Setup demo assets (APK, screenshots, QR code)
python setup_assets.py
```

### Step 2: Deploy to Azure
```bash
# Run the deployment script
./deploy.sh

# Follow the git commands shown after deployment
```

### Step 3: Access Your Site
Your website will be available at: `https://harmonyai.azurewebsites.net`

## 🎨 Features

### Modern Design
- **Gradient Hero Section** - Eye-catching background with floating animations
- **Interactive QR Code** - Glowing, animated QR code for APK download
- **Phone Mockup** - 3D phone with floating feature cards
- **Responsive Design** - Works perfectly on all devices

### Content Sections
1. **Hero** - Main intro with download QR code
2. **Features** - 6 key app features with icons
3. **Screenshots** - App interface previews
4. **Tech Stack** - Technology highlights
5. **CTA** - Final download call-to-action
6. **Footer** - Contact and links

### Interactive Elements
- Smooth scrolling navigation
- Hover animations on cards
- Parallax hero background
- Pulsing QR code effects
- Loading animations

## 📁 File Structure

```
website/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── deploy.sh             # Azure deployment script
├── setup_assets.py       # Asset preparation script
├── generate_qr.py        # QR code generation
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Modern CSS styling
    ├── script.js         # JavaScript interactions
    ├── qr-code.png       # Download QR code
    ├── harmony-app.apk   # Your compiled APK
    ├── harmony-icon.png  # App icon
    └── screenshot-*.png  # App screenshots
```

## 🔧 Customization

### Update Content
Edit `templates/index.html` to modify:
- App description
- Feature descriptions
- Contact information

### Styling
Edit `static/style.css` to change:
- Color scheme
- Animations
- Layout

### Add Real Screenshots
Replace placeholder images in `static/` with:
- `app-screenshot.png` - Main hero screenshot
- `screenshot-1.png` - Dashboard view
- `screenshot-2.png` - Chat interface
- `screenshot-3.png` - Goal tracking

## 🌐 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Setup assets
python setup_assets.py

# Run locally
python app.py

# Visit http://localhost:8000
```

## 📱 APK Download

The website automatically serves your APK from `/download`. Make sure to:
1. Build your app: `./gradlew assembleDebug`
2. Run `python setup_assets.py` to copy the APK
3. Update QR code URL after deployment

## 🎯 Demo Tips

### For Your Presentation
1. **Open website on projector** - Professional landing page
2. **Show QR code** - Let audience scan to download
3. **Navigate through features** - Highlight key capabilities
4. **Mobile responsive** - Demo on phone/tablet

### Performance Features
- **Fast loading** - Optimized images and code
- **Mobile-first** - Perfect for phone demos
- **Professional design** - Impressive for investors
- **QR download** - Easy for audience to get app

## 🚨 Troubleshooting

### APK not found
```bash
# Build the APK first
cd ..
./gradlew assembleDebug
cd website
python setup_assets.py
```

### Azure deployment fails
```bash
# Check Azure CLI login
az account show

# Verify resource group
az group list --query "[?name=='harmony-demo-rg']"
```

### QR code not working
- Update URL in `generate_qr.py`
- Regenerate: `python generate_qr.py`

## 🎉 Ready for Demo!

Your professional Harmony website is ready to impress your audience with:
- ✅ Beautiful modern design
- ✅ Working QR code download
- ✅ Professional presentation
- ✅ Mobile responsive
- ✅ Fast loading
- ✅ Azure hosted

Perfect for tonight's demo! 🚀
