# #requirement arguments
# def devision(first, second):
#     return first/second

# # devision(10, 2)
# # print(devision(10, 2))

# print(devision(first=10, second=2))


# #keyword arguments
# def division(second = 2, first = 10):
#     return first/second

# # print(division(10, 2))
# print(division(first=10, second=2))

# #default arguments
# def division(first, second = 2):
#     return first/second

# print(division(10, 2))
# print(division(50))

# #variable number of arguments
# def addition(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# answer = addition(10, 20, 30, 40, 50)
# print(answer)

# def fancy_name_plate(name):
#     print("****************************")
#     print("****************************")
#     print("**" + name.center(24, "-") + "**")
#     print("****************************")
#     print("****************************")

# fancy_name_plate(name = "Ujjwal Tomar")
# fancy_name_plate(name = "Python Programming")

# def fancy_name_plate_defargs(name, length, symbol = "*"):
#     print(symbol * length)
#     print(symbol * 2 + (length - 4) * "-" + symbol * 2)
#     print(symbol * 2  + name.center(length-4, " ") + symbol * 2)
#     print(symbol * 2 + (length - 4) * "-" + symbol * 2)
#     print(symbol * length)

# #fancy_name_plate_defargs(name = "Ujjwal Tomar", length = 30, symbol = "*")
# fancy_name_plate_defargs("Ujjwal Tomar", 30, "#")

def fancy_name_plate(name):
    for name in name:
        print("****************************")
        print("****************************")
        print("**" + name.center(24, "-") + "**")
        print("****************************")
        print("****************************")


fancy_name_plate(["Ujjwal Tomar","Python Programming"])