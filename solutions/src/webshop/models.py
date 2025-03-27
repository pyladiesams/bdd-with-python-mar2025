from pydantic import BaseModel, Field
from typing import Dict, ClassVar, List, Literal


class Product(BaseModel):
    name: str
    price: float
    stock: int
    category: Literal["books", "electronics", ""] = ""
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, value) -> bool:
        if isinstance(value, str):
            return value == self.name
        return value.name == self.name
    

class Basket(BaseModel):
    OUT_OF_STOCK_MESSAGE: ClassVar[str] = "This item is out of stock!"
    items: Dict[Product, int] = Field(default_factory=dict)
    
    @property
    def total(self) -> float:
        return sum(product.price*quantity for product, quantity in self.items.items())
    
    def add(self, product: Product):
        if product.stock < 1:
            raise ValueError(self.OUT_OF_STOCK_MESSAGE)
        if product in self.items:
            self.items[product] += 1
            return
        self.items[product] = 1
        
    def remove(self, product_name: str):
        if product_name in self.items:
            self.items[product_name] -= 1
        if self.items[product_name] == 0:
            del(self.items[product_name])
            
    def show(self) -> List[str]:
        return list(self.items.keys())

        
class User(BaseModel):
    basket: Basket
    country: str  = ""
    is_vip: bool = False
    
    def with_name(self, name: str) -> 'RegisteredUser':
        return RegisteredUser(name=name, basket=self.basket)
    
    def checkout(
        self,
        tax_rates: Dict[str, Dict[bool, float]],
        shipping_costs: Dict[str, Dict[bool, float]]
        ) -> float:
        total: float = 0.0
        for product, quantity in self.basket.items.items():
            product_tax_rate = float(tax_rates[self.country][product.category]) + 1
            total += product.price * quantity * product_tax_rate
            
        shipping = float(shipping_costs[self.country]["vip" if self.is_vip else "not_vip"])
        total += shipping
        return round(total, 2)
        
    
class RegisteredUser(User):
    name: str
    
    @classmethod
    def login(cls, user_data: User, name: str) -> 'RegisteredUser':
        return cls(
            **user_data.model_dump(),
            name=name,
        )
