class SerializableMixin:
    '''Super Class which allows a serializable form from a SQLAlchemy model'''
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
