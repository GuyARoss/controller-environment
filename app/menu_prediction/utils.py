from typing import List

def average_prediction(predictions: List[str], limit: int = 5) -> str:
    '''
    average_prediction finds the average prediction out of n (limit) predictions
    '''
    n_predictions = predictions[len(predictions) - limit:len(predictions)]

    counted_predictions = {}
    best_prediction = (None, -1)

    for prediction in predictions:
        if prediction not in counted_predictions:
            counted_predictions[prediction] = 0
        else:
            counted_predictions[prediction] += 1
        
        if counted_predictions[prediction] >= best_prediction[1]:
            best_prediction = (prediction, counted_predictions[prediction])

    return best_prediction[0]
    