from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    title: str
    iscompleted: bool

class TaskCreate(TaskSchema):
    pass

class TaskResponse(TaskSchema):
    id: int

    class Config:
        from_attributes = True