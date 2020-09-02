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
time.sleep(2)""","""print('N = ',end='')
N = int(input())
Y = [0]*N
X = [0]*N
for i in range(N):
    print('Y[',i + 1,'] = ', sep='', end='')
    Y[i] = int(input())
    print('X[',i + 1,'] = ', sep='', end='')
    X[i] = int(input())
print(Y)
print(X)
R = int(input('R = '))
for i in range(N):
    if X[i]**2 + Y[i]**2 <= R**2:
        print('dot',i + 1)
time.sleep(2)""","""N = int(input('N = '))
A = [0]*N
for i in range(N):
    print('A[', i+1,'] = ', sep='', end='')
    A[i] = int(input())
print(A)
max = A[0]
min = A[0]
for i in range(N):
    if A[i] > max:
        max = A[i]
    if A[i] < min:
        min = A[i]
A[0] = max
A[N - 1] = min
print(A)
time.sleep(2)""","""N = int(input('N = '))
A = [0]*N
for i in range(N):
    print('A[', i+1,'] = ', sep='', end='')
    A[i] = int(input())
Cheker_deg = True
Cheker_bel = True
for i in range(N):
    if A[i] < 0:
        if Cheker_deg == True:
            max_deg = A[i]
            Cheker_deg = False
        if A[i] > max_deg:
            max_deg = A[i]
    if A[i] > 0:
        if Cheker_bel == True:
            min_bel = A[i]
            Cheker_bel = False
        if A[i] < min_bel:
            min_bel = A[i]
for i in range(N):
    for j in range(N - 1):
        if A[j] < A[j + 1]:
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp
print('a)',max_deg)
print('b)',min_bel)
print('c)',A[1])
time.sleep(2)""","""N = int(input('N = '))
A = [0]*N
for i in range(N):
    print('A[', i+1,'] = ',sep='',end='')
    A[i] = int(input())
a = 0
b = 0
c = 0
d = 0
for i in range(N - 1):
    if A[i] > 0 and A[i + 1] > 0:
        a += 1
    if (A[i] > 0 and A[i + 1] < 0) or (A[i] < 0 and A[i + 1] > 0):
        b += 1
    if (A[i] > 0 and A[i + 1] > 0 and abs(A[i]) > abs(A[i + 1])) or (A[i] < 0 and A[i + 1] < 0 and abs(A[i]) > abs(A[i + 1])):
        c += 1
for i in range(1,N - 1,2):
    if A[i] % 2 == 0 and A[i + 1] % 2 != 0:
        d += 1
print('a)',a)
print('b)',b)
print('c)',c)
print('d)',d)
time.sleep(2)""","""N = int(input('N = '))
A = [0]*N
for i in range(N):
    print('A[', i + 1, '] = ',sep='',end='')
    A[i] = int(input())
print(A)
for i in range(N):
    if A[i] >= 0:
        A[i] = A[i] / 2
    else:
        A[i] = i + 1
print(A)
time.sleep(2)""","""N = int(input('N = '))
A = [0]*N
for i in range(N):
    print('A[', i + 1, '] = ',sep='',end='')
    A[i] = int(input())
print(A)
sum = 0
count = 0
mult = 1
for i in range(N):
    if A[i] > 0:
        sum = sum + A[i]
        mult = A[i]*mult
        count = count + 1
sr_arefm = sum / count
sr_geom = mult / count
print(sr_arefm)
print(sr_geom)
time.sleep(2)""","""N = int(input('N = '))
A = [0]*N
B = []
for i in range(N):
    print('A[', i + 1, '] = ',sep='',end='')
    A[i] = int(input())
count = 0
print(A)
for i in range(N):
    if A[i] > 5:
        B.append(A[i])
        count = count + 1
print(B)
print(count)
time.sleep(2)""","""N = int(input('N = '))
X = [0]*N
Y = [0]*N
Z = [0]*(2*N)
for i in range(N):
    print('X[', i + 1, '] = ',sep='',end='')
    X[i] = int(input())
    print('Y[', i + 1, '] = ',sep='',end='')
    Y[i] = int(input())
