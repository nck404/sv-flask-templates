import os
import requests
from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password') or not data.get('recaptcha_token'):
        return jsonify({"msg": "Missing required fields"}), 400
    
    # Verify Google reCAPTCHA
    secret_key = os.getenv('RECAPTCHA_SECRET_KEY', '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe')
    token = data['recaptcha_token']
    
    verify_response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': secret_key,
            'response': token
        }
    )
    
    result = verify_response.json()
    if not result.get('success'):
        return jsonify({"msg": "Invalid reCAPTCHA"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "Username already exists"}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Email already exists"}), 400

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"msg": "Missing username or password"}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        user.last_login_ip = request.remote_addr
        db.session.commit()
        
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 401
    return jsonify(user.to_dict()), 200

@auth_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    data = request.get_json()
    if 'username' in data and data['username'] != user.username:
        # Check cooldown
        if user.username_last_updated:
            from datetime import datetime, timedelta
            diff = datetime.utcnow() - user.username_last_updated
            if diff < timedelta(days=14):
                remaining = 14 - diff.days
                return jsonify({"msg": f"Bạn mới đổi tên gần đây. Hãy đợi thêm {remaining} ngày nữa."}), 400

        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user and existing_user.id != user.id:
            return jsonify({"msg": "Username already exists"}), 400
        
        user.username = data['username']
        from datetime import datetime
        user.username_last_updated = datetime.utcnow()
    
    if 'email' in data:
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user and existing_user.id != user.id:
            return jsonify({"msg": "Email already exists"}), 400
        user.email = data['email']
        
    if 'avatar_url' in data:
        user.avatar_url = data['avatar_url']

    if 'bio' in data:
        user.bio = data['bio']
    
    if 'job_title' in data:
        user.job_title = data['job_title']
    
    if 'links' in data:
        user.links = data['links']


    db.session.commit()
    return jsonify(user.to_dict()), 200

@auth_bp.route('/user/<int:user_id>', methods=['GET'])
def get_public_profile(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

