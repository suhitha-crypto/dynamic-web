from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    """
    Returns the HTML content for the home page.
    """
    return """
<body style="font-family: Poppins, sans-serif;display:flex;justify-content:center;align-items:center;
height:100vh;background:linear-gradient(135deg, #667eea, #764ba2);color:white;">
    <div style="max-width:400px;text-align:center;">
        <h1>
            <span>👋</span>Welcome to my Dynamic Flask App!<span></h1>
        <p>Powered by Flask <span>&</span> enthusiasm!<span>🎉</span></p>
    </div>
</body>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)