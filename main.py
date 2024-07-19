import dash
from dash import dcc
from dash import html
# import dash_html_components as html
# import dash_core_components as dcc


# Create a Dash application
app = dash.Dash(__name__)

# Define the Layout of the Dashboard
app.layout = html.Div(
    children=[
        html.H1('My Data Analysis Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data':[
                    {'x':[1,2,3],'y':[4,1,2],'type': 'bar', 'name': 'Bar Chart'},
                    {'x':[1,2,3],'y':[2,4,5],'type': 'line', 'name': 'Line Chart'}
                ],
                'layout':{
                    'title': 'My Graph Title',
                    'xaxis': {'title':'x-axis'},
                    'yaxis': {'title':'y-axis'}
                }
            }
        )
    ]
)

# Run the application

if __name__ == '__main__':
    app.run_server(debug=True)