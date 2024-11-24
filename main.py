import time
x = -3

if x <= 0:
    print(" x é menor ou igual a 0")
elif x < 2:
    print ("x é menor que 2")
else:
    print("more")   

cond = True
vezes =0
while cond and vezes !=2 :
   print("de novo")
   vezes += 1
   time.sleep(2)
   
print("acabou")