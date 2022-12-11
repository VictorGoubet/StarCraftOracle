import json
import typing
import requests

def predict_league(data:dict) -> typing.List[str]:
    """Predict league using REST API

    :param dict data: Dictionnary containing features for predictions
    :return typing.List[str]: List of predicted league for each input
    """
    url = 'http://localhost:5000/API_request'
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=data, headers=headers).json()
    return r



if __name__ == '__main__':
    # Example of sended data (here 2 rows)
    data = {'Age':[21, 56],
            'HoursPerWeek': [256, 6],
            'TotalHours': [15, 2],
            'APM': [54 ,23.5],
            'SelectByHotkeys': [85.3, 0.3],
            'AssignToHotkeys': [85.3, 1],
            'UniqueHotkeys': [1, 3],
            'MinimapAttacks': [7, 6],
            'MinimapRightClicks': [85 ,33], 
            'NumberOfPACs': [7, 3],
            'GapBetweenPACs': [1, 1],
            'ActionLatency': [5, 0.2],
            'ActionsInPAC': [0.9, 6],
            'TotalMapExplored': [7, 9],
            'WorkersMade': [3, 6],
            'UniqueUnitsMade': [152, 363],
            'ComplexUnitsMade': [59, 62],
            'ComplexAbilitiesUsed': [5, 6]}
    response = predict_league(data)
    for i, pred in enumerate(response):
        print(f'Prediction {i+1}: {pred}')


