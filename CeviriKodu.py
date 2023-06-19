from deep_translator import GoogleTranslator

dosya = open('CevirilecekMetin.txt', 'r')
TurkceListe = []

for j in dosya:
    TurkceListe.append(j)

for i in TurkceListe:
    translated = GoogleTranslator(source='tr', target='en').translate(i)
    print(translated)
    IngilizceListe = [translated]

