score=int(input("Score:"))
if(score<35):
    print("Poor Student")
elif(score>35 and score<70):
    print("Average Student")
elif(score>100):
    print("Invalid Score")
else:
    print("Good Student")
