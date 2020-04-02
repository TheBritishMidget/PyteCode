
# https://en.wikipedia.org/wiki/Java_bytecode_instruction_listings

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
    if instrct == "aload_0":
    	stack.insert(0, local_variables[0])
    if instrct == "aload_1":
    	stack.insert(0, local_variables[1])
    if instrct == "aload_2":
    	stack.insert(0, local_variables[2])
    if instrct == "aload_3":
    	stack.insert(0, local_variables[3])
    if instrct == "swap":
        stack[0], stack[1] = stack[1], stack[0]
    if instrct == "dup":
    	stack.insert(0, stack[0])
    if instrct == "dup_x1":
    	stack.insert(2, stack[0])
    if instrct == "dup_x2":
    	stack.insert(3, stack[0])
    if instrct == "dup2":
    	stack.insert(0, stack[1])
    	stack.insert(0, stack[1])
    if instrct == "dup2_x1":
    	stack.insert(3, stack[0])
    	stack.insert(4, stack[1])
    if instrct == "dup2_x2":
    	stack.insert(4, stack[0])
    	stack.insert(5, stack[1])	
    	    


while True:
    instruction = input("Enter Instruction: ")
    check(instruction)
    print(f"stack = {stack}")
    print(f"localvariables = {local_variables}")
