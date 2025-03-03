# Base class Vehicle
class Vehicle:
    def __init__(self, vehicle_type, capacity):
        self.vehicle_type = vehicle_type  # Type of the vehicle (Bus, Car, etc.)
        self.capacity = capacity  # Maximum capacity of passengers
    
    def get_vehicle_info(self):
        return f"Vehicle Type: {self.vehicle_type}, Capacity: {self.capacity} passengers"

# Child class Bus inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self, vehicle_type, capacity, fare_per_passenger):
        super().__init__(vehicle_type, capacity)  # Call the constructor of the parent class
        self.fare_per_passenger = fare_per_passenger  # Fare per passenger

    def calculate_total_fare(self, passengers):
        if passengers > self.capacity:
            return "Error: Number of passengers exceeds capacity!"
        return passengers * self.fare_per_passenger

# Example usage:
bus = Bus("City Bus", 40, 2.5)  # Bus with 40 seats and 2.5 fare per passenger
print(bus.get_vehicle_info())  # Prints vehicle type and capacity

# Calculate the total fare for 30 passengers
total_fare = bus.calculate_total_fare(30)
print(f"Total fare for 30 passengers: ${total_fare}")
