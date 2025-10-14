from flask import Flask, render_template_string
import os
import socket

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { margin-top: 0; }
        .info { 
            margin: 20px 0; 
            padding: 15px; 
            background: rgba(0,0,0,0.2); 
            border-radius: 5px; 
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 DevOps Project - Successfully Deployed!</h1>
        <div class="info">
            <p><strong>Hostname:</strong> {{ hostname }}</p>
            <p><strong>Environment:</strong> {{ environment }}</p>
            <p><strong>Version:</strong> {{ version }}</p>
        </div>
        <p>✅ Your CI/CD pipeline is working!</p>
        <p>This application was automatically deployed using GitHub Actions, Docker, and AWS.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        hostname=socket.gethostname(),
        environment=os.getenv('ENVIRONMENT', 'production'),
        version=os.getenv('APP_VERSION', '2.0.0')
    )

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)