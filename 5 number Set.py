##this program allows the user to set an upper and lower limit for a list of numbers. Then, it allows the user to input qualifying numbers. It then compiles them into a list and give some data on the set##

upperbound = input("Please enter the upper limit for your list: ")

lowerbound = input("Please enter the lower limit for your list: ")

#this portion checks to make sure the user's lower bound is not above his upper bound#

while int(lowerbound, 10) >= int(upperbound, 10):
  lowerbound = (input("Your lower limit may not be larger than your upper limit. Please try again: "))

num1 = int(input("Please enter five values between " + lowerbound + " and " + upperbound + ": "), 10)
while (num1 >= int(upperbound, 10)) or (num1 <= int(lowerbound, 10)):
    num1 = int(input("That number is not within your selected range. Try again: "), 10)

num2 = int(input(), 10)
while (num2 >= int(upperbound, 10)) or (num2 <= int(lowerbound, 10)):
    num2 = int(input("That number is not within your selected range. Try again: "), 10)

num3 = int(input(), 10)
while (num3 >= int(upperbound, 10)) or (num3 <= int(lowerbound, 10)):
    num3 = int(input("That number is not within your selected range. Try again: "), 10)

num4 = int(input(), 10)
while (num4 >= int(upperbound, 10)) or (num4 <= int(lowerbound, 10)):
    num4 = int(input("That number is not within your selected range. Try again: "), 10)

num5 = int(input(), 10)
while (num5 >= int(upperbound, 10)) or (num5 <= int(lowerbound, 10)):
    num5 = int(input("That number is not within your selected range. Try again: "), 10)

list = [num1, num2, num3, num4, num5]

largest = str(max(list))
smallest = str(min(list))
sum = (list[0] + list[1] + list[2] + list[3] + list[4])
mean = sum / 5
print("---------------------------------------------------------")
print(list)
print("Your smallest value was " + smallest)
print("Your largest value was " + largest)
print("Your mean is " + str(mean))