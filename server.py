from flask import Flask, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager # For Auth Module
app = Flask(__name__)

# Importing Apps
# -- Auth
# -- En/Dec Suite

# Signin
"""
Check for Password and username
    Please enter username and password
If provided check if length is between 8 and 30
    If not, return: Ooops.. Username or Password seems to be incorrect
If yes, check for username and it's corresponding hashed password. Retrieve the password and verify it.
    If inaccurate return: Ooops.. Username or Password seems to be incorrect
If correct, return a JWT
    If error occurs return: Something seems to be not right, try again please? 
"""

# Signup



# Signout



@app.route('/')
def hello_world():
    return jsonify({"message":"Dream on"});