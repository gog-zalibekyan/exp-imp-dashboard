import dash

import dash_core_components as dcc

import dash_html_components as html

from figures_f import df_exp, f1, f1data,df_imp, f2, f2data,f3, f4, f7, df_trend

from dash.dependencies import Input, Output, State

import plotly.graph_objs as go


app=dash.Dash()

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.title = "Project on Exports and Imports of Armenia"



year = [i for i in range(2000,2017)]

app.layout = html.Div([



#Heading



html.Div([

  html.H1("", className='four columns'),

  html.H2("Exports and Imports of Armenia (2000-2016)", style={'color': '#0099cc', 'fontSize': 40}, className='eight columns'),

    ], className="row"),


html.Div([], className="twelve columns"),


#Export/Import dropdown
       
html.Div([
        
  dcc.Dropdown(

    id = 'option_in',

    options=[

      {'label': 'Export', 'value': "f1"},

      {'label': 'Import', 'value': "f2"}

        ], value="f1"

        ),

html.Div([], className="twelve columns"),

#Button

html.Button(id='show',n_clicks=0, children='show'),

  html.Div([], className="twelve columns"),

  html.Div(dcc.Graph(id='text_out',className='twelve columns')),
    ]),

  html.Div([], className="twelve columns"),


#Slider

html.Div([

  dcc.Slider(

    id='slider',

    min=min(year),

    max=max(year),

    value=min(year),

    marks={str(year): str(year) for year in year},

      ),

      ], style={'width':800, 'margin':25}),


#Pie Chart


html.Div([], className="twelve columns"),

html.Div([
  html.Div(
    [
      html.Div([
        dcc.RadioItems(
          id = 'figure_in',
          options=[
                {'label': 'Export', 'value':"f3"},
                {'label': 'Import', 'value':"f4" }
                ],
                style={'fontSize': 40, 'width':100, 'margin':100}
        )
      ], className="three columns"),
      
      html.Div([], className="twelve columns"),

      html.Div([
        
        dcc.Graph(id='figure_out'),
      ], className="eight columns")
    ], className="row"),
         ], className= "row"),


#Trend Chart

html.Div([], className="twelve columns"),

 html.Div([
        dcc.Graph(id="f7",figure=f7),
        ], className= "row"),
         ])


#Callbacks





@app.callback(

    Output(component_id='text_out', component_property='figure'),

    [Input(component_id='show', component_property='n_clicks')],

    [State(component_id='option_in', component_property='value'),
    State(component_id='slider',component_property='value')]

)


def update_map(clicks,val_1,year_input):
	if val_1=="f1":
		eval(val_1+"data")[0]["z"]=df_exp['export_val'][df_exp.year==year_input]
	else:
		eval(val_1+"data")[0]["z"]=df_imp['import_val'][df_imp.year==year_input]
	return eval(val_1)


@app.callback(
    Output(component_id='figure_out', component_property='figure'),
    [Input(component_id='figure_in', component_property='value')],
)

def update_graph(input_value):
    if input_value=="f3":
        return f3
    elif input_value=="f4":
        return f4
    else:
        return f3

   



if __name__ == '__main__':
	app.run_server(debug=True)