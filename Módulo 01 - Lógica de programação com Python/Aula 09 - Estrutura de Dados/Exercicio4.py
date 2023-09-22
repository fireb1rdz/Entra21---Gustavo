"""4. Escreva um algoritmo que receba um texto e retorne um dicionário com a contagem de cada palavra na string.

Entrada:

“aprenda python, Python é divertido.”

Saída:

{"aprenda": 1, "python": 2, "é": 1, "divertido": 1}
"""

texto = ["Aprenda python", "Python é divertido."]
texto_completo = " ".join(texto)
palavras = texto_completo.lower().split()


contagem = {}


for palavra in palavras:
   palavra = palavra.strip('.,!?')


   if palavra in contagem:
       contagem[palavra] += 1
   else:
       contagem[palavra] = 1


print(contagem)
