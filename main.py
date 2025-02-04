from persistencia import Persistencia
from prato import Prato

def main():
    persistencia = Persistencia()

    pratos = [
        Prato(1, "Bacalhau à Brás", "Bacalhau desfiado com batata, cebola e ovos", 25.00),
        Prato(2, "Caldo Verde", "Sopa de couve e batata com linguiça", 15.00),
        Prato(3, "Arroz de Pato", "Arroz com pato, cebola e especiarias", 22.00),
        Prato(4, "Feijoada à Transmontana", "Feijoada com carne de porco e especiarias", 28.00),
        Prato(5, "Cataplana de Peixe", "Peixe cozido em cataplana com especiarias", 30.00),
        Prato(6, "Leitão à Bairrada", "Leitão assado com batata e especiarias", 35.00),
    ]

    for prato in pratos:
        persistencia.gravar_prato(prato)

    while True:
        print("\n2. Listar Pratos")
        print("5. Sair")
        opcao = input("Escolher uma opcao: ")

        if opcao == "2":
            pratos = persistencia.ler_pratos()
            for prato in pratos:
                print(prato)
        elif opcao == "5":
            break

if __name__ == "__main__":
    main()
