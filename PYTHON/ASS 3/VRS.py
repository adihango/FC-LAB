import requests

class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.is_available = True

    def __str__(self):
        return f"{self.brand} {self.model} (ID: {self.vehicle_id}, Rental Price: ₹{self.rental_price})"

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, fuel_type, seating_capacity):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.fuel_type = fuel_type
        self.seating_capacity = seating_capacity

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, engine_cc, max_speed):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.engine_cc = engine_cc
        self.max_speed = max_speed

class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, load_capacity):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.load_capacity = load_capacity

class Customer:
    def __init__(self, name, driver_license_number):
        self.name = name
        self.driver_license_number = driver_license_number
        self.rented_vehicles = []

    def __str__(self):
        return f"{self.name} (Driver's License: {self.driver_license_number})"

class RentalService:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def rent_vehicle(self, vehicle, customer):
        if vehicle.is_available:
            customer.rented_vehicles.append(vehicle)
            vehicle.is_available = False
            print(f"{customer.name} rented {vehicle}.")
        else:
            print(f"{vehicle} is not available.")

    def return_vehicle(self, vehicle, customer):
        if vehicle in customer.rented_vehicles:
            customer.rented_vehicles.remove(vehicle)
            vehicle.is_available = True
            print(f"{customer.name} returned {vehicle}.")
        else:
            print(f"{customer.name} does not have {vehicle} rented.")

    def view_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.vehicles:
            if vehicle.is_available:
                print(vehicle)

    def view_rental_history(self, customer):
        print(f"{customer.name}'s Rental History:")
        for vehicle in customer.rented_vehicles:
            print(vehicle)

# Fetch real-time vehicle data from an API (replace with your preferred API)
def fetch_vehicle_data():
    url = "https://api.example.com/vehicles"
    response = requests.get(url)
    vehicles_data = response.json()

    vehicles = []
    for vehicle_data in vehicles_data:
        vehicle_id = vehicle_data['id']
        brand = vehicle_data['brand']
        model = vehicle_data['model']
        rental_price = vehicle_data['rental_price']
        # Add specific attributes based on vehicle type (e.g., fuel_type, engine_cc)
        vehicles.append(Car(vehicle_id, brand, model, rental_price, "Petrol", 5))

    return vehicles

# Create a rental service and add vehicles
rental_service = RentalService()
rental_service.vehicles.extend(fetch_vehicle_data())

# Create customers
customer1 = Customer("Alice", "1234")
customer2 = Customer("Bob", "5678")

# Rent and return vehicles
rental_service.rent_vehicle(rental_service.vehicles[0], customer1)
rental_service.rent_vehicle(rental_service.vehicles[1], customer2)
rental_service.return_vehicle(rental_service.vehicles[0], customer1)

# View available vehicles and rental history
rental_service.view_available_vehicles()
rental_service.view_rental_history(customer1) 