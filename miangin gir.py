tedad = 0
jam = 0
adad = int(input("adad ro vared konid: "))
while adad != -1:
    tedad = tedad + 1
    jam = adad + jam
    adad = int(input("adad badi ro vared konid: "))
    print("tedade adad ha: ",tedad)
    print("jame adad ha: ",jam)
    print("adad akhar: ",adad)
miangin_adad_ha = jam / tedad
print("miangin adad ha: ",miangin_adad_ha)