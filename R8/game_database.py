class GameDatabase:
    def __init__(self, database):
        self.db = database

    # Cria um jogador
    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    # Atualiza o nome de um jogador
    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    # Exclui um jogador e todas as suas conexões
    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    # Recupera todos os jogadores
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    # Cria uma partida e registra os jogadores participantes
    def create_match(self, match_id, players):
        query = (
            "CREATE (m:Match {id: $match_id}) "
            "WITH m UNWIND $players AS player_name "
            "MATCH (p:Player {name: player_name}) "
            "CREATE (p)-[:PARTICIPATES_IN]->(m)"
        )
        parameters = {"match_id": match_id, "players": players}
        self.db.execute_query(query, parameters)

    # Adiciona o resultado de uma partida (vencedor ou pontuações)
    def add_match_result(self, match_id, result):
        query = "MATCH (m:Match {id: $match_id}) SET m.result = $result"
        parameters = {"match_id": match_id, "result": result}
        self.db.execute_query(query, parameters)

    # Exclui uma partida pelo ID
    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    # Recupera informações de uma partida específica
    def get_match(self, match_id):
        query = (
            "MATCH (m:Match {id: $match_id})<-[:PARTICIPATES_IN]-(p:Player) "
            "RETURN m.id AS match_id, m.result AS result, collect(p.name) AS players"
        )
        parameters = {"match_id": match_id}
        result = self.db.execute_query(query, parameters)[0]
        return {
            "match_id": result["match_id"],
            "result": result.get("result", None),
            "players": result["players"],
        }

    # Recupera todas as partidas de um jogador
    def get_player_matches(self, player_name):
        query = (
            "MATCH (p:Player {name: $player_name})-[:PARTICIPATES_IN]->(m:Match) "
            "RETURN m.id AS match_id, m.result AS result"
        )
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [
            {"match_id": result["match_id"], "result": result.get("result", None)}
            for result in results
        ]
