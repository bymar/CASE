from datetime import date, datetime

def encriptando(senha):
    senha = senha.title()
    senha = senha.replace(" ", "")
    senha = senha.replace("i", "@")
    senha = senha.replace("e", "!")
    senha = senha.replace("u", "$")
    senha = senha.replace("a", "@")
    senha = senha.replace("E", "%")
    senha = senha.replace("o", "#")
    mes = datetime.now()
    mes = str(mes)
    mes = mes.replace('0', '°')
    mes = mes.replace('1', '[')
    mes = mes.replace('2', 's')
    mes = mes.replace('3', '§')
    mes = mes.replace('4', '£')
    mes = mes.replace('5', '¢')
    mes = mes.replace('6', '/')
    mes = mes.replace('7', '¬')
    mes = mes.replace('8', '&')
    mes = mes.replace('9', 'ª')
    hoje = date.today()
    hoje = str(hoje)
    hoje = hoje.replace('-', '')
    hoje = list(hoje)
    i = 0
    while i < len(hoje):
        for v in hoje:
            hoje[i] = int(v)
            i += 1
    magic = sum(hoje)
    segredo = senha + mes
    parte1 = segredo[magic-7:magic]
    parte2 = segredo[-7:]
    parte3 = segredo[magic:magic+7]
    senhagerada = parte1 + parte2 + parte3
    senhagerada = senhagerada[::-1]
    return senhagerada

def arrumarcsv(listas):
    listas = ''.join(listas)
    listas = listas.replace(',','')
    return listas