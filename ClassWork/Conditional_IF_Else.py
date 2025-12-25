
marks=int (input("enter your marks:"))

if marks>=91 and marks<=100:
    print("Your gtrade is A") 
elif marks>=71 and marks<=90:
    print("Your gtrade is B")
elif marks>=51 and marks<=70:
    print("Your gtrade is C")
elif marks>=35 and marks<=50:
    print("Your gtrade is D")    
elif marks==0 and marks<=34:
    print("You Are Failed")
else:
    print("Please type Inavlid Marks")

