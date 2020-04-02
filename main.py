# https://en.wikipedia.org/wiki/Java_bytecode_instruction_listings
# http://homepages.inf.ed.ac.uk/kwxm/JVM/codeByNm.html

stack = []
local_variables = []

instruction = ""


def check(instrct):
    instrct = instrct.lower()
    instrct = instrct.split(" ")
    if instrct[0] == "iconst_m1":
        stack.insert(0, -1)
    elif instrct[0] == "iconst_0":
        stack.insert(0, 0)
    elif instrct[0] == "iconst_1":
        stack.insert(0, 1)
    elif instrct[0] == "iconst_2":
        stack.insert(0, 2)
    elif instrct[0] == "iconst_3":
        stack.insert(0, 3)
    elif instrct[0] == "iconst_4":
        stack.insert(0, 4)
    elif instrct[0] == "iconst_5":
        stack.insert(0, 5)
    elif instrct[0] == "pop":
        stack.pop(0)
    elif instrct[0] == "pop2":
        stack.pop(0)
        stack.pop(0)
    elif instrct[0] == "aload":
        stack.insert(0, local_variables[instrct[1]])
    elif instrct[0] == "aload_0":
        stack.insert(0, local_variables[0])
    elif instrct[0] == "aload_1":
        stack.insert(0, local_variables[1])
    elif instrct[0] == "aload_2":
        stack.insert(0, local_variables[2])
    elif instrct[0] == "aload_3":
        stack.insert(0, local_variables[3])
    elif instrct[0] == "swap":
        stack[0], stack[1] = stack[1], stack[0]
    elif instrct[0] == "dup":
        stack.insert(0, stack[0])
    elif instrct[0] == "dup_x1":
        stack.insert(2, stack[0])
    elif instrct[0] == "dup_x2":
        stack.insert(3, stack[0])
    elif instrct[0] == "dup2":
        stack.insert(0, stack[1])
        stack.insert(0, stack[1])
    elif instrct[0] == "dup2_x1":
        stack.insert(3, stack[0])
        stack.insert(4, stack[1])
    elif instrct[0] == "dup2_x2":
        stack.insert(4, stack[0])
        stack.insert(5, stack[1])
    elif instrct[0] == "istore":
        local_variables.insert(int(instrct[1]), stack[0])
    elif instrct[0] == "istore_0":
        local_variables.insert(0, stack[0])
    elif instrct[0] == "istore_1":
        local_variables.insert(1, stack[0])
    elif instrct[0] == "istore_2":
        local_variables.insert(2, stack[0])
    elif instrct[0] == "istore_3":
        local_variables.insert(3, stack[0])
    elif instrct[0] == "isub":
        result = stack[1] - stack[0]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    else:
        print("Unknown Instruction")




while True:
    instruction = input("Enter Instruction: ")
    check(instruction)
    print(f"stack = {stack}")
    print(f"localvariables = {local_variables}")
