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
        with open('data/aqi_data.csv', 'r', encoding='utf-8') as f:
            file_exists = True
    except FileNotFoundError:
        pass
    
    with open('data/aqi_data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
        HEADERS = ['date', 'time', 'pm25', 'temperature', 'pressure', 'humidity', 'wind']
        
        # write header
        csv_writer = csv.DictWriter(csv_file, fieldnames=HEADERS)
        
        # Check if file exists
        if not file_exists:
            csv_writer.writeheader()
        
        # write rows
        csv_writer.writerows(data)
        