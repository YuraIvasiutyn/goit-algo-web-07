from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.configuration import postgres


engine = create_engine(f"postgresql://{postgres.user}:{postgres.password}@{postgres.host}:{postgres.port}/postgres", echo=True)

DBSession = sessionmaker(bind=engine)

session = DBSession()


