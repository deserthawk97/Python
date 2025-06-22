def calculate_love_score(name1,name2):
    word1 = "true"
    word2 = "love"
    per1 = 0
    per2 = 0
    wordlength = len(name1) + len(name2)
    #print(wordlength)
    name1_list=[]
    name = ""
    for i in name1:
        name1_list.append(i)

    for i in name2:
        name1_list.append(i)
    #print(name1_list)
    for i in range (wordlength):
        name ="".join(name1_list)
    #print(name)

    for i in name:
        if i in word1:
            per1 = per1 +1
    #print(per1)

    for i in name:
        if i in word2:
            per2 = per2 +1
    #print(per2)

    print(f"The love score is {per1}{per2}")



name1 = input("Enter name 1: \n")
name2 = input("Enter name 2: \n")

calculate_love_score(name1,name2)
