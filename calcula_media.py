def calculadora():
    while True:
        try:
            expressao = input("Digite a operação matemática (ou 'sair' para encerrar): ")
            if expressao.lower() == 'sair':
                print("Encerrando a calculadora...")
                break
            resultado = eval(expressao)
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")

# if __name__ == "__main__":
#     calculadora()


def crazyDetector():
    verify = input('Digite o nome da pessoa que será verificada: ').capitalize()
    if verify == 'Lisiane':
        print('Eita, a Lisiane é louca sim.')
    else: 
        print('Não há dados suficiente nesta máquina parea analisar está pessoa, recomendo ir à psicólogo...')



apelidos = []

def giveLisiName ():
    apelido = input("Escreva um apelido para a Lisiane: ")
    return apelido


def apelidoGiver():
    while True:
        print("Selecione uma opção:")
        print("1 - Dar apelido.")
        print("2 - Imprimir lista.")
        print("3 - Sair.")
        escolha = input('')

        if escolha == "1":
            newSurname = input("Digite o apelido para Lisiane: ")
            apelidos.append(newSurname)
            input('ENTER')

        elif escolha == "2":
            print(apelidos)
            input('ENTER')
        
        elif escolha == "3":
            break

        else:
            print('Te liga tchê,aperta os botões certos.')
            input('ENTER')

apelidoGiver()