from flask import Flask, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [18.50, 10.50]
plt.rcParams["figure.autolayout"] = True

app = Flask(__name__)

@app.route('/')
def myChart(radius=1):
    fig = Figure()
    
    axis = fig.add_subplot(1, 1, 1)
    theta = np.linspace(0, 2*np.pi, 1000)
    xs = radius * np.cos(theta)
    ys = radius * np.sin(theta)
    axis.scatter(xs,ys, s=0.3)
    output = io.BytesIO()

    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8181")
