import csv
import string
import random
from urllib.parse import urlparse
from flask import jsonify, json

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def random_dict():
  random_string = id_generator()
  _str = random_string
  globals()[_str] = 5000
  random_string = {}
  return random_string

class PostmanCollection:
  def __init__(self, csv_filename, collection_name):
    self.csv_filename = csv_filename
    self.collection_name = collection_name

  def request(self):
    collection_shceme = {
                          "info": {
                                "_postman_id": "432f9e34-5f9d-4ed2-ad2e-f60b1163248b",
                                "name": "PostmanCollection",
                                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
                                "_exporter_id": "24072707"
                                  },
                          "items": []
                        }
    with open(self.csv_filename) as csv_file:
      csv_file = csv.DictReader(csv_file)
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

        # append to collection_shceme itmes
        collection_shceme['items'].append(rand_dict)
    # beautify collection by indentation 4 and write to file
    collection = json.dumps(collection_shceme, indent=4)
    with open(self.collection_name, 'w') as outfile:
      outfile.write(collection)

  def with_nested_folder(self):
    collection_shceme = {
                          "info": {
                                "_postman_id": "432f9e34-5f9d-4ed2-ad2e-f60b1163248b",
                                "name": "PostmanCollection",
                                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
                                "_exporter_id": "24072707"
                                  },
                          "item": []
                        }
    with open(self.csv_filename) as csv_file:
    	csv_file = csv.DictReader(csv_file)
    	folder_name = None
    	counter_folder_name = 0
    	always_true = True
    	for row in csv_file:
    		# init random dictionary
    		rand_dict = random_dict()
    		rand_dict_item = random_dict()
    		rand_dict_request = random_dict()
    		rand_dict_body = random_dict()
    		rand_dict_url = random_dict()

    		# for fullfied collection_shceme['item'] if was fullfiled we continue in else
    		if counter_folder_name == 0:
    			# get folder name
    			folder_name = row['folder']

    			# assing folder_name to name
	    		rand_dict['name'] = folder_name

	    		# assing item with empty list
	    		rand_dict['item'] = []

	    		subfolder = row['subfolder']
	    		request_name = row['request-name']
	    		rand_dict_request['method'] = row['method']
	    		rand_dict_request['header'] = []
	    		rand_dict_request['body'] = rand_dict_body
	    		rand_dict_request['body']['mode'] = 'raw'
	    		rand_dict_request['body']['raw'] = row['body']
	    		rand_dict_request['body']['options'] = {"raw": {"language": "json"}}
	    		rand_dict_request['url'] = rand_dict_url
	    		rand_dict_request['url']['raw'] = row['url']
	    		# extract url to get protocol
	    		_url = urlparse(row['url'])
	    		protocol = _url.scheme
	    		rand_dict_request['url']['protocol'] = protocol
	    		# extract url to get hostname
	    		hostname = _url.netloc
	    		# extract hostname by (.)
	    		hostname = hostname.split('.')
	    		rand_dict_request['url']['host'] = []
	    		counter = 0
	    		for x in hostname:
	    			rand_dict_request['url']['host'].append(hostname[counter])
	    			counter += 1
	    			rand_dict_request['url']['path'] = []
	    			path = _url.path
	    		path = path.split('/')
	    		for x in path:
	    			if x != '':
	    				rand_dict_request['url']['path'].append(x)
    			rand_dict['item'] .append({'name':subfolder, 'item': [{'name': request_name, 'request': rand_dict_request}]})
    			collection_shceme['item'].append(rand_dict)
    			counter_folder_name += 1

    		else:
    			# if folder has same name then we want to merge them to one folder
    			if row['folder'] in collection_shceme['item'][-1]['name']:
    				subfolder = row['subfolder']
    				request_name = row['request-name']
    				rand_dict_request['method'] = row['method']
    				rand_dict_request['header'] = []
    				rand_dict_request['body'] = rand_dict_body
    				rand_dict_request['body']['mode'] = 'raw'
    				rand_dict_request['body']['raw'] = row['body']
    				rand_dict_request['body']['options'] = {"raw": {"language": "json"}}
    				rand_dict_request['url'] = rand_dict_url
    				rand_dict_request['url']['raw'] = row['url']
    				# extract url to get protocol
    				_url = urlparse(row['url'])
    				protocol = _url.scheme
    				rand_dict_request['url']['protocol'] = protocol
    				# extract url to get hostname
    				hostname = _url.netloc
    				# extract hostname by (.)
    				hostname = hostname.split('.')
    				rand_dict_request['url']['host'] = []
    				counter = 0
    				for x in hostname:
    					rand_dict_request['url']['host'].append(hostname[counter])
    					counter += 1
    				rand_dict_request['url']['path'] = []
    				path = _url.path
    				path = path.split('/')
    				for x in path:
    					if x != '':
    						rand_dict_request['url']['path'].append(x)
    				collection_shceme['item'][-1]['item'].append({'name':subfolder, 'item': [{'name': request_name, 'request': rand_dict_request}]})

    			# if the folder is not same, then we make them
    			else:
    				folder_name = row['folder']
    				rand_dict['name'] = folder_name
    				rand_dict['item'] = []
    				subfolder = row['subfolder']
    				request_name = row['request-name']
    				rand_dict_request['method'] = row['method']
    				rand_dict_request['header'] = []
    				rand_dict_request['body'] = rand_dict_body
    				rand_dict_request['body']['mode'] = 'raw'
    				rand_dict_request['body']['raw'] = row['body']
    				rand_dict_request['body']['options'] = {"raw": {"language": "json"}}
    				rand_dict_request['url'] = rand_dict_url
    				rand_dict_request['url']['raw'] = row['url']
    				# extract url to get protocol
    				_url = urlparse(row['url'])
    				protocol = _url.scheme
    				rand_dict_request['url']['protocol'] = protocol
    				# extract url to get hostname
    				hostname = _url.netloc
    				# extract hostname by (.)
    				hostname = hostname.split('.')
    				rand_dict_request['url']['host'] = []
    				counter = 0
    				for x in hostname:
    					rand_dict_request['url']['host'].append(hostname[counter])
    					counter += 1
    				rand_dict_request['url']['path'] = []
    				path = _url.path
    				path = path.split('/')
    				for x in path:
    					if x != '':
    						rand_dict_request['url']['path'].append(x)
    				rand_dict['item'] .append({'name':subfolder, 'item': [{'name': request_name, 'request': rand_dict_request}]})
    				collection_shceme['item'].append(rand_dict)
    collection_shceme = json.dumps(collection_shceme, indent=4)
    with open(self.collection_name, 'w') as outfile:
    	outfile.write(collection_shceme)
