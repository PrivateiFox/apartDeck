from pydantic import BaseModel


class ApartmentBase(BaseModel):
    link: str
    city: str
    street: str
    apartment_price: int
    hoa_price: int
    rates_price: int
    notes: str
    phone_number: str

    class Config:
        orm_mode = True


class ApartmentCreate(ApartmentBase):
    pass


class Apartment(ApartmentBase):
    id: int
    is_valid: int

    class Config:
        orm_mode = True
