#######################################################################################################
# SET UP #
from setup import *
#######################################################################################################

# LOGIQUE #

# Météo France
result_meteo = requests.get(url_meteo)
soup_meteo = BeautifulSoup(result_meteo.text, 'html.parser')
image_meteo = soup_meteo.find('img', id='image')
hours = soup_meteo.find('select', id='heures')
selected_hour = hours.find(attrs={"selected" : True})

f = open('/tmp/today.jpg','wb')
response = requests.get(image_meteo['src'])
f.write(response.content)
f.close()
    
# Levé / Couché du soleil today
result_sun = requests.get(url_sun)
soup_sun = BeautifulSoup(result_sun.text, 'html.parser')
today = soup_sun.find('td', class_="today")
today_sunrise = today.find('span', class_='sunrise')
today_sunset = today.find('span', class_='sunset')
    
#######################################################################################################
    
# CREATION DU MESSAGE #
message_content = 'Bonjour, nous sommes le ' + current_date + '\nLe soleil se lèvera à ' + today_sunrise.text + ' et se couchera à ' + today_sunset.text + '\nRetrouvez la météo en France à ' + selected_hour.text + '\nL\'ensemble de votre météo : ' + url_meteo + '\n(Source : ' + url_meteo + ')'
    
print(message_content)
    
# Récupération de l'image
media = "/tmp/today.jpg"

#######################################################################################################
    
# TWEET #
api.update_status_with_media(status=message_content, filename=media)
#api.update_status(status=message_content)
    
#######################################################################################################