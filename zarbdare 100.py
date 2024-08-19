adad_ha = []
while True: 
    try: 
        x = input("Please enter a number (or type 'exit'): ")
        if x.lower() == 'exit': 
            break
        x = int(x) 
        adad_ha.append(x)
    except ValueError: 
        print("Oops!  That was no valid number.  Try again...")

for madad in adad_ha: # madad ya adad baraye in fargh nadare vartolo ke nist :)
    print(madad * 100)