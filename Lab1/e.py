arr = list(map(int, input().split()))
n = arr[0]
a = arr[1]

cnt = 0
i = 2

if a % 2 == 0:
    if n < 500:
        while i < n:
            if n % i == 0:
                cnt += 1
            i += 1
        if cnt == 0:
            print("Good job!")
        else:
            print("Try next time!")

    else:
        print("Try next time!")    
else:
     print("Try next time!")    