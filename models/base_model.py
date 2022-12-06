from abc import ABC, abstractmethod

class BaseModel( ABC ):
  @abstractmethod
  def train( self, train_data, valid_data ):
    pass

  @abstractmethod
  def predict( self, data ):
    pass
