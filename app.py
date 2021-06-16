from gradcam import gradcam

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from utils import base64_to_img, img_to_base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=False
    ),
    dcc.Graph(
        id='gradcam')
])


@app.callback(Output('gradcam', 'figure'),
              Input('upload-image', 'contents'))
def update_output(image_str):
    if image_str is not None:
        img = base64_to_img(image_str)
        figure = gradcam(img)
        return figure


if __name__ == '__main__':
    app.run_server(debug=True)
