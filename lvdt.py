import numpy as np
import matplotlib.pyplot as plt

# Dados experimentais
distancia = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
tensao_bobina1 = np.array([14.6, 17.8, 29.3, 72.5, 179, 360, 348, 132, 35, 20, 15, 14.5, 14.3, 14.3])
tensao_bobina2 = np.array([15, 14, 13.7, 14.2, 16.8, 34.8, 86, 292, 345, 240, 77, 35, 18, 14.1])

# Cálculo da diferença entre as tensões das duas bobinas
diferenca_tensao = tensao_bobina1 - tensao_bobina2

# Plotar os pontos experimentais
plt.plot(distancia, diferenca_tensao, 'bo', label='Pontos Experimentais')

# Encontrar região linear
regiao_linear = np.where((distancia >= 2) & (distancia <= 10))
distancia_regiao_linear = distancia[regiao_linear]
diferenca_tensao_regiao_linear = diferenca_tensao[regiao_linear]

# Realizar regressão linear
regressao_linear = np.polyfit(distancia_regiao_linear, diferenca_tensao_regiao_linear, 1)

# Calcular sensibilidade
coef_angular = regressao_linear[0]
sensibilidade = coef_angular * 10
print("Sensibilidade: {:.2f} mV/mm".format(sensibilidade))

# Calcular coeficiente de determinação (R²)
residuos = diferenca_tensao_regiao_linear - np.polyval(regressao_linear, distancia_regiao_linear)
var_residuos = np.var(residuos)
var_total = np.var(diferenca_tensao_regiao_linear)
coef_determinacao = 1 - (var_residuos / var_total)
print("Coeficiente de Determinação (R²): {:.4f}".format(coef_determinacao))

# Plotar a reta ajustada
plt.plot(distancia_regiao_linear, np.polyval(regressao_linear, distancia_regiao_linear), 'r-', label='Reta Ajustada')

# Configurar o gráfico
plt.title('Curva do Sensor LVDT')
plt.xlabel('Valor inserido no conduíte (cm)')
plt.ylabel('Tensão nas bobinas (mV)')
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()
