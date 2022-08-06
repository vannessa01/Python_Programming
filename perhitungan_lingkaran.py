def rumus_lingkaran(r, metode):
    '''
    r adalah integer
    r adalah jari-jari lingkaran
    dalam module perhitungan_lingkaran yang berisi fungsi rumus_lingkaran terdapat 3 metode
    metode pertama menghitung diameter lingkaran dengan mengalikan jari-jari dengan 2
    metode kedua menghitung luas lingkaran dengan mengalikan phi(3.14) dengan jari-jari dengan jari-jari
    metode ketiga menghitung keliling lingkaran dengan mengalikan phi dengan 2 kali jari-jari
    fungsi ini dibuat untuk mempermudah dalam menghitung rumus lingkaran
    
    '''
    try:
        if metode == 'diameter':
            hasil = 2*r
            return 'diameternya adalah', hasil
        elif metode == 'luas':
            hasil = 3.14*r*r
            return 'luasnya adalah', hasil
        elif metode == 'keliling':
            hasil = 3.14*2*r
            return 'kelilingnya adalah', hasil
        else:
            raise TypeError
    except TypeError:
            return("Invalid, rumus must be ('luas','keliling','diameter')")