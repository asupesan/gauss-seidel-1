import numpy as np

def gs(n, v, a, b, e):
    vant = [0 for i in range(n)]
    it = 0
    x = [0 for i in range(n)]
    while 1 == 1:
        
        it+=1
        print("it",it)
        for i in range(n):
            vant[i]=v[i]
            h = 0
            for j in range(n):
                if i != j:
                    h = h -1*float(a[i][j])*float(v[j])
            v[i]=h
            v[i]+=float(b[i])
            v[i]/=float(a[i][i])

        print(v)
        if float(v[i]) - float(vant[i]) < e and float(v[i]) - float(vant[i]) > -1*e and it != 1:
            break

n = int(input("Tamanho: "))
v = [0 for i in range(n)]
a = [[ 0 for i in range(n)] for j in range(n)]
b = [0 for i in range(n)]

for c in range(n):
    v[c] = int(input(f"Valor inicial {c+1}: "))

for i in range(n):
    for j in range(n):
        
        a[i][j] = np.array(input(f"Valor de a{i+1}{j+1}: "))
    
    b[i] = input(f"Valor de b{i+1}: ")
e = float(input("Erro aceitavel: "))
gs(n, v, a, b, e)