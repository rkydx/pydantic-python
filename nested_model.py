# A nested model in Pydantic means using one BaseModel class inside another model as a field type.

from pydantic import BaseModel

class Address(BaseModel):

    city: str
    area: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'woodland', 'area': 'west', 'pin': '435643'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Ramesh', 'gender': 'male', 'age': 54, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)