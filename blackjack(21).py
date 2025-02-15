import random



def point_varagh(varagh):
    if varagh[0] in ['JACK', 'BB', 'SHAH']:
        return 10
    elif varagh[0] == 'ACE':
        return 11
    else:
        return int(varagh[0])

def adjust_ace(points, cards):
    for card in cards:
        if card[0] == 'ACE' and points > 21:
            points -= 10
    return points

def play_blackjack():
    while True:
        khal_ha = ['del', 'khesht', 'KHAJ', 'peak']
        tak_varagh = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'BB', 'SHAH']
        dast = [(varagh, khal) for khal in khal_ha for varagh in tak_varagh]
        random.shuffle(dast)

        varagh_bazikon = [dast.pop(), dast.pop()]
        varagh_dealer = [dast.pop(), dast.pop()]

        point_bazikon = sum(point_varagh(varagh) for varagh in varagh_bazikon)
        point_bazikon = adjust_ace(point_bazikon, varagh_bazikon)

        if point_bazikon == 21 and len(varagh_bazikon) == 2:
            print("varagh haye shoma:", varagh_bazikon)
            print("majmoe point shoma:", point_bazikon)
            print("BLACKJACK kardi  (;  bordi")
            baz_dasti_dige = input("\nMikhay ye dast dige bezani? (bale / na): ").lower()
            if baz_dasti_dige != "bale":
                print("Bazi tamom shod GG")
                break
            else:
                continue

        while True:
            print("varagh haye shoma:", varagh_bazikon)
            print("majmoe point shoma:", point_bazikon)
            print("\n")

            if point_bazikon > 21:
                print("dealer barande shod!!! (shoma az 21 bishtar dashti)")
                break

            entekhab = input('lotfan entekhabet konid [bazam varagh mikhay? "bede biad", dige nemikhay? "basame"]: ').lower()
            if entekhab == "bede biad":
                varagh_bazikon.append(dast.pop())
                point_bazikon = sum(point_varagh(varagh) for varagh in varagh_bazikon)
                point_bazikon = adjust_ace(point_bazikon, varagh_bazikon)
            elif entekhab == "basame":
                break
            else:
                print("eshtebah vared kardi lotfan dobare emtehan kon")
                continue

        point_dealer = sum(point_varagh(varagh) for varagh in varagh_dealer)
        point_dealer = adjust_ace(point_dealer, varagh_dealer)

        while point_dealer < 17:
            varagh_dealer.append(dast.pop())
            point_dealer = sum(point_varagh(varagh) for varagh in varagh_dealer)
            point_dealer = adjust_ace(point_dealer, varagh_dealer)

        print("varagh haye dealer:", varagh_dealer)
        print("majmoe point haye dealer:", point_dealer)
        print("varagh haye shoma:", varagh_bazikon)
        print("majmoe point shoma:", point_bazikon)

        if point_bazikon > 21:
            print("dealer barande shod!!! (shoma az 21 bishtar dashti)")
        elif point_dealer > 21:
            print("shoma bordi GG (dealer az 21 bishtar dasht)")
        elif point_bazikon > point_dealer:
            print("shoma bordi GG (shoma point haye bishtari az dealer dari)")
        elif point_dealer > point_bazikon:
            print("dealer barande shod!!!")
        else:
            print("mosavi shod ye dast dige bezan be nazar man")

        baz_dasti_dige = input("\nMikhay ye dast dige bezani? (bale / na): ").lower()
        if baz_dasti_dige != "bale":
            print("Bazi tamom shod GG")
            break

play_blackjack()



