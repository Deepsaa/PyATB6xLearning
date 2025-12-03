# Skip numbers divisible by 3, from (0,100)
# Using for loop
for i in range(0,101):
    if i%3==0:
        continue
    print(i,end=' ')

print()
#Using While loop

n=0
while n<101:
    if n%3==0:
        n+=1
        continue
    print(n,end=' ')
    n+=1