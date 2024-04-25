import argparse

onboard_parser = reqparse.RequestParser()
onboard_parser.add_argument('email', type=str, required=True, help='User email is required')
onboard_parser.add_argument('company_name', type=str)
onboard_parser.add_argument('first_name', type=str)
onboard_parser.add_argument('last_name', type=str)
onboard_parser.add_argument('password', type=str, required=True, help='User password is required')
onboard_parser.add_argument('mobile_number', type=str)