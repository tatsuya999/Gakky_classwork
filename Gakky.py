n=input('正の整数を入力してください:')
x=int(n)

while x<=0:
    n=input('正の整数を入力してください:')
    x=int(n)

divisor=""
count = 0
for i in range(1,x+1):
    if x%i==0:
        divisor = divisor + " " + str(i)
        count += 1
    
    else:
        pass

print(x,'の約数は',divisor,'です。')
print('全部で', count,'個あります')