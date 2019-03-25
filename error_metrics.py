# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:06:51 2019

@author: xxzac
"""
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score


def print_reg_error_metrics(predictions, y_test):
    print('MSE, MAE, R^2, EVS: ' +str([mean_squared_error(y_test, predictions),
                                      median_absolute_error(y_test, predictions),
                                      r2_score(y_test, predictions),
                                       explained_variance_score(y_test, predictions)]))