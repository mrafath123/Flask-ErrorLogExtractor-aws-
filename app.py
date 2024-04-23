from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'files[]' not in request.files:
        return "No file part"
    
    files = request.files.getlist('files[]')
    error_lines = []

    for file in files:
        if file.filename == '':
            return 'No selected file'
        
        if file:
            filename = file.filename
            file.save(os.path.join('./uploads', filename))
            with open(os.path.join('./uploads', filename), 'r') as f:
                for line in f:
                    if 'error' in line.lower():
                        error_lines.append(line)
    
    with open('./uploads/error_log.txt', 'w') as f:
        f.write('\n'.join(error_lines))
    
    return send_file('./uploads/error_log.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
