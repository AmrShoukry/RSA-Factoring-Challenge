import sys
import math

if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as file_pointer:
        for line in file_pointer:
            n = int(line.strip())
            for y in range(2, n):
                mod = n % y
                if mod == 0:
                    x = int(n / y)
                    break

            print(f"{n}={x}*{y}")
