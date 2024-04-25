user_serializer = api.model('User', {
    'email': fields.String(required=True, description='User email'),
    'company_name': fields.String(description='Company name'),
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
    'password': fields.String(description='User password'),
    'mobile_number': fields.String(description='Mobile number')
})