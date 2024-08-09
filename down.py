import requests

url = 'https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata'  # Replace with the URL of the CSV file
response = requests.get(url)

if response.status_code == 200:
    with open('downloaded_file.csv', 'wb') as file:
        file.write(response.content)
    print('CSV file downloaded successfully.')
else:
    print(f'Failed to download CSV file. Status code: {response.status_code}')
