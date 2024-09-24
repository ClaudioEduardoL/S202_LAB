from bson.objectid import ObjectId
from classes import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        try:
            perfil = {
                'Nota do motorista': motorista.nota, 
                'Corridas': [
                    {
                
                    'Nota da corrida':corrida.nota, 
                    'Distância':corrida.distancia, 
                    'Valor':corrida.valor, 
                    'Passageiro': {
                        'Nome':corrida.passageiro.nome, 
                        'Documento':corrida.passageiro.documento
                    }

                    } for corrida in motorista.corridas
                ]
            }

            res = self.db.collection.insert_one(perfil)

            print(f"ID do Motorista: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            perfil = self.db.collection.find_one({"_id": ObjectId(id)})
            nota = perfil['Nota do motorista']
            corrida = perfil['Corridas']
            print(f"Motorista found: {perfil}")
            return Motorista(nota,corrida)
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, id, motorista):
        try:
            perfil = {
                'Nota do motorista': motorista.nota, 
                'Corridas': [{
                
                    'Nota da corrida':corrida.nota, 
                    'Distância':corrida.distancia, 
                    'Valor':corrida.valor, 
                    'Passageiro': {
                        'Nome':corrida.passageiro.nome, 
                        'Documento':corrida.passageiro.documento
                    }

                }for corrida in motorista.corridas
            ]
            }
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": perfil})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documentos(s) deletados")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None