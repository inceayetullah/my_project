# coding :utf-8
import tkinter as tk #Arayüz araçları kütüphanesi
import time # Zamanlayıcı için

while True:
   
    root = tk.Tk()  # Boş pencere oluşturma
    root.configure(bg="#1a1a2e")
    root.title("Su Hatırlatıcısı")  
    root.geometry("500x300")  

   
    
    metin = tk.Label(root,text = "💧 Su İçme Zamanı!\n 3 saat sonra görüşürüz!" ,fg="#e0e0ff" , font = ("Helvetica" , 20, "bold") , bg="#1a1a2e")    
    metin.pack(pady=50)
    kapatma_butonu = tk.Button(
        root,
        text = "✅ Tamam!" ,
        bg="#6c63ff" ,
        fg = "white" ,
        activebackground="#8b83ff",
        activeforeground="white",
        font=("Helvetica", 12, "bold"),
        relief="flat",
        cursor="hand2",
        command=root.destroy,
        padx=20,
        pady=8,
    )
    kapatma_butonu.pack(pady=15)
    
    def hatirlat():
        print("Su İçme Zamanı !")
      
    hatirlat()

    root.mainloop() 

   
    time.sleep(10800) # 3 saat = 10800 saniye