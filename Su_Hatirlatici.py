# coding :utf-8
import tkinter as tk #Arayüz araçları kütüphanesi
import ctypes # C kütüphanesi

zamanlayici = ctypes.CDLL("./zamanlayici.dll") #Paylaşımlı dosyayı py dosyasına ekleme

while True:
   
    root = tk.Tk()  # Boş pencere oluşturma
    root.configure(bg="#626262")
    root.title("Su Hatırlatıcısı") #Pencere isimlendirme 
    root.geometry("500x300")  #Pencere boyutu

   
    
    metin = tk.Label(root,text = "Su İçme Zamanı !" ,fg="white" , font = ("Helvetica" , 30) , bg="#626262") # Hatırlatma mesajı
    metin.pack(pady=50) #pady dikey boşluk bırakma # metin.pack ekranda konumlandırma

    kapatma_butonu = tk.Button(
        root,
        text = "Tamam!" ,
        bg="#515151" ,
        fg = "White" ,
        command=root.destroy,
        padx=10,
        pady=5,
    )
    kapatma_butonu.pack(pady=5)
    
    def hatirlat(): #Burada hatırlatma bildiriminin atılacağı zaman aralığını beliriyoruz
        print("Su İçme Zamanı !")
        # root.after(10800000,hatirlat) #milisaniye cinsinden 3 saate tekabul ediyor (Artık C beklediği için iptal edildi)

    hatirlat()

    root.mainloop() #Pencereyi açık tutup kullanıcının etkileşime geçmesini bekleyen yapı(Döngü)

    # Arayüz çarpıdan kapatıldığı an Python alt satıra geçer ve C'deki bekleme başlar
    zamanlayici.bekle_3_saat()