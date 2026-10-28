nota=int(input("introduce nota"))
match nota:
nota=int(input("Introduce nota: "))
match nota:
    case 0|1|2|3|4:
        print("Estás suspenso")
    case 5|6:
        print("Estás aprobado")
    case 7|8:
        print("Tienes un notable")
    case 9|10:
        print("Tienes un sobresaliente")
    case _:
        print("nota no valida")
        