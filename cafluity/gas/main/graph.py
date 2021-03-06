import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
	buffer = BytesIO()
	plt.savefig(buffer, format='png')
	buffer.seek(0)
	image_png = buffer.getvalue()
	graph = base64.b64encode(image_png)
	graph = graph.decode('utf-8')
	buffer.close()

	return graph

def get_plot(x, y, title, xlabel, ylabel):
	plt.switch_backend('AGG')
	plt.figure(figsize=(5,3.5))
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(x, y, color = 'darkorange')
	# plt.scatter(x, y)
	plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
	plt.tight_layout()
	graph = get_graph()

	return graph