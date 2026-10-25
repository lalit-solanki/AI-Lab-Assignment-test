a = 0
b = 0

A = int(input("Enter capacity of Jug A: "))
B = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

step = 0

while a != target and b != target:

    # Fill Jug A
    if a == 0:
        a = A
        step += 1
        print("Step", step, ": Fill Jug A =", a, b)

    # Pour Jug A into Jug B
    elif b < B:
        water = min(a, B - b)
        a = a - water
        b = b + water
        step += 1
        print("Step", step, ": Pour A into B =", a, b)

    # Empty Jug B
    elif b == B:
        b = 0
        step += 1
        print("Step", step, ": Empty Jug B =", a, b)

print("Target achieved!")
print("Jug A =", a)
print("Jug B =", b)
