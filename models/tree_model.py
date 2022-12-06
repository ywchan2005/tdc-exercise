import xgboost
import pandas as pd
import torch

from models.base_model import BaseModel
from utils.encoder import Encoder

class TreeModel( BaseModel ):
  def __init__( self ):
    # TODO: use cherrypicked handcraft features
    # use same encoding as graph neural network
    self.drug_encoding = 'MPNN'
    self.model = xgboost.XGBRegressor(
        n_estimators=5,
        max_depth=3,
        max_leaves=3,
    )
  
  def encode( self, data ):
    # flatten all features for each entity
    return pd.DataFrame( data.drug_encoding.apply( lambda x: torch.cat( [
      i.reshape( -1 ) for i in x
    ] ).numpy() ).tolist() )
  
  def train( self, train_data, valid_data ):
    train_data = Encoder.encode( train_data, self.drug_encoding )
    train_x = self.encode( train_data )
    self.model.fit( train_x, train_data.Label )
    
  def predict( self, data ):
    data = Encoder.encode( data, self.drug_encoding )
    x = self.encode( data )
    return self.model.predict( x )
