# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:14:52 2019
@author: engoliveira

"""

# Solver de Programação Linear

"""
 Minimizar Z = 8x1 + 5x2

 Sujeito a

		-3x1 + 2x2 <= 30
		2x1 + x2 >= 50
		x1 + x2 <= 30

"""

from gekko import GEKKO

# Cria Modelo
Modelo = GEKKO()

# Cria Variávreis
x1 = Modelo.Var(lb = 0, integer = False)
x2 = Modelo.Var(lb = 0, integer = False)

# Seta o Tipo de Modelo
Modelo.Minimize(8*x1 + 5*x2)

# Cria Restrições
Modelo.Equation(-3*x1 + 2*x2 <= 30)
Modelo.Equation(2*x1 + x2 >= 50)
Modelo.Equation(x1 + x2 <= 30)

# Soluciona o Modelo
Modelo.solve(disp = False)

# Imprime Valor das Variaveis
print("(x1): " + str(x1.value[0]))
print("(x2): " + str(x2.value[0]))
print("Z(x1,x2): " + str(8*x1.value[0] + 5*x2.value[0]))
