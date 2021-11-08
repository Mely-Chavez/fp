c = True

while c:
    cal = int(input('Ingresa tu calificacion obtenida: '))

    if cal >= 7:
        print('Estas aprobado, felicidades!!')
        # El ciclo termina
        c = False
    else:
     print('Estas reprobado, suerte el proximo año :(')
     c= False