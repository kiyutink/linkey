from pydantic import BaseModel


class LinkBase(BaseModel):
    original_url: str
    has_redirection: bool


class LinkCreate(LinkBase):
    pass


class Link(LinkBase):
    short_url: str

    class Config:
        orm_mode = True
