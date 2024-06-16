from bs4 import BeautifulSoup
import datetime as dt

import utils
    
if __name__ == '__main__':
    all_aqi_data = list()

    print('Making request...')
    content = utils.make_request('https://aqicn.org/city/nigeria/abuja/us-embassy/')

    # Initialize beautiful soup
    soup = BeautifulSoup(content,'html.parser')

    print('Scraping relevant data...')

    # Start getting all required values
    pm25 = soup.find('div', class_='aqivalue').text
    temperature = soup.find('td', id='cur_t').text
    pressure = soup.find('td', id='cur_p').text
    humidity = soup.find('td', id='cur_h').text
    wind = soup.find('td', id='cur_w').text
    # temperature = soup.select_one('tr td#cur_t.tdcur').text

    aqi_data = {
        'date': dt.datetime.now().date().strftime('%d-%m-%Y'),
        'time': dt.datetime.now().time().strftime('%H:%M:%S'),
        'pm25': pm25,
        'temperature': temperature,
        'pressure': pressure,
        'humidity': humidity,
        'wind': wind,
    }
    all_aqi_data.append(aqi_data)

    utils.dict_to_csv(all_aqi_data)

    print(aqi_data)
      