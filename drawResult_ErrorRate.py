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

colorAndNodeTypeArray = ['-rs', '-b>', '-go', '-k*', '-c*', '-m*']

#load data from file
outputFolder_path = 'Result/pic'
folder_path = 'Result/ErrorRate'
for index in range(1,3):
	numberOfTag = 50 * index
	folder_Name = "1000_{}_30".format(numberOfTag)

	mpl.rcParams.update({'font.size': font_fig})
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)

	for index in range(0,6):
		errorRate = 10 * index
		fileName = "ErrorRateTest_{}".format(errorRate)
		file_path = folder_path + '/' + folder_Name + '/' + fileName + '.txt'
		open_file = open(file_path, "r")
		x_node = []
		y_responseTime = []
		for line in open_file:
			tempStr = line.split()
			x_node.append(tempStr[0])
			y_responseTime.append(tempStr[1])
		open_file.close()

		#plt.plot(x_Ratio,y_responseTime) 
		labelName = "{}".format(errorRate)
		#plt.plot(x_node, y_responseTime, color=colorArray[index], linewidth=1.5, linestyle="-", label=labelName)
		plt.plot(x_node, y_responseTime, colorAndNodeTypeArray[index], linewidth=line_size_3, ms=ms_size_3, label=labelName)

		plt.legend(loc='upper left', ncol=3)
		plt.xticks(np.arange(0,900,100))
		#xlim_Max = 900;
		#xlim_Min = 0;
		#plt.xlim(xlim_Min,xlim_Max)
		# plt.ylim(0,50)
		plt.ylim(0,30)
		plt.xlabel("Number of Nodes") 
		plt.ylabel("Response Time") 

	# plt.grid()
	ax.yaxis.grid(True, linestyle='-', which='major', color='lightgray', alpha=0.5)
	pic_filePath = outputFolder_path + '/errorRate_' + str(numberOfTag) + '.png'
	plt.savefig(pic_filePath,dpi=300,format="png") 
	plt.clf()
	plt.cla()
	plt.close()
	#plt.show() 		