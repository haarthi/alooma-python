import alooma
import yaml

with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)

api = alooma.Client(api_key=config['alooma']['api_key'], account_name=config['alooma']['account_name'])

print api

