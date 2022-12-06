import sklearn.metrics

from metrics.base_metrics import BaseMetrics

class MAE( BaseMetrics ):
  def evaluate( self, pred, true ):
    return sklearn.metrics.mean_absolute_error( true, pred )
