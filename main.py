def contorno (s1):
    tam = len(s1)
    if tam:
        print('+','|','-'*tam,'|','+')
        print('+','|',s1,'|','+')
        print('+','|','-'*tam,'|','+')

contorno(input("Seu texto de preferencia: "))