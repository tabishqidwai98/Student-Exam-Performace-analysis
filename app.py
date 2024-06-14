import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
from dash import Dash, html, dcc, callback, Output, Input, dash_table, ctx
import joblib

df = pd.read_csv("data/student_exam_data.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__,external_stylesheets=external_stylesheets)

#app = Dash(__name__)

app.layout = html.Div(children=[html.Div(children=[
    html.H1(children= 'Student Result Prediction', style = {'textAlign' : 'center', 'color' : '#355BF5','padding-top':'30px','padding-bottom':'25px', 'font-family' : 'Segoe Print'}),

    html.Div(children=[
        html.H3(children = 'Dataset', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        dash_table.DataTable(data=df.to_dict('records'), page_size=10),
        #html.Hr(style={'border-color': '#599F68'})

        ], style = {'background-color':'white'}),

    html.Div(children=[
        html.H3(children = 'Graphs', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        html.H4(children = 'Bar Graph', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        dcc.Graph(figure= px.histogram(df, x = 'Pass/Fail', color='Pass/Fail', barmode="group")),
        #dcc.Graph(figure= px.histogram(df, y = 'Previous Exam Score', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='count')),
        html.H4(children='Histogram plot', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        html.H5(children = 'Previous Exam score and Pass/Fail (avg)', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        dcc.Graph(figure= px.histogram(df, y = 'Previous Exam Score', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='avg')),
        html.H5(children = 'Previous Exam score and Pass/Fail (sum)', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        dcc.Graph(figure= px.histogram(df, y = 'Previous Exam Score', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='sum')),
        html.H5(children = 'Study Hours and Pass/Fail (avg)', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        dcc.Graph(figure= px.histogram(df, y = 'Study Hours', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='avg')),
        html.H5(children = 'Study Hours and Pass/Fail (sum)', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        dcc.Graph(figure= px.histogram(df, y = 'Study Hours', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='sum')),
        html.H5(children = 'Scatter Plot : Study hours and Previous Exam Score', style = {'textAlign' : 'left', 'color' : 'black', 'font-family' : 'Comic Sans MS'}),
        dcc.Graph(figure= px.scatter(data_frame=df, y = 'Previous Exam Score', x = 'Study Hours', color = 'Pass/Fail')),
        dcc.Graph(figure= px.scatter(data_frame=df, y = 'Previous Exam Score', x = 'Study Hours', trendline = 'ols')),
        html.P()

        ],), #style = {'background-color':'green'}),

    html.Div(children=[
        html.H3(children = 'Predicton', style = {'color' : '#F17D08'}),
        dcc.Input(id="Studyhours", type="number", placeholder="Study Hours", style={'margin-bottom':'10px'}),
        html.Br(),
        dcc.Input(id="PreviousExamScore", type="number", placeholder="Previous Exam Score",   style={'margin-bottom':'10px'}),
        html.P(children='0 : Fail, 1: Pass', style={'border':'1px soild #09BFC9', 
                                                    'border-radius': '5px','background-color':'#add8e6', 
                                                    'padding-left' : '10px','margin-bottom':'10px'}),
        html.Button('Predict', id = 'btn-nclicks-1', n_clicks=0, style={'color': 'white','border-color':'#154734',
                                                                        'background-color' : '#355BF5','margin-bottom':'10px'}),
        html.Div(id="number-out",style={'border':'1px','border-color':'#154734',
                                        'background-color':'#599F68',
                                        'border-radius': '5px', 'padding-left' : '10px', 
                                        'color': 'white', 'margin-bottom':'10px' }),
        ], style={"background-color":"#4B4B4B", "padding":"10px", 'border-radius':'3px', 'padding-bottom' : '10px'}),

    ], style = {'width' : '700px', 'margin' : 'auto', 'background-color': 'white'})],

    style = {'background-color' : 'white'}
    )

@callback(
    Output("number-out", "children"),
    Input("Studyhours", "value"),
    Input("PreviousExamScore", "value"),
    Input('btn-nclicks-1', 'n_clicks'),
)

def update_graph(Studyhours, PreviousExamScore, btn1):
    #return "Study Hours : {}, PreviousExamScore : {}".format(Studyhours, PreviousExamScore)
    arrdetails = ['Fail', 'Pass'] 
    if "btn-nclicks-1" == ctx.triggered_id:
        if Studyhours != None and PreviousExamScore != None:
            try:
                arrInput = np.array([Studyhours, PreviousExamScore])
                features = standardScaler.transform(arrInput.reshape(1, -1))
                PassFail = model.predict(features)[0]
                return 'As per the data entered the student will {}'.format(arrdetails[PassFail])
            except ValueError:
                return 'Unable to give Result Pass or Fail'
        else:
            return "Input is Empty"
            


if __name__ == '__main__':
    model = joblib.load("logisticRegression.pkl")
    standardScaler = joblib.load("standardScaler.pkl")
    app.run(debug=True)