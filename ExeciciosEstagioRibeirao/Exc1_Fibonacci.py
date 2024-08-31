#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def funPertenceFibonacci(numero):
    if numero < 0:
        return "Por favor, insira um número inteiro positivo."
    
    num1, num2 = 0, 1

    if numero == num1 or numero == num2:
        return "Esse número pertence à sequência de Fibonacci."
    
    while num2 < numero:
        num1, num2 = num2, num1 + num2
        if num2 == numero:
            return "Esse número pertence à sequência de Fibonacci."
    
    return "Esse número não pertence à sequência de Fibonacci."

def main():
        numero = int(input("Informe o número a ser analisado: "))
        resul = funPertenceFibonacci(numero)
        print(resul)
  

if __name__ == "__main__":
    main()