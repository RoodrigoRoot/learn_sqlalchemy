import orm
from models import Products

def execute():
    pass

if __name__ == "__main__":
    orm.Base.metadata.create_all(orm.engine)
