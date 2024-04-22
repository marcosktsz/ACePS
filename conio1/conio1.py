T = int(input())


for _ in range(T):
    tagli = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    utilizzi = [0 for _ in range(len(tagli))]
    cifra = int(input())

    while cifra:
        # print(cifra % tagli[len(tagli) - 1])
        if cifra % tagli[len(tagli) - 1] != cifra:
            utilizzi[len(tagli) - 1] = int(cifra / tagli[len(tagli) - 1])
            cifra = cifra % tagli[len(tagli) - 1]
        else:
            tagli.pop()

    print(sum(utilizzi))
    for utilizzo in utilizzi:
        print(utilizzo, end=" ")
    print()
