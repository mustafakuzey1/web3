from flask import Flask
import random
facts_list=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.","2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50 den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."]
app = Flask(__name__)

@app.route("/")  
def index():
    return f'<h1>MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!  <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a></h1>'

@app.route("/rastgele_gercek")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)