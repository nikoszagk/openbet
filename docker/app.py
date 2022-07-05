from flask import Flask, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [12.50, 6.50]
plt.rcParams["figure.autolayout"] = True

app = Flask(__name__)

@app.route('/')
def myChart():
    fig = Figure()

    axis = fig.add_subplot(1, 1, 1)
    xs = np.linspace(0, 100, 1000)
    ys = np.sin(xs)
    axis.scatter(xs,ys, s=3)
    output = io.BytesIO()

    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
