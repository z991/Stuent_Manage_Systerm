subtotal,gratuityrate=eval(input("Enter the subtotal and a ruatuityrate:"))
gratuity=subtotal*gratuityrate*0.01
total=gratuity+subtotal

print(gratuity)
print(round(total,2))