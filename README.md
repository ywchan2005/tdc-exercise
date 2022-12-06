## Datasets
Datasets and associated metrics selected for benchmarking the models
| | Dataset | Metric |
| - | - | - |
| Absorption | Hydration Free Energy, FreeSolv (`HydrationFreeEnergy_FreeSolv`) | MAE |
| Distribution | PPBR (Plasma Protein Binding Rate), AstraZeneca (`PPBR_AZ`) | MAE |
| Metabolism | CYP P450 1A2 Inhibition, Veith et al. (`CYP1A2_Veith`) | Accuracy |
| Excretion | Clearance, AstraZeneca (`Clearance_Microsome_AZ`) | MAE |

## Results
### Summary
- If a single model is picked to predict all four properties, choose the transformer because
  - the tree model is excluded, as we got no result for metabolism dataset; and
  - the transformer has better performance than graph neural network in 3 out of 4 predictions
- If one model is picked for each property, pick the one with the best performance in predicting that property

### Absorption
| Model | Score* |
| - | - |
| Graph Neural Network (`MPNN`) | 12.9798±0.5261 |
| **Transformer** | **12.2864**±0.2462 |
| Tree (`XGBoost`) | 19.6880±0.2900 |
\* the smaller the score the better is the performance of the model

### Distribution
| Model | Score* |
| - | - |
| Graph Neural Network (`MPNN`) | 3.0247±0.1143 |
| Transformer | 2.6273±0.2139 |
| **Tree (`XGBoost`)** | **2.2357**±0.1840 |
\* the smaller the score the better is the performance of the model

### Metabolism
| Model | Score* |
| - | - |
| **Graph Neural Network (`MPNN`)** | **0.7722**±0.0086 |
| Transformer | 0.7391±0.0139 |
| Tree (`XGBoost`) | N/A** |
\* the larger the score the better is the performance of the model
\*\* not enough resource to run the model

### Excretion
| Model | Score* |
| - | - |
| Graph Neural Network (`MPNN`) | 35.6565±2.4137 |
| Transformer | 33.7023±2.2962 |
| **Tree (`XGBoost`)** | **29.8566**±1.2515 |
\* the smaller the score the better is the performance of the model

## Remarks
- model parameters and training configurations are not yet finetuned due to limited computation resources. they should be carefully finetuned
- tree model is trained in the same way in both classification and regression problems. it should be trained with a loss function which better reflects the error in classification problem
- the tree model can be further improved by inputting handcraft features which best fit the problem to be solved
- accuracy and mean absolute error are used in reporting model performance since they are easier to understand and illustrate
- ROC AUC, Spearman correlation and R^2 may be used to identify the best model and model parameters within R&D team or for clients from professional bodies
- if a single performance indicator is needed, a dataset with continuous target value should be picked for metabolism property, so that all four predictions are measured by the same metric
- Solubility, AqSolDB (`Solubility_AqSolDB`) cannot be used, as an error indicating that MAX_ATOM should be increased is thrown
- two-sample Kolmogorov-Smirnov test is used to test whether a training dataset looks like its validation counterpart

## Timeline
- preparation of working environment: 1 hour
- getting familiar with TDC: 2 hours
- data exploration: 1 hour
- coding & refactoring: 1 hours
- result gathering: 1 hour