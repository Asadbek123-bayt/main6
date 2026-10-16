sonlar_1=[2,5,8,11,14,17,20]
sonlar_2=[]
for son in sonlar_1:
  if son % 2==0:
       sonlar_2.append(son)
print(sonlar_2)
laptop = {'modeli': 'lenovo', 'xotirasi': '512 GB','CPU':'AMD Ryzen 5 7520U',
'OZU': 'DDR5  8 GB','OS': 'Windows 11 PRO','display': 15.6 ,'narxi':'5 mln','xolati':'yaxshi'}
for noutbook in laptop:
    print(noutbook)

taomlar = {"Alining": "osh","Valining": "shashlik","Olimning": "somsa",
           "Zuhraning": "manti","Anvarning": "lag'mon"}
print(f"Alining sevimli taomi {taomlar['Alining']}")
print(f"Valining sevimli taomi {taomlar['Valining']}")
print(f"Olimning sevimli taomi {taomlar['Olimning']}")
python_lugat = {"integer": "Butun son","float": "O'nlik son","string": "Matn (satr)",
    "if": "Agar","else": "Aks holda","dictionary": "Lug'at","list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat","boolean": "Mantiqiy qiymat","for": "Sikl (takrorlanish operatori)"}
tarjima = python_lugat.get('kalit', "Bunda so'z mavjud emas")
print(tarjima)

kalit = input("Kalit so'z kiriting: ").lower().strip()
if kalit in python_lugat:
    print(f"{kalit.title()} so'zi \"{python_lugat[kalit]}\" deb tarjima qilinadi")
else:
    print("Bunday so'z mavjud emas")

davlatlar = {"O'zbekiston": "Toshkent","Rossiya": "Moskva","AQSh": "Washington D.C.",
    "Italiya": "Rim","Malayziya": "Kuala-Lumpur","Qirg'iziston": "Bishkek","Qozog'iston": "Nursulton",
    "Tojikiston": "Dushanbe","Singapur": "Singapur"}
for davlat in davlatlar:
    print(davlat,":",davlatlar[davlat])