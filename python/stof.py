import cmath
import math

def get_coefficients(stform):
    stform = stform.strip()
    print(stform)
    if stform[0] == "x":
        stform = "1" + stform[0:]

    a = stform.split("x")

    for i in range(len(a)):
        if "^2" in a[i]:
            a[i] = a[i].replace("^2", "")

    conf = int(a[0])

    for i in range(len(a)):
        a[i] = int(a[i])/conf
        print(a[i])

    A = a[0]
    B = a[1]
    C = a[2]

    return conf, A, B, C

def standard_to_factored_form(stform):
    conf, A, B, C = get_coefficients(stform)

    try:
        root1 = -((-B+math.sqrt(B**2-4*A*C))/(2*A))
        root2 = -((-B-math.sqrt(B**2-4*A*C))/(2*A))
    except ValueError:
        root1 = -((-B+cmath.sqrt(B**2-4*A*C))/(2*A))
        root2 = -((-B-cmath.sqrt(B**2-4*A*C))/(2*A))




    answer = f"roots: {root1}, {root2}"
    factored_form = f"{conf if conf != 1 else ''}(x+{root1})(x+{root2})"

    return factored_form

print("Welcome to the standard to factored form converter!")
standard_form = input("Please enter the standard form equation: ")
print(f"The factored form is: {standard_to_factored_form(standard_form)}")