K = list(input())
if len(K) <= 2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    N = len(K)
    gap = int(K[0]) - int(K[1])
    for k in range(1, N - 1):
        if int(K[k]) - int(K[k + 1]) != gap:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
    else:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")