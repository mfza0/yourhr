from flask import Blueprint, request, redirect, url_for,render_template
from models import save_user
import os

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    resume = request.files.get('resume')

    if not resume:
        return "No File Part" , 400

    # Save the resume file
    resume_path = os.path.join('uploads', resume.filename)
    os.makedirs('uploads', exist_ok=True)
    resume.save(resume_path)

    # Store user details in MongoDB
    user_data = {
        'name': name,
        'email': email,
        'phone': phone,
        'resume_path': resume_path
    }
    save_user(user_data)

    return render_template('signup.html' , success=True)
