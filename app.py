import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World !!! Your Cloud Run pipeline is working perfectly! 🚀\n"

if __name__ == "__main__":
    # Cloud Run injects the PORT environment variable automatically
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
