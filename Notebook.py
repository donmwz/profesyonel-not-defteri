import tkinter as tk
import random
#power by eren dönmez

colors = ["white", "light green", "light yellow", "light blue", "pink"]
def new_books_ekran():
    window_new_books = tk.Toplevel()
    window_new_books.geometry("1920x1080")
    window_new_books.title("Yeni Not Defteri Oluştur")
    window_new_books.configure(bg=random.choice(colors))

    new_books_name = tk.Label(window_new_books, text="Yeni Not Defteri Adı:")
    new_books_name.place(x=705, y=247)

    new_books_name_input = tk.Entry(window_new_books, bg="pink")
    new_books_name_input.place(x=700, y=270)

    new_books_name_button = tk.Button(window_new_books, text="Kaydet", command=lambda: new_books_name_save(new_books_name_input), bg="light green")
    new_books_name_button.place(x=738, y=302)

    info = tk.Label(window_new_books, text="Kaydet'e basttığınızda değişiklikleriniz başarıyla kaydedilir. Gönül rahatlığıyla bu sekmeyi kapatabilirsiniz.", fg="black")
    info.place(x=468, y=340)
    # kullanıcı notlarının içerikleri
    new_books_text = tk.Entry(window_new_books, width=150,  bg="yellow", fg="black")
    new_books_text.place(x=310, y=400)
    new_books_text_button = tk.Button(window_new_books, text="Kaydet",  bg="light green", width=7, command=lambda: new_books_text_save(new_books_text) )
    new_books_text_button.place(x=1215, y=398)

    powerby = tk.Label(window_new_books, text="Power By: Eren Dönmez", font=("Times 11 bold"), bg="orange")
    powerby.place(x=5, y=0)
    powerby = tk.Label(window_new_books, text="Altınbaş Unıversty 2024", bg="red")
    powerby.place(x=5, y=25)

def new_books_name_save(entry):
    global notebook_count
    girilen_not_defter_adi = entry.get()
    notebook_count += 1
    new_notebook_name = f"{girilen_not_defter_adi} {notebook_count}"
    notebooks_list_name.append(new_notebook_name)
    notebooks_list_text[new_notebook_name] = []
    print("Not Defteri Adı Kaydedildi:", new_notebook_name)

def new_books_text_save(entry):
    new_books_text = entry.get()
    notebook_name = notebooks_list_name[-1]
    notebooks_list_text[notebook_name].append(new_books_text)
    print("Not Defteri İçeriği Kaydedildi:", new_books_text)

def my_books_ekran():
    window_my_books = tk.Toplevel()
    window_my_books.geometry("1920x1080")
    window_my_books.title("Not Defterlerim")
    window_my_books.configure(bg=random.choice(colors))
    #
    info_my_books = tk.Label(window_my_books, text="Kayıtlı Not Defterleri:", fg="red", bg="white", font=(15))
    info_my_books.place(x=700, y=12)
    #
    y_position = 40
    for notebook_name in notebooks_list_name:
        kayitli_not_defterleri = tk.Button(window_my_books, text=notebook_name, width=50, height=15, bg=random.choice(colors), command=lambda nb=notebook_name: kayitli_not_defterleri_text_içerik(nb))
        kayitli_not_defterleri.place(x=19, y=y_position)
        y_position += 250

def kayitli_not_defterleri_text_içerik(notebook_name):
    window_kayitli_not_defterleri_text_içerik = tk.Toplevel()
    window_kayitli_not_defterleri_text_içerik.geometry("1920x1080")
    window_kayitli_not_defterleri_text_içerik.title(notebook_name)
    window_kayitli_not_defterleri_text_içerik.configure(bg=random.choice(colors))
    #
    notebook_content_label = tk.Label(window_kayitli_not_defterleri_text_içerik, text='\n'.join(notebooks_list_text[notebook_name]), bg=(random.choice(colors)))
    notebook_content_label.place(x=5, y=350)

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

my_books = tk.Button(window, text="Mevcut Not Defterlerim.", bg="red", width=112, height=60, command=my_books_ekran)
my_books.place(x=750, y=0)
my_books.bind("<Enter>", my_books_hover)
my_books.bind("<Leave>", my_books_normal)

# Sayaç değişkeni
notebook_count = 0

notebooks_list_text = {}
notebooks_list_name = []

window.mainloop()
