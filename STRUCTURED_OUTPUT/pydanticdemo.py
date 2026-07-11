from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Nipun" # default value
    age: Optional[int] = None # default value
    email: EmailStr
    cgpa: float = Field(gt=3.0, lt=10.0, default=5.0, description="A description of cgpa between 3 and 10")

new_student = {"age" : '22',"email":"abc@gmail.com", "cgpa":9.5} # automatic type conversion by pydantic 

std = Student(**new_student)

print(std)
student = dict(std) # convert to dict
print(student["cgpa"])
student_json = std.model_dump_json() # convert to json
print(student_json)
