

for n in range(4):
    if n%2 == 0:
        print("even")
    elif n%2 == 1:
        print("odd")


for n in range(100):
    if n%2 == 1:
        print("weird")
    elif n%2 == 0 and 2<=n<=5:
        print("not weird")
    elif n%2 == 0 and 6<=n<=20:
        print("weird")
    elif n%2 == 0 and n>20:
        print("not weird")

### Answer to pythong if-else

#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 1:
        print("Weird")
    elif n%2 == 0 and 2<=n<=5:
        print("Not Weird")
    elif n%2 == 0 and 6<=n<=20:
        print("Weird")
    elif n%2 == 0 and n>20:
        print("Not Weird")