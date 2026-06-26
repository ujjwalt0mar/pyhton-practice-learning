
rainfall = [68, 75, 80, 90, 100]
city = "New York"

def print_rainfall(value):
    day = 1
    for val in value:
        print("Day", day, ":", val, "mm")
        day += 1

def average_rainfall(value):
    import math
    return math.fsum(value) / len(value)

def change_city(new_city):
    global city
    city = new_city

print("Rainfall in", city)
print_rainfall(rainfall)
print("Average rainfall:", average_rainfall(rainfall), "mm")
print(city, "is old selected city.")
change_city("Los Angeles")
print(city, "is now the selected city.")