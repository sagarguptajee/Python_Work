a = 10

def test():
    global a
    a=20
    print(f"inside: {a}")

print(a)
test()
print(a)