weight = input('WEIGHT>>>  ')
lk = input('L(lbs) or K(kg)>>>  ')
if lk.upper() == 'L':
    kg = int(weight) * 0.45
    print(f"YOU ARE {kg} kilos")
    if int(kg) > 80:
        print('LOL SO HEAVY')
    else:
        print('NOT SO HEAVY I SEE')
elif lk.upper() == 'K':
    kgf = int(weight) / 0.45
    print(f"YOU ARE {kgf} pounds")
    if int(kgf) > 190:
        print('HEAVY MAN OR WOMAN I DONT DISCRIMINATE')
    else:
        print('NICE NOT SO HEAVY')
else:
    print('JUST TYPE WHAT U ARE ASKED FOR MAN (SO ANNOYING)')
