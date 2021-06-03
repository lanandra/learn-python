# salary.py

# input hours and rate
hours = int(input("Please enter working hours: "))
rate = int(input("Please enter rate per hour: "))

# function to count salary
# check if there is any overtime
def computepay(hours, rate):
    if hours <= 40:
        salary = hours * rate
    elif hours > 40:
        overtime = hours - 40
        salary = (hours * rate) + (overtime * rate/2)
    return salary

# print salary
salary = float(computepay(hours,rate))
print("Your salary: " + str(salary))
