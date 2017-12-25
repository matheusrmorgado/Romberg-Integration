import math

def trapz(a, b, T, i, fx):
    
    h = (b-a)/(2**i)

    if (i == 0):
        x = (a+h)
        y = h*(eval(fx))

    if (i > 0):
        s = 0
        for j in range (1, 1+2**(i-1)):
            x = (a+(2*j-1)*h)
            s+= (eval(fx))
        y = 0.5*T + h*s
    
    return (y)

def romb(a, b, n, ε, ITMAX, fx):

    #Constrói um vetor utilizando o método de triângulos
    for i in range (0, n+1):
        if (i == 0):
            H = []
            H.append(trapz(a, b, H, i, fx))
        if (i > 0):
            H.append(trapz(a, b, H[i-1], i, fx))

    #Constrói um novo vetor por meio do método de Romberg e aproveitando o vetor já construído 
    IT = 0
    while (IT < ITMAX):
        for i in range (0, n+1):

            if (i == 0):
                T = []
                T.append([H[IT]])
                
            if (i > 0):
                T.append([H[IT+i]])
                for k in range (1, i+1):
                    T[i].append(T[i][k-1]+((T[i][k-1]-T[i-1][k-1])/(-1+4**k)))
        IT+= 1

        "Delete os # caso queira ver os triângulos a cada iteração"
        #print("\n")
        #for i in range(0, n+1):
            #print(T[i])
        "Delete os # caso queira ver os triângulos a cada iteração"
        
        if (abs(T[n][n] - T[n][n-1]) <= ε*abs(T[n][n])):
            break

        H.append(trapz(a, b, H[n+IT-1], n+IT, fx))

    return (T[n][n], IT)

def main():

    print ("\n- Método de Romberg para integração de funções\n")

    fx = input(("Digite a f(x) que deseja-se integrar: "))

    print ("\nSeja [a,b] o intervalo de integração de f(x)")
    a = eval(input("     Digite o valor de a: "))
    b = eval(input("     Digite o valor de b: "))

    n = 4
    ε = 1e-06
    ITMAX = 20

    integral, iteracoes = romb(a, b, n, ε, ITMAX, fx)

    print ("\n ∫ " + fx + " dx = %f no intervalo [%.3f,%.3f] \n Integral calculada após %d iterações"%(integral, a, b, iteracoes))

if __name__ == "__main__":
    main()
