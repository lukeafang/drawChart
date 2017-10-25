import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
mpl.rcParams['text.latex.preamble']=[r"\usepackage{amssymb}",
                                     r"\usepackage{amsmath}",
                                     r"\usepackage{bm}"]
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#plt.rc('font',**{'family':'serif','serif':['Palatino']})
#plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
plt.rc('text', usetex=True);
#plt.rcParams['savefig.facecolor'] = "0.8"

font_legend  = 18;
font_fig = 20;
ms_size_1 = 12.0;
ms_size_2 = 12.0;
ms_size_3 = 12.0;
ms_size_4 = 12.0;
line_size_1 = 2.0;
line_size_2 = 2.0;
line_size_3 = 2.0;
line_size_4 = 2.0;
tl_font_size = 30;

leg_1 = '--rs';
leg_2 = '--b>';
leg_3 = 'rd';
leg_4 = 'b+';

    
col_1 = 'r';
col_2 = 'b';
col_3 = 'r';
col_4 = 'b';

#load data from file
outputFolder_path = 'Result/pic'
folder_path = 'Result/Nodes'
for index in range(1,3):
	numberOfTag = 50 * index
	folder_Name = "1000_{}_30".format(numberOfTag)
	file_path = folder_path + '/' + folder_Name + '/' + 'node_Location.txt'
	open_file = open(file_path, "r")
	x_location = []
	y_location = []
	for line in open_file:
		tempStr = line.split()
		x_location.append(tempStr[0])
		y_location.append(tempStr[1])
	open_file.close()

	file_path = folder_path + '/' + folder_Name + '/' + 'node_tag.txt'
	open_file = open(file_path, "r")
	x_tag = []
	y_tag = []
	for line in open_file:
		tempStr = line.split()
		x_tag.append(tempStr[0])
		y_tag.append(tempStr[1])
	open_file.close()

	file_path = folder_path + '/' + folder_Name + '/' +'node_Popularity.txt'
	open_file = open(file_path, "r")
	x_popularity = []
	y_popularity = []
	for line in open_file:
		tempStr = line.split()
		x_popularity.append(tempStr[0])
		y_popularity.append(tempStr[1])
	open_file.close()

	file_path = folder_path + '/' + folder_Name + '/' +'node_Prediction.txt'
	open_file = open(file_path, "r")
	x_prediction = []
	y_prediction = []
	for line in open_file:
		tempStr = line.split()
		x_prediction.append(tempStr[0])
		y_prediction.append(tempStr[1])
	open_file.close()

	lg1 = r'\bm{$LL^P$}'
	lg2 = r'\bm{$R^P$}'
	lg3 = r'\bm{$LL^J$}'
	lg4 = r'\bm{$R^J$}' 

	mpl.rcParams.update({'font.size': font_fig})
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)

	#plt.plot(x,y) 
	plt.plot(x_location, y_location, '-rs', linewidth=line_size_1, ms=ms_size_1, label="Location")
	plt.plot(x_tag, y_tag, '-b>', linewidth=line_size_2, ms=ms_size_2, label="Classification")
	plt.plot(x_popularity, y_popularity, '-go', linewidth=line_size_3, ms=ms_size_3, label="Popularity")
	plt.plot(x_prediction, y_prediction, '-k*', linewidth=line_size_4, ms=ms_size_4, label="Prediction")

	plt.legend(loc='upper left')
	plt.xticks(np.arange(0,900,100))
	#xlim_Max = 900;
	#xlim_Min = 0;
	#plt.xlim(xlim_Min,xlim_Max)
	plt.ylim(0,60)
	   
	plt.xlabel("Number of Nodes") 
	plt.ylabel("Response Time") 
	#plt.title("Simulation") 
	# plt.grid()
	ax.yaxis.grid(True, linestyle='-', which='major', color='lightgray', alpha=0.5)

	pic_filePath = outputFolder_path + '/nodes_' + str(numberOfTag) + '.png'
	plt.savefig(pic_filePath,dpi=300,format="png") 
	#plt.show() 
	plt.clf()
	plt.cla()
	plt.close()
