answer = 36
count = 5

for i in range(1, count + 1):
    print("[%s/%s] 数値を入力してください" % (i, count), end=': ')
    val = int(input())

    if val == answer:
        print("正解！こたえは %s です！" % val)
        exit()
    elif val < answer:
        print("[%s/%s] ハズレ！こたえは %s より上の数字です\n" % (i, count, val))
    elif val > answer:
        print("[%s/%s] ハズレ！こたえは %s より下の数字です\n" % (i, count, val))

print("%s 回はずれました、ゲームはあなたの負けです\n正解は %s でした" % (count, answer))
