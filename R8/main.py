from database import Database
from game_database import GameDatabase

# Conecta ao banco de dados Neo4j
db = Database("bolt://3.235.168.48:7687", "neo4j", "badge-aid-strips")

# Instancia o manipulador de dados do jogo
game_db = GameDatabase(db)

# Cria alguns jogadores
game_db.create_player("Julia")
game_db.create_player("Bruno")
game_db.create_player("Pedro")

# Recupera e exibe a lista de jogadores
print("Jogadores:", game_db.get_players())

# Cria uma partida com dois jogadores e registra o resultado
game_db.create_match("match1", ["Julia", "Bruno"])
game_db.add_match_result("match1", "Julia venceu")

# Exibe informações da partida
print("Partida 1:", game_db.get_match("match1"))

# Registra outra partida com três jogadores
game_db.create_match("match2", ["Julia", "Pedro", "Bruno"])
game_db.add_match_result("match2", "Pedro venceu")

# Exibe o histórico de partidas de Alice
print("Partidas de Julia:", game_db.get_player_matches("Julia"))

# Exclui um jogador e uma partida
game_db.delete_player("Pedro")
game_db.delete_match("match1")

# Exibe a lista atualizada de jogadores e partidas
print("Jogadores:", game_db.get_players())

# Fecha a conexão com o banco de dados
db.close()
