arvores <- read.csv("arvores.csv", header = TRUE, sep = ",", dec = ".")

tabela <- head(arvores)
print('Tabela')
print(tabela)

frequencia_absoluta <- table(arvores$pesquisador)
print('Frequência absoluta:')
print(frequencia_absoluta)

frequencia_relativa <- prop.table(table(arvores$pesquisador))
print('Frequência relativa:')
print(frequencia_relativa)

arvores$altura <- gsub(",", ".", arvores$altura)
arvores$altura <- as.numeric(arvores$altura)
frequencia_classes <- table(cut(arvores$altura, breaks = 5))
print('Frequência por intervalos (classes):')
print(frequencia_classes)
