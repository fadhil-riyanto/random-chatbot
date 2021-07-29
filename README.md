# Random ChatBOT
Random chatbot yang mengirim pesan sesuai prediksi berdasarkan kecocokan dengan data.

Contoh: `skrng gempa ya?`
Response: 

```json
{
    "ctx": "earthquake_information",
    "msg": "Gempa terakhir dari BMKG menunjukan pada tanggal 27 Jul 2021, pukul 23:21:48 WIB terjadi gempa bumi bermagnitudo 5.2 pada kedalaman 10 km. Di Pusat gempa berada di laut 95 km Tenggara Pacitan dan III-IV Pacitan, III Nganjuk, III Karangkates, III Blitar, III Trenggalek, III Tulungagung, II Kepanjen, II Gunung Kidul, II Kendal, II Madiun, berpotensi \"Gempa ini dirasakan untuk diteruskan pada masyarakat\"\nGoogle Map: https://www.google.com/maps/search/?api=1&query=8.99 LS,111.40 BT\nShakemap: https://data.bmkg.go.id/DataMKG/TEWS/20210727232148.mmi.jpg"
}
```

Contoh: `halo`
Response:

```json
{
    "ctx": null,
    "msg": "naonsi"
}
```

# Deploy
Install beberapa module yakni `tensorflow`, `matplotlib`, dan `nltk` untuk ngebuat dan train modelnya.
Lalu, kalau mau deploy ke rest api install juga `flask`

Kalau penginstallan diatas udh semua, jalankan file `datasets_parse.py` untuk memindahkan datasets yang ada ke file `intents.json`. Untuk maksimal data default ke `5000`item, bisa diubah di file `config.py`

# Source dataset dan informasi

- Model dapat di download dengan cara menjalankan file `dl_models.py`
- Datasets percakapan diambil dari tiga grup ([AnonymousChatGroup2](https://t.me/Anonymouschatgroupdua), [AnonymousChatGroup](https://t.me/Anonymouschatgroupsaatu), dan [AnonymousChatGroupBaru](https://t.me/anonymousgroupchatbaru)) (Jika ingin download datasetsnya bisa jalankan file `dl_datasets.py`)
- Informasi gempa diambil dari website data terbuka BMKG (https://data.bmkg.co.id)
