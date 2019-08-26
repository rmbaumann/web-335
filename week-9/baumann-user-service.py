# ;============================================
# ; Title: Exercise 9.2
# ; Author: Reva Baumann
# ; Date: 25 August 2019
# ; Modified By: Reva Baumann
# ; Description: Python query
# ;===========================================

# Import Python mongo, python datetime, pretty print
import pymongo
import datetime
import pprint

# Headeer
print ('Reva Baumann')
print ('Web 335 - Exercise 9.2')
print(f'{datetime.datetime.now().strftime("%c")}')

# Expected Output
# Reva Baumann
# Web 335 - Exercise 9.2
# datetime

#import MongoCiient using
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
employee_id = 2430304

# Declare user document and define
user = {
    "first_name": "Diana",
    "last_name": "Prince",
    "email": "dprince@jla.com",
    "employee_id": employee_id,
    "date_created": datetime.datetime.utcnow()
}

# Declare the user variables
user_id = db.users.insert_one(user).inserted_id
result = db.users.find_one({"employee_id":employee_id})

# Print the output
print(f'Inserted user id {user_id}')
print(f'Find by employee_id {employee_id}')
pprint.pprint(results)

# end program