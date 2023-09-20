rows = int(input())
direction = input()

if direction == 'd':
    for i in range(rows):
        for j in range(i):
            print(end='*')
        print('*')
elif direction == 'u':
    for i in range(rows, 0, -1):
        for j in range(1, i, + 1):
            print(end='*' )
        print('*')