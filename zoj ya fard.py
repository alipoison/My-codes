def adad_zoj_ya_fard():
    try:
        vorodi = int(input('adad mored nazareto vared kon: '))
    except ValueError:
        print("in ke adad nist *.*")
        return

    if not isinstance(vorodi, int):
        print("in ke adad nist")
    elif vorodi % 2 == 0:
        print("zoj")
    else:
        print("fard")
adad_zoj_ya_fard()
edame = input("baraye khoroj <<bye>> ro vared kon:")
while edame != "bye":
    adad_zoj_ya_fard()
    edame = input("baraye khoroj <<bye>> ro vared kon:")
else:
    print("bye bye :)")