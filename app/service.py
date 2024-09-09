from form_validator import Orders, Address
from abc import ABC, abstractmethod

class Processor(ABC):
    def __init__(self):
        pass
        
    @abstractmethod
    def process():
        pass
    
class NameProcessor(Processor):
    def __init__(self, orders: Orders):
        self.orders= orders
        
    def process(self):
        if not self.is_name_all_letters():
            return (400, 'Name contains non-English characters')
        if not self.are_name_initials_uppercase():
            return (400, 'Name is not capitalized')
        return (0,'')
    
    def is_name_all_letters(self):
        name = self.orders.name
        return name.replace(" ", "").isalpha()
    
    def are_name_initials_uppercase(self):
        name = self.orders.name
        return all(word[0].isupper() for word in name.split())
    
class PriceProcessor(Processor):
    def __init__(self, orders: Orders, threshold=2000):
        self.orders= orders
        self.threshold=threshold
        
    def process(self):
        if self.is_price_above_threshold():
            return (400, 'Price is over 2000')
        return (0,'')
        
    def is_price_above_threshold(self):
        return int(self.orders.price) > self.threshold
    
class CurrencyProcessor(Processor):
    def __init__(self, orders: Orders):
        self.orders= orders
        
    def process(self):
        if not self.check_currency():
            return (400, 'Currency format is wrong')
        self.convert_currency()
        return (0,'')
    
    def check_currency(self):
        return self.orders.currency in ['TWD', 'USD']

    def convert_currency(self):
        if self.orders.currency=='USD':
            self.orders.price=str(int(self.orders.price*31))
            self.orders.currency='TWD'
            
            
    
    
    


    