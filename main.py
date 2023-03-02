import csv
import string
import random
from urllib.parse import urlparse
from flask import jsonify, json

collection = {
"info": {
    "_postman_id": "432f9e34-5f9d-4ed2-ad2e-f60b1163248b",
    "name": "Test",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    "_exporter_id": "24072707"
  },
"items": []
}

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def random_dict():
  random_string = id_generator()
  _str = random_string
  globals()[_str] = 5000
  random_string = {}
  return random_string


with open('collection.csv') as csv_file:
  csv_file = csv.DictReader(csv_file)
  line_count = 0
  for row in csv_file:
    # make random dictionary
    rand_dict = random_dict()

    # add request name to dict
    request_name = row['name']
    rand_dict['name'] = request_name

    # make dictionary request and append to random dictionary
    rand_dict['request'] = {}

    # add method random dictionary
    method = row['method']
    rand_dict['request']['method'] = method

    # add headers random dictionary
    rand_dict['request']['headers'] = []

    # init body dictionary to random dictionary
    rand_dict['request']['body'] = {}

    # add mode, raw body and options to random dictionary
    rand_dict['request']['body']['mode'] = 'raw'
    body = row['body']
    rand_dict['request']['body']['raw'] = body
    options = {
      "raw": {"language": "json"}
    }
    rand_dict['request']['body']['options'] = options

    # init url dictionary to random dictionary
    rand_dict['request']['url'] = {}

    # add url to url in random dictionary
    url = row['url']
    rand_dict['request']['url']['raw'] = url

    # extract url to get protocol
    _url = urlparse(url)
    protocol = _url.scheme

    # assing protocol to url protocol
    rand_dict['request']['url']['protocol'] = protocol

    # extract url to get hostname
    hostname = _url.netloc

    # extract hostname by (.)
    hostname = hostname.split('.')
    rand_dict['request']['url']['host'] = []
    counter = 0
    for x in hostname:
      rand_dict['request']['url']['host'].append(hostname[counter])
      counter += 1

    # add path list
    rand_dict['request']['url']['path'] = []

    # extract path by (/) and assing to path list
    path = _url.path
    path = path.split('/')
    for x in path:
      if x != '':
        rand_dict['request']['url']['path'].append(x)

    # append to collection itmes
    collection['items'].append(rand_dict)

# beautify collection by indentation 4 and write to file
collection = json.dumps(collection, indent=4)
with open('collection.json', 'w') as outfile:
  outfile.write(collection)












































