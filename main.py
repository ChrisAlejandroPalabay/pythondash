import pandas as pd
import matplotlib.pyplot as plt


arts = pd.read_csv('/Users/jakirice/Desktop/art.csv')
result = arts.loc[:,['Condition', 'ArtID']].groupby('Condition').size().reset_index(name='Number of Arts')
result.sort_values(by=['Number of Arts'], inplace=True)
con = result.iloc[-4:]
colors = ["orange", "yellow", "lightblue", "pink"]
explode = (0, 0, 0, 0.1)  
plt.pie(con['Number of Arts'], labels=con['Condition'],explode = explode, colors=colors,
autopct='%.1f%%', shadow=True, startangle=200)
plt.title('Percentages of Art conditions')
plt.show()

