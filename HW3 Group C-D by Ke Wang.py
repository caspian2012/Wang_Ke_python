""" Question 1"""

# Import the pandas module.
import pandas as pd

# Create a dataframe with data from the website and column names found in 
# iris.names file.
Iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
              names=['Sepal Length(cm)','Sepal Width(cm)','Petal Length(cm)','Petal Width(cm)','Class']) 


""" Question 2"""

# The head function gives the first 10 rows of data.
Iris.head(10) 

# The tail function gives the last 10 rows of data.
Iris.tail(10) 


""" Question 3"""

# The describe function gives all the info we need, a.k.a.
# Count, Mean, STD, Min, 25%, 50%, 75%, MAX.
Iris.describe() 


""" Question 4"""

# The list of column names of numeric columns.
column_name = ['Sepal Length(cm)', 'Sepal Width(cm)', 'Petal Length(cm)',
          'Petal Width(cm)']
          
# Define a function that takes a list of bin sizes and produce a histogram for
# each column (a total of 4 columns) and each bin size.
def plt_hist(bin_lst):
    for col in column_name[0:4]: 
        for i in bin_lst: 
            Iris.hist(column = col, bins = i) 

# Print sample histograms of bin sizes 10, 50, and 100.
plt_hist([10, 50, 100])
        
""" Question 5"""

# We create a new figure for each box plot we need to produce, then give them
# the corresponding title and create the box plot.
import matplotlib.pyplot as plot
plot.figure('SL Box')
plot.title('Sepal Length Box Plot')
Iris['Sepal Length(cm)'].plot.box()

plot.figure('SW Box')
plot.title('Sepal Width Box Plot')
Iris['Sepal Width(cm)'].plot.box()

plot.figure('PL Box')
plot.title('Petal Length Box Plot')
Iris['Petal Length(cm)'].plot.box()

plot.figure('PW Box')
plot.title('Petal Width Box Plot')
Iris['Petal Width(cm)'].plot.box()


""" Question 6"""

# "Class" is the only nominal column and we plot a bar chart counting the 
# frequency of each name appreared in the "Class" column.
Iris['Class'].value_counts().plot.bar()