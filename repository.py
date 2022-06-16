import abc
import model
import os , pickle

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Batch).all()

class PickleRepository(AbstractRepository):
    #  Complete the definition of this class
    def __init__(self, path = None): 
        pass

    def add(self, batch):
        pass

    def get(self, reference):
        pass

    def list(self):
        pass
