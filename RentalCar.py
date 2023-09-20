"""******************************************************************
Author: Marissa Langham
Assignment Number: LAB 6: Adress Book
File Name: RentalCar.py
Date: 09/20/2023
This program will allow the user to enter a car that they would like
to rent (Toyota) and it will let the user knwo if the car is available.
******************************************************************"""

import sys

Dict = {"ACURA", "ALFAROMEO", "ASTON MARTIN", "AUDI", "BENTLEY", 
        "BMW", "BUICK", "CADILLAC", "CHEVROLET", "CHRYSLER", "DODGE", 
        "FERRARI", "FIAT", "FORD", "GENESIS", "GMC", "HONDA", "HYUNDAI", 
        "INFINITI", "JAGUAR", "JEEP", "KIA", "LAMBORGHINI", "LAND ROVER", 
        "LEXUS", "LINCOLN", "MASERATI", "MAZDA", "MCLAREN", "MERCEDESBENZ", 
        "MINI", "MITSUBISHI", "NISSAN", "PORSCHE", "RAM", "ROLLS ROYCE", 
        "SUBARU", "TESLA", "TOYOTA", "VOLKSWAGEN", "VOLVO"}

print("Welcome to the Rental Car Program!")
print("Please enter a car brand that you would like to rent.")
userCar = input("Car Brand: ")
userCar = userCar.upper()              

if userCar in Dict:
    userCar = userCar.lower()
    userCar = userCar.capitalize()
    
    print(f"\n We have a {userCar} available for you!")
else:
    print(f"Sorry, we do not have a(n) {userCar} available for you.")
    print("Please try again.")
    sys.exit()