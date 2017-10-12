finalaccount=eval(input("Enter finalaccount value: "))
interestrate=eval(input("Enter annual interestrate in percent:"));
monthrate=interestrate/12/100
years=eval(input("Enter number of years:"));
months=years*12
Initialdeposit=finalaccount/((1+monthrate)**months)
print(Initialdeposit)
