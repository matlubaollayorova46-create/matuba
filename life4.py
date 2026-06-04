import tkinter as tk
from tkinter import messagebox
from random import choice

# Song class, foydalanuvchi kiritgan so'zga asoslangan qo'shiq yaratish
class Song:
    def __init__(self, keyword):
        self.keyword = keyword
        
    def generate_song(self):
        # Kengroq va ko'proq misralarga ega qo'shiq yaratish
        verses = [
            [f"Yorug'likda ham, {self.keyword} nur kabi porlaydi,",
             f"Bu {self.keyword} har doim yuragimda yondi,",
             f"Hayotdagi har bir qadamimda {self.keyword}ni his qilaman,",
             f"{self.keyword} bilan kechayu kunduz o'zimni his etaman,",
             f"{self.keyword} - bu dunyodagi eng buyuk quvonchdir,"],

            [f"Sen menga {self.keyword}ni o'rgatding, har bir qadamingni,",
             f"Har safar {self.keyword}ni eslaganda, qalbim titraydi,",
             f"{self.keyword} bilan yashashga qaror qildim, hayotim yorishdi,",
             f"Hayotning har bir yulduzi {self.keyword} bilan porlaydi,",
             f"Har bir kuzda {self.keyword} bilan sevaman, vaqtni his qilaman."],

            [f"Qorong'u tunlarda {self.keyword} bilan yorug'lik topdim,",
             f"{self.keyword} meni so'nggi quvonchga yetkazadi,",
             f"{self.keyword}ning issiq nafasi bilan jonlanaman,",
             f"{self.keyword}da ulug'vorlik va kuchni topaman,",
             f"Sen bilan dunyo o'zgaradi, {self.keyword} bilan yonaman,"],

            [f"{self.keyword} bilan haqiqiy sevgini tushundim,",
             f"Sevgi haqida barcha tushunchalar {self.keyword} bilan yuksaldi,",
             f"{self.keyword}da orzu va umidni topdim,",
             f"{self.keyword} menga kuch bag'ishladi, hayotga yangi qaradim,",
             f"{self.keyword} bilan dunyo yangi shaklga kirdi,"]  
        ]
        
        # 15 misrali qo'shiqni yaratish
        song_lyrics = ""
        for i in range(15):
            # Har bir so'zga mos turli misra tanlanadi
            song_lyrics += choice(verses[i % len(verses)]) + "\n"
        return song_lyrics

# Rasmlar yaratish uchun (tasodifiy rasm yaratish)
def generate_image(keyword):
    # Rasmlar yaratish bo'yicha fikrni faqat tasavvur qiling
    # Hozircha tasodifiy rasmni generatsiya qilish uchun o'zgaruvchi tasavvur qiling
    image_urls = [
        "https://via.placeholder.com/150?text=So'z+rasmi+1",
        "https://via.placeholder.com/150?text=So'z+rasmi+2",
        "https://via.placeholder.com/150?text=So'z+rasmi+3"
    ]
    return choice(image_urls)

# Tkinter interfeysi
class SongGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Qo'shiq Generator")
        self.root.geometry("600x600")
        
        # Kirish maydoni
        self.label = tk.Label(self.root, text="Bir so'z kiriting:", font=("Helvetica", 14))
        self.label.pack(pady=10)
        
        # So'z kiritish maydoni
        self.entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        
        # Qo'shiqni generatsiya qilish tugmasi
        self.generate_button = tk.Button(self.root, text="Qo'shiqni Yaratish", font=("Helvetica", 14), command=self.generate_song)
        self.generate_button.pack(pady=20)
        
        # Natija uchun matn oynasi
        self.result_text = tk.Text(self.root, height=15, width=50, font=("Helvetica", 12), wrap=tk.WORD)
        self.result_text.pack(pady=10)
        
        # Rasmni ko'rsatish uchun labellar
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

    def generate_song(self):
        # Foydalanuvchidan kiritilgan so'zni olish
        keyword = self.entry.get().strip()
        
        # Agar so'z kiritilmagan bo'lsa, xabar ko'rsatish
        if not keyword:
            messagebox.showerror("Xatolik", "Iltimos, so'zni kiriting!")
            return
        
        # Song ob'ektini yaratish va qo'shiqni olish
        song = Song(keyword)
        song_lyrics = song.generate_song()
        
        # Rasmlar yaratish
        image_url = generate_image(keyword)

        # Qo'shiqni matn oynasiga chiqarish
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, song_lyrics)

        # Rasmni ko'rsatish
        self.show_image(image_url)
    
    def show_image(self, image_url):
        # Rasmlar URL manzilini ko'rsatish
        self.image_label.config(text=f"Rasm: {image_url}")
        
# Asosiy dastur
if __name__ == "__main__":
    root = tk.Tk()
    app = SongGeneratorApp(root)
    root.mainloop()