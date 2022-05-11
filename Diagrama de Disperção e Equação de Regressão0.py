import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
## teste

# Importação do Case para calculos
df1 = pd.read_excel(r'C:\Users\André Chiezi\Estudos\Faculdade\Analise estatistica\Códigos\arquivos_excel_exemplo\excel1.xlsx',names=["x","y"])


# Colunas necessárias para calculo do Coeficiente de Correlação Linear ou coeficiente de correlação de Pearson
df1['x*y'] = df1['x']*df1['y']
df1['x²'] = df1['x']*df1['x']
df1['y²'] = df1['y']*df1['y']

## Variaveis necessárias para calculo do Coeficiente de Correlação Linear ou coeficiente de correlação de Pearson

vN = len(df1)
vSOMA_xi_yi = float(sum(df1['x*y']))
vSOMA_xi = float(sum(df1['x']))
vSOMA_yi = float(sum(df1['y']))
vSOMA_x2i = float(sum(df1['x²']))
vSOMA_y2i = float(sum(df1['y²']))

## Variaveis para calculo

## Inicio calculo do  Coeficiente de Correlação Linear ou coeficiente de correlação de Pearson
imgplot = plt.imshow(mpimg.imread(r'C:\Users\André Chiezi\Estudos\Faculdade\Analise estatistica\Códigos\imagens\img_coeficiente_de_relacao.jpg'))
plt.show()


vCOEFICIENTE_DE_RELAÇÃO = ((vN*vSOMA_xi_yi)-(vSOMA_xi*vSOMA_yi))/(((vN*vSOMA_x2i-(vSOMA_xi*vSOMA_xi))**0.5)*(vN*vSOMA_y2i-(vSOMA_yi*vSOMA_yi))**0.5)
print(f'\nO coeficiente de relação é : {vCOEFICIENTE_DE_RELAÇÃO} \n')

## Variaveis para calculo Equação de Regressão

imgplot = plt.imshow(mpimg.imread(r'C:\Users\André Chiezi\Estudos\Faculdade\Analise estatistica\Códigos\imagens\vA.jpg'))
plt.show()

vA = ((vN*vSOMA_xi_yi)-(vSOMA_xi*vSOMA_yi))/((vN*vSOMA_x2i)-(vSOMA_xi*vSOMA_xi))
print(f'\nO resultado de A é : {vA} \n')

imgplot = plt.imshow(mpimg.imread(r'C:\Users\André Chiezi\Estudos\Faculdade\Analise estatistica\Códigos\imagens\vB.jpg'))
plt.show()

vB =(vSOMA_yi-(vA*vSOMA_xi))/vN
print(f'\nO resultado de B é : {vB} \n')

vINPUTX = 60

print(f'O X é : {vINPUTX} \n')

## Inicio calculo da Equação de Regressão

vEQUACAO_DE_REGRESSAO = vB+(vA*vINPUTX)
imgplot = plt.imshow(mpimg.imread(r'C:\Users\André Chiezi\Estudos\Faculdade\Analise estatistica\Códigos\imagens\vEQUACAO_DE_REGRESSAO.jpg'))
plt.show()
print(f'\ne com base no X a Equação de Regressão é : {vEQUACAO_DE_REGRESSAO}\n')

plt.scatter(df1['x²'], df1['y²'])
plt.title('Gráfico de Dispersão entre Publicidade e vendas')
plt.show()
