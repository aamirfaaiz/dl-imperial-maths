import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter

def reset_plots():
	"""
	Makes axes large, and enables LaTeX for matplotlib plots
	"""
	plt.close('all')
	fontsize = 20
	legsize = 15
	plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
	plt.rc('text', usetex=True)
	font = {'size' : fontsize}
	plt.rc('font', **font)
	rc={'axes.labelsize': fontsize,
	'font.size': fontsize,
	'axes.titlesize': fontsize,
	'xtick.labelsize':fontsize,
	'ytick.labelsize':fontsize,
	'legend.fontsize': legsize}
	mpl.rcParams.update(**rc)
	mpl.rc('lines', markersize=10)
	plt.rcParams.update({'axes.labelsize': fontsize})
	mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

def remove_tex_axis(ax, xtick_fmt = '%d', ytick_fmt = '%d'):
	"""
	Makes axes normal font in matplotlib.
	Params:
	xtick_fmt : A string, defining the format of the x-axis
	ytick_fmt : A string, defining the format of the y-axis
	"""
	fmt = matplotlib.ticker.StrMethodFormatter("{x}")
	ax.xaxis.set_major_formatter(fmt)
	ax.yaxis.set_major_formatter(fmt)
	ax.xaxis.set_major_formatter(FormatStrFormatter(xtick_fmt))
	ax.yaxis.set_major_formatter(FormatStrFormatter(ytick_fmt))
