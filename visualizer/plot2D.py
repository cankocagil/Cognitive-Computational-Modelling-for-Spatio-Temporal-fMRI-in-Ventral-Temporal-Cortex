# For plotting
import plotly.io as plt_io
import plotly.graph_objects as go
import numpy as np


def plot_2d(component1:np.ndarray, component2:np.ndarray,  path:str, y = None,) -> None:
    
    fig = go.Figure(data=go.Scatter(
        x = component1,
        y = component2,
        mode='markers',
        marker=dict(
            size=20,
            color=y, #set color equal to a variable
            colorscale='Rainbow', # one of plotly colorscales
            showscale=True,
            line_width=1
        )
    ))
    fig.update_layout(margin=dict(l=100,r=100,b=100,t=100),width=2000,height=1200)                 
    fig.layout.template = 'plotly_dark'
    
    fig.show()
    
    
    fig.write_image(path)
