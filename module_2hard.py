def password(n):
    result = ''
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result


for n in range(3, 21):
    window_2 = password(n)
    print(f'{n} - {window_2}')
