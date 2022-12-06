from benchmark_pipeline import BenchmarkPipeline
from models.graph_neural_network import GraphNeuralNetwork
from models.transformer import Transformer
from models.tree_model import TreeModel

pipeline = BenchmarkPipeline( name='CYP1A2_Veith', metrics='accuracy' )

model, result = pipeline.evaluate( GraphNeuralNetwork )
print( '=' * 20, 'Graph Neural Network', '=' * 20 )
print( result )

model, result = pipeline.evaluate( Transformer )
print( '=' * 20, 'Transformer', '=' * 20 )
print( result )

model, result = pipeline.evaluate( TreeModel )
print( '=' * 20, 'Tree Model', '=' * 20 )
print( result )