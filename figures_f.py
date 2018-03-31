#Figure 1 - Map

from plotly.offline import plot, iplot

import plotly.graph_objs as go

import pandas as pd

import plotly.plotly as py

#Data from https://atlas.media.mit.edu/en/

df_exp = pd.read_csv('https://raw.githubusercontent.com/gog-zalibekyan/bi-project/master/en_visualize_explore_tree_map_hs92_export_arm_show_all_2000.2016.csv')



f1data = [ dict(

    type = 'choropleth',

    locations = df_exp['country_destination_id'],

    z = df_exp['export_val'][df_exp.year==2000],

    text = df_exp['country_destination_id'],

    colorscale = 'Viridis',
       
    autocolorscale = False,

    reversescale = True,


    marker = dict(

        line = dict (

        color = 'rgb(180,180,180)',

        width = 0.5

            ) ),

    colorbar = dict(

        autotick = False,

        tickprefix = '$',

        title = 'Millions US$'),

        width= 300,

        height=10

        ) ]



layout = dict(

    title = 'Exports from<br>Armenia',
    font = dict(color = 'black', size = 20),

        width= 2000,

        height=1000,
    
  
    geo = dict(

        showframe = False,


        showcoastlines = False,

    projection = dict(

        type = 'Mercator'

        )

    )

)



f1 = dict( data=f1data, layout=layout )





#Figure 2 - Map

import plotly.plotly as py

import pandas as pd



df_imp = pd.read_csv('https://raw.githubusercontent.com/gog-zalibekyan/bi-project/master/en_visualize_explore_tree_map_hs92_import_arm_show_all_2000.2016.csv')



f2data = [ dict(

    type = 'choropleth',

    locations = df_imp['country_destination_id'],

    z = df_imp['import_val'][df_imp.year==2000],

    text = df_imp['country_destination_id'],

    colorscale = 'Viridis',
    
    autocolorscale = False,

    reversescale = True,

    marker = dict(

        line = dict (

            color = 'rgb(180,180,180)',

            width = 0.5

            ) ),

    colorbar = dict(

        autotick = False,

        tickprefix = '$',

        title = 'Millions US$',
            
        width= 300,

        height=10,
           ),

      ) ]



layout = dict(

    title = 'Imports of<br>Armenia',
    font = dict(color = 'black', size = 20),
        
        width= 2000,

        height=1000,

    geo = dict(

        showframe = False,

        showcoastlines = False,

    projection = dict(

            type = 'Mercator'
        ),

    )

)



f2 = dict( data=f2data, layout=layout )






##Figure 3 - Pie chart



import plotly.plotly as py

import plotly.graph_objs as go



df_expp = pd.read_csv('https://raw.githubusercontent.com/gog-zalibekyan/bi-project/master/export_2016.csv')


labels = df_expp['Category']

values = df_expp['Percent']

colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']

trace = go.Pie(labels=labels, values=values, 

                textfont=dict(size=30),

                marker=dict(colors=colors, 

                line=dict(color='#000000', width=1)))


layout = go.Layout(title='Export by Product Categories', font = dict(size = 32),height= 656,width= 1188,)

data = [trace]
f3 = dict(data=data,layout=layout)




df_impp = pd.read_csv('https://raw.githubusercontent.com/gog-zalibekyan/bi-project/master/import_2016.csv')


labels = df_impp['Category']

values = df_impp['Percent']

colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']



trace = go.Pie(labels=labels, values=values,

                textfont=dict(size=30),

                marker=dict(colors=colors, 

                line=dict(color='#000000', width=1)))


layout = go.Layout(title='Import by Product Categories', font = dict(size = 32),height= 656,width= 1188,)

data = [trace]

f4 = dict(data=data,layout=layout)



##Figure 4 - Trend Chart

import plotly.plotly as py

import plotly.graph_objs as go

import pandas as pd

df_trend = pd.read_csv("https://raw.githubusercontent.com/gog-zalibekyan/bi-project/master/trend1.csv")

trace_high = go.Scatter(
    x=df_trend['year'],
    
    y=df_trend['import_val'],
                
    name = "Import",
                
    mode = 'lines+markers',
                
    fill = 'tozeroy',
                
    line = dict(color = '#17BECF'),
                
    opacity = 0.8)


trace_low = go.Scatter(
    
    x=df_trend['year'],
                
    y=df_trend['export_val'],
                
    name = "Export",
                
    mode = 'lines+markers',
                
    fill = 'tozeroy',
    
    line = dict(color = '#7F7F7F'),
                
    opacity = 0.8)


data = [trace_high,trace_low]


layout = dict(
    
    title = "Trend Line for Exports and Imports",
    
    xaxis = dict(
        
        title= 'Year'),
    
    yaxis = dict(
        
        title= 'Trade in USD'),

)


f7 = dict(data=data, layout=layout)











