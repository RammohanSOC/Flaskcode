from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def home():
    return 'ISS Technologies - Website is Live!'

if __name__ == '__main__':
    app.run()
