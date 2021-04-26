# For plotting
import plotly.io as plt_io
import plotly.graph_objects as go



def plot_3d(component1,component2,component3):
    fig = go.Figure(data=[go.Scatter3d(
            x=component1,
            y=component2,
            z=component3,
            mode='markers',
            marker=dict(
                size=10,
                color=y,                # set color to an array/list of desired values
                colorscale='Rainbow',   # choose a colorscale
                opacity=1,
                line_width=1
            )
        )])
    # tight layout
        fig.update_layout(margin=dict(l=50,r=50,b=50,t=50),width=1800,height=1000)
        fig.layout.template = 'plotly_dark'
        
        fig.show()
