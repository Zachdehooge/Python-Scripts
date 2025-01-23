import requests
import schedule

# TODO: Output to log file with URL and date being the file name

def fetch_url(url):
    response = requests.get(url)
    status_code = response.status_code
    response_time = response.elapsed.total_seconds()
   
    if status_code == 200 and response_time < 0.5:
        print(f'Status Code: {status_code}, Response Time: {response_time}')
    else:
        print(f'TOOK TOO LONG: Status Code: {status_code}, Response Time: {response_time}')



test = input("Enter a site to get metrics for: ")

print(f"GETTING SITE DATA FOR: {test}")

schedule.every(0.5).seconds.do(fetch_url, test)

while True:
    schedule.run_pending()
