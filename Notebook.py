import tkinter as tk

def new_books_ekran():
    window_new_books = tk.Toplevel()
    window_new_books.geometry("1920x1080")
    window_new_books.title("Yeni Not Defteri Oluştur")
    window_new_books.configure(bg="white")

    new_books_name = tk.Label(window_new_books, text="Yeni Not Defteri Adı:")
    new_books_name.place(x=705, y=247)

    new_books_name_input = tk.Entry(window_new_books, bg="pink")
    new_books_name_input.place(x=700, y=270)

    new_books_name_button = tk.Button(window_new_books, text="Kaydet", command=lambda: new_books_name_save(new_books_name_input), bg="light green")
    new_books_name_button.place(x=738, y=302)

    info = tk.Label(window_new_books, text="Kaydet'e basttığınızda değişiklikleriniz başarıyla kaydedilir. Gönül rahatlığıyla bu sekmeyi kapatabilirsiniz.", fg="black")
    info.place(x=468, y=340)
    # kullanıcı notlarının içerikleri
    new_books_text = tk.Entry(window_new_books, width=150, bg="yellow", fg="black")
    new_books_text.place(x=310, y=400)
    new_books_text_button = tk.Button(window_new_books, text="Kaydet",  bg="light green", width=7, command=lambda: new_books_text_save(new_books_text) )
    new_books_text_button.place(x=1215, y=398)



    powerby = tk.Label(window_new_books, text="Power By: Eren Dönmez", font=("Times 11 bold"), bg="orange")
    powerby.place(x=5, y=0)
    powerby = tk.Label(window_new_books, text="Altınbaş Unıversty 2024", bg="red")
    powerby.place(x=5, y=25)

def new_books_name_save(entry):
    girilen_not_defter_adi = entry.get()
    notebooks_list_name.append(girilen_not_defter_adi)
    print("Not Defteri Adı Kaydedildi:", girilen_not_defter_adi)

def new_books_text_save(entry):
    new_books_text = entry.get()
    notebooks_list_text.append(new_books_text)
    print("Not Defteri Adı Kaydedildi:", new_books_text)



def my_books_ekran():
    window_my_books = tk.Toplevel()
    window_my_books.geometry("1920x1080")
    window_my_books.title("Not Defterlerim")
    window_my_books.configure(bg="white")
    #
    info_my_books = tk.Label(window_my_books, text="Kayıtlı Not Defterleri:", fg="red", bg="white", font=(15))
    info_my_books.place(x=700, y=12)

    info_my_books = tk.Label(window_my_books, text="________________________________________________________________________", fg="red", bg="white", width=100)
    info_my_books.place(x=420, y=30)
    #
    kayitli_not_defterleri = tk.Button(window_my_books, text=(notebooks_list_name), width=50, height=15, bg="light green", command=kayitli_not_defterleri_text_içerik)
    kayitli_not_defterleri.place(x=10, y=100)


def kayitli_not_defterleri_text_içerik():
    window_kayitli_not_defterleri_text_içerik = tk.Toplevel()
    window_kayitli_not_defterleri_text_içerik.geometry("1920x1080")
    window_kayitli_not_defterleri_text_içerik.title("Yeni Not Defteri Oluştur")
    window_kayitli_not_defterleri_text_içerik.configure(bg="white")
    #
    kayitli_not_defterleri_text_içerik_kullanıcı_okuma = tk.Label(window_kayitli_not_defterleri_text_içerik, text=(notebooks_list_text))
    kayitli_not_defterleri_text_içerik_kullanıcı_okuma.pack()

def new_books_hover(event):
    event.widget.config(bg="SystemButtonFace", fg="blue")

def new_books_normal(event):
    event.widget.config(bg="light green", fg="black")

def my_books_hover(event):
    event.widget.config(bg="SystemButtonFace", fg="blue")

def my_books_normal(event):
    event.widget.config(bg="red", fg="black")

window = tk.Tk()
window.geometry("1920x1080")
window.title("Note Book & Kişisel Not Defteri")
window.configure(bg="white")

new_books = tk.Button(window, text="Yeni Not Defteri Oluştur.", bg="light green", width=110, height=60, command=new_books_ekran)
new_books.place(x=0, y=0)
new_books.bind("<Enter>", new_books_hover)
new_books.bind("<Leave>", new_books_normal)

my_books = tk.Button(window, text="Mevcut Not Defterlerim.", bg="red", width=110, height=60, command=my_books_ekran)
my_books.place(x=750, y=0)
my_books.bind("<Enter>", my_books_hover)
my_books.bind("<Leave>", my_books_normal)

notebooks_list_name = []
notebooks_list_text = []

window.mainloop()
