import typing
import numpy as np
import pickle as p
import pandas as pd

MODEL_PATH = './model.pickle'
LEAGUES = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 
           'Master', 'GrandMaster', 'Professional leagues']
           
def preprocessing(data:dict) -> np.array:
    """Apply a simple preprocessing on data
    before sending them to prediction

    :param dict data: A dictionnary containing the features used for prediction
    :return np.array: The processed features
    """
    data = pd.DataFrame.from_dict(data)
    # Drop data
    data.drop(['Age',
               'HoursPerWeek',
               'MinimapRightClicks',
               'ComplexUnitsMade',
               'UniqueUnitsMade'], axis=1, inplace=True)
    # Add log columns
    for column in ['APM', 'TotalHours', 'ActionLatency', 'TotalMapExplored']:
        data['log({})'.format(column)] = np.log(data[column])

    return data.to_numpy()



def predict(data:dict) -> typing.List[str]:
    """preprocess and launch the prediction of the league using
    given features

    :param dict data: A dictionnary containing the features used for prediction
    :return typing.List[str]: The predicted league for each input
    """
    model = p.load(open(MODEL_PATH, 'rb'))
    data = preprocessing(data)
    preds = model.predict(data)
    preds = [LEAGUES[x - 1] for x in preds]
    return preds