print(X)
print(Y)
k = 0
for i in range(N):
    Z[k] = X[i]
    Z[k + 1] = Y[i]
    k = k + 2
print(Z)
time.sleep(2)""","""N = int(input('N = '))
X = [0]*N
for i in range(N):
    print('X[', i + 1, '] = ',sep='',end='')
    X[i] = int(input())
print(X)
i = 0
j = N - 1
while i < j:
    temp = X[i]
    X[i] = X[j]
    X[j] = temp
    i = i + 1
    j = j - i
print(X)
time.sleep(2)""","""a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
min = d
x = 0
while round(x,1) < 2:
    x = x + 0.2
    y = a*x**3 + b*x**2 + c*x + d
    if y < min:
        min = y
        save_x = x
    print(x)
print('y =',round(y,1))
print('x =',round(x,1))
time.sleep(2)""",""" N = int(input('N = '))
A = [0]*N
count = 0
for i in range(N):
    print('A[', i + 1, '] = ',sep='',end='')
    A[i] = int(input())
    if A[i] == 0:
        count = count + 1
for i in range(N):
    for j in range(N - 1):
        if A[j] == 0:
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp
for i in range(N - count):
    print(A[i])
time.sleep(2)""","""N = int(input('N = '))
A = [0]*(2*N)
B = [0]*(2*N)
C = [0]*(2*N)
for i in range(2*N):
    print('A[', i + 1, '] = ',sep='',end='')
    A[i] = int(input())
k = 0
print(A)
for i in range(0,2*N,2):
    B[i] = A[k]
    B[i + 1] = A[N + k]
    k = k + 1
print(B)
k = 0
for i in range(0,2*N,2):
    C[i] = A[2*N - 1 -k]
    C[i + 1] = A[k]
    k = k + 1
print(C)
time.sleep(2)""","""
N = int(input('N = '))
A = []
for i in range(3):
        A.append([0]*N)
B = []
for i in range(3):
    for j in range(N):
        print('A[', i + 1, '][',j+1,'] = ',sep='',end='')
        A[i][j] = int(input())
for i in range(3):
    for j in range(N):
        print(A[i][j],' ',end='')
    print()
for i in range(N - 1):
    cos = (A[0][i]**2 + A[1][i]**2 - A[2][i]**2) / 2*A[0][i]*A[1][i]
    if 0 > cos and cos < 1:
        B.append(1)
    else:
        B.append(0)
print(B)
time.sleep(2)""","""N = int(input('N = '))
time_in = 1
print('a)')
for i in range(N):
    time_in = time_in + i
    print('№',i + 1,' ',time_in,sep='')
print('b)',N)
time.sleep(2)""","""print('????????')
time.sleep(2)""","""N = int(input('N = '))
M = int(input('M = '))
A = [0]*N
for i in range(N):
    print('A[',i+1,'] = ',sep='',end='')
    A[i] = int(input())
sum = 0
multi = 1
i = 0
while multi < M and i < N:
    multi = multi*A[i]
    if multi < M:
        sum =  sum + A[i]
    i = i + 1
print(sum)
time.sleep(2)""","""M = int(input('M = '))
F = [1,1]
i = 2
while F[-1] <= M:
    F.append(F[i - 1] + F[i - 2])
    i = i + 1
print(F[-1])
time.sleep(2)""","""N = int(input('N = '))
A = [0]*N
for i in range(N):
    print('A[',i+1,'] = ',sep='',end='')
    A[i] = int(input())
print(A)
count = 0
i = 0
while A[i] > 0:
    count = count + 1
    i = i + 1
print(count)
time.sleep(2)""","""deposit = int(input('deposit = '))
rate = int(input('rate = '))
size = int(input('desired size = '))
years = 0
while deposit < size:
    deposit = deposit + deposit*(rate/100)
    years = years + 1
print('deposit is ',deposit)
print('time is',years,'years')
time.sleep(2)""","""N = int(input('N = '))
sum = 0
for i in range(1,N):
    for j in range(1,i - 1):
        if i % j == 0:
            sum = sum + j
    if i == sum:
        print(i)
    sum = 0
print('end')
time.sleep(2)"""]










