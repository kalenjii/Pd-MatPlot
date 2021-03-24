#Fandango Bias
#Data journalist Walt Hickey found strong evidence to suggest that Fandango's rating system was biased and dishonest

import pandas as pd
rating_before = pd.read_csv('fandango_score_comparison.csv')
rating_after = pd.read_csv('movie_ratings_16_17.csv')

pd.options.display.max_columns = 100

fandango_before = rating_before[['FILM','Fandango_Stars', 'Fandango_Ratingvalue', 'Fandango_votes', 'Fandango_Difference']]
fandango_after = rating_after[['movie', 'year', 'fandango']]

print(fandango_before.head(3))
print(fandango_after.head(3))

print(fandango_before.sample(10, random_state = 1))
print(fandango_after.sample(10, random_state = 1)) #In this case, we need to check
#ourselves on fandango website whether samples are representable (over 30 votes)

#Add new column with years
fandango_before['Year'] = fandango_before['FILM'].str[-5:-1]
print(fandango_before.head(2))

fandango_after['year'].value_counts() #get rid of 2017

fandango_2015 = fandango_before[fandango_before['Year'] == '2015']
fandango_2016 = fandango_after[fandango_after['year'] == 2016]

#Draw density plot
import matplotlib.pyplot as plt
from numpy import arange
%matplotlib inline #its important to display a graph

plt.style.use('fivethirtyeight')
fandango_2015['Fandango_Stars'].plot.kde(label = '2015', legend= True)
fandango_2016['fandango'].plot.kde(label = '2016', legend = True)
plt.title('Fandango ratings in 2015 and 2016', fontsize = 15)
plt.xlabel('Rating')
plt.xlim(0,5)
plt.xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
plt.show()

fandango_2015['Fandango_Stars'].value_counts(normalize = True).sort_index() *100
fandango_2016['fandango'].value_counts(normalize = True).sort_index() *100