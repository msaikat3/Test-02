#Name: Monowar Hossain Saikat
#Lamar ID: L20488191
#Defining finction for calculating area:

def fx(n,R,S,Q):
    A= (Q*n)/(1.49)*(R**(0.67))*(S**0.5)  #simplifying the function for area
    return(A)

                
#Calling Function:
#Accoring to the link: https://waterdata.usgs.gov/nwis/wys_rpt/?site_no=08039100
#Historic maximum annual data is 42100 ft^3/s
Q = 0.75 * 42100           #Design discharge
n=0.020                    #mannings n value
S= 3/100                   #slope
R= 2*605*(1+1)**(0.5)      # Wetted perimeter calculated from slope where z=1
width=600+5                #width + freebody               
Area =fx(n,R,S,Q)          #Calculating the area
print(Area)                #Printing the area


#Volume of soil:
Volume_of_soil = Area * width   #multiplicating area with width to get the volume
print(Volume_of_soil) 


    