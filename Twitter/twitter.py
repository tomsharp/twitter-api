from TwitterAPI import TwitterAPI
import yaml
import json 

def get_twitter_api_credentials(config_file):
    with open(config_file, 'r') as file:
        vals = yaml.load(file, Loader=yaml.FullLoader)
    if not ('CONSUMER_KEY' in vals.keys() and
            'CONSUMER_SECRET' in vals.keys() and
            'ACCESS_TOKEN' in vals.keys() and
            'ACCESS_TOKEN_SECRET' in vals.keys()
            ):
        raise Exception('Bad config file (need api keys): ' + config_file)
    return vals['CONSUMER_KEY'], vals['CONSUMER_SECRET'], vals['ACCESS_TOKEN'], vals['ACCESS_TOKEN_SECRET']

def connect(config_file='./twitter/config.yaml'):
    consumer_key, consumer_secret, access_token, access_token_secret = get_twitter_api_credentials(config_file)
    connection = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    return connection

def request(connection=None, endpoint=None, params=None):
    if not connection:
        connection = connect()
    response = connection.request(endpoint, params)
    return response.json()