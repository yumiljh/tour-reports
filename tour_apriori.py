#-*- coding:utf-8 -*-
from apyori import apriori

transactions = [['Bread','Milk'],
        ['Bread','Diapers','Beer','Eggs'],
        ['Milk','Diapers','Beer','Cola'],
        ['Bread','Milk','Diapers','Beer'],
        ['Bread','Milk','Beer','Cola']]

result = list(apriori(transactions, min_support=0.6, min_confidence=1.0, max_length=2))

for row in result:
    print list(row.items)
    for rule in row.ordered_statistics:
        print list(rule.items_base), "-->", list(rule.items_add), "support:", row.support, "confidence:", rule.confidence, "lift:", rule.lift
