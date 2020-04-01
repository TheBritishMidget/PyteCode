from instructions import check

stack = []
local_variables = []

instruction = ""


while True:
    instruction = input("Enter Instruction: ")
    check(instruction)
    print(f"stack = {stack}")
    print(f"localvariables = {local_variables}")


