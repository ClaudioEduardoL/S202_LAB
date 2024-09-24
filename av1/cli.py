from classes import Motorista, Passageiro, Corrida

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = []
        controle = 1
        while(controle == 1):
            nome = input("Nome do passageiro: ")
            documento = input("Documento do passageiro: ")
            passageiro = Passageiro(nome,documento)

            notaCorrida = int(input("Nota da corrida: "))
            distancia = float(input("Distância da corrida: "))
            valor = float(input("Valor da corrida: "))
            corrida = Corrida(notaCorrida,distancia,valor,passageiro)
            corridas.append(corrida)

            controle = int(input("Continuar adicionando corridas?   1- Sim  0- Não: "))
        
        notaMotorista = int(input("Nota do motorista: "))
        motorista = Motorista(notaMotorista,corridas)
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Entre com o ID: ")
        self.motorista_model.read_motorista_by_id(id)
        

    def update_motorista(self):
        id = input("Entre com o ID: ")
        
        controle = 1
        corridas = []
        
        while(controle == 1):
            nome = input("Nome do passageiro: ")
            documento = input("Documento do passageiro: ")
            passageiro = Passageiro(nome,documento)

            notaCorrida = int(input("Nota da corrida: "))
            distancia = float(input("Distância da corrida: "))
            valor = float(input("Valor da corrida: "))
            corrida = Corrida(notaCorrida,distancia,valor,passageiro)
            corridas.append(corrida)

            controle = int(input("Continuar adicionando corridas?   1- Sim  0- Não: "))
        
        notaMotorista = int(input("Nota do motorista: "))
        motorista = Motorista(notaMotorista,corridas)
        self.motorista_model.update_motorista(id, motorista)
        

    def delete_motorista(self):
        id = input("Entre com o ID: ")
        self.motorista_model.delete_motorista(id)
        
    
    def run(self):
        print("Welcome to the Motoristas CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()