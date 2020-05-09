from flask import request, jsonify, url_for, redirect
from common.models import User, AdminUser


@app.route('/member_register', methods=['POST'])
def member_register():
    """
    註冊 會員
    """
    request_data = request.get_json()
    email = request_data.get('email')
    username = request_data.get('username')
    non_hash_password = request_data.get('password')
    hash_password = Encrypt.encrypt_password(non_hash_password)
    source = OAuthType.OUR
    user = User(email=email,
                username=username,
                password=hash_password,
                source=source)
    db.session.add(user)
    db.session.commit()
    response_data = {'email': email, 'username': username, 'source': source}
    return jsonify(response_data)


@app.route('/member_login', methods=['POST'])
def member_login():
    """
    登錄 會員
    """
    request_data = request.get_json()
    email = request_data.get('email')
    password = request_data.get('password')
    user = User.query.filter_by(email=email).first()
    if not user:
        raise ValidationError(error_code=ErrorCodeDefine.USER_NOT_EXIST_OR_WRONG_PASSWORD)
    if not Encrypt.check_password(user.password, password):
        raise ValidationError(error_code=ErrorCodeDefine.USER_NOT_EXIST_OR_WRONG_PASSWORD)
    token = Login(user=user, email=email).get_token()
    response_data = {'email': user.email, 'username': user.username, 'token': token, 'source': user.source}
    return jsonify(response_data)


@app.route('/admin_login', methods=['POST'])
def admin_login():
    """
    登錄 管理員
    """
    request_data = request.get_json()
    username = request_data.get('username')
    password = request_data.get('password')
    user = AdminUser.query.filter_by(username=username).first()
    if not user:
        raise ValidationError(error_code=ErrorCodeDefine.USER_NOT_EXIST_OR_WRONG_PASSWORD)
    if not Encrypt.check_password(user.password, password):
        raise ValidationError(error_code=ErrorCodeDefine.USER_NOT_EXIST_OR_WRONG_PASSWORD)
    token = AdminLogin(user=user, username=username).get_token()
    response_data = {'email': user.email, 'username': user.username, 'token': token}
    return jsonify(response_data)
