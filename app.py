import os
from flask import Flask, request, render_template, send_file
import boto3

app = Flask(__name__)

# AWS S3 configuration
S3_BUCKET_NAME = 'your-s3-bucket-name'
AWS_ACCESS_KEY_ID = 'your-access-key-id'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def extract_error_lines(files):
    error_lines = []
    for file in files:
        # Read the file content
        content = file.read().decode('utf-8')
        # Extract error lines (case-sensitive)
        error_lines.extend([line.strip() for line in content.split('\n') if 'ERROR' in line.upper()])
    return error_lines

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('file[]')
    
    # Extract error lines
    error_lines = extract_error_lines(files)
    
    # Write error lines to a new file
    with open('error_log.txt', 'w') as f:
        for line in error_lines:
            f.write(line + '\n')
    
    # Upload the file to S3
    s3.upload_file('error_log.txt', S3_BUCKET_NAME, 'error_log.txt')
    
    # Return success message with download link
    return """
    <h3>Files uploaded and error lines extracted successfully.</h3>
    <p><a href="/download">Download Error Log</a></p>
    """

@app.route('/download')
def download_file():
    # Download the error log file from S3
    s3.download_file(S3_BUCKET_NAME, 'error_log.txt', 'downloaded_error_log.txt')
    
    # Return the file for download
    return send_file('downloaded_error_log.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
