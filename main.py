# https://en.wikipedia.org/wiki/Java_bytecode_instruction_listings
# http://homepages.inf.ed.ac.uk/kwxm/JVM/codeByNm.html

import re

stack = []
local_variables = []


def expand(a_list, index, value, empty=None):
    l = len(a_list)
    if index >= l:
        a_list.extend([empty] * (index + 1 - l))
    a_list[index] = value


def other_instructions(instrct):
    instrct = instrct.lower()
    instrct = instrct.split(" ")
    if instrct[0] == "pop":  # Pop top of stack.
        stack.pop(0)
    elif instrct[0] == "pop2":  # Pop top 2 of stack.
        stack.pop(0)
        stack.pop(0)
    elif instrct[0] == "swap":  # Swap top 2 of stack with each other.
        stack[0], stack[1] = stack[1], stack[0]
    elif instrct[0] == "dup":  # Duplicates the top of stack and places in second spot in stack (2nd place).
        stack.insert(0, stack[0])
    elif instrct[0] == "dup_x1":  # Duplicates the top of stack and places below 2nd place in stack (3rd place).
        stack.insert(2, stack[0])
    elif instrct[0] == "dup_x2":  # Duplicates the top of stack and places below 3rd place in stack (4rd place).
        stack.insert(3, stack[0])
    elif instrct[0] == "dup2":  # Duplicates top 2 values in stack and put in 3rd and 4th spots in stack.
        stack.insert(0, stack[1])
        stack.insert(0, stack[1])
    elif instrct[0] == "dup2_x1":  # Duplicates top 2 values in stack and put in 4th and 5th spots in stack.
        stack.insert(3, stack[0])
        stack.insert(4, stack[1])
    elif instrct[0] == "dup2_x2":  # Duplicates top 2 values in stack and put in 5th and 6th spots in stack.
        stack.insert(4, stack[0])
        stack.insert(5, stack[1])
    elif instrct[0] == "iadd":  # Integer at pos 1 + Integer at pos 2 (top 2 values). Removes the 2 values and puts the answer on top of stack.
        result = stack[0] + stack[1]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "isub":  # Integer at pos 1 - Integer at pos 2 (top 2 values). Removes the 2 values and puts the answer on top of stack.
        result = stack[1] - stack[0]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "imul":  # Integer at pos 1 * Integer at pos 2 (top 2 values). Removes the 2 values and puts the answer on top of stack.
        result = stack[0] * stack[1]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "idiv":  # Integer at pos 1 / Integer at pos 2 (top 2 values). Removes the 2 values and puts the answer on top of stack.
        result = stack[1] / stack[0]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "irem":  # Integer at pos 1 / Integer at pos 2 (top 2 values) and gives the remainder. Removes the 2 values and puts the answer on top of stack.
        result = stack[1] % stack[0]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "ineg":  # Makes the Integer at top of stack Negative.
        stack.insert(0, -stack[0])
        stack.pop(1)
    else:
        print("Unknown Instruction")


def const_instructions(instrct):
    instrct = instrct.lower()
    instrct = instrct.split(" ")
    if instrct[0] == "iconst_m1":  # Push integer -1 to stack.
        stack.insert(0, -1)
    elif instrct[0] == "iconst_0":  # Push integer 0 to stack.
        stack.insert(0, 0)
    elif instrct[0] == "iconst_1":  # Push integer 1 to stack.
        stack.insert(0, 1)
    elif instrct[0] == "iconst_2":  # Push integer 2 to stack.
        stack.insert(0, 2)
    elif instrct[0] == "iconst_3":  # Push integer 3 to stack.
        stack.insert(0, 3)
    elif instrct[0] == "iconst_4":  # Push integer 4 to stack.
        stack.insert(0, 4)
    elif instrct[0] == "iconst_5":  # Push integer 5 to stack.
        stack.insert(0, 5)


def local_load_instructions(instrct):
    instrct = instrct.lower()
    instrct = instrct.split(" ")
    if instrct[0] == "iload_0":  # Load integer from local variable 0.
        stack.insert(0, local_variables[0])
    elif instrct[0] == "iload_1":  # Load integer from local variable 1.
        stack.insert(0, local_variables[1])
    elif instrct[0] == "iload_2":  # Load integer from local variable 2.
        stack.insert(0, local_variables[2])
    elif instrct[0] == "iload_3":  # Load integer from local variable 3.
        stack.insert(0, local_variables[3])
    elif instrct[0] == "iload":  # Load integer from local variable instrct[1].
        try:
            stack.insert(0, local_variables[int(instrct[1])])
        except IndexError:
            print("Please provide an index")
    elif instrct[0] == "aload_0":  # Load object from local variable 0.
        stack.insert(0, local_variables[0])
    elif instrct[0] == "aload_1":  # Load object from local variable 1.
        stack.insert(0, local_variables[1])
    elif instrct[0] == "aload_2":  # Load object from local variable 2.
        stack.insert(0, local_variables[2])
    elif instrct[0] == "aload_3":  # Load object from local variable 3.
        stack.insert(0, local_variables[3])
    elif instrct[0] == "aload":  # Load object from local variable instrct[1].
        try:
            stack.insert(0, local_variables[int(instrct[1])])
        except IndexError:
            print("Please provide an index")


def store_instructions(instrct):
    instrct = instrct.lower()
    instrct = instrct.split(" ")
    if instrct[0] == "istore_0":  # Store integer in local variable 0.
        local_variables[0] = stack[0]
        stack.pop(0)
    elif instrct[0] == "istore_1":  # Store integer in local variable 1.
        expand(local_variables, 1, stack[0])
        stack.pop(0)
    elif instrct[0] == "istore_2":  # Store integer in local variable 2.
        expand(local_variables, 2, stack[0])
        stack.pop(0)
    elif instrct[0] == "istore_3":  # Store integer in local variable 3.
        expand(local_variables, 3, stack[0])
        stack.pop(0)
    elif instrct[0] == "istore":  # Store integer in local variable instrct[1].
        try:
            expand(local_variables, int(instrct[1]), stack[0])
        except IndexError:
            print("Please provide an index")


def check(instrct):
    instrct_split = instrct.split(" ")
    if re.compile("[abcdfils]const").match(instrct_split[0]):
        const_instructions(instrct)
    elif re.compile("[abcdfils]load").match(instrct_split[0]) and not re.compile("[abcdfils]aload").match(
            instrct_split[0]):
        local_load_instructions(instrct)
    elif re.compile("[abcdfils]store").match(instrct_split[0]):
        store_instructions(instrct)
    else:
        other_instructions(instrct)


while True:
    instruction = input("Enter Instruction: ")
    check(instruction)
    print(f"stack = {stack}")
    print(f"localvariables = {local_variables}")
