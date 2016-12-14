#!/usr/bin/env python
"""
| Src: https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/base.py
| License: BSD 3-Clause https://github.com/scikit-learn/scikit-learn/blob/master/COPYING
"""

import csv
import numpy as np
from os.path import join, dirname
from sklean.datasets import Bunch


def load_house_prices(return_X_y=False, data_file='train.csv'):
    """Load and return the house_prices house-prices dataset (regression).
    ==============     ==============
    Samples total                 506
    Dimensionality                 13
    Features           real, positive
    Targets             real 5. - 50.
    ==============     ==============
    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.
        .. versionadded:: 0.18
    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn, 'target', the regression targets,
        and 'DESCR', the full description of the dataset.
    (data, target) : tuple if ``return_X_y`` is True
        .. versionadded:: 0.18
    Examples
    --------
    >>> from sklearn.datasets import load_house_prices
    >>> house_prices = load_house_prices()
    >>> print(house_prices.data.shape)
    (506, 13)
    """
    module_path = dirname(__file__)

    fdescr_name = join(module_path, 'data', 'data_description.txt')
    with open(fdescr_name) as f:
        descr_text = f.read()

    data_file_name = join(module_path, 'data', data_file)
    with open(data_file_name) as f:
        data_file = csv.reader(f)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,))
        temp = next(data_file)  # names of features
        feature_names = np.array(temp)

        for i, d in enumerate(data_file):
            data[i] = np.asarray(d[:-1], dtype=np.float64)
            target[i] = np.asarray(d[-1], dtype=np.float64)

    if return_X_y:
        return data, target

    return Bunch(data=data,
                 target=target,
                 # last column is target value
                 feature_names=feature_names[:-1],
                 DESCR=descr_text)