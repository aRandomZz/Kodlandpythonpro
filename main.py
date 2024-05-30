meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado"}

while True:
    meme= input("Introduce una palabra que no entiendas:").upper()
    if meme == 'STOP':
        break
    else:
        try:
            float(meme)
        except:
            if meme in meme_dict.keys():
                for i in range(len(meme_dict)):
                    if meme==meme_dict.keys()[i]:
                        print(meme, end=': ')
                        print(meme_dict.values()[i])
            else:
                print('Esa palabra no existe')
                pass
        else:
            print('Palabras, no números')
            pass
