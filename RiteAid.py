# importing the requests library 
import requests 
import array
import json
# api-endpoint 
URL = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots"

responses = list() # stores responses for postal codes
# grab a list of rite aid store numbers you want to check
riteStoreNumbers = [11119, 995, 11158, 1144, 11116, 11101, 1733, 1567, 857, 11160,11127, 2564, 822,1672, 9845734]


# defining a params dict for the parameters to be sent to the API 

for store in riteStoreNumbers: 
    #print(i) 
    PARAMS = {'storeNumber':store} 
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    # extracting data in json format 
    data = r.json()
    y = json.dumps(data)
    slot1 = data['Data']['slots']['1']
    slot2 = data['Data']['slots']['2']

    if (slot1 == True):
        print(str(store) + ": " + y)
    
    if (slot2== True):
        print(str(store) + ": " + y)


