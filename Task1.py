import sys

script_name = sys.argv[0]  # unused
first_arg = "none"
second_arg = "none"
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    first_arg = int(sys.argv[1])
if len(sys.argv) > 1 and sys.argv[2].isdigit():
    second_arg = int(sys.argv[2])

#  script that returns the higher of 2 numbers

output = 0
if first_arg < second_arg:
    output = second_arg
if second_arg < first_arg:
    output = first_arg

print(output)

