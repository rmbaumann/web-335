# ;============================================
# ; Title: Exercise 9.3
# ; Author: Reva Baumann
# ; Date: 25 August 2019
# ; Modified By: Reva Baumann
# ; Description: Updating and Deleting Documents
# ;===========================================

# Headeer
print ('Reva Baumann')
print ('Web 335 - Exercise 9.3')
print(f'{datetime.datetime.now().strftime("%c")}')

# import modules
import pymongo
import datetime
import pprint

# Import MongoClient 
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.web335
employee_id = 2430304

# declare user variable and insert
db.users.update_one{
    {"employee_id":employee_id}
    {
        "$set":{
            "email":"dprince@jla.com"
        }
    }
}

# results
result = db.user.find_one({"employee_id":employee_id})

# Output and print
print(f'Find by employee_id {employee_id}')
pprint.pprint(result)

# End program