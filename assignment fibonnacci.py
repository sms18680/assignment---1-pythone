# fibonnacci

n = int(input('enter the n terms:'))
n1, n2 = 0, 1
count = 0
if n <= 0:
    print('enter a positive int')
elif n == 1:
    print('fibonnacci sequence upto', n,':')
    print(n1)
else:
    print('fibonaacci sequence:')
    while(count<n):
        print(n1)
        r = n1 + n2
        n1 = n2
        n2 = r
        count += 1