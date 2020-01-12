n=input('正の整数を入力してください:')
x=int(n)
for i in range(1,x+1):
    count = 0
    for m in range(1,i+1):
        if i%m==0:
            count += m
        else:
            pass
    print(i,'の約数の合計は',count,'です。')
