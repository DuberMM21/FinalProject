from pydantic import BaseModel

class ResourceBase(BaseModel):
    name: str
    description: str
    quantity: int
    available: bool

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int

    class Config:
        from_attributes = True
