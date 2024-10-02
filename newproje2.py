# Türkçe karakterlere dikkat ederek küçük harfe çeviren fonksiyon
def formatDomain(domain):
    turkish_lower_map = str.maketrans("IİŞĞÜÇÖ", "ıişğüçö")
    return domain.translate(turkish_lower_map).lower()