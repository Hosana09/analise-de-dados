import pandas as pd

arvores = pd.read_csv('arvores.csv')
arvores.head()
print('Tabela')
print(arvores.head())

frequencia_absoluta = arvores['pesquisador'].value_counts()
print('Frequência absoluta:')
print(frequencia_absoluta)

frequencia_relativa = arvores['pesquisador'].value_counts(normalize=True)
print('Frequência relativa:')
print(frequencia_relativa)

arvores['altura'] = arvores['altura'].str.replace(',', '.')
arvores['altura'] = pd.to_numeric(arvores['altura'], errors='coerce')
frequencia_classes = pd.cut(arvores['altura'], bins=10).value_counts()
print('Frequência por intervalos (classes):')
print(frequencia_classes)

