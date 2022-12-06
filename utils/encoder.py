from DeepPurpose import utils

class Encoder:
  @staticmethod
  def encode( data, drug_encoding ):
    return utils.data_process(
      X_drug=data.Drug,
      y=data.Y,
      drug_encoding=drug_encoding,
      split_method='no_split',
    )
