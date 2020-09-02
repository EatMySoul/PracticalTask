CODE = ["""print('N = ',end = '')
N = int(input())
sum = 0
A = [0]*N
for i in range(N):
    print('A[',i + 1,'] = ',sep='', end='')
    A[i] = int(input())
    sum = sum + A[i]
print(sum)
time.sleep(2)""", """print('N = ',end ='')
N = int(input())
A = [0]*N
for i in range(N):
    print('A[',i + 1,'] = ',sep='', end='')
    A[i] = int(input())
    if i == 0 :
        num = 1
        max = A[i]
    elif A[i] > max:
        num = i + 1
        max = A[i]
print(max)
print('num is',num)
time.sleep(2)""", """print('N = ',end = '')
N = int(input())
X = [0]*N
for i in range(N):
    print('X[',i + 1,'] = ',sep='', end='')
    X[i] = int(input())
print('X[N]',X)
for i in range(N):
    for j in range(1,N):
        if X[j] > X[j-1]:
            temp = X[j]
            X[j] = X[j-1]
            X[j-1] = temp
print('Y[N]',X)
time.sleep(2)""", """print('N = ',end='')
N = int(input())
sum = 0
X = [0]*N
for i in range(N):
    print('X[',i + 1,'] = ',sep='',end='')
    X[i] = int(input())
    if X[i] % 5 != 0:
        sum = sum + X[i]**2
print('sum is',sum)
time.sleep(2)""", """
print('N = ',end='')
N = int(input())
C = [0]*N
for i in range(N):
    print('C[',i + 1,'] = ',sep='',end='')
    C[i] = int(input())
for i in range(N):
    a = i
    b = 5 + i
    z = (a + b + C[i])
    print('z = ',z,sep='')
time.sleep(2)""", """print('N = ',end ='')
N = int(input())
A = [0]*N
for i in range(N):
    print('A[',i + 1,'] = ',sep='', end='')
    A[i] = int(input())
print(A)
for i in range(N):
    if i == 0:
        min_num = 0
        max_num = 0
        max = A[i]
        min = A[i]
    elif A[i] > max:
        max_num = i
        max = A[i]
    elif A[i] < min:
        min_num = i
        min = A[i]
temp = A[min_num]
A[min_num] = A[max_num]
A[max_num] = temp
print(A)
time.sleep(2)""", """
print('N = ',end ='')
N = int(input())
A = [0]*N
count = 0
for i in range(N):
    print('A[',i + 1,'] = ',sep='', end='')
    A[i] = int(input())
print('X = ',end ='')
X = int(input())
for i in range(N):
    if A[i] < X:
        count = count + 1
print('count is',count)
time.sleep(2)""", """print('N = ',end ='')
N = int(input())
A = [0]*N
B = [0]*N
sum = 0
for i in range(N):
    print('A[',i + 1,'] = ',sep='', end='')
    A[i] = int(input())
for i in range(N):
    for j in range(i+1):
        sum = sum + A[j]
    B[i] = sum/(i + 1)
    sum = 0
print(A)
print(B)
time.sleep(2)""", """print('N = ',end ='')
N = int(input())
A = []
B = [0]*(2*N)
C = []
for i in range(2*N):
    print('B[',i + 1,'] = ',sep='', end='')
    B[i] = int(input())
    if i % 2 == 0:
        A.append(B[i])
    else:
        C.append(B[i])
print('B ',B)
print('A ',A)
print('C ',C)
time.sleep(2)""",  """print('N = ',end='')
N = int(input())
Y = [0]*N
for i in range(N):
    print('Y[',i + 1,'] = ', sep='', end='')
    Y[i] = float(input())
print(Y)
for i in range(N):
    if Y[i] < 1 and Y[i] > 0:
        print(i + 1)
time.sleep(2)"""]

11

print('N = ',end='')
N = int(input())
Y = [0]*N
for i in range(N):
    print('Y[',i + 1,'] = ', sep='', end='')
    Y[i] = int(input())
print(Y)
for i in range(N):
    if Y[i] < 1 and Y[i] > 0:
        print(i)
time.sleep(2)

    





    
    
