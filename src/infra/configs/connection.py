from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandle:
    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:sousa123@localhost:3306/cinema'
        self.__engine = self.__create_database_engine()
        self.session = None
        
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
        
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker() 
        return self
         
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.__engine.dispose()
        return False