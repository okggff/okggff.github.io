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

def standard_to_vertex_form(standard):
    conf, A, B, C = get_coefficients(standard)
    h = -B/(2*A)
    k = A*h**2 + B*h + C
    vertex_form = f"{conf}(x-({h}))^2+({k})"
    return vertex_form

a = "2x^2+4x+1"
get_coefficients(a)
print(standard_to_vertex_form(a))

