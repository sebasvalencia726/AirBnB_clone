#!/usr/bin/python3
"""BaseModel module
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel constructor.
    """
    def __init__(self, *args, **kwargs):
        """Init method.

        Args:
            kwargs:
            id: (string) - assign with an uuid when an instance is created:
            you can use uuid.uuid4() to generate unique id but don’t forget
            to convert to a string. The goal is to have unique id for each
            BaseModel.
            created_at: (datetime) - assign with the current datetime when an
            instance is created.
            updated_at: (datetime) - assign with the current datetime when an
            instance is created and it will be updated every time you change
            your object.

        """
        format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, format)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, format)
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """repr method.

        Args:
            None

        """
        representation = "[%s] (%s) %s" % (self.__class__.__name__,
                                           self.id,
                                           self.__dict__)
        return(representation)

    def save(self):
        """ Public method that updates the public instance
        attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance:

        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with the class name
        of the object.
        created_at and updated_at must be converted to string object in ISO
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259).
        This method is the first piece of the serialization/deserialization
        process: create a dictionary representation with “simple object type”
        of the BaseModel.

        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return (new_dict)
