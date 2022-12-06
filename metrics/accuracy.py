import sklearn.metrics

from metrics.base_metrics import BaseMetrics

class Accuracy( BaseMetrics ):
  def evaluate( self, pred, true ):
    # TODO: to better handle prediction values on binary problem
    pred = [ x >= .5 for x in pred ]
    return sklearn.metrics.accuracy_score( true, pred )
