# Operational_Research
Este é um repositório com métodos numéricos simples para iniciantes em programação Python e Pesquisa Operacional. <br>
Utilizam-se os pacotes GEKKO e GUROBI.<br>

## Método Numérico para Programação Linear:<br>

Dado o problema de Programação Linear:<br>

![Programação_Linear](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Programação_Linear.png).<br>

Executa-se código **Programação_Linear**.<br> 
Através do Método **Simplex** para obtém-se uma solução contínua.<br><br>

Exemplo:<br>

Minimizar Z = 8x1 + 5x2 <br>

Sujeito a:<br>
    -3x1 + 2x2 <= 30 <br>
     2x1 +  x2 >= 50 <br>
      x1 +  x2 <= 30 <br>

Tem como solução:<br>

(x1): 25.0 <br>
(x2): 0.0  <br>
Z(x1,x2): 200.0 <br>

## Método Numérico para Programação Linear Inteira:<br>

Dado o problema de Programação Linear Inteira:<br>

![Programação_Linear_Inteira](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Programação_Linear_Inteira.png).<br>

Executa-se código **Programação_Linear_Inteira**.<br> 
Através do Método **Branch and Bound** para obtém-se uma solução inteira.<br><br>

Exemplo:<br>

Maximizar Z = 5x1 + x2 <br>

Sujeito a:<br>
      -x1 + 2x2 <= 4 <br>
       x1 -  x2 <= 1 <br>
      4x1 +  x2 <= 12 <br>

Tem como solução:<br>

(x1): 2.0 <br>
(x2): 3.0  <br>
Z(x1,x2): 13.0 <br>


## Método Numérico para Programação Linear Inteira Binária:<br>

Dado o problema de Programação Linear Inteira Binária:<br>

![Programação_Linear_Inteira_Binária](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Programação_Linear_Inteira_Binária.png).<br>

Executa-se código **Programação_Linear_Inteira_Binária**.<br> 
Através do Método **Branch and Bound** para obtém-se uma solução inteira pertencente ao conjunto **S = {0,1}**.<br><br>

Exemplo:<br>

Maximizar Z = 2x1 - x2 + 5x3 - 3x4 + 4x5 <br>

Sujeito a:<br>
      3x1 - 2x2 + 7x3 - 5x4 + 4x5 <= 6 <br>
       x1 - x2 + 2x3 - 4x4 +2x5 <= 0 <br>

Tem como solução: <br>

(x1): 0.0 <br>
(x2): 0.0 <br>
(x3): 1.0 <br>
(x4): 1.0 <br>
(x5): 1.0 <br>
Z(x1,x2,x3,x4,x5): 6.0 <br>















