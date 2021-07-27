# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:14:52 2019
@author: engoliveira

"""

# Solver de Programação Linear Inteira

"""
 Maximizar Z = 5x1 + x2

 Sujeito a

		-x1 + 2x2 <= 4
		 x1 - x2 <= 1
		4x1 + x2 <= 12

"""

from gekko import GEKKO

# Cria Modelo
Modelo = GEKKO()
Modelo.solver_options = ['minlp_branch_method 2']
Modelo.options.SOLVER = 1

# Cria Variávreis
x1 = Modelo.Var(lb = 0, integer = True)
x2 = Modelo.Var(lb = 0, integer = True)

# Seta o Tipo de Modelo
Modelo.Maximize(5*x1 + x2)

# Cria Restrições
Modelo.Equation(-x1 + 2*x2 <= 4)
Modelo.Equation(x1 - x2 <= 1)
Modelo.Equation(4*x1 + x2 <= 12)

# Soluciona o Modelo
Modelo.solve(disp = False)

# Imprime Valor das Variaveis
print("(x1): " + str(x1.value[0]))
print("(x2): " + str(x2.value[0]))
print("Z(x1,x2): " + str(5*x1.value[0] + x2.value[0]))
