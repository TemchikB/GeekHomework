number= int(input())
phone = open('phone.txt', encoding="utf-8")
new_phone = open('new_phone.txt','w')
new=enumerate(phone)

print(number)
for n, line in enumerate(phone):
    if n+1 == number:
        new_phone.write(line)
   
    
    
 