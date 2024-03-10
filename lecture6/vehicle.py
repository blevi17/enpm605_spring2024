class Vehicle:
    ''' 
    A class to represent a vehicle
    '''

    # methods
    def __init__(self, color, weight):
        # attributes
        self.color = color
        self.weight = weight
        
    
    def drive_forward(self):
        '''
        Drive the vehicle forwards.
        '''
        print(f"The {self.color} vehicle is driving.")
    
    
    def steer(self, angle):
        '''
        Steer the vehicle.
        '''
        print(f"The {self.color} vehicle is steering.")
    
    
    def honk(self):
        """
        Honk the vehicle's horn.
        """
        print(f"The {self.color} vehicle is honking its horn,")
        
        
if __name__ == "__main__":
    vehicle_blue = Vehicle("blue", 2000)
    vehicle_red = Vehicle("red", 1500)
    vehicle_blue.drive_forward()
    vehicle_red.drive_forward()
    print(vehicle_blue.weight)
    print(vehicle_red.weight)
    