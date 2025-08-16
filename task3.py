import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv('C:/Users/HP/Desktop/quantium-starter-repo-main/quantium-starter-repo-main/data/daily_sales_data_0.csv')
df = pd.read_csv('C:/Users/HP/Desktop/quantium-starter-repo-main/quantium-starter-repo-main/data/daily_sales_data_1.csv')
df = pd.read_csv('C:/Users/HP/Desktop/quantium-starter-repo-main/quantium-starter-repo-main/data/daily_sales_data_2.csv')
df['date'] = pd.to_datetime(df['date'])
df['price'] = df['price'].replace({r'\$': '', ',': ''}, regex=True).astype(float)
df['quantity'] = df['quantity'].astype(int)
df = df[df['product'] == 'pink morsel']

df['Sales'] = df['quantity'] * df['price']
daily_sales = df.groupby(df['date'].dt.date)['Sales'].sum().reset_index()
daily_sales.columns = ['date', 'Sales']

fig = px.line(daily_sales, x='date', y='Sales', title='Daily Sales for Pink Morsel')

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Soul Foods', style={'font-family':'Arial, serif', 'padding-left':'10px'}),

    dcc.Graph(
        id='daily-sales-graph',
        figure=px.line(daily_sales, x='date', y='Sales', title='Daily Sales for Pink Morsel')
    )
])

if __name__ == '__main__':
    app.run(debug=True)
