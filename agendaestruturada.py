lista = []

def createContacts():
    stop = 0
    print(25*"-","Criar Contato",25*"-")
    name = input("\nDigite seu nome: ")
    number = int(input("Digite seu número: "))
    contacts = {"name": name, "number": number}
    lista.append(contacts)
    print(" \n Contato criado!.\n \n (1) - Voltar \n (2) - Criar Contato")
    while stop != '':
        voltar = int(input(":"))
        match voltar:
            case 1:
                loop()
                break
            case 2:
                createContacts()
                break
    return contacts

def listContacts():
    i=0
    stop = 0
    print(25*"-","CONTATOS",25*"-")
    printContacts()
    print("\n (1) - Voltar \n (2) - Criar Contato")
    while stop != 1:
        voltar = int(input(":"))
        match voltar:
            case 1:
                if voltar == 1:
                    loop()
                    stop = 1
                break
            case 2:
                createContacts()
                break

def printContacts():
    for i in range(len(lista)):
        temporary = lista[i]
        name = temporary.get("name")
        number = temporary.get("number")
        print(f"{i+1}°\nContato: {name}\n Número: {number}\n",25*"-")
        i+=1            

def removeContacts(lista):
    print(25*"-","Remover Contato",25*"-")
    printContacts()
    remove = int(input("Digite a posição que você deseja remover: "))
    remove = remove - 1
    temporary = lista[remove]
    name = temporary.get("name")
    number = temporary.get("number")
    del lista[remove]
    print(25*"-",f"\n {remove+1}°\n\n Contato: {name}\n Número: {number}\n foi Removido PERMANENTEMENTE!.\n",25*"-")
    loop()

def editContacts():
    stop = 0
    print(25*"-","Editar Contato",25*"-")
    printContacts()
    while stop != '':
        edit = int(input("Qual posição você deseja remover: "))
        if edit != len(lista):
            print("Essa posição não existe!.")
        else:
            edit = edit - 1
            editing = lista[edit]
            break
    while stop != '':
        what = int(input("O que você deseja editar neste contato: \n\n (1) - Nome \n (2) - Número:  \n (3) - Voltar \n:"))
        match what:
            case 1:
                newName = input("Digite o novo nome: ")
                editing["name"] = newName
            case 2:
                newNumber = input("Digite o novo número: ")
                editing["number"] = newNumber
            case 3:
                print("Voltando")
                break
    loop()

def loop():
    stop = 0
    while stop != '':
        print(25*"-","AGENDA",25*"-","\n\n (1) - Criar Contato \n (2) - Listar Contato \n (3) - Remover Contato \n (4) - Editar Contato \n (5) - Parar\n\n",25*"-","AGENDA",25*"-")
        parar = int(input(":"))
        match parar:
            case 1:
                createContacts()
                break
            case 2:
                listContacts()
                break
            case 3:
                removeContacts(lista)
                break
            case 4:
                editContacts()
                break
            case 5:
                print("Código parando...")
                break
loop()