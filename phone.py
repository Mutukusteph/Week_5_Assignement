class Phone:
    
    def __init__(self, brand, color, for_sale):
        # Attributes:
        self.brand = brand 
        self.color = color
        self.for_sale = for_sale

        # Method
    def call(self, number):
        print(f"{self.brand} is calling {number}")

    def display_info(self):
        sale_status = "available for sale" if self.for_sale else "not for sale"
        print(f"This is a {self.color} {self.brand} phone and it's {sale_status}")


# Step 2: Addition of Inheritance (Smartphone Class)

class Smartphone(Phone):
    def __init__(self, brand, color, for_sale, os, camera_megapixels):
        super().__init__(brand, color, for_sale)
        self.os = os
        self.camera_megapixels = camera_megapixels

    def browse_internet(self):
        print(f"{self.brand} is browsing the internet using {self.os}")

    def take_photo(self):
        print(f"{self.brand} is taking a photo with its {self.camera_megapixels} MP camera")

# Step 3: Demonstration:

# Creating instances and calling methods.
basic_phone = Phone("Sumsung A04E", "Black", False)
basic_phone.display_info()
basic_phone.call("0711397290")

smartphone =Smartphone("Sumsung", "Black", False, "Android", 64)
smartphone.display_info()
smartphone.call("0711397301")
smartphone.browse_internet()
smartphone.take_photo()
        

# Assignment 2

from abc import ABC, abstractmethod

# Step 1: Abstraction
class Device(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Step 2: Encapsulation and Inheritance
class Phone(Device):
    def __init__(self, brand, color, for_sale):
        self.__brand = brand   
        self.__color = color
        self.__for_sale = for_sale

    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__brand = brand

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

    def is_for_sale(self):
        return self.__for_sale
    
    def set_for_sale(self, status):
        self.__for_sale = status

    def call(self, number):
        print(f"{self.__brand} is calling {number}")

    def display_info(self):
        sale_status = "available for sale" if self.__for_sale else "not for sale"
        print(f"This is a {self.__color} {self.__brand} phone and it's {sale_status}")

# Step 3: Polymorphism
class Smartphone(Phone):
    def __init__(self, brand, color, for_sale, os, camera_megapixels):
        super().__init__(brand, color, for_sale)
        self.os = os
        self.camera_megapixels = camera_megapixels

    def browse_internet(self):
        print(f"{self.get_brand()} is browsing the internet using {self.os}")

    def take_photo(self):
        print(f"{self.get_brand()} is taking a photo with its {self.camera_megapixels} MP camera")

    def display_info(self):
        sale_status = "available for sale" if self.is_for_sale() else "not for sale"
        print(f"This is a {self.get_color()} {self.get_brand()} smartphone running {self.os} with a {self.camera_megapixels} MP camera. It's {sale_status}")

# Step 4: Demonstration
basic_phone = Phone("Samsung A04E", "Black", False)
smartphone = Smartphone("Samsung", "Black", True, "Android", 64)

# Encapsulation in action
print(basic_phone.get_brand())   # Getter
basic_phone.set_for_sale(True)   # Setter

# Polymorphism in action
devices = [basic_phone, smartphone]
for device in devices:
    device.display_info()

# Other method calls
basic_phone.call("0711397290")
smartphone.browse_internet()
smartphone.take_photo()