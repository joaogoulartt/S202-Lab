from database import Database
from teacherCRUD import TeacherCRUD

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.208.73.25:7687", "neo4j", "intercom-drivers-radio")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
teacher_crud = TeacherCRUD(db)

# # Criando o professor
teacher_crud.create('Chris Lima', 1956, '189.052.396-66')

# # Lendo o professor pelo nome
print(teacher_crud.read('Chris Lima'))

# # Atualizando o cpf do professor pelo nome
teacher_crud.update('Chris Lima', '162.052.777-77')

# # Lendo o professor novamente pelo nome
print(teacher_crud.read('Chris Lima'))

# Fechando a conexão
db.close()