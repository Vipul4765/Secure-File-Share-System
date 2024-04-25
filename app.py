from flask import Flask
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']  # Replace 'your_database' with your actual database name
users_collection = db['users']


@api.route('/user-onboard')
class UserOnboard(Resource):
    @api.expect(onboard_parser)
    def post(self):
        """Onboard User"""
        args = onboard_parser.parse_args()
        email = args.get('email')
        company_name = args.get('company_name')
        first_name = args.get('first_name')
        last_name = args.get('last_name')
        password = args.get('password')

        # Check if email already exists
        if users_collection.find_one({'email': email}):
            return {"message": "Email already exists"}, 400

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert user data into the database
        user_data = {
            'email': email,
            'company_name': company_name,
            'first_name': first_name,
            'last_name': last_name,
            'password': hashed_password,
            'mobile_number': args.get('mobile_number')
        }
        users_collection.insert_one(user_data)

        return {"message": "User onboarded successfully"}, 201

if __name__ == '__main__':
    app.run(debug=True)
