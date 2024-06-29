from pydantic import BaseModel

class Grievance(BaseModel):
    title:str
    description:str
    type:str
    department:str
    severity:str
    postedBy:str
    status:str= None
    forwardedTo:str= None