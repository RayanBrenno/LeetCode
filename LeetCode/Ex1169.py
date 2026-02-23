# Nesse código a ideia é percorrer todas as transações, separar nome, tempo, valor e cidade, e agrupar as transações por nome em um dicionário para poder comparar apenas aquelas da mesma pessoa. Para cada nova transação, primeiro verificamos se o valor é maior que 1000; se for, ela já é marcada como inválida. Depois, comparamos essa transação com todas as anteriores do mesmo nome que já estão salvas no dicionário: se a diferença de tempo for menor ou igual a 60 minutos e as cidades forem diferentes, então ambas as transações são marcadas como inválidas. No final, adicionamos a transação atual ao dicionário e, ao terminar o loop, retornamos todas as transações cujos índices foram marcados como inválidos. O ponto importante é que mesmo uma transação já inválida por valor ainda precisa ser comparada com as outras, pois ela pode invalidar mais transações pela regra da cidade.

from typing import List

def invalidTransactions(self, transactions: List[str]) -> List[str]:
    dic_transactions = {}
    invalid_transactions = set()

    for i, transaction in enumerate(transactions):
        name, time, cash, city = transaction.split(",")
        time = int(time)
        cash = int(cash)

        if name not in dic_transactions:
            dic_transactions[name] = []

        if cash > 1000:
            invalid_transactions.add(i)

        for t, c, idx in dic_transactions[name]:
            if abs(t - time) <= 60 and c != city:
                invalid_transactions.add(idx)
                invalid_transactions.add(i)

        dic_transactions[name].append((time, city, i))

    return [transactions[i] for i in invalid_transactions]


transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
print(invalidTransactions(None, transactions))