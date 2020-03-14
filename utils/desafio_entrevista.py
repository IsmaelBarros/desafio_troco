import math
from pymongo import MongoClient


def troco_facil(preco, pgto):

    nota_de_1 = 0
    nota_de_5 = 0
    nota_de_10 = 0
    nota_de_50 = 0

    moeda_de_1 = 0
    moeda_de_5 = 0
    moeda_de_10 = 0
    moeda_de_50 = 0

    if pgto >= preco:
        troco = pgto - preco
        unidade = math.floor(troco) % 10
        dezena = (math.floor((troco - unidade) / 10)) % 10

        troco_arr = round(troco, 2)
        decimo = (math.floor(troco_arr * 10)) % 10
        centesimo = (math.floor(troco_arr * 100)) % 10

        #troco para notas
        if dezena == 0:

            if unidade > 0 and unidade < 5:
                nota_de_1 = 1
                for i in range(1, unidade):
                    nota_de_1 += 1

            elif unidade == 5:
                nota_de_5 = 1

            elif unidade > 5:
                nota_de_5 = 1
                nota_de_1 = 1
                for i in range(6, unidade):
                    nota_de_1 += 1

        elif dezena > 0 and dezena < 5:
            nota_de_10 = 1
            for i in range(1, dezena):
                nota_de_10 += 1
            if unidade > 0 and unidade < 5:
                nota_de_1 = 1
                for i in range(1, unidade):
                    nota_de_1 += 1

            elif unidade == 5:
                nota_de_5 = 1

            elif unidade > 5:
                nota_de_5 = 1
                nota_de_1 = 1
                for i in range(6, unidade):
                    nota_de_1 += 1

        elif dezena == 5:
            nota_de_50 = 1
            if unidade > 0 and unidade < 5:
                nota_de_1 = 1
                for i in range(1, unidade):
                    nota_de_1 += 1

            elif unidade == 5:
                nota_de_5 = 1

            elif unidade > 5:
                nota_de_5 = 1
                nota_de_1 = 1
                for i in range(6, unidade):
                    nota_de_1 += 1
        elif dezena > 5:
            nota_de_50 = 1
            nota_de_10 = 1
            for i in range(6, dezena):
                nota_de_10 += 1
            if unidade > 0 and unidade < 5:
                nota_de_1 = 1
                for i in range(1, unidade):
                    nota_de_1 += 1

            elif unidade == 5:
                nota_de_5 = 1

            elif unidade > 5:
                nota_de_5 = 1
                nota_de_1 = 1
                for i in range(6, unidade):
                    nota_de_1 += 1
        # Troco para centavos
        if decimo > 0 and decimo < 5:
            moeda_de_10 = 1
            for i in range(1, decimo):
                moeda_de_10 += 1

            if centesimo > 0 and centesimo < 5:
                moeda_de_1 = 1
                for i in range(1, centesimo):
                    moeda_de_1 += 1

            elif centesimo == 5:
                moeda_de_5 = 1

            elif centesimo > 5:
                moeda_de_5 = 1
                moeda_de_1 = 1
                for i in range(6, centesimo):
                    moeda_de_1 += 1

        elif decimo == 5:
            moeda_de_50 = 1

            if centesimo > 0 and centesimo < 5:
                moeda_de_1 = 1
                for i in range(1, centesimo):
                    moeda_de_1 += 1

            elif centesimo == 5:
                moeda_de_5 = 1

            elif centesimo > 5:
                moeda_de_5 = 1
                moeda_de_1 = 1
                for i in range(6, centesimo):
                    moeda_de_1 += 1

        elif decimo > 5:
            moeda_de_50 = 1
            moeda_de_10 = 1
            for i in range(6, decimo):
                moeda_de_10 += 1

            if centesimo > 0 and centesimo < 5:
                moeda_de_1 = 1
                for i in range(1, centesimo):
                    moeda_de_1 += 1

            elif centesimo == 5:
                moeda_de_5 = 1

            elif centesimo > 5:
                moeda_de_5 = 1
                moeda_de_1 = 1
                for i in range(6, centesimo):
                    moeda_de_1 += 1

    resultado = {}
    resultado['troco'] = troco_arr

    if nota_de_50 > 0:
        resultado['nota_50_reais'] = nota_de_50
    if nota_de_10 > 0:
        resultado['nota_10_reais'] = nota_de_10
    if nota_de_5 > 0:
        resultado['nota_5_reais'] = nota_de_5
    if nota_de_1 > 0:
        resultado['nota_1_real'] = nota_de_1

    if moeda_de_50 > 0:
        resultado['moeda_50_centavos'] = moeda_de_50
    if moeda_de_10 > 0:
        resultado['moeda_10_centavos'] = moeda_de_10
    if moeda_de_5 > 0:
        resultado['moeda_5_centavos'] = moeda_de_5
    if moeda_de_1 > 0:
        resultado['moeda_1_centavo'] = moeda_de_1

    client = MongoClient('localhost', 27017)
    #print(client.list_database_names())
    db = client.caixaDB
    db.troco_trococerto .insert_one(resultado)

    del resultado["_id"]
    return resultado