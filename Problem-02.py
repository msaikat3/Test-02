#Name: Monowar Hossain Saikat
#Lamar ID: L20488191

#Importing libraries
import os                              #to read the directory
import pandas as pd                    # to read the csv file
import matplotlib.pyplot as plot       #importing library for plot

#Defining the path:
path = 'C:\\Users\\User\\OneDrive\\Desktop\\Exam'  # Setting the directory
os.chdir(path)

# CSV file reading

a =pd.read_csv('CSV file for plot.csv')  #reading the CSV file from directory
print(a)

#Plotting map: 
x = a['Year']   # Extracting the column from CSV file
x
y = a['Annual_Discharge']  # Extracting the column from CSV file
y
plot.plot(x,y,'ro')    # plotting the x and y value as year and annual discharge
plot.xlebel('Year')    # labelling the x plot as year
plot.ylebel('Anuall maximum flow')  # lebeling the y plot as annual maximum flow
plot.title('Year vs flow')   # provind a title for the plot
plot.show()                  # using this function to show  plot
#Function defining:
def fx(r,n):
    Fx=(r-0.44)/(n+0.12)
    return(Fx)
#Calling the function to calculate y for different r:
n= 26
r = 1    #when rank=1
y= fx(r,n)
print(round(y,4))


n= 26
r = 2    #when rank=2
y= fx(r,n)
print(round(y,4))

n= 26
r = 3   #when rank=3
y= fx(r,n)
print(round(y,4))

n= 26
r = 4    #when rank=4
y= fx(r,n)
print(round(y,4))

n= 26
r = 5    #when rank=5
y= fx(r,n)
print(round(y,4))

n= 26
r = 6    #when rank=6
y= fx(r,n)
print(round(y,4))

n= 26
r = 7    #when rank=7
y= fx(r,n)
print(round(y,4))

n= 26
r = 8    #when rank=8
y= fx(r,n)
print(round(y,4))

n= 26
r = 9   #when rank=9
y= fx(r,n)
print(round(y,4))

n= 26
r = 10    #when rank=10
y= fx(r,n)
print(round(y,4))

n= 26
r = 11    #when rank=11
y= fx(r,n)
print(round(y,4))
n= 26
r = 12   #when rank=12
y= fx(r,n)
print(round(y,4))

n= 26
r = 13   #when rank=13
y= fx(r,n)
print(round(y,4))
n= 26
r = 14    #when rank=14
y= fx(r,n)
print(round(y,4))
n= 26
r = 15   #when rank=15
y= fx(r,n)
print(round(y,4))
n= 26
r = 16   #when rank=16
y= fx(r,n)
print(round(y,4))

n= 26
r = 17   #when rank=17
y= fx(r,n)
print(round(y,4))
n= 26
r = 18   #when rank=18
y= fx(r,n)
print(round(y,4))
n= 26
r = 19   #when rank=19
y= fx(r,n)
print(round(y,4))
n= 26
r = 20   #when rank=20
y= fx(r,n)
print(round(y,4))
n= 26
r = 21   #when rank=21
y= fx(r,n)
print(round(y,4))
n= 26
r = 22   #when rank=22
y= fx(r,n)
print(round(y,4))
n= 26
r = 23   #when rank=23
y= fx(r,n)
print(round(y,4))
n= 26
r = 24   #when rank=24
y= fx(r,n)
print(round(y,4))
n= 26
r = 25   #when rank=25
y= fx(r,n)
print(round(y,4))
n= 26
r = 26   #when rank=26 


#Plotting F(X),annual flow vs year:

a =pd.read_csv('CSV file for plot.csv')  #reading the CSV file from directory
print(a)

fx = a['Valueof_F(X)'] #extracting column from csv
fx

y = a['Annual_Discharge'] #extracting column from csv
y

z = a['Year']  #extracting column from csv
z

# Plotting the data as rank:
    
plot.plot(y,fx,'ro')    # plotting the x and y value as year and annual discharge
plot.plot(y,z,'ro')    # plotting the x and y value as year and annual discharge
plot.xlebel('Year')    # labelling the x plot as year
plot.ylebel('Anuall maximum flow')  # lebeling the y plot as annual maximum flow
plot.zlebel(' rank')  #lebeling as rank
plot.title('Year vs flow as rank')   # provind a totle for the plot
plot.show()       #showing the plot
