f = open('JudgeSystem/a_example.in', 'r')
R, C, L, H = [int(x) for x in f.readline().strip().split()]
pizza = []
for i in range(R):
    pizza.append(f.readline().strip())
ans = []
for i in range(R):
    ans.append([])
    for j in range(C):
        if i == 0 and j == 0:
            tomato, mushroom = 0, 0
        elif i == 0:
            tomato, mushroom = ans[i][j - 1]
        elif j == 0:
            tomato, mushroom = ans[i - 1][j]
        else:
            tomato = ans[i - 1][j][0] + ans[i][j - 1][0] - ans[i - 1][j - 1][0]
            mushroom = ans[i - 1][j][1] + ans[i][j - 1][1] - ans[i - 1][j - 1][1]
        
        x = pizza[i][j]
        if x == 'T':
            tomato += 1
        elif x == 'M':
            mushroom += 1

        ans[i].append([tomato, mushroom])
for r in ans:
    print(r)