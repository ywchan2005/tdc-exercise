from DeepPurpose import utils, CompoundPred

from models.base_model import BaseModel
from utils.encoder import Encoder

class GraphNeuralNetwork( BaseModel ):
  def __init__( self ):
    self.drug_encoding = 'MPNN'
    self.model = CompoundPred.model_initialize( **utils.generate_config(
      drug_encoding=self.drug_encoding,
      train_epoch=5,
      LR=.001,
      batch_size=128,
      mpnn_hidden_size=32,
      mpnn_depth=2,
    ) )

  def train( self, train_data, valid_data ):
    train_data = Encoder.encode( train_data, self.drug_encoding )
    valid_data = Encoder.encode( valid_data, self.drug_encoding )
    self.model.train( train_data, valid_data, verbose=False )
  
  def predict( self, data ):
    data = Encoder.encode( data, self.drug_encoding )
    return self.model.predict( data )
