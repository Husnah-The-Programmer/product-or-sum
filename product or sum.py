def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product<=1000:
        return product
    else:
        return num1 + num2


num1=200
num2=300

print ("\n")
result = multiplication_or_sum(num1,num2)
print("result is",result)
    
    