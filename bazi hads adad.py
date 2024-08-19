import random

def bazi_hads_adad():
    count = 0
    name = input("esmet chie?") + "e aziz"
    shoro = int(input("adad aval ro vared kon: "))
    paiyan = int(input("adad dovom ro vared kon: "))

    adad_random = random.randint(shoro, paiyan)
    hads = int(input("lotfan adad ro hads bezan: "))
    
    while True:
        if hads == adad_random:
            print("adad ro hads zadi kalak ;)")
            print(count, 'bar hads zadi', name)
            break
        elif hads > adad_random:
            print("kochiktaram", name)
            hads = int(input("lotfan dobare adad ro hads bezan: "))
            count += 1
        elif hads < adad_random:
            print("bozorgtaram", name)
            hads = int(input("lotfan dobare adad ro hads bezan: "))
            count += 1

bazi_hads_adad()

aya_mikhay = input("mikhay ye dast dige bezani? (are/noch): ")
while aya_mikhay.lower() == "are":
    bazi_hads_adad()
    aya_mikhay = input("mikhay ye dast dige bezani? (are/noch): ")



    