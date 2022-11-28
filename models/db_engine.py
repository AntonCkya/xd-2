from sqlalchemy import create_engine, MetaData

"""
Движок который коннектится к базе данных
"""

engine = create_engine("postgresql+psycopg2://postgres:XD_120403_1000$@localhost/cinema")
engine.connect()

metadata = MetaData()
