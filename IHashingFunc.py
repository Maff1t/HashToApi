# Interface that must be implemented 
# to create a new hashing function

import abc

class IHashingFunc(metaclass=abc.ABCMeta):
   
   @abc.abstractmethod
   def hashString(self, s):
        pass