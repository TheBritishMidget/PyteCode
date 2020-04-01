from main import stack


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
