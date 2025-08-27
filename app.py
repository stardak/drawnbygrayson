import os
from flask import Flask, render_template, make_response
from werkzeug.middleware.proxy_fix import ProxyFix

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "grayson-portraits-key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.route('/')
def index():
    """Render the main page with cache-busting headers."""
    response = make_response(render_template('index.html'))
    # Add cache-busting headers to prevent old versions from being served
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response



if __name__ == '__main__':
    app.run(debug=True)
