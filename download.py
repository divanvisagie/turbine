import requests
import csv
import os


def download_json_data(latitude, longitude, start_date, end_date):
    url = 'https://archive-api.open-meteo.com/v1/era5'
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ['temperature_2m', 'snowfall']
    }
    request = requests.Request('GET', url, params=params)

    print(request.prepare().url)

    response = requests.Session().send(request.prepare())
    if response.status_code == 200:
        return response.json()
    else:
        print('Error: ', response.status_code)
        print('Message: ', response.text)


def download_and_save_data(latitude, longitude, start_date, end_date, name):
    if not os.path.exists('data'):
        os.makedirs('data')

    json_data = download_json_data(latitude, longitude, start_date, end_date)
    file_name = os.path.join('data', name + '.csv')
    with open(file_name, 'w') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["time", "temperature", "snowfall", "city"])

        # Iterate over the data and write each row to the CSV
        for i in range(len(json_data["hourly"]["time"])):
            writer.writerow([
                json_data["hourly"]["time"][i],
                json_data["hourly"]["temperature_2m"][i],
                json_data["hourly"]["snowfall"][i],
                name
            ])


def main():
    cities = [{
        "name": 'Stockholm',
        "latitude": 59.32,
        "longitude": 18.06
    }, {
        "name": 'Durban',
        "latitude": -29.86,
        "longitude": 31.03
    }, {
        "name": 'Cape Town',
        "latitude": -33.92,
        "longitude": 18.42
    }, {
        "name": 'Oslo',
        "latitude": 59.91,
        "longitude": 10.75
    }, {
        "name": 'London',
        "latitude": 51.51,
        "longitude": -0.13
    }]
    start_date = '2022-01-01'
    end_date = '2022-12-31'

    print('Start downloading data...')
    # Http Request data from https://open-meteo.com/
    for c in cities:
        download_and_save_data(c["latitude"], c["longitude"],
                               start_date, end_date, c["name"])
    # Save data to data.csv
    print('Data downloaded successfully!')


if (__name__ == '__main__'):
    main()
