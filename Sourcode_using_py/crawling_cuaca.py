import requests
import json
import pandas as pd

def get_weather_data(api_key, location, start_date, end_date):
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    elements = "datetime,datetimeEpoch,temp,tempmax,tempmin,precip,windspeed,windgust,feelslike,feelslikemax,feelslikemin,pressure,stations,degreedays,accdegreedays"
    include = "fcst,obs,histfcst,stats,hours"
    options = "preview"
    
    url = f"{base_url}{location}/{start_date}/{end_date}?elements={elements}&include={include}&key={api_key}&options={options}&contentType=json"

    response = requests.get(url)

    if response.status_code == 200:
        # Mengonversi respons JSON ke bentuk Python
        weather_data = json.loads(response.text)
        return weather_data
    else:
        # Menampilkan pesan kesalahan jika permintaan gagal
        print(f"Terjadi Error. Status: {response.status_code}")
        return None

def save_to_excel(data, excel_filename):
    df = pd.DataFrame(data['days'])
    df.to_excel(excel_filename, index=False, engine='openpyxl')
    print(f"Data saved to {excel_filename}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your Visual Crossing Weather API key
    api_key = 'UHW9DCUNX38FQ56RPGSF6L7D9'

    # Replace 'jakarta/2021-06-17/2024-01-01' with your desired location and date range
    location = 'jakarta/2021-04-07/2024-01-01'

    # Replace 'output_file.xlsx' with the desired Excel file name
    excel_filename = 'output_file.xlsx'

    weather_data = get_weather_data(api_key, location, "", "")

    if weather_data:
        save_to_excel(weather_data, excel_filename)
