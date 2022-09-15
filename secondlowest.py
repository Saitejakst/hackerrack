if __name__ == '__main__':
    n = int(input())
    list_c = []
    for m in range(n):
        name = input()
        score = float(input())
        
        list_a = []
        list_a.append(name)
        list_a.append(score)
        list_c.append(list_a)

    score_list = []
    for i in range(len(list_c)):
        score_list.append(list_c[i][1])
    mini = min(score_list)

    list_x = []
    for x in score_list:
        if mini < x:
            list_x.append(x)
    secLow = min(list_x)
    
    output = []
    for i in list_c:
        if secLow == i[1]:
            output.append(i[0])
    
    result = sorted(output)
    for i in result:
        print(i)
