import random
import time
correctCount=0
count=0
NUMBER_OF_QUESTIONS=5

startTime=time.time()

while count<NUMBER_OF_QUESTIONS:

    number1=random.randint(1,15)
    number2=random.randint(1,15)


    answer=eval(input("What is"+str(number1)+"+"+str(number2)+"?"))
    if number1+number2==answer:
        print("You are correct!")
        correctCount +=1
    else:
        print("Your answer is wrong.\n",number1,"+",
              number2,"is",number1+number2)
    count+=1
endTime=time.time()
testTime=int(endTime-startTime)
print("Correct count is",correctCount,"out of",
      NUMBER_OF_QUESTIONS,"\nTest time is",testTime,"seconds")

