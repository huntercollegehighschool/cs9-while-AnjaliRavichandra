'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
times = int(input("Times to print: "))
times_counter = 0
while times_counter < times:
  print("Hunter")
  times_counter = times_counter + 1
