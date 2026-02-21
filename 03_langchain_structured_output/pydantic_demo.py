""" "this file is for the demo of the pydantic library
using pip install pydantic

pydantic is a data validation and data parsing library
in python .
it ensures that the data you work with is correct structured and type safe"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str


new_student = {"name": "yashchauhan"}

student = Student(**new_student)

print(student)  # name='yashchauhan'
print(type(student))  # <class '__main__.Student'>

# if i try to put another type value in name it will throw error
# for eg

# wrong_student_dict = {"name":32}
# wrong_student= Student(**wrong_student_dict)
# print(wrong_student)
# print(type(wrong_student))


# this code give below error
# Traceback (most recent call last):
#   File "c:\Users\pc\Desktop\langchain_structured_output\pydantic_demo.py", line 26, in <module>
#     wrong_student= Student(**wrong_student_dict)
#   File "C:\Users\pc\AppData\Local\Programs\Python\Python313\Lib\site-packages\pydantic\main.py", line 250, in __init__
#     validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
# pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
# name
#   Input should be a valid string [type=string_type, input_value=32, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_type


# Now how to give default values in pydantic


class Student2(BaseModel):
    name: str = (
        "yash"  ##this will come in output if no name is configured in input dict
    )
    age: Optional[int] = None
    email: EmailStr


new_student = {"email": "abc@gmail.com"}

student_3 = Student2(**new_student)

print(student_3)

print(student_3.name)

# pydantic smart enough for type conversions normal values it can understand like '32' to 32 in age

# i used emailstr type in email
# so if i do

new_student = {"email": "abc@gmail.com"}


student_3 = Student2(**new_student)

print(student_3)


# field function used to do many things defaultvalues , contraints and regex


class Student3(BaseModel):
    name: str = (
        "yash"  ##this will come in output if no name is configured in input dict
    )
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(
        gt=0,
        lt=10,
        default=5.0,
        description="A decimal value represting the cgpa of the student",
    )


new_student = {"age": 32, "email": "abcd@yahoo.com", "cgpa": 9.9}

student_testing = Student3(**new_student)
print(student_testing)

# when i pass cgpa like this new_student = {'age':32,'email':'abcd@yahoo.com','cgpa':15}
# it throws error like this below
# Traceback (most recent call last):
#   File "c:\Users\pc\Desktop\langchain_structured_output\pydantic_demo.py", line 84, in <module>
#     student_testing = Student3(**new_student)
#   File "C:\Users\pc\AppData\Local\Programs\Python\Python313\Lib\site-packages\pydantic\main.py", line 250, in __init__
#     validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
# pydantic_core._pydantic_core.ValidationError: 1 validation error for Student3
# cgpa
#   Input should be less than 10 [type=less_than, input_value=15, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/less_than
