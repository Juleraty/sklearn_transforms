from setuptools import setup
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np

iris  =  load_iris ()

X  =  íris . dados
y  =  íris . alvo 


y_names  =  iris . target_names


test_ids  =  np . aleatório . permutação ( len ( X ))



X_train  =  X [ test_ids [: - 100 ]]
X_test  =  X [ test_ids [ - 100 :]]

y_train  =  y [ test_ids [: - 100 ]]
y_test  =  y [ test_ids [ - 100 :]]

setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/vnderlev/sklearn_transforms/',
      author='Vanderlei Munhoz',
      author_email='vnderlev@protonmail.ch',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms'
      ],
      zip_safe=False
)
