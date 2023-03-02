# CSV FILE TO POSTMAN COLLECTION

## INSTALLING 
``` bash
git clone git@github.com:ikromnurrohim/csv-to-postman-collection.git
```
``` bash
pip install -r requirements.txt
```


## CSV FORMAT
#### - For make a collection without folder, CSV format must like this
![image](https://user-images.githubusercontent.com/59647417/222404294-0557dbcd-54f2-419d-bdea-ad02a9644167.png)

#### Result of collection will be like this
![image](https://user-images.githubusercontent.com/59647417/222405393-16f58976-e8f9-45f3-b4f1-f6386b690051.png)
<br>
#### - For make a collection with nested folder, CSV format must like this
![image](https://user-images.githubusercontent.com/59647417/222403422-b00b0f0a-c83b-4eb4-b379-f62e497b057c.png)

#### Result of collection will be like this
![image](https://user-images.githubusercontent.com/59647417/222408799-8fc3f18a-9de9-40f7-a4b4-5157f97d39e8.png)


## FOR USING 
### Edit file run.py
- To make collection without folder \
update csv file and json file 
![image](https://user-images.githubusercontent.com/59647417/222413066-35a530ce-62d0-43be-95df-9228d5da7c4f.png)

- To make collection with nested folder \
update csv file and json file 
![image](https://user-images.githubusercontent.com/59647417/222413465-b98a7a76-70f0-4d9e-8bcf-49edf21175e7.png)

### Running script
```python
python run.py
```

