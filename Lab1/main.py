import vis
from prediction_model import PredictionModel

name = 'age_data.xls'
fem_sheet = 'f; 1950-2005, estimates'
male_sheet = 'm; 1950-2005, estimates'
both_sheet = 'both; 1950-2005, estimates'

model = PredictionModel(name, fem_sheet, male_sheet, both_sheet)


def print_available_years(data):
    print(", ".join([str(i) for i in data["date"].tolist()]))
    return


type = 'both'
# prediction = model.pred_model_5_years(100, type)
# vis.show_profile(prediction, 2050, type, '2050 profile for '+type)
# vis.profile_compare_years(prediction, [2010, 2020, 2030], type, 'prediction for ' + str([2010, 2020, 2030])+ ' ' + type)

prediction = model.pred_model_1_year_with_fertility(118, 0, type)
# vis.show_profile(prediction, 3000, type, '1 year model 3000 profile for '+type)
# vis.profile_compare_years(prediction, [3000, 4000, 5000], type, '1 year model prediction for ' + str([3000, 4000, 5000])+ ' ' + type)
# print(prediction[prediction['date'] == 2050])
given = model.extract_given_prediction(type)
vis.compare_profiles(prediction, given, 2045, 'prediction_comp_2045')
