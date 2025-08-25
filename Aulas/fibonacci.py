while True:
    seq = []
    n = int(input("Quantos números vc deseja:"))
    if n == 0:
        print ("Não há número a mostrar")
        break
    elif n == 1:
        print ("1")
    elif n == 2:
        print ("1,1")
    else:
        seq.append(1)
        seq.append(1)
        for i in range(2, n):
            seq.append(seq[i-1] + seq[1-2])
            print (seq)
