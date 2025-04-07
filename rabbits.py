def recurrence(n, k):
    #eingabe = input(nk)
   # liste = list(map(int, eingabe.split()))
    seq = [1, 1]
    for i in range(2, n):
        next_val = seq[i - 1] + seq[i - 2] * k
        seq.append(next_val)
    return seq

result = recurrence(30, 3)
print(result)