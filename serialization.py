'''
Serialization in Pydantic means converting a Pydantic model object into formats like dict, JSON, or string so it can be stored, 
sent over network, or logged.

Serialization is used when sending API responses, saving to DB, or writing files from validated Python objects.
'''

from pydantic import BaseModel

class Address(BaseModel):

    city: str
    area: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address                # This is the nested model 

address_dict = {'city': 'woodland', 'area': 'west', 'pin': '435643'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Ramesh', 'gender': 'male', 'age': 54, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)
#temp = patient1.model_dump(include=['name', 'gender'])            # Only the name and gender field will be appearing 
#temp = patient1.model_dump_json(exclude_unset=True)

print(temp)
print(type(temp))