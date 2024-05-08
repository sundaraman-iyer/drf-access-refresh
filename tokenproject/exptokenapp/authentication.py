import jwt, datetime
from rest_framework import exceptions

def create_access_token(id): #access should faster than the refresh token
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.now() + datetime.timedelta(seconds = 60),
        'iat': datetime.datetime.now()
    }, 'access_secret', algorithm='HS256')

#method to decode the access token 
def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthicated!!')

#create refresh token
def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.now() + datetime.timedelta(days = 7),
        'iat': datetime.datetime.now()
    }, 'refresh_secret', algorithm='HS256')


#method to decode the refresh token 
def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthicated')
