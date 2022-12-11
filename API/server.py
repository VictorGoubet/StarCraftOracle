from flask import (
    Flask, 
    request, 
    jsonify, 
    Response,
    render_template
    )
from predictor import predict



app = Flask(__name__, template_folder="templates")

#---------------------------------------------------------------------------------------------

@app.route('/API_request', methods=['POST'])
def request_page() -> Response:
    """Catch a post request, do the prediction with
    the given data and return the predicted league

    :return Response: The response containing the prediction
    """
    data = request.get_json() 
    prediction = predict(data)
    return jsonify(prediction)

#---------------------------------------------------------------------------------------------

@app.route('/API_form')
def form_page() -> str:
    """Display the form to predict its league

    :return str: The html template to display
    """
    return render_template("form.html")

#---------------------------------------------------------------------------------------------

@app.route('/API_response_form', methods=['POST'])  
def response_form_page() -> str: 
    """Display the league prediction after filling and validating
    the form
    :return str: The html template of the result page
    """
    # prepare the payload to send for prediction using form data
    data = {'Age': [int(request.form['Age'])],
            'HoursPerWeek': [int(request.form['HoursPerWeek'])],
            'TotalHours': [int(request.form['TotalHours'])],
            'APM': [float(request.form['APM'])],
            'SelectByHotkeys': [float(request.form['SelectByHotkeys'])],
            'AssignToHotkeys': [float(request.form['AssignToHotkeys'])],
            'UniqueHotkeys': [float(request.form['UniqueHotkeys'])],
            'MinimapAttacks': [float(request.form['MinimapAttacks'])],
            'MinimapRightClicks': [float(request.form['MinimapRightClicks'])], 
            'NumberOfPACs': [float(request.form['NumberOfPACs'])],
            'GapBetweenPACs': [float(request.form['GapBetweenPACs'])],
            'ActionLatency': [float(request.form['ActionLatency'])],
            'ActionsInPAC': [float(request.form['ActionsInPAC'])],
            'TotalMapExplored': [float(request.form['TotalMapExplored'])],
            'WorkersMade': [float(request.form['WorkersMade'])],
            'UniqueUnitsMade': [float(request.form['UniqueUnitsMade'])],
            'ComplexUnitsMade': [float(request.form['ComplexUnitsMade'])],
            'ComplexAbilitiesUsed': [float(request.form['ComplexAbilitiesUsed'])]}
    prediction = predict(data)[0]
    return render_template("response.html", response=prediction)      

#---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')