from flask import Flask, render_template, request, redirect, url_for
from database.config import db
from routes.user import user_bp

app = Flask(__name__)

# Register the user blueprint
app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
