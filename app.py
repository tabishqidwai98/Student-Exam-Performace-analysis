import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
from dash import Dash, html, dcc, callback, Output, Input, dash_table

df = pd.read_csv("C:/Users/tabis/Desktop/Student Exam Performace analysis/data/student_exam_data.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

#app = Dash(__name__)

app.layout = html.Div(children=[html.Div(children=[
    html.H1(children= 'Student Exam Analyis and Prediction', style = {'textAlign' : 'center', 'color' : '#7B68EE'}),
    html.H3(children = 'Dataset', style = {'textAlign' : 'left', 'color' : '#ffffff'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    html.H3(children = 'Graphs', style = {'textAlign' : 'left', 'color' : '#ffffff'}),
    html.H5(children = 'Plot between study hours and pass fail (bar)', style = {'textAlign' : 'left', 'color' : '#ffffff'}),
    dcc.Graph(figure= px.histogram(df, x = 'Pass/Fail', color='Pass/Fail', barmode="group")),
    html.H5(children = 'Plot between study hours and Previous Exam Score (bar)', style = {'textAlign' : 'left', 'color' : '#ffffff'}),
    #dcc.Graph(figure= px.histogram(df, y = 'Previous Exam Score', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='count')),
    dcc.Graph(figure= px.histogram(df, y = 'Previous Exam Score', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='avg')),
    dcc.Graph(figure= px.histogram(df, y = 'Previous Exam Score', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='sum')),
    dcc.Graph(figure= px.histogram(df, y = 'Study Hours', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='avg')),
    dcc.Graph(figure= px.histogram(df, y = 'Study Hours', x = 'Pass/Fail', color='Pass/Fail', barmode="group", histfunc='sum')),
    dcc.Graph(figure= px.scatter(data_frame=df, y = 'Previous Exam Score', x = 'Study Hours', color = 'Pass/Fail')),
    dcc.Graph(figure= px.scatter(data_frame=df, y = 'Previous Exam Score', x = 'Study Hours', trendline = 'ols')),
], style = {'width' : '700px', 'margin' : 'auto', 'background-color': '#191919'})], 
style = {'background-color' : '#191919'}
)

#@callback(
#    Output('graph-content', 'figure'),
#    Input('dropdown-selection', 'value')
#)
#def update_graph(value):
#    dff = df[df.country==value]
#    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)