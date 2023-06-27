class Product:
    def __init__(self, db):
        self.db = db

    def create(self, category_name, name, description, quantity):
        query = """
        MATCH (c:Category {name: $category_name})
        CREATE (p:Product {name: $name, description: $description, quantity: $quantity})
        CREATE (c)-[:HAS]->(p)
        RETURN p
        """
        parameters = {
            "category_name": category_name,
            "name": name,
            "description": description,
            "quantity": quantity
        }
        return self.db.execute_query(query, parameters)

    def get_all(self):
        query = """
        MATCH (p:Product)
        RETURN p.name
        """
        return self.db.execute_query(query)
    
    def get_by_name(self, name):
        query = """
        MATCH (p:Product {name: $name})
        RETURN p
        """
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

    def update(self, name, description=None, quantity=None):
        query = """
        MATCH (p:Product {name: $name})
        SET p.description = coalesce($description, p.description),
            p.quantity = coalesce($quantity, p.quantity)
        RETURN p
        """
        parameters = {"name": name, "description": description, "quantity": quantity}
        return self.db.execute_query(query, parameters)

    def delete(self, name):
        query = """
        MATCH (p:Product {name: $name})
        OPTIONAL MATCH (p)-[r]-()
        DELETE r, p
        """
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

    def get_products_by_category(self, category_name):
        query = """
        MATCH (c:Category {name: $category_name})-[:HAS]->(p:Product)
        RETURN p.name
        """
        parameters = {"category_name": category_name}
        return self.db.execute_query(query, parameters)
