n=int(input())

prev_line=[]

for i in range(1, n+1):
    if not prev_line:
        this_line = [0, 1, 0]
    else:
        for j in range (1, len(prev_line)):
            this_line[j] = prev_line[j-1] + prev_line[j] 
        this_line.append(0)
    print (this_line[1:-1])
    prev_line = this_line.copy()
