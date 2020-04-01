stack = []
local_variables = []

instruction = ""

def check(instruction):
    instrct = instruction.lower()
    if instrct == "iconst_m1":
        stack.append(-1)
    if instrct == "iconst_0":
        stack.append(0)
    if instrct == "iconst_1":
        stack.append(1)
    if instrct == "iconst_2":
        stack.append(2)
    if instrct == "iconst_3":
        stack.append(3)
    if instrct == "iconst_4":
        stack.append(4)
    if instrct == "iconst_5":
        stack.append(5)

while True:
    instruction = input("Enter Instruction: ")
    check(instruction)
    print(f"stack = {stack}")
    print(f"localvariables = {local_variables}")


