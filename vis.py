import pandas as pd
import plotly.express as px 

df= pd.read_csv('dates.csv')
max_val=df['value'].max()
max_date=df['date'].max()
min_date=df['date'].min()

fig = px.bar(df, x="name", y="value", color="name",
   animation_frame="date", animation_group="name", 
   range_y=[0,max_val])
fig.update_layout(
    height=600,
    title_text='Number of job opening from '+min_date+' till '+max_date
)
fig.show()