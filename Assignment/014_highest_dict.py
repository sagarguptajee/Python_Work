# 14.Write a Python program to find the highest 3 values in a dictionary.

dc={'a':10,'b':23,'c':12,'d':15,'e':18,'f':19}

sort_dc=sorted(dc.values(),reverse=True)

last_three=sort_dc[:3]
print(last_three)