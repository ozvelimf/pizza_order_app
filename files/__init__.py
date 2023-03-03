import files.classroom.pizza_class as pc
import files.classroom.decarator_class as dc
import files.classroom.souce_class as sc
import files.model.app_model as app_model
     
def run():
    # Sipariş geçmişini ekrana çıktısnı veren fonksiyon
    app_model.show_order_history()

    # Menu fonsiyonu
    app_model.show_menu()

    # Pizza ve sos için sözlükler oluşturuldu
    pizza_order = dict()
    souce_order = dict()

    # get_order fonsiyonu ile müşteriden siparişi alındı
    pizza_input, souce_input = get_order()

    # Sözlükleri ve girdi bilgilerini ait oldukları sınıflarına gönderdik.
    selected_pizza = register_pizza(pizza_input)
    selected_souce = register_souce(souce_input)

    # sınıflara tanımlanan veriler show_order_info fonsiyonuna Decarator sınıfına gönderilmesi için parametre olarak girildi.
    description, cost  = show_order_info(selected_pizza, selected_souce)

    # Kullanıcıdan siparişi tamamlaması için kart bilgileri isteniyor.
    name, id, cardno, passs  = payment()

    # Şifreyi encrypt'leme için fonsiyona şifreyi yolladık ve encrypt'li şekilde geri aldık.
    password = app_model.encrypt_pass(passs)

    # Kullanıdan alınan ve encrypt'li şifrenin database'e kaydedilmek üzere modele gönderilmesi.
    app_model.save(name, id, cardno, password, description, cost)

            
def get_order():
    while True:
            try:
                pizza_input = input("Pizza tabanı seçiniz :")
                if int(pizza_input) > 0 and int(pizza_input) < 5:
                    break                
                else:
                    print("Geçersiz sipariş. Lütfen siparişinizi yeniden giriniz..")
                    continue
            except:
                print("Geçersiz sipariş. Lütfen siparişinizi yeniden giriniz..")

    while True:
        try:
            souce_input = input("Pizza sosu seçiniz :")
            if int(souce_input) > 10 and int(souce_input) < 17:
                break
            else:
                print("Geçersiz sipariş. Lütfen siparişinizi yeniden giriniz..")
                continue
        except:
            print("Geçersiz sipariş. Lütfen siparişinizi yeniden giriniz..")

    return pizza_input, souce_input
                
def register_pizza(pizza_input):

    if pizza_input == "1":
        selected = pc.Classic(pizza_input)

    elif pizza_input == "2":
        selected = pc.Margarita(pizza_input)

    elif pizza_input == "3":
        selected = pc.Turkish(pizza_input)

    else:
        selected = pc.Plain(pizza_input)

    return selected
    

def register_souce(souce_input):
    if souce_input == "11":
        selected = sc.Olive(souce_input)

    elif souce_input == "12":
        selected = sc.Mushroom(souce_input)

    elif souce_input == "13":
        selected = sc.GoatCheese(souce_input)

    elif souce_input == "14":
        selected = sc.Meat(souce_input)

    elif souce_input == "15":
        selected = sc.Onion(souce_input)
        
    else:
        selected = sc.Sweetcorn(souce_input)
    return selected

def show_order_info(selected_pizza, selected_souce):
    show = dc.Decorator(selected_pizza, selected_souce)
    print(f"Siparişiniz : {show.get_description()}")
    print(f"Sipariş Tutatı : {show.get_cost()} ₺'dir.")
    return show.get_description(), show.get_cost()

def payment():
    print("============================")
    print("ÖDEME EKRANINA HOŞ GELDİNİZ.")
    print("============================")
    # İSİM
    while True:
            try:
                name = input("isminizi giriniz :")
                if not len(name) == 0:
                    break
                else:
                    print("Lütfen bilginizi yeniden giriniz..")
                    continue
            except:
                print("Lütfen bilginizi yeniden giriniz..")
    # TC NO
    while True:
            try:
                id = input("TC Kimlik numarası giriniz :")
                if len(id) == 11:
                    break
                else:
                    print("Lütfen bilginizi yeniden giriniz..")
                    continue
            except:
                print("Lütfen bilginizi yeniden giriniz..")
    # Kart Numarası        
    while True:
            try:
                cardno = input("Kredi kartı numarası giriniz :")
                if not len(cardno) == 0:
                    break
                else:
                    print("Lütfen bilginizi yeniden giriniz..")
                    continue
            except:
                print("Lütfen bilginizi yeniden giriniz..")
    
    # Şifre
    while True:
            try:
                password = input("Kart şifresini giriniz :")
                if not len(password) == 0:
                    break
                else:
                    print("Lütfen bilginizi yeniden giriniz..")
                    continue
            except:
                print("Lütfen bilginizi yeniden giriniz..")
    
    return name, id, cardno, password