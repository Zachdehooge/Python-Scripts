import requests
import schedule
import datetime

# TODO: Have name of site populate the top of the log file

file_path = f"{datetime.datetime.now()}.log"

def fetch_url(url):
    response = requests.get(url)
    status_code = response.status_code
    response_time = response.elapsed.total_seconds()

    with open(file_path, 'a') as file:        
        if status_code == 200 and response_time < 0.5:
            file.write(f'Status Code: {status_code}, Response Time: {response_time}\n')
        else:
            file.write(f'TOOK TOO LONG: Status Code: {status_code}, Response Time: {response_time}\n')



test = input("Enter a site to get metrics for: ")

print(f"GETTING SITE DATA FOR: {test}")

schedule.every(0.05).seconds.do(fetch_url, test)

while True:
    schedule.run_pending()
