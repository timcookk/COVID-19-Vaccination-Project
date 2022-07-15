# Importing the packages
import matplotlib.pyplot as plt
import pandas as pd
from skimage import io
from bs4 import BeautifulSoup
import requests
import time


def vaccination_graph():
    
    dfc = pd.read_excel('Vaccination_Rate.xlsx')
    df_fil=dfc[['Location','Vaccination Rate']]
    top_five=df_fil.iloc[:5,:]
    low_five=df_fil.iloc[-5:,:]


    # Declaring the figure or the plot (y, x) or (width, height)
    plt.figure(figsize=[14, 10])


    # Append 'h' to the bar to make horizontal bar
    plt.barh(low_five['Location'],low_five['Vaccination Rate'], label = "Lowest vaccination rate", color = 'r')
    plt.barh(top_five['Location'],top_five['Vaccination Rate'] ,label = "Highest vaccination rate", color = 'g')


    # Creating the legend of the bars in the plot
    plt.legend()

    # Namimg the x and y axis
    plt.xlabel('Vaccination rate')
    plt.ylabel('State')

    # Giving the tilte for the plot
    plt.title(' Top/Low 5 States of Vaccination Rate')

    # Displaying the bar plot
    plt.show()
    
    return plt.show()



def vaccination_image():
    
    # the image was dowloaded from uiowa.edu website
    img=io.imread('vaccination.jpeg') 
    print(img.shape)
    plt.imshow(img)
    
    
    #Cut the area we want from the original image
    plt.figure()
    img2 = img[110:290,100:950]     
    plt.imshow(img2)
    io.imsave('get_vaccinated.jpeg',img2)
    
    
    #Apply color to the background for emphasis
    plt.figure()
    img3 = img2[:]                   
    img3[:,:,1] = 0                 
    plt.imshow(img3)
    io.imsave('get_vaccinated_pink.jpeg',img3)
    
    return plt.imshow(img3)



def get_covidcase_description():        
    url = f'https://www.worldometers.info/coronavirus/usa/{statename}/'
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, "lxml")
    p_tag = soup.find_all('div', class_='maincounter-number')[0]
    time.sleep(1)
    return p_tag.text
    

statenames = ["Iowa","California","Texas","Florida","New-York","Pennsylvania","Illinois","Ohio","Michigan","Georgia","Massachusetts","Washington","Arizona","Maryland","Colorado","Minnesota","Tennessee","Wisconsin","Indiana","Missouri","Oregon"] 
file = open('statename.txt','w')  

for statename in statenames:
    desc = get_covidcase_description()
    file.write(f'Statename: {statename}\nTotal Coronavirus Cases: {desc}\n\n')
    
file.close()




def vaccination_age():
    dfx = pd.read_excel("Vaccination_Age.xlsx")
    df_age = dfx[['Location', 'Age 12-17', 'Age 18-64', 'Age 65+']]


    df_state = df_age.groupby('Location').mean()
    

    # Vaccination Rate in Age 12-17, set threshold line to 0.75
    plt.figure(figsize=[14, 10])
    df_state['Age 12-17'].plot(kind='bar')
    plt.legend()
    plt.xlabel('State')
    plt.ylabel('Vaccination Rate')
    plt.title('Vaccination Rate in Age 12-17')
    plt.axhline(y=0.75,linewidth=4,color='r')



    # Vaccination Rate in Age 18-64, set threshold line to 0.75
    plt.figure(figsize=[14, 10])
    df_state['Age 18-64'].plot(kind='bar')
    plt.legend()
    plt.xlabel('State')
    plt.ylabel('Vaccination Rate')
    plt.title('Vaccination Rate in Age 18-64')
    plt.axhline(y=0.75,linewidth=4,color='r')


    # Vaccination Rate in Age 65+, set threshold line to 0.75
    plt.figure(figsize=[14, 10])
    df_state['Age 65+'].plot(kind='bar')
    plt.legend()
    plt.xlabel('State')
    plt.ylabel('Vaccination Rate')
    plt.title('Vaccination Rate in Age 65+')
    plt.axhline(y=0.75,linewidth=4,color='r')



    # We were interested in states that had more than 75% of Vaccination Rate among age 18-64.
    threshold=dfx[dfx['Age 18-64']>0.75]
    threshold.plot(kind='bar')
    dff_state=threshold.groupby('Location').mean()
    dff_state['Age 18-64'].plot(kind='bar',color='r')
    plt.legend()
    plt.xlabel('State')
    plt.ylabel('Vaccination Rate')
    plt.title('States that have Vaccination Rate above 75% among Age 18-64')
    
    return plt.show('Vaccination Rate above 75%')
