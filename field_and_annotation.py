# pip install pydantic
# pip install email-validator

from pydantic import BaseModel, EmailStr, Field, AnyUrl
from typing import Annotated, List, Optional, Dict

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the Patient', description='Provide the name of the patient in less than 50 chars', examples=['Ramesh', 'Sam'])]
    email: EmailStr
    linkedinUrl: AnyUrl
    age: int = Field(gt=0, lt=80)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='is the patient married or not')]
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_details: Dict[str, str]

def get_patient_data(patient: Patient):
    print(patient.name)    
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("Patient's record has been fetched")

patient_info = {'name': 'Ramesh',
                'email': 'ramesh@gmail.com',                    # email will be validated by using emailstr (must install email-validator for it to work)
                'linkedinUrl': 'http://linkedin.com/abcd342d',  # Email validator
                'age': '40',                                    # It will automatically converted to integer by pydantic
                'weight': 76.3,
                'contact_details': {
                    'phone': '4567890'
                }
                }

patient1 = Patient(**patient_info)                  # Dictionary unpacking
get_patient_data(patient1)

'''
patient1 = Patient(**patient_info)

This above line is exactly the same as:

patient1 = Patient(
    name='Ramesh',
    email='ramesh@gmail.com',
    linkedin_url='http://linkedin.com/abcd342d',
    age='40',
    weight=76.3,
    contact_details={'phone':'4567890'}
)

'''
