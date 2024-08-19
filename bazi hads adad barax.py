import random
adad_aval = int(input("adad aval ro vared kon: "))
adad_dovom = int(input("adad dovom ro vared kon: "))
adad_dorost = input("adadeto bego: ")
hads = random.randint(adad_aval, adad_dovom)
hads = random.randint(adad_aval,adad_dovom)
javab = input(adad_dorost)
print("k=kochiktar, b=bozorgtar, d=dorost")
while javab != hads :
    print(hads)
    print(adad_dorost)
    k_b_d = input("k , b ya d: ")
    if 'd' == k_b_d :
        print(hads , "adad shomast ;)")
        break
    elif 'b' == k_b_d :
        adad_aval = hads
        hads = random.randint(adad_aval, adad_dovom)
    elif 'k' == k_b_d :
        adad_dovom = hads
        hads = random.randint(adad_aval, adad_dovom)
    else:
        print("lotfan k, b ya d vared kon :)")
