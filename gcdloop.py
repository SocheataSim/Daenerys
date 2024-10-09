# n1=eval(input("Please enter first integer: "))
# n2=eval(input("Please enter second integer: "))
# k=2
# gcd = 1
# while k<=n1 and k<=n2:
#     if n1%k==0 and n2%k==0:
#         gcd=k
#     k+=1
# print("The greatest common divisor for ",n1," and ",n2," is ",gcd)
# year =0
# tuition = 10000
# while tuition<20000:
#     tuition = tuition*1.07
#     year+=1
# print("The tuition will be doubled in",year,"years")
# print("It will be $",tuition,"in",year,"years")
# number =0
# sum =0
# while number<20:
#     number+=1
#     sum+=number
#     if sum>=100:
#         break
# print("The sum is ",sum)
# sum=0
# number=0
# while number<20:
#     number+=1
#     sum+=number
#     if number ==10 and number == 11:
#         continue
# print("The sum is ",sum)
sum=0
number=0
while number<20:
    number+=1
    if number ==10 or number == 11:
        continue
    sum+=number
print("The sum is ",sum)