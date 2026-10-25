from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
   <h1>Cloud Computing Lab - PaaS - Version 2</h1>
   
    """
