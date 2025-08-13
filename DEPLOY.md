# Deploy Harmony Website to cts-vibeappau6113-4.azurewebsites.net

## 🚀 Quick Deployment (Recommended)

### Option 1: Azure Portal Zip Deploy (Easiest)

1. **Download the package**: `harmony-website.zip` (already created)

2. **Go to Azure Portal**:
   - Navigate to your App Service: `cts-vibeappau6113-4`
   - Go to **Development Tools** > **Advanced Tools** > **Go**
   - This opens Kudu console

3. **Deploy**:
   - Click **Tools** > **Zip Push Deploy**
   - Drag and drop `harmony-website.zip`
   - Wait for deployment to complete

4. **Verify**: Visit https://cts-vibeappau6113-4.azurewebsites.net

### Option 2: Git Deployment

```bash
# Run the deployment script
./deploy-to-existing.sh

# Follow the git commands shown
git init
git add .
git commit -m "Harmony demo website"
git remote add azure [URL_FROM_SCRIPT]
git push azure main
```

## 🎯 What You Get

### Beautiful Landing Page
- **Professional design** with gradient hero section
- **Animated QR code** for instant APK download
- **App screenshots** showcasing features
- **Mobile responsive** for all devices

### Working Download
- **QR Code**: Points to `https://cts-vibeappau6113-4.azurewebsites.net/download`
- **Direct Link**: Downloads your actual APK file
- **Mobile optimized**: Perfect for demo scanning

### Demo Ready Features
- ✅ **Fast loading** - Optimized for presentations
- ✅ **Professional look** - Impressive for investors
- ✅ **QR code works** - Real download functionality
- ✅ **Mobile responsive** - Works on all devices
- ✅ **Your actual APK** - Real app download

## 📱 For Tonight's Demo

### Presentation Flow
1. **Show website** on projector: https://cts-vibeappau6113-4.azurewebsites.net
2. **Let audience scan QR code** to download app
3. **Navigate through features** on the website
4. **Demo app** on mobile device

### QR Code Usage
- **Audience scans** → Downloads APK immediately
- **No app store needed** → Direct install
- **Works offline** → QR code cached on phones

## 🔧 Files Included

```
✅ app.py - Flask web server
✅ templates/index.html - Beautiful landing page
✅ static/style.css - Modern responsive design
✅ static/script.js - Interactive animations
✅ static/harmony-app.apk - Your actual APK (50MB)
✅ static/qr-code.png - QR code pointing to your site
✅ static/screenshots/ - App preview images
✅ requirements.txt - Python dependencies
✅ web.config - Azure configuration
```

## 🎉 You're Ready!

After deployment:
- **Website**: https://cts-vibeappau6113-4.azurewebsites.net
- **APK Download**: https://cts-vibeappau6113-4.azurewebsites.net/download
- **QR Code**: Points to your download link
- **Demo Ready**: Professional presentation platform

## 🚨 Quick Checklist

- [ ] Deploy `harmony-website.zip` to Azure
- [ ] Test website loads: https://cts-vibeappau6113-4.azurewebsites.net
- [ ] Test APK download works
- [ ] Test QR code scanning
- [ ] Practice demo flow

**Perfect for tonight's demo! 🎯**
