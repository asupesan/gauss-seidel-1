import numpy as np

def gs(n, v, a, b, e):
    it = 0
    x = [0 for i in range(n)]
    while 1 == 1:
        it+=1
        print("it",it)
        for i in range(n):
            for j in range(n):
                if i != j:
                    x[i]= -1*float(a[i][j])*float(v[j])
            x[i]+=float(b[i])
            x[i]/=float(a[i][i])
            v[i]=x[i]
            print(x)
        if float(v[i])/float(x[i]) < e and float(v[i])/float(x[i]) > 2-e and it != 1:
            break

n = int(input("Tamanho: "))
v = [0 for i in range(n)]
a = [[ 0 for i in range(n)] for j in range(n)]
b = [0 for i in range(n)]

for c in range(n):
    v[c] = int(input("Valor inicial: "))

for i in range(n):
    for j in range(n):
        
        a[i][j] = np.array(input("Valor de a: "))
    
    b[i] = input("Valor de b: ")
e = float(input("Erro aceitavel: "))
gs(n, v, a, b, e)