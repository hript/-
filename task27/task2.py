n = int(input())
sum_ = 0
min_razn = 10000

for i in range(n):
    first, second = map(int, input().split())
    sum_ += min(first, second)
    if abs(first - second) % 8 != 0:
        min_razn = min(min_razn, abs(first - second))

if sum_ % 8 != 2:
    print(sum_)
else:
    print(min_razn + sum_, min_razn, sum_)
    
    #https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6
