inicio = int(input('Ingrese el primer numero '))
end =  int(input('Ingrese el valor final '))

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
for num in range(inicio,end):
    if es_primo(num):
        print(num)    