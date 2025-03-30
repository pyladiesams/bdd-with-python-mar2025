from typing import List

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    stock: int


class Basket(BaseModel):
    @property
    def total(self) -> float:
        pass

    def add(self, product: Product):
        pass

    def remove(self, product_name: str):
        pass

    def show(self) -> List[str]:
        pass


class User(BaseModel):
    basket: Basket
    country: str = ""
    is_vip: bool = False
