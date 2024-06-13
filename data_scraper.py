from bs4 import BeautifulSoup
import requests, csv, datetime as dt

def make_request(url):
    '''Function to make a request to a certina url'''
    
    try:
        req = requests.get(url)
        
        if req.status_code == 200:
            print('Request successful')
        else:
            print('Request unsuccessful')
    except Exception as e:
        print(f'An error occured: {e}')
        
    return req.content


def dict_to_csv(data: dict):
    '''Function to write data to csv'''
    
    # Track if file exists or not
    file_exists = False
    try:
        with open('aqi_data.csv', 'r', encoding='utf-8') as f:
            file_exists = True
    except FileNotFoundError:
        pass
    
    with open('aqi_data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
        HEADERS = ['date', 'time', 'pm25', 'temperature', 'pressure', 'humidity', 'wind']
        
        # write header
        csv_writer = csv.DictWriter(csv_file, fieldnames=HEADERS)
        
        # Check if file exists
        if not file_exists:
            csv_writer.writeheader()
        
        # write rows
        csv_writer.writerows(data)
    

if __name__ == '__main__':
    all_aqi_data = list()
    
    content = make_request('https://aqicn.org/city/nigeria/abuja/us-embassy/')
    
    # Initialize beautiful soup
    soup = BeautifulSoup(content,'html.parser')
    
    # Start getting all required values
    pm25 = soup.find('div', class_='aqivalue').text
    temperature = soup.find('td', id='cur_t').text
    pressure = soup.find('td', id='cur_p').text
    humidity = soup.find('td', id='cur_h').text
    wind = soup.find('td', id='cur_w').text
    
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
    
    dict_to_csv(all_aqi_data)
    
    print(aqi_data)
    
    
    
    
            
               