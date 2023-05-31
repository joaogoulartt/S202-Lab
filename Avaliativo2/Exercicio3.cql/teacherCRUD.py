class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (p:Teacher {name: $name}) RETURN p.name AS name"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["name"] for result in results]

    def update(self, old_name, new_cpf):
        query = "MATCH (p:Teacher {name: $name}) SET p.cpf = $new_cpf"
        parameters = {"name": old_name, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)

    def delete(self, name):
        query = "MATCH (p:Teacher {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)