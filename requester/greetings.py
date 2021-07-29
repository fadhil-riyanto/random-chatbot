import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, "id_ID")
def getGreets():
    now = datetime.now()
    
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    second = int(now.strftime("%S"))
    suasana = ""

    if hour < 12:
        suasana = "Pagi"
    elif hour < 15:
        suasana = "Siang"
    elif hour < 19:
        suasana = "Sore"
    elif hour < 21:
        suasana = "Malam"
    elif hour <= 24 or hour == 0:
        suasana = "Tengah Malam"
    
    text = f"Selamat {suasana}, saat ini menunjukan pukul {hour}:{minute}:{second} di waktu saya."
    return text