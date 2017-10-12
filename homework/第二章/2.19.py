investmentamount=eval(input("Enter investmentamount: "))
rate=eval(input("Enter annual rate in percent:"));
monthrate=rate/12/100
years=eval(input("Enter number of years:"));
months=years*12
accumulated=investmentamount*((1+monthrate)**months)
print(round(accumulated,2))