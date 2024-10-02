# Türkçe karakterlere dikkat ederek küçük harfe çeviren fonksiyon
def formatDomain(domain):
    turkish_lower_map = str.maketrans("IİŞĞÜÇÖ", "ıişğüçö")
    return domain.translate(turkish_lower_map).lower()

# Alan adlarını liste olarak tanımlama

domains = [
    "TEKNOLOJI.COM", "teknoloji.com", "TeKnoLoJi.cOm", "KITAPLIK.COM", "kitaplik.com",
    "KiTaPlIk.CoM", "EĞİTİM.COM", "egitim.com", "EgItIm.cOm", "SAĞLIK.COM",
    "saglik.com", "SaGlIk.CoM", "YEMEKTARİFİ.COM", "yemektarifi.com", "YeMeKTaRiFi.CoM",
    "OYUNLAR.COM", "oyunlar.com", "OyUnLaR.cOm", "SİTE.COM", "site.com"
]

for domain in domains:
    print(formatDomain(domain))