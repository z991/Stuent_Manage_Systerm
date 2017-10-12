amount=eval(input("Enter an amount,for example,11.56:"))

remainingAmount=int(amount*100)

number0f0neDollars=remainingAmount//100
remainingAmount=remainingAmount%100

number0fQuarters=remainingAmount//25
remainingAmount=remainingAmount%25

number0fDimes=remainingAmount//10
remainingAmount=remainingAmount%10

numberOfnickels=remainingAmount//5
remainingAmount=remainingAmount%5

numberOfPennies=remainingAmount

print("Your amount",amount,"consists of\n",
      "\t",number0f0neDollars,"dollars\n",
      "\t",number0fQuarters,"quarters\n",
      "\t",number0fDimes,"dimes\n",
      "\t",numberOfnickels,"nickels\n",
      "\t",numberOfPennies,"pennies")




