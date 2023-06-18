import sys
sys.path.insert(1, './lib/python3.7/site-packages')
import pandas as pd
import googletrans
import matplotlib.pyplot as plt; plt.rcdefaults() 

data = pd.read_csv("Amazon.csv", thousands = '.')

#view data

data.shape
data.head()
data.describe(include="all")

#check for any missing values

data.isna().sum()

#Break the dataset into smaller subsets:

data = data.replace(0, np.nan)
data2 = data.dropna(subset=['number'])
data2.describe(include="all")

#creating subset of the data:

forest_fire_per_month = data2.groupby('month')['number'].sum()
print(forest_fire_per_month)

forest_fire_per_month = forest_fire_per_month.reindex(months_unique, axis=0) 
months_unique = list(data.month.unique())

#converting series into dataframe
forest_fire_per_month = forest_fire_per_month.to_frame()
forest_fire_per_month.head()
forest_fire_per_month.reset_index(level=0, inplace=True)

forest_fire_per_month.head()
#create an object of Translator 
translator = Translator() 
for month in months_unique: 
    detected = translator.detect(month)     
    translated = translator.translate(month)     
    print(detected)     
    print(translated)     
    print("...")
translator2 = Translator() #create a new object of Translator. 
for i, m in enumerate(forest_fire_per_month['month']):
    translated = translator2.translate(m)  
    month1 = translated.text    
    forest_fire_per_month.at[i, 'month'] = month1

print(forest_fire_per_month)


plt.figure(figsize=(25, 15)) #specify width and height 
#plt.bar(x-values, y-values) 
plt.bar(
forest_fire_per_month['month'],
forest_fire_per_month['number'], 
color = (0.5,0.1,0.5,0.6)) 

#using.suptitle for the actual title and.title for the subheading

plt.suptitle('Amazon Forest Fires Over the Months', fontsize=20)
plt.title('Using Data from Years 1998 - 2017', fontsize=20) 
plt.xlabel('Month', fontsize=20) 
plt.ylabel('Number of Forest Fires', fontsize=20)
for i, num in enumerate(forest_fire_per_month['number']):
    plt.text(
        i,
        num + 10000,
        num,
        ha='center',
        fontsize=15)  
    
#setting the fontsize and alignment of the x and y axis tick labels

plt.setp(plt.gca().get_xticklabels(),
         rotation=45,
         horizontalalignment='right',
         fontsize=20)
plt.setp(plt.gca().get_yticklabels(), fontsize=20)