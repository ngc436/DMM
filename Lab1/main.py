import pandas as pd
import numpy as np
from prediction_model import PredictionModel
import vis

name = 'age_data.xls'
fem_sheet = 'f; 1950-2005, estimates'
male_sheet = 'm; 1950-2005, estimates'
both_sheet = 'both; 1950-2005, estimates'

model = PredictionModel(name, fem_sheet, male_sheet, both_sheet)

def print_available_years(data):

    print(", ".join([str(i) for i in data["date"].tolist()]))
    return

type = 'both'
#prediction = model.pred_model_5_years(100, type)
#vis.show_profile(prediction, 2050, type, '2050 profile for '+type)
#vis.profile_compare_years(prediction, [2010, 2020, 2030], type, 'prediction for ' + str([2010, 2020, 2030])+ ' ' + type)

prediction = model.pred_model_1_year(20, type)
#vis.show_profile(prediction, 2018, type, '1 year model 2018 profile for '+type)
vis.profile_compare_years(prediction, [2010, 2018, 2024], type, '1 year model prediction for ' + str([2010, 2018, 2024])+ ' ' + type)
print(prediction)