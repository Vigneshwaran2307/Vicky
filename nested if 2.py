Tamil=int(input("Tamil:"))
English=int(input("English:"))
Maths=int(input("Maths:"))
Science=int(input("Science:"))
Social=int(input("Social:"))
Total=(Tamil+English+Maths+Science+Social)/5
if(Total<35):
    print("Additional Class Required")
else:
    print("You are good to go")
