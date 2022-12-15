import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.express as px

import pandas as pd
import utils

cdc = pd.read_csv('./data/cdc_2022-11-18-05-12-04.csv')
jhu = pd.read_csv('./data/jhu_2022-11-18-05-14-54.csv')
# jhu = pd.read_csv('./data/jhu_with_cdc_start.csv')

type_data = {
    'running_avg_1': ('new_death', 'daily_deaths'),
    'running_avg_3': ('rolling_deaths_3', 'rolling_deaths_3'),
    'running_avg_7': ('rolling_deaths_7', 'rolling_deaths_7'),
}

common_cdc, common_jhu = utils.get_common_data(cdc, jhu)
state_dfs = utils.get_state_dfs(common_cdc, common_jhu)

state_df_dict = {}
for state, df_cdc, df_jhu in state_dfs:
    state_df_dict[state] = (df_cdc, df_jhu)

config = {
    'staticPlot': False,
    'scrollZoom': True,
    'doubleClick': 'reset',
    'showTips': False,
    'displayModeBar': True
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

l = []
l.append(
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='type',
                options=[
                    { 'label': 'Running Avg 1', 'value': 'running_avg_1'},
                    { 'label': 'Running Avg 3', 'value': 'running_avg_3'},
                    { 'label': 'Running Avg 7', 'value': 'running_avg_7'},
                ],
                multi=False,
                value='running_avg_1',
                clearable=False,
                style={ 'width': '170px', 'font-size': '0.8rem'}
            )
        ], width=1)
    ], justify='center', style={'margin-top': '10px'}),
)

output = []
hover_output = {}
states = list(cdc['State'].unique())
for i, state in enumerate(states):
    output.append(Output(component_id=f'{state}_diff', component_property='figure'))

    hover_output[state] = []
    hover_output[state].append(Output(component_id=f'{state}_cdc', component_property='figure'))
    hover_output[state].append(Output(component_id=f'{state}_jhu', component_property='figure'))
    hover_output[state].append(Input(component_id=f'{state}_diff', component_property='hoverData'))
    hover_output[state].append(Input(component_id=f'{state}_diff', component_property='figure'))
    hover_output[state].append(Input(component_id='type', component_property='value'))

    l.append(
        dbc.Row([
            dbc.Col([
                dcc.Graph(id=f'{state}_diff', config=config)
            ], width=7, style={'margin-top': '0px'}),

            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id=f'{state}_cdc', config=config)
                    ], width=12)
                ]),

                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id=f'{state}_jhu', config=config)
                    ], width=12)
                ])
            ], width=5),
        ])
    )

app.layout = dbc.Container(l, fluid=True, style={'height': '100vh'})

@app.callback(
    output,
    [Input(component_id='type', component_property='value')]
)
def update_graph(type_value):
    cdc_col, jhu_col = type_data[type_value]
    out = []
    for i, (state, df_cdc, df_jhu) in enumerate(state_dfs):
        diff = utils.get_diff_list(df_cdc, cdc_col, df_jhu, jhu_col, 1)

        fig_diff = px.line(diff, x='Date', y='Diff', labels={'Diff': 'Diff (cdc - jhu)'}, height=700, title=state)

        out.append(fig_diff)

    return out

l = []
def update(hover_data, figure, type_value):
    state = figure['layout']['title']['text']
    df_cdc, df_jhu = state_df_dict[state]
    cdc_col, jhu_col = type_data[type_value]
    interval = 10
    out = []

    if hover_data is None:
        diff = utils.get_diff_list(df_cdc, cdc_col, df_jhu, jhu_col, 1)

        diff['abs'] = diff['Diff'].abs()
        print(state, diff['abs'].max().item())
        max_diff_index = diff['abs'].idxmax()
    else:
        max_diff_index = hover_data['points'][0]['pointIndex'] + 1

    low = max(1, max_diff_index-interval)
    high = min(max_diff_index+interval, df_cdc.shape[0]-1)
    
    df_cdc_interval = df_cdc[low:high+1]
    df_jhu_interval = df_jhu[low:high+1]

    fig_cdc = px.line(df_cdc_interval, x='Date', y=cdc_col, labels={cdc_col: 'Deaths'}, title='CDC')
    fig_jhu = px.line(df_jhu_interval, x='Date', y=jhu_col, labels={jhu_col: 'Deaths'}, title='JHU')

    out.append(fig_cdc)
    out.append(fig_jhu)
    return out

for i, state in enumerate(states):
    app.callback(hover_output[state])(update)

if __name__ == "__main__":
    app.run_server(debug=True)