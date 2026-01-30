print("program started")

try:
    a=10
    b=a/0
    print(b)
except Exception as e:
    print(e)
else:
    print("there is no exception ")

finally:
    print("always excutable")

print("program ended")




try:
    a=10/0
    print(k)
    a=21-"kugjh"

except ZeroDivisionError as e:
    print(e)

except NameError as e:
    print(e)