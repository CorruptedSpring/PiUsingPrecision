#A function that would calculate pi depending of the precision inputed by the user
def PiWithPrecision(PrecisionWanted):
    n = 0
    var = 2**(1/2)
    LastVar = 1
    while n != PrecisionWanted:
        n += 1
        LastVar, var = var , (((var/2)**2)+((1-(LastVar-var))**2))**(1/2)
    print((var/2)*4*(2**n)) #pi using n precision