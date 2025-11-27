import sys
if len(sys.argv) > 1:
    numbers = list(map(int, sys.argv[1:]))
    print("User provided list:")
else:
    numbers = [1, 2, 3, 4, 5, 6]
    print("No input given - using default list:")

even = sum(1 for n in numbers if n % 2 == 0)
odd = sum(1 for n in numbers if n % 2 != 0)

print("Count of Even Numbers:", even)
print("Count of Odd Numbers:", odd)
