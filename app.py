from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/download')
def download():
    """Direct download link for APK"""
    return send_from_directory('static', 'harmony-app.apk', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
