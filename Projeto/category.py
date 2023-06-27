class Category:
    def __init__(self, db):
        self.db = db

    def create(self, name, description):
        query = """
        CREATE (c:Category {name: $name, description: $description})
        RETURN c
        """
        parameters = {"name": name, "description": description}
        return self.db.execute_query(query, parameters)

    def get_all(self):
        query = """
        MATCH (c:Category)
        RETURN c.name
        """

        return self.db.execute_query(query)

    def get_by_name(self, name):
        query = """
        MATCH (c:Category {name: $name})
        RETURN c
        """
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        if result:
            return result[0]["c"]
        else:
            return None

    def update(self, name, description=None):
        query = """
        MATCH (c:Category {name: $name})
        SET c.description = coalesce($description, c.description)
        RETURN c
        """
        parameters = {
            "name": name,
            "description": description,
        }
        return self.db.execute_query(query, parameters)

    def delete(self, name):
        query = """
        MATCH (c:Category {name: $name})
        OPTIONAL MATCH (p)-[r]-(c)
        DELETE p,r,c
        """
        parameters = {
            'name':name
        }
        return self.db.execute_query(query, parameters)
