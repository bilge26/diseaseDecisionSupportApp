# Kategori ve hastalıkları içeren ağaç yapısı
kategori_hastaliklar = {
    "Genel": {
        "Grip": {"ateş": True, "oksürük": True, "burun_akıntısı": True, "baş_ağrısı": True},
        "Soğuk Algınlığı": {"oksürük": True, "burun_akıntısı": True, "hapşırma": True, "boğaz_ağrısı": True},
        "Yüksek Tansiyon": {"baş_ağrısı": True, "baş_dönmesi": True, "göğüs_ağrısı": True, "nefes_darlığı": True},
        "Kolesterol": {"göğüs_ağrısı": True, "baş_dönmesi": True, "halsizlik": True, "mide_bulantısı": True, "yorgunluk": True, "nefes_darlığı": True, "geç_iyileşen_yaralar": True, "uzuvlarda_uyuşma": True, "göz_çevresinde_yağ_birikimi": True},
        
    },
    "Kadın Hastalıkları": {
        "Menstrüel Sendrom": {"karın_ağrısı": True, "baş_ağrısı": True, "göğüs_şişkinliği": True, "ruhsal_değişiklikler": True, "halsizlik": True, "gaz_şikayeti": True},
        "Endometriozis": {"pelvik_ağrı": True, "ağrılı_menstruasyon": True, "gebelik_öncesi_kanama": True, "sık_idrara_çıkma": True, "sırt_ağrısı": True, "karnın_alt_bölgesinde_şiddetli_ağrı": True},
        "Miyom": {"sık_idrara_çıkma": True, "kasıklarda_ağrı": True, "kansızlık": True, "kabızlık": True, "uzun_süreli_adet_kanamaları": True, "yorgunluk_ve_halsizlik": True, "karında_baskı_veya_yumru_hissi": True},
        "POS(Polistik Over Sendromu)": {"adet_düzensizliği": True, "kilo_artışı": True, "Yüz_ve_sırtta_sivilcelenme": True, "seste_kalınlaşma": True, "tüylenme": True, "saç_dökülmesi": True, "ciltte_lekelenmeler": True},
        "Yumurtalık Kistleri": {"kasıklarda_ağrı": True, "karın_ağrısı": True, "adet_düzensizliği": True, "gebe_kalmakta_sıkıntı": True, "ilişki_esnasında_ağrı": True, "karın_şişliği": True},

    },

    "Çocuk Hastalıkları": {
        "Suçiçeği": {"kırmızı_döküntü": True, "su_baloncukları": True, "ateş": True},
        "Kızamık": {"kırmızı_döküntü": True, "ateş": True, "göz_ıslaklığı": True},
        "Nezle" : {"hapşırık": True, "burunda_tıkanıklık_veya_akıntı": True, "ateş": True, "halsizlik": True, "boğaz_ağrısı": True, "kas_ağrıları": True},
        "Kabakulak" : {"yüzde_şişlik": True, "baş_ağrısı": True, "kas_ağrıları": True, "halsizlik": True, "yorgunluk": True,"iştahsızlık": True, "mide_bulantısı": True, "ağız_kuruluğu": True, "yutkunurken_ağrı": True},
        "Bademcik İltihabı": {"halsizlik": True, "ateş": True, "yutkunurken_ağrı": True, "bademciklerde_şişkinlik_ve_kızarıklık": True},
        "Orta Kulak İltihabı": {"şiddetli_kulak_ağrısı": True, "kulak_akıntısı": True, "ateş": True, "iştahsızlık": True, "işitme_kaybı": True, "ishal": True, "baş_dönmesi": True, "kulaklarda_çınlama": True, "kulak_kepçesini_çekiştirme": True},
        "Bronşit": {"burun_akıntısı": True, "hapşırık": True, "huzursuzluk": True, "hırıltılı_solunum": True, "nefes_almada_sıklık": True, "göğüste_çekilme": True},
        "Zatürre": {"yüksek_ateş": True, "öksürük": True, "iltihaplı_balgam_çıkarma": True, "üşüme-titreme": True, "iştahsızlık": True, "halsizlik": True, "kuru_öksürük": True, "kusma": True, "baş_ağrısı": True}
    },

    "İç Hastalıkları":{
        "Ülser": {"mide_yanması": True, "hazımsızlık": True, "mide_bulantısı": True, "kusma": True, "iştahsızlık": True, "kilo_kaybı": True, "baş_dönmesi": True, "nefes_darlığı": True, "yorgunluk": True},
        "Gastrit": {"mide_ağrısı": True, "sırt_ağrısı": True, "mide_bulantısı": True, "mide_yanması": True, "hazımsızlık": True, "iştahsızlık": True, "geğirme": True, "kilo_kaybı": True, "midede_şişkinlik": True},
        "Reflü": {"göğüste_yanma": True, "mide_ekşimesi": True, "yutma_güçlüğü": True, "boğaz_ağrısı": True, "geğirme": True, "hıçkırık": True, "midede_şişkinlik": True, "mide_bulantısı": True},
        "Guatr": {"boyunda_ağrısız_şişlik": True, "ses_kısıklığı": True, "yorgunluk": True, "cilt_kuruluğu": True, "kabızlık": True, "kilo_kaybı": True, "baş_dönmesi": True, "ishal": True},
        "Anemi": {"yorgunluk": True, "el_ve_ayaklarda_soğukluk": True, "nefes_darlığı": True, "baş_dönmesi": True, "baş_ağrısı": True, "konsantrasyon_bozukluğu": True, "dilde_iltihap": True, "ciltte_soluklaşma": True, "kalp_ritminde_düzensizlik": True}, 
    },

    "Kalp Damar Hastalıkları": {
    "Koroner Arter": {"nefes_darlığı": True, "çarpıntı": True, "hızl_kalp_atışı": True, "güçsüzlük": True, "baş_dönmesi": True, "mide_bulantısı": True, "terleme": True, "göğüste_ağırlık_yanma_hissi" : True},
    "Kalp Krizi": {"göğüste_basınç": True, "kolda_ağrı_ya da_basınç": True, "boğulma_hissi": True, "mide_bulantısı": True, "terleme": True, "bulantı": True, "kusma": True, "baş_dönmesi": True,"aşırı_güçsüzlük": True, "düzensiz_kalp_atışları": True},
    "Aritmi": {"göğüste_basınç": True, "çarpıntı": True, "baş_dönmesi": True, "sersemlik": True, "bayılma": True, "nefes_darlığı": True, "güçsüzlük": True, "aşırı_yorgunluk_hissi": True},
    "Kalp Kapağı Hastalığı": {"nefes_darlığı": True, "halsizlik": True, "baş_dönmesi": True, "göğüste_basınç": True, "çarpıntı": True, "ayaklarda_şişlik": True, "hızlı_kilo_alımı": True},
    "Kalp Yetmezliği": {"hareket_halinde_nefes_darlığı": True, "uzanırken_nefes_darlığı": True, "beyaz_balgamlı_öksürük": True, "hızlı_kilo_alımı": True, "ayaklarda_şişlik": True, "baş_dönmesi": True, "yorgunluk": True, "halsizlik": True, "mide_bulantısı": True, "çarpıntı": True, "göğüste_basınç": True}

    },

    "Beyin Hastalıkları": {
        "Epilepsi": {"bilinç_kaybı": True, "diş_kenetlenmesi": True, "aniden_yere_yığılma": True, "dejavuya_kapılma": True, "koku_tat_halüsinasyonları": True, "kontrol_edilemeyen_titremeler": True, "nöbet_anında_vücudun_kaskatı_kesilmesi": True},
        "Demans(Bunama)": {"hafıza_kaybı": True, "iletişimde_güçlük": True, "akıl_yürütmede_güçlük": True, "planlama_ve_organize_edememe": True, "hareketlerin_koordinasyonunda_zayıflık": True, "yer_bulma_becerilerinde_zayıflama": True},
        "Alzheimer": {"hatırlama_güçlüğü": True, "planlama_ve_organize_edememe": True, "muhakeme_yeteneğinde_zayıflık": True, "iletişimde_güçlük": True, "hafıza_kaybı": True, "zaman_kavramını_yitirme": True, "uyku_bozuklukları": True, "yeme_güçlüğü": True}
    }

}

# Kullanıcıdan hangi kategori ile ilgili belirtileri sormak istediğini sor
print("Hangi kategoriyle ilgili belirtileri sormak istersiniz?")
for i, kategori in enumerate(kategori_hastaliklar.keys()):
    print(f"{i + 1}. {kategori}")

secilen_kategori = None
while secilen_kategori is None:
    try:
        secim = int(input("Seçim (1-{}): ".format(len(kategori_hastaliklar))))
        if 1 <= secim <= len(kategori_hastaliklar):
            secilen_kategori = list(kategori_hastaliklar.keys())[secim - 1]
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")

# Kullanıcıdan bilgi alma
isim = input("Adınız: ")
yas = int(input("Yaşınız: "))

# Kullanıcının daha önce verdiği cevapları saklamak için bir sözlük
verilen_cevaplar = {}

# Belirtileri almak için ağaç üzerinde dolaşma
def belirtileri_al(hastalik_agaci, verilen_cevaplar):
    belirtiler = {}
    for belirti, var_mi in hastalik_agaci.items():
        if belirti in verilen_cevaplar:
            # Daha önce verilen cevap varsa, tekrar sormadan önceki cevabı kullan
            cevap = verilen_cevaplar[belirti]
        else:
            cevap = input(f"{belirti.replace('_', ' ')} var mı? (Evet/Hayır): ").lower()
            verilen_cevaplar[belirti] = cevap

        belirtiler[belirti] = True if cevap == "evet" else False

    return belirtiler

