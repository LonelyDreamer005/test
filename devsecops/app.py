
from flask import Flask

app = Flask(__name__)

# Vulnerability 1: Hardcoded password
# password = "admin123"
os.environ.get("APP_PASSWORD")

@app.route('/')
def home():
    return "Welcome!"

# Vulnerability 2: Debug mode enabled
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)  
