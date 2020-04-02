stack = []
local_variables = []

instruction = ""


def check(instrct):
    instrct = instrct.lower()
    if instrct == "iconst_m1":
        stack.insert(0, -1)
    if instrct == "iconst_0":
        stack.insert(0, 0)
    if instrct == "iconst_1":
        stack.insert(0, 1)
    if instrct == "iconst_2":
        stack.insert(0, 2)
    if instrct == "iconst_3":
        stack.insert(0, 3)
    if instrct == "iconst_4":
        stack.insert(0, 4)
    if instrct == "iconst_5":
        stack.insert(0, 5)
    if instrct == "pop":
        stack.pop(0)
    if instrct == "pop2":
        stack.pop(0)
        stack.pop(0)


while True:
    instruction = input("Enter Instruction: ")
    check(instruction)
    print(f"stack = {stack}")
    print(f"localvariables = {local_variables}")
