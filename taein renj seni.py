#   taein renj seni mikad ba input  tahvil migiri
#   khordsal 0 ta kochiktar az 6
#   kodak 6 ta kochiktar az 10
#   nojavan 10 ta kochiktar az 14
#   javan 14  ta kochiktar az 24
#   miansal 40 be bala
#   bozorgtar mosavi yadet nare
sen = input('please give me your age *-* :')
sen = int(sen)
if sen <= 6:
    print('khordsal')
elif sen <= 10:
    print('kodak')
elif sen <= 14:
    print('nojavan')
elif sen == 18:
    print('you can do some stuff from now ;)')
elif sen == 21:
        print('happy drinking ;)')

elif sen <= 24:
    print('javan')
else:
    print('miansal')