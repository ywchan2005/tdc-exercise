from tdc.single_pred import ADME
import scipy

from metrics.mae import MAE
from metrics.roc_auc import ROC_AUC
from metrics.accuracy import Accuracy

class BenchmarkPipeline:
  def __init__( self, name, metrics ):
    self.data = ADME( name=name )
    # TODO: to have a better way to specify or pick metrics according the nature of the problem
    # TODO: to have an error check for inappropriate pairs of dataset and metrics
    if metrics == 'mae':
      self.metrics = MAE()
    elif metrics == 'roc_auc':
      self.metrics = ROC_AUC()
    else:
      self.metrics = Accuracy()
  
  def evaluate( self, model_class ):
    scores = []
    best_score = 0
    best_model = None
    # perform multiple evaluations on randomly split data to an average performance
    for seed in [ 42, 43, 44, 45, 46 ]:
      # split into training, validation & test dataset
      split_data = self.data.get_split( seed=seed )
      train_data = split_data[ 'train' ]
      valid_data = split_data[ 'valid' ]
      test_data = split_data[ 'test' ]
      # create a model and train
      model = model_class()
      model.train( train_data, valid_data )
      prediction = model.predict( test_data )
      score = self.metrics.evaluate( prediction, test_data.Y )
      # keep the best performing model
      if score > best_score:
        best_model = model
      scores.append( score )
    result = {
      'avg': scipy.stats.tmean( scores ),
      'std': scipy.stats.tstd( scores ),
    }
    return best_model, result

# TODO: some datasets are not supported by the official benchmark code
# class BenchmarkPipeline:
#   def __init__( self, name, metrics ):
#     self.benchmark_group = admet_group()
#     self.benchmark = self.benchmark_group.get( benchmark=name )
  
#   def evaluate( self, model_class ):
#     predictions = []
#     best_score = 0
#     best_model = None
#     for seed in [ 42, 43, 44, 45, 46 ]:
#       train_data, valid_data = self.benchmark_group.get_train_valid_split( seed, self.benchmark[ 'name' ], split_type='scaffold' )
#       test_data = self.benchmark[ 'test' ]
#       model = model_class()
#       model.train( train_data, valid_data )
#       prediction = {
#         self.benchmark[ 'name' ]: model.predict( test_data ),
#       }
#       predictions.append( prediction )
#       score = self.benchmark_group.evaluate( prediction, save_dict=False )[ self.benchmark[ 'name' ] ]
#       if score[ list( score.keys() )[ 0 ] ] > best_score:
#         best_model = model
#     result = self.benchmark_group.evaluate_many( predictions )[ self.benchmark[ 'name' ] ]
#     return best_model, result
