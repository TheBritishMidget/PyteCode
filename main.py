# https://en.wikipedia.org/wiki/Java_bytecode_instruction_listings

stack = []
local_variables = []

instruction = ""


def check(instrct):
    instrct = instrct.lower()
    if instrct == "iconst_m1":
        stack.insert(0, -1)
    elif instrct == "iconst_0":
        stack.insert(0, 0)
    elif instrct == "iconst_1":
        stack.insert(0, 1)
    elif instrct == "iconst_2":
        stack.insert(0, 2)
    elif instrct == "iconst_3":
        stack.insert(0, 3)
    elif instrct == "iconst_4":
        stack.insert(0, 4)
    elif instrct == "iconst_5":
        stack.insert(0, 5)
    elif instrct == "pop":
        stack.pop(0)
    elif instrct == "pop2":
        stack.pop(0)
        stack.pop(0)
    elif instrct == "aload_0":
        stack.insert(0, local_variables[0])
    elif instrct == "aload_1":
        stack.insert(0, local_variables[1])
    elif instrct == "aload_2":
        stack.insert(0, local_variables[2])
    elif instrct == "aload_3":
        stack.insert(0, local_variables[3])
    elif instrct == "swap":
        stack[0], stack[1] = stack[1], stack[0]
    elif instrct == "dup":
        stack.insert(0, stack[0])
    elif instrct == "dup_x1":
        stack.insert(2, stack[0])
    elif instrct == "dup_x2":
        stack.insert(3, stack[0])
    elif instrct == "dup2":
        stack.insert(0, stack[1])
        stack.insert(0, stack[1])
    elif instrct == "dup2_x1":
        stack.insert(3, stack[0])
        stack.insert(4, stack[1])
    elif instrct == "dup2_x2":
        stack.insert(4, stack[0])
        stack.insert(5, stack[1])


while True:
    instruction = input("Enter Instruction: ")
    check(instruction)
    print(f"stack = {stack}")
    print(f"localvariables = {local_variables}")
