print("Bankamıza Hoşgeldiniz\n")

şifre=int(input("Şifrenizi giriniz...\n"))

if(şifre==1234):
    print("Şifre Doğru. Hesabınız Açılıyor...\n")
    para=1000
    print("Hesabınıza Hoşgeldiniz Murat Kağan YILMAZ :)\n\n")
    while True:
        print("1. Hesaptaki Para\n\n2. Para Yatırma\n\n3. Para Çekme\n\n4.Çıkış\n")
        hesap=int(input("İşlem Seçiniz...\n"))
    

        if(hesap==4):
                print("İyi  Günler :)\n")
                break
            
    
        elif(hesap==2):
            yatırma=float(input("Hesabınıza kaç TL para yatırmak istiyorsunuz...\n"))
            para+=yatırma
            print("İşleminiz gerçekleşti\nHesaptaki tutar: {} TL\n".format(para))
            

        elif(hesap==3):
            çekme=float(input("Hesabınızdan kaç TL para çekmek istiyorsunuz...\n"))
            if(çekme<=para):
                para-=çekme
                print("İşleminiz gerçekleşti.\nHesaptaki tutar: {} TL\n".format(para))
                
            
            else:
                print("Hesabınızda yeterince para yok.\n")
                
        elif(hesap==1):
            print("Hesaptaki tutar: {} TL\n".format(para))
        
        else:
            print("Lütfen sadece size sunulan seçenekleri kullanın.\n")
elif(şifre!=1234):
    print("Şifreyi yanlış girdiniz! Tekrar deneyiniz...\n")
    
    şifre=int(input("Şifrenizi giriniz...\n"))    

    if(şifre==1234):
        print("Şifre Doğru. Hesabınız Açılıyor...\n")
        para=1000
        print("Hesabınıza Hoşgeldiniz Murat Kağan YILMAZ :)\n\n")
        while True:
            print("1. Hesaptaki Para\n\n2. Para Yatırma\n\n3. Para Çekme\n\n4.Çıkış\n")
            hesap=int(input("İşlem Seçiniz...\n"))
    

            if(hesap==4):
                    print("İyi  Günler :)\n")
                    break
            
    
            elif(hesap==2):
                yatırma=float(input("Hesabınıza kaç TL para yatırmak istiyorsunuz...\n"))
                para+=yatırma
                print("İşleminiz gerçekleşti\nHesaptaki tutar: {} TL\n".format(para))
            

            elif(hesap==3):
                çekme=float(input("Hesabınızdan kaç TL para çekmek istiyorsunuz...\n"))
                if(çekme<=para):
                    para-=çekme
                    print("İşleminiz gerçekleşti.\nHesaptaki tutar: {} TL\n".format(para))
                
            
                else:
                    print("Hesabınızda yeterince para yok.\n")
                
            elif(hesap==1):
                print("Hesaptaki tutar: {} TL\n".format(para))
        
            else:
                print("Lütfen sadece size sunulan seçenekleri kullanın.\n")
    
    elif(şifre!=1234):
        print("Şifreyi yanlış girdiniz! Tekrar deneyiniz...\n")

        şifre=int(input("Şifrenizi giriniz...\n"))

        if(şifre==1234):
                print("Şifre Doğru. Hesabınız Açılıyor...\n")
                para=1000
                print("Hesabınıza Hoşgeldiniz Murat Kağan YILMAZ :)\n\n")
                while True:
                    print("1. Hesaptaki Para\n\n2. Para Yatırma\n\n3. Para Çekme\n\n4.Çıkış\n")
                    hesap=int(input("İşlem Seçiniz...\n"))
    

                    if(hesap==4):
                        print("İyi  Günler :)\n")
                        break
            
    
                    elif(hesap==2):
                        yatırma=float(input("Hesabınıza kaç TL para yatırmak istiyorsunuz...\n"))
                        para+=yatırma
                        print("İşleminiz gerçekleşti\nHesaptaki tutar: {} TL\n".format(para))
            

                    elif(hesap==3):
                        çekme=float(input("Hesabınızdan kaç TL para çekmek istiyorsunuz...\n"))
                        if(çekme<=para):
                            para-=çekme
                            print("İşleminiz gerçekleşti.\nHesaptaki tutar: {} TL\n".format(para))
                
            
                        else:
                            print("Hesabınızda yeterince para yok.\n")
                
                    elif(hesap==1):
                        print("Hesaptaki tutar: {} TL\n".format(para))
        
                    else:
                        print("Lütfen sadece size sunulan seçenekleri kullanın.\n")
            
        elif(şifre!=1234):
            print("Şifreyi yanlış girdiniz. Hesabınız bloke oldu.\n")
