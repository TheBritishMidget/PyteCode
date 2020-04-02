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
    if instrct[0] == "pop":
        stack.pop(0)
    elif instrct[0] == "pop2":
        stack.pop(0)
        stack.pop(0)
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
    elif instrct[0] == "iadd":
        result = stack[0] + stack[1]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "isub":
        result = stack[1] - stack[0]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "imul":
        result = stack[0] * stack[1]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "idiv":
        result = stack[1] / stack[0]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "irem":
        result = stack[1] % stack[0]
        stack.pop(0)
        stack.pop(0)
        stack.insert(0, result)
    elif instrct[0] == "ineg":
        stack.insert(0, -stack[0])
        stack.pop(1)
    else:
        print("Unknown Instruction")


def const_instructions(instrct):
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


def local_load_instructions(instrct):
    instrct = instrct.lower()
    instrct = instrct.split(" ")
    if instrct[0] == "iload_0":
        stack.insert(0, local_variables[0])
    elif instrct[0] == "iload_1":
        stack.insert(0, local_variables[1])
    elif instrct[0] == "iload_2":
        stack.insert(0, local_variables[2])
    elif instrct[0] == "iload_3":
        stack.insert(0, local_variables[3])
    elif instrct[0] == "iload":
        try:
            stack.insert(0, local_variables[int(instrct[1])])
        except IndexError:
            print("Please provide an index")
    elif instrct[0] == "aload_0":
        stack.insert(0, local_variables[0])
    elif instrct[0] == "aload_1":
        stack.insert(0, local_variables[1])
    elif instrct[0] == "aload_2":
        stack.insert(0, local_variables[2])
    elif instrct[0] == "aload_3":
        stack.insert(0, local_variables[3])
    elif instrct[0] == "aload":
        try:
            stack.insert(0, local_variables[int(instrct[1])])
        except IndexError:
            print("Please provide an index")

def store_instructions(instrct):
    instrct = instrct.lower()
    instrct = instrct.split(" ")
    if instrct[0] == "istore_0":
        local_variables[0] = stack[0]
        stack.pop(0)
    elif instrct[0] == "istore_1":
        expand(local_variables, 1, stack[0])
        stack.pop(0)
    elif instrct[0] == "istore_2":
        expand(local_variables, 2, stack[0])
        stack.pop(0)
    elif instrct[0] == "istore_3":
        expand(local_variables, 3, stack[0])
        stack.pop(0)
    elif instrct[0] == "istore":
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