# Hasta bilgisi oluşturma
hasta_bilgisi = {
    "isim": isim,
    "yas": yas,
}

# Seçilen kategoriye ait hastalıkların belirtilerini sormak
muhtemel_hastaliklar = []
for hastalik, belirtiler_agaci in kategori_hastaliklar[secilen_kategori].items():
    belirtiler_kullanicidan = belirtileri_al(belirtiler_agaci, verilen_cevaplar)

    # Belirtilerin karşılaştırılması
    uyumlu_belirtiler = sum(belirtiler_kullanicidan[belirti] == var_mi for belirti, var_mi in belirtiler_agaci.items())
    oran = (uyumlu_belirtiler / len(belirtiler_agaci)) * 100

    if oran > 60:
        muhtemel_hastaliklar.append((hastalik, oran))

# Oranları yazdırma
print("\n{} ({} yaş), aşağıdaki hastalıklara sahip olma olasılıkları:".format(isim, yas))
for hastalik, oran in muhtemel_hastaliklar:
    print(f"- {hastalik}: {round(oran, 2)}%")


# Öneriler
for hastalik, _ in muhtemel_hastaliklar:
    if hastalik in ["Grip", "Soğuk Algınlığı"]:
        print(f"\n{hastalik} için aile hekimine başvurmanızı öneririz.")
    elif hastalik == "Yüksek Tansiyon":
        print("Yüksek tansiyon için düzenli olarak ilaç kullanılmalı ve sağlıklı bir yaşam tarzı benimsemelisiniz.")
    elif hastalik in ["Ülser", "Gastrit", "Reflü", "Guatr", "Anemi"]:
        print(f"\n{hastalik} için Dahiliyeye görünmenizi öneririz.")
    elif hastalik == "Kolesterol":
        print("Kolesterol için Kardiyoloji bölümüne görünmenizi tavsiye ederiz.")
    elif hastalik in ["Suçiçeği", "Kızamık", "Nezle", "Kabakulak", "Bademcik İltihabı", "Orta Kulak İltihabı", "Bronşit", "Zatürre"]:
        print(f"\n{hastalik} için Çocuk Polikliniğine görünmenizi öneririz.")
    elif hastalik in ["Menstrüel Sendrom", "Endometriozis", "Miyom", "POS (Polistik Over Sendromu)", "Yumurtalık Kistleri"]:
        print(f"\n{hastalik} için Kadın Hastalıkları ve Doğum bölümüne görünmenizi öneririz.")
    elif hastalik in ["Koroner Arter", "Kalp Krizi", "Aritmi", "Kalp Kapağı Hastalığı", "Kalp Yetmezliği"]:
        print(f"\n{hastalik} için Kardiyoloji bölümüne görünmenizi öneririz.")
    elif hastalik in ["Epilepsi", "Demans(Bunama)", "Alzheimer"]:
        print(f"\n{hastalik} için Nöroloji Bölümüne görünmenizi öneririz.")