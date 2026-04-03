
def oddsum(n):
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    return sum

def evensum(n):
    sum=0
    for i in range(2,n+1,2):
        sum+=i
    return sum

n=int(input("Type Number:"))

odd_sum=oddsum(n)
even_sum=evensum(n)

print(f"Sum of {n} Odd Number",odd_sum)
print(f"Sum of {n} even Number",even_sum)

