# Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.

import math
n = int(input("Enter the number"))
print(round(math.pi,n))
