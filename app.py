from flask import Flask

app = Flask(__name__)  # Create a Flask web app

@app.route('/')
def home():
    return "Hello, Docker!"  # Display this text on the webpage

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run the app on port 5000

