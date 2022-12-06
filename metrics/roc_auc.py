import sklearn.metrics

from metrics.base_metrics import BaseMetrics

class ROC_AUC( BaseMetrics ):
  def evaluate( self, pred, true ):
    # TODO: to better handle prediction values on binary problem
    pred = [ x >= .5 for x in pred ]
    return sklearn.metrics.roc_auc_score( true, pred )

