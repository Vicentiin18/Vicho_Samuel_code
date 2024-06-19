import random
import time
i = 0
a = 0
b = 0
t = 0
balance = 1000
while i == 0 :
    while a == 0:
        print(f"Tu dinero es {balance}")
        time.sleep(1)
        print("¿Cuanto quieres apostar?")
        bet = int(input("$"))
        if balance >= bet and bet > 0:
            balance -= bet
            a = 1
        elif balance < bet:
            print("El Monto que ingresaste es mayor al dinero que tienes")
            time.sleep(1)
        elif bet < 0:
            print("No puedes apostar numeros negativos")
            time.sleep(1)
    time.sleep
    a = 0


    cartas=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    Dcartas=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    rand1 = random.randint(0,12)
    rand2 = random.randint(0,12)
    carta1 = cartas[rand1]
    carta2 = cartas[rand2]
    total = carta1 + carta2
    print("Mezclando mazo")
    time.sleep(2)
    print(f"Obtuviste un: {carta1}")
    time.sleep(1)
    print(f"Y tu segunda carta es: {carta2}")
    time.sleep(1)
    
    if not carta1 == 1 and not carta2 == 11:
        total= carta1+carta2
        print(f"Tu total es {total}")
    if carta1==11:
        total1=1 + carta2
        total2= 11 + carta2
        print(f"Obtuviste un As tu total puede ser {total1} o {total2}")
    all_cards=[]
    time.sleep(1)
    rand_Dealer1=random.randint(0,13)
    CartaDealer1=Dcartas[rand_Dealer1]
    print(f"El dealer obtuvo un {CartaDealer1}")
    time.sleep(1)

    while b==0:
        print("¿Que deseas hacer?\n1.Otra Carta\n2.Plantarte")  
        otra_carta=int(input())
        if otra_carta==1:
            randOtracarta=random.randint(0,12)
            LaotraCarta=cartas[randOtracarta]
            print(f"Obtuviste un {LaotraCarta}")
            time.sleep(1)
            if LaotraCarta==11:
                print("Obtiviste un As, ¿Que valor le quieres dar? (1 o 11)")
                valor_as=int(input())
                if valor_as==1:
                    LaotraCarta=1
                else:
                    LaotraCarta==11
            all_cards.append(LaotraCarta)

            time.sleep(1)
        
        if otra_carta==2:
            b=1
    b=0

    if carta1==11:
        print("Obtiviste un As, ¿Que valor le quieres dar? (1 o 11)")
        valor_as=int(input())
        if valor_as==1:
            carta1=1
        else:
            carta1==11
    if carta2==11:
        print("Obtiviste un As, ¿Que valor le quieres dar? (1 o 11)")
        valor_as=int(input())
        if valor_as==1:
            carta2=1

        else:
            carta2==11
    
    all_cards.append(carta1)
    all_cards.append(carta2)
    time.sleep(1)
    totalcartas=sum(all_cards)
    time.sleep(1)
    print(f"Estas son tus cartas {all_cards}")
    time.sleep(1)
    print(F"Tu total oficial es {totalcartas}")
    time.sleep(2)
    print("Ahora,Le toca al Dealer")
    time.sleep(1)

    print(f"La primera carta del dealer es {CartaDealer1}")
    rand_Dealer2=random.randint(0,13)
    CartaDealer2=cartas[rand_Dealer2]
    time.sleep(1)
    print(f"El dealer obtuvo {CartaDealer2}   Dealer{CartaDealer1+CartaDealer2}")
    all_cardsDealer=[]
    all_cardsDealer.append(CartaDealer1)
    all_cardsDealer.append(CartaDealer2)
    totalDealer=CartaDealer1+CartaDealer2
    time.sleep(1)
    
    while totalDealer <= 16:
        randOtracartaDealer=random.randint(0,12)
        otra_cartaDealer=cartas[randOtracartaDealer]
        all_cardsDealer.append(otra_cartaDealer)
        totalDealer+=otra_cartaDealer
        print(f"El dealer pide y obtiene un {otra_cartaDealer}")
        time.sleep(1)
    totalcartasDealer=sum(all_cardsDealer)
    time.sleep(1)
    print(f"Resultado Jugador:{totalcartas}\nResultado Dealer:{totalcartasDealer}\n")
    time.sleep(2)

    if (totalcartas>21 and totalcartasDealer>21) or (totalcartas==totalcartasDealer and not totalcartas>21 and totalcartasDealer >21):
        Win=bet
        balance+=Win
        print("Empate, Nadie Gano")
    elif totalcartas<=totalcartasDealer<=21:
        print("Perdiste")
    elif totalcartasDealer<totalcartas<=21:
        Win=bet*2
        balance+=Win
        print(f"Has ganado {Win}")
    elif totalcartas<=21<totalcartasDealer:
        Win=bet*2
        balance+=Win
        print(f"Ganaste {Win}")
    else:
        print("Perdiste :(")
