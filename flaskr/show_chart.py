from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request, make_response

from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

from io import BytesIO
from PIL import Image, ImageOps
import requests
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


bp = Blueprint("show_chart", __name__)

# raspberry piからhttp通信で画像データをDBに格納するmethod/api

# @bp.route("/send_image") 
# def send_image():
#     image = request.form["image"]
#     # https://teratail.com/questions/222843
#     img = Image.open(BytesIO(image))
#     flipped_img = ImageOps.flip(img)
#     flipped_img.show()
#     # return render_template("login.html")
# fig = plt.figure()
# ax = fig.add_subplot()

@bp.route('/plot')
def plot_png():
    import pdb; pdb.set_trace()
    fig = create_figure()
    # output = io.BytesIO()
    # FigureCanvas(fig).print_png(output)

    canvas = FigureCanvasAgg(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)

    return response

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

