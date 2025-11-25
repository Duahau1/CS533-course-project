import pandas as pd
from flask import Flask, request, render_template, url_for, jsonify
import pickle
import translate as TranslateService

app= Flask(__name__)
model = pickle.load(open('../random_forest_model.pkl', 'rb'))
CATEGORIES = ['Comics', 'Crafts', 'Dance', 'Design', 'Fashion', 'Film_Video', 'Food',
    'Games', 'Journalism', 'Music', 'Photography', 'Publishing', 'Technology', 'Theater']
_translate = TranslateService.translate()

@app.route('/')
def home():
    return render_template("main.html", categories=CATEGORIES, translate=_translate)

@app.route('/predict' ,methods=['POST'])
def predict():
    campaign_goal_USD = request.form['goal_usd']
    campaign_location_US = request.form['country_US']
    campaign_timeline = request.form['cam_duration']
    prep_timeline = request.form['prep_duration']
    category_value = request.form["category_input"]
    input_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if category_value in CATEGORIES:
        input_list[CATEGORIES.index(category_value)] = 1
    
    category_input = pd.DataFrame([input_list],columns=CATEGORIES,dtype=float)
    input_variables = pd.DataFrame([[campaign_goal_USD, campaign_location_US, campaign_timeline, prep_timeline]], columns=['campaign_goal_USD', 'campaign_location_US', 'campaign_timeline','prep_timeline'], dtype=float)
    normalized_input = pd.concat([input_variables,category_input],axis=1)
    
    result = model.predict(normalized_input)
    
    if int(result)==1:
        prediction = _translate('successProject')
    else:
        prediction = _translate('failureProject')
    
    return render_template("result.html", prediction=prediction, translate=_translate)


if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD']=True
