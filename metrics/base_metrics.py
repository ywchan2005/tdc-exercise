from abc import ABC, abstractmethod

class BaseMetrics( ABC ):
  @abstractmethod
  def evaluate( self, pred, true ):
    pass
