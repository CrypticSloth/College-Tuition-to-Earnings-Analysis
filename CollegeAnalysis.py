# College Earnings Analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
from trendline import trendline

data_loc = "C:/Users/Erik Sorensen/Desktop/Data/College Dataset/CollegeScorecard_Raw_Data/CollegeScorecard_Raw_Data/"

# Read in the 2014-2015 data first
data = pd.read_csv(data_loc + "MERGED2012_13_PP.csv",low_memory=False)

# Pull the Name of the College, the Tuition, and the Earnings
name = data['INSTNM']
tuition = data['TUITIONFEE_OUT']
earnings = data['MD_EARN_WNE_P6']

# Make the data columns we just pulled into nice numpy arrays
school = [x for x in name]
tuition = [x for x in tuition]
earnings = [x for x in earnings]
earnings = [0 if x == 'PrivacySuppressed' else x for x in earnings]
earnings = [int(x) if type(x) == str else x for x in earnings]
earnings = [0 if x == math.nan else x for x in earnings]

# Put these arrays into a new data frame
d = {'School':school, 'Tuition':tuition,'Earnings':earnings}
df = pd.DataFrame(data=(d))

# Sort the data by low to high earnings
df = df.sort_values('Earnings')

# Remove outliers
df = df[(df.Earnings < 60000 ) & (df.Earnings > 1)]

# Plots
def tuitionLine():
	# Set figure size
	plt.figure(figsize=(10,7.5))

	# Take out unecessary chartjunk
	ax = plt.subplot()
	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.get_yaxis().tick_left()
	ax.get_xaxis().tick_bottom()
	ax.tick_params(left='off',bottom='off')

	# Take out whitespace
	plt.ylim(0,60000)
	plt.xlim(0,6250)

	# Plot horizontal lines
	for y in range(0,60001,10000):
		plt.plot(range(0,6250),[y] * len(range(0,6250)), "--",
			lw=.5,color='black',alpha=.3)
	# Labels
	plt.xticks(range(0,6500,1000),alpha=0.5)
	plt.yticks(range(0,60001,10000),alpha=0.5)
	plt.ylabel('$USD',alpha=0.75)
	plt.xlabel('School # in order from cheapest to most expensive',alpha=0.75)
	plt.text(3000,62000,'Income (per year) after College in Relation to Tuition Costs',
			fontsize=12,ha='center')
	# Legend
	plt.text(5500,55000,'Earnings',color='#3F5D7D',fontweight='bold')
	plt.text(6250,20000,'Tuition',color='#BC8F8F',fontweight='bold')
	# Credits
	plt.text(-1200,-5000,'Data Source: https://catalog.data.gov/dataset/college-scorecard'
			'\nBy Erik Sorensen (CrypticSloth on github)',
			fontsize=6)

	color = ['#3F5D7D','#BC8F8F']
	# Create numbers which will be the school numbers sorted by low to high cost
	name = range(len(df.Earnings))

	plt.plot(name,df.Earnings,color=color[0])
	plt.scatter(name,df.Tuition,color=color[1],s=.75)
	plt.savefig('College Tuition with Earnings Line.png',bbox_inches='tight')
	#plt.show()

def scatterplot():
	# Set figure size
	plt.figure(figsize=(10,7.5))

	# Take out unecessary chartjunk
	ax = plt.subplot()
	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.get_yaxis().tick_left()
	ax.get_xaxis().tick_bottom()
	plt.tick_params(bottom='off',left='off')

	# Take out whitespace
	plt.ylim(0,50050)
	plt.xlim(7500,60000)

	# Labels for Data
	plt.xticks(range(10000,60001,10000),alpha=0.5,fontsize=8)
	plt.yticks(range(0,50001,10000),alpha=0.5,fontsize=8)
	plt.ylabel('Tuition Cost (USD)',alpha=0.6,fontsize=10)
	plt.xlabel('Income (per year) 6 years after College (USD)',alpha=0.6,fontsize=10)
	plt.text(33000,51000,'Tuition and Median Earnings of Colleges',
			fontsize=12,ha='center')
	# Credits
	plt.text(-1000,-5000,'Data Source: https://catalog.data.gov/dataset/college-scorecard'
			'\nBy Erik Sorensen (CrypticSloth on github)',
			fontsize=6)

	# Plot horizontal lines
	for y in range(0,50001,10000):
		plt.plot(range(7500,60001), [y] * len(range(7500,60001)), "--", 
    			lw=0.5, color="black", alpha=0.3)

	# Plot the Data
	plt.scatter(df.Earnings,df.Tuition,color='#3F5D7D',s=.75)
	# Plot the line of best fit
	trendline(df.Earnings,df.Tuition,c='#BC8F8F')

	plt.savefig('College Tuition-Income Scatterplot.png',bbox_inches='tight')
	#plt.show()

scatterplot()
tuitionLine()