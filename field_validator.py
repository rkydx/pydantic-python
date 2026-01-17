# pip install pydantic
# pip install email-validator

from pydantic import BaseModel, EmailStr, Field, AnyUrl, field_validator
from typing import Annotated, List, Optional, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedinUrl: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')                               # For validating email address's domain name
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['boa.com', 'fox.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')                                 # It will help to capitalize the name field's value
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('Updated the record')

patient_info = {
    'name': 'John',
    'email': 'john@boa.com', 
    #'email': 'john@gmail.com', 
    'linkedinUrl': 'http://linkedin.com/34509',
    'age': '48',
    'weight': 78.2,
    'married': True,
    'allergies': ['dust', 'sun'],
    'contact_details': {
        'phone': '34595095'
    }
}    

patient1 = Patient(**patient_info)

update_patient_data(patient1)
