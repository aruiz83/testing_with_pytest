
def calculate_shipping_cost(weight, destination):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")
    if not isinstance(destination, str):
        raise TypeError("Destination must be a string")
    if not destination:
        raise ValueError("Destination cannot be empty")
    if destination.lower() == "usa":
        return 0
    if destination.lower() == "canada":
        return weight * 1.5
    if destination.lower() == "mexico":
        return weight * 2.0
    return weight * 5.0
