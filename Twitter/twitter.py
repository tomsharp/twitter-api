from TwitterAPI import TwitterAPI
import yaml
import json 

def get_twitter_api_credentials(config_file):
    with open(config_file, 'r') as file:
        vals = yaml.load(file, Loader=yaml.FullLoader)
    if not ('API_KEY' in vals.keys() and
            'API_SECRET_KEY' in vals.keys() and
            'ACCESS_TOKEN' in vals.keys() and
            'ACCESS_TOKEN_SECRET' in vals.keys()
            ):
        raise Exception('Bad config file (need api keys): ' + config_file)
    return vals['API_KEY'], vals['API_SECRET_KEY'], vals['ACCESS_TOKEN'], vals['ACCESS_TOKEN_SECRET']

def connect(config_file='./twitter/config.yaml'):
    api_key, api_secret_key, access_token, access_token_secret = get_twitter_api_credentials(config_file)
    connection = TwitterAPI(api_key, api_secret_key, access_token, access_token_secret)
    return connection

def request(connection=None, endpoint=None, params=None):
    if not connection:
        connection = connect()
    response = connection.request(endpoint, params)
    return response.json()