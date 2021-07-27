# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:14:52 2019
@author: engoliveira

"""

# Solver de Programação Linear Inteira Binária

"""
 Maximizar Z = 2x1 - x2 + 5x3 - 3x4 + 4x5

 Sujeito a

		3x1 - 2x2 + 7x3 - 5x4 + 4x5 <= 6
		 x1 - x2 + 2x3 - 4x4 +2x5 <= 0

"""

from gekko import GEKKO

# Cria Modelo
Modelo = GEKKO()
Modelo.solver_options = ['minlp_branch_method 2']
Modelo.options.SOLVER = 1

# Cria Variávreis
x1 = Modelo.Var(lb = 0, ub = 1, integer = True)
x2 = Modelo.Var(lb = 0, ub = 1, integer = True)
x3 = Modelo.Var(lb = 0, ub = 1, integer = True)
x4 = Modelo.Var(lb = 0, ub = 1, integer = True)
x5 = Modelo.Var(lb = 0, ub = 1, integer = True)

# Seta o Tipo de Modelo
Modelo.Maximize(2*x1 - x2 + 5*x3 - 3*x4 + 4*x5)

# Cria Restrições
Modelo.Equation(3*x1 - 2*x2 + 7*x3 - 5*x4 + 4*x5 <= 6)
Modelo.Equation(x1 - x2 + 2*x3 - 4*x4 +2*x5 <= 0)


# Soluciona o Modelo
Modelo.solve(disp = False)

# Imprime Valor das Variaveis
print("(x1): " + str(x1.value[0]))
print("(x2): " + str(x2.value[0]))
print("(x3): " + str(x3.value[0]))
print("(x4): " + str(x4.value[0]))
print("(x5): " + str(x5.value[0]))
print("Z(x1,x2,x3,x4,x5): " + str(2*x1.value[0] - x2.value[0] + 5*x3.value[0] - 3*x4.value[0] + 4*x5.value[0]))
