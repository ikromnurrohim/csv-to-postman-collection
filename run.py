from main import PostmanCollection
collection = PostmanCollection('collection.csv', 'collection.json')
collection.request()

collection = PostmanCollection('collection-v2.csv', 'collection-v2.json')
collection.with_nested_folder()

