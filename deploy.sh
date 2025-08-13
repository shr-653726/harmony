#!/bin/bash

# Azure App Service Deployment Script for Harmony Website

echo "🚀 Deploying Harmony Website to Azure App Service..."

# Set variables
RESOURCE_GROUP="harmony-demo-rg"
APP_NAME="harmonyai"
LOCATION="eastus"
PLAN_NAME="harmony-demo-plan"

# Check if Azure CLI is installed
if ! command -v az &> /dev/null; then
    echo "❌ Azure CLI is not installed. Please install it first:"
    echo "   https://docs.microsoft.com/en-us/cli/azure/install-azure-cli"
    exit 1
fi

# Login to Azure (if not already logged in)
echo "🔐 Checking Azure login status..."
if ! az account show &> /dev/null; then
    echo "🔐 Please login to Azure..."
    az login
fi

# Create resource group
echo "📦 Creating resource group: $RESOURCE_GROUP"
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create App Service Plan (Linux, Free tier)
echo "📋 Creating App Service Plan: $PLAN_NAME"
az appservice plan create \
    --resource-group $RESOURCE_GROUP \
    --name $PLAN_NAME \
    --is-linux \
    --sku F1

# Create Web App
echo "🌐 Creating Web App: $APP_NAME"
az webapp create \
    --resource-group $RESOURCE_GROUP \
    --plan $PLAN_NAME \
    --name $APP_NAME \
    --runtime "PYTHON|3.11" \
    --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 app:app"

# Configure deployment from local git
echo "🔧 Configuring deployment..."
az webapp deployment source config-local-git \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME

# Get deployment URL
DEPLOY_URL=$(az webapp deployment list-publishing-credentials \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --query scmUri \
    --output tsv)

echo "✅ Azure App Service created successfully!"
echo "🌍 Your app will be available at: https://$APP_NAME.azurewebsites.net"
echo "📤 Deploy your code using:"
echo "   git init"
echo "   git add ."
echo "   git commit -m 'Initial commit'"
echo "   git remote add azure $DEPLOY_URL"
echo "   git push azure main"

# Generate QR code with the correct URL
echo "🔢 Generating QR code with deployment URL..."
python3 generate_qr.py

echo "🎉 Deployment configuration complete!"
echo ""
echo "📋 Next steps:"
echo "1. Copy your Harmony APK to the static folder"
echo "2. Add app screenshots to the static folder"
echo "3. Run the git commands above to deploy"
echo ""
echo "📁 Required files in static folder:"
echo "   - harmony-app.apk (your compiled APK)"
echo "   - app-screenshot.png (main app screenshot)"
echo "   - screenshot-1.png, screenshot-2.png, screenshot-3.png"
echo "   - harmony-icon.png (app icon)"
