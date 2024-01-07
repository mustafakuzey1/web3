from flask import Flask, render_template
import random
import string

app = Flask(__name__)

# Ana sayfa
@app.route("/")
def home():
    return "Ana Sayfa"

# İkinci sayfa
@app.route("/sayfa2")
def page2():
    return "İkinci Sayfa"

# Üçüncü sayfa
@app.route("/sayfa3")
def page3():
    # 1. Yazı tura
    yazitura = random.choice(["Yazı", "Tura"])

    # 2. Şifre oluşturucu
    sifre = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

    # 3. Rastgele bir resim gösterme (örnek için bir resim URL'si)
    resim_url = "https://example.com/image.jpg"

    # HTML şablonunu kullanarak sayfayı oluştur
    return render_template("sayfa3.html", yazitura=yazitura, sifre=sifre, resim_url=resim_url)

if __name__ == "__main__":
    app.run(debug=True)