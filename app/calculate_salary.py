import warnings


def calculate_salary(wages, hours):
    if len(wages) != len(hours):
        raise ValueError("Wages and hours lists must have the same length")
    if not all(isinstance(wage, (int, float)) for wage in wages):
        raise TypeError("Wages list must contain numbers")
    if not all(isinstance(hour, (int, float)) for hour in hours):
        raise TypeError("Hours list must contain numbers")
    if not all(hour >= 0 for hour in hours):
        raise ValueError("Hours must be non-negative")
    if not all(wage >= 0 for wage in wages):
        raise ValueError("Wages must be non-negative")
    total_salary = sum([wages[i]*hours[i] for i in range(len(wages))])
    if total_salary == 0:
        warnings.warn("Total salary is zero or negative")
    return total_salary
