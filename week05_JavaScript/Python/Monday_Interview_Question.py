# Create a class for a car
# Create 2 child classes for electric vehicles and internal combustion engine vehicles
# All cars have curb weight, top speed, either all wheel drive or rear wheel drive, horsepower
# All cars can accelerate, brake, and reverse. When accelerating print moving, when braking prin stopping, when reversing print backing up
# The electric vehicles should have battery capacity(kwH) and range
# Evs shoud have a function called charging the prints charging
# ICE vehicles should have miles per gallon(mpg) and function refill

# Dez solution:

# class Car:
#     def __init__(self, curbWeight: int, topSpeed: int, allWheelDrive: bool, horsepower: int, accelerate: bool, brake: bool, reverse: bool):
#         self.curbWeight = curbWeight
#         self.topSpeed = topSpeed
#         self.allWheelDrive = allWheelDrive
#         self.horsepower = horsepower
#         self.accelerate = accelerate
#         self.brake = brake 
#         self.reverse = reverse 
        
#         if allWheelDrive == True:
#             print('AWD')
#         else: 
#             print('FWD')
#         if accelerate == True:
#             print('Moving')
#         else:
#             pass
#         if reverse == True:
#             print("Backing Up")
#         else:
#             pass
#         if brake == True:
#             print("Stopping")
#         else:
#             pass 
        
        
# class ICE(Car):
#     def __init__(self, curbWeight: int, topSpeed: int, allWheelDrive: bool, horsepower: int, accelerate: bool, brake: bool, reverse: bool, mpg: int):
#         super().__init__(curbWeight, topSpeed, allWheelDrive, horsepower, accelerate, brake, reverse)
#         self.mpg = mpg
        
#     def refill(self):
#         print("Refilling")

# class EV(Car):
#     def __init__(self, curbWeight: int, topSpeed: int, allWheelDrive: bool, horsepower: int, accelerate: bool, brake: bool, reverse: bool, batteryCapacity: int, driveRange: int):
#         super().__init__(curbWeight, topSpeed, allWheelDrive, horsepower, accelerate, brake, reverse)
#         self.batteryCapacity = batteryCapacity
#         self.driveRange = driveRange
    
#     def charging(self):
#         print("Charging")
        
# tesla = EV(3000, 200, True, 250, True, False, True, 500, 300)

# print(tesla.batteryCapacity)