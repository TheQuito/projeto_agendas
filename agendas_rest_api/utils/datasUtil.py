from datetime import datetime, date, timedelta

def gerarListaDeDatas(inicio, fim, intervalo):
    atual = inicio
    while atual <= fim:
        yield atual
        atual += intervalo





def obterListaDeDatas(inicio, fim, intervalo):
        datas = []
        for data in gerarListaDeDatas(inicio, fim, intervalo):
                datas.append(data.strftime('%d/%m/%Y'))
        return datas


def getDia(data):
	return int(data.split('-')[2])

def getMes(data):
	return int(data.split('-')[1])

def getAno(data):
	return int(data.split('-')[0])


def getData(data):
        data = str(getDia(data)) + '/' + str(getMes(data)) + '/' + str(getAno(data))
        return data