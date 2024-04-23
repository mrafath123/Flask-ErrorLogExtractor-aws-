# Flask-ErrorLogExtractor-aws-

This is a Flask web application that allows users to upload multiple text files (logs), extracts error lines from the files, consolidates them into a single output file, and then stores the output file in an AWS S3 bucket. Users can also download the consolidated error log file.

## Prerequisites

- Python 3.x
- Flask
- Boto3

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your_username/log-analyzer-web-app.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Set up AWS credentials:

    Before running the application, ensure that you have set up your AWS credentials. You can either provide them directly in the code or set them as environment variables.

## Usage

1. Run the Flask application:

    ```
    python app.py
    ```

2. Access the application in your web browser at `http://localhost:5000`.

3. Upload one or more text files containing log data using the provided file upload form.

4. Click the "Upload" button to process the uploaded files. The application will extract error lines from the files, consolidate them into a single output file, and upload the output file to an AWS S3 bucket.

5. Once the upload is complete, you will see a success message with a link to download the consolidated error log file.

## Customization

- To customize the appearance or behavior of the application, you can modify the HTML templates (`index.html`) and the Python code (`app.py`).
- You can also modify the AWS S3 configuration in the Python code to use your own S3 bucket.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
