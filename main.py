import csv
import matplotlib.pyplot
meses = []
valores = []
with open('taveira_planilha.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=",")
    for coluna in leitor:
        meses.append(coluna[0])
        valores.append(coluna[1])
    print(meses)
    print(valores)
    matplotlib.pyplot.plot(meses, valores)
    matplotlib.pyplot.show()

    matplotlib.pyplot.bar(meses, valores)
    matplotlib.pyplot.show()

    matplotlib.pyplot.pie(valores)
    matplotlib.pyplot.show()
