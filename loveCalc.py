def calculate_love_score(name1, name2):
    name1 = name1.upper()
    name2 = name2.upper()
    sum_count1 = 0
    sum_count2 = 0
    for letter in "TRUE":
        if letter in name1:
            count1= name1.count(letter)
            print(f"{letter} occurs {count1} times")
            sum_count1 += count1
        if letter in name2:
            count2 = name2.count(letter)
            print(f"{letter} occurs {count2} times")
            sum_count2 += count2

    count_name1 = sum_count1 + sum_count2
    print(count_name1)

    sum_count3 = 0
    sum_count4 = 0
    for letter in "LOVE":
        if letter in name1:
            count3 = name1.count(letter)
            print(f"{letter} occurs {count3} times")
            sum_count3 += count3
        if letter in name2:
            count4 = name2.count(letter)
            print(f"{letter} occurs {count4} times")
            sum_count4 += count4

    count_name2 = sum_count3 + sum_count4
    print(count_name2)

    print(str(count_name1)+str(count_name2))


calculate_love_score("Febin", "Sasha")