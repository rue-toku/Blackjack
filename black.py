import random

deck_list = []
mark_list = ["h", "s", "d", "c"]

for i in range(1, 14):
    for j in range(4):
        if i >= 10:
            i = 10
        deck_list.append((mark_list[j], i))

l = len(deck_list)

# dealerの1枚目
d1 = random.randint(0, l-1)
card_d1 = deck_list[d1]
#print("1枚目：", card_d1)

# dealerの2枚目
d2 = random.randint(0, l-1)
card_d2 = deck_list[d2]
#print("2枚目：", card_d2)

# 2枚の合計
d_total = card_d1[1] + card_d2[1]
#print("合計：", d_total)

# 合計が17以上になるまでカードを引く
while True:
    if d_total >= 17:
        break
    else:
        d3 = random.randint(0, l-1)
        card_d3 = deck_list[d3]
        d_total = d_total + card_d3[1]
    #print("追加：", card_d3)

# print(d_total)


# playerの1枚目
p1 = random.randint(0, l-1)
card_p1 = deck_list[p1]

# playerの2枚目
p2 = random.randint(0, l-1)
card_p2 = deck_list[p2]

# playerの2枚合計
p_total = card_p1[1] + card_p2[1]

print("1枚目のカード：", card_p1)
print("2枚目のカード：", card_p2)
print("合計は", p_total, "です")

# playerが選ぶ
while True:
    if p_total > 21:
        print("burst(合計が21を超えました)")
        break
    elif p_total == 21:
        print("blackJack")
    else:
        select = input("追加でカードを引きますか？(Y/N)")
        if select == "Y":
            p3 = random.randint(0, l-1)
            card_p3 = deck_list[p3]
            print("追加のカード：", card_p3)
            p_total = p_total + card_p3[1]
            print("合計は", p_total, "です")

        elif select == "N":
            print("合計は", p_total, "です")
            break
        else:
            print("！！！！WARNING！！！！：引く場合は[Y]、引かない場合は[N]を選んでください！！！")

p_sub = 21 - p_total
d_sub = 21 - d_total

print("ディーラーの合計は", d_total, "です")
if p_total > 21:
    print("You are lose...")
elif p_total <= 21 and d_total > 21:
    print("You are win !!!")
elif p_sub < d_sub:
    print("You are win !!!")
elif p_sub == d_sub:
    print("draw")
else:
    print("You are lose...")
