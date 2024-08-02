import sys

script_name = sys.argv[0]  # unused
first_arg = "none"
second_arg = "none"
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    first_arg = int(sys.argv[1])
if len(sys.argv) > 1 and sys.argv[2].isdigit():
    second_arg = int(sys.argv[2])

# script that returns if the first value is higher, lower or equal to the second value

output = "none"
if first_arg < second_arg:
    output = "first number is lower than second number"
elif first_arg > second_arg:
    output = "first number is higher than second number"
elif first_arg == second_arg:
    output = "first number is equal to second number"

print(output)
