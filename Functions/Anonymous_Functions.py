# add = lambda x, y: x + y
# print(add(2, 3))

# process = lambda x,y : 5*(x**2) - y
# print(process(2, 3))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#1. lambda function calculate the kinetic energy ke = (m*v**2)/2
kinetic_energy = lambda m, v: (m * v**2) / 2
print("Kinetic Energy:", kinetic_energy(10, 5), "Joules")

#2. lambda function to calculate the energy = Mc^2
rest_energy = lambda m, c: m * c**2
print("Rest Energy:", rest_energy(10, 3e8), "Joules")

#3. lambda function to calculate the gravitational force = (G * m1 * m2) / r**2
gravitational_force = lambda G, m1, m2, r: (G * m1 * m2) / r**2
print("Gravitational Force:", gravitational_force(6.67e-11, 5.97e24, 7.35e22, 3.84e8), "Newtons")

#4.  lambda function creating abbreviations of months from the list of months
month_abbreviations = list(map(lambda month: month[:3], months))
print("Month Abbreviations:", month_abbreviations)