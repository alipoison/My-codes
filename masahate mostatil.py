#   masahat mostatil
tool = input('tool mostatil ra vared konid: ')
arz = input('arz mostatil ra vared konid: ')
tool = int(tool)
arz = int(arz)
masahat = (tool * arz)
if tool == arz:
    print("in # hastesh azizam :)")
elif tool < arz:
        print('ja be ja vared kardi *-* ')
else:
    print(masahat)