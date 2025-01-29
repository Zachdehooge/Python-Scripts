import requests
import schedule
import datetime

# TODO: Have name of site populate the top of the log file


print(
    r"""
 /$$   /$$             /$$     /$$                        
| $$  | $$            | $$    |__/                        
| $$  | $$  /$$$$$$  /$$$$$$   /$$ /$$$$$$/$$$$   /$$$$$$ 
| $$  | $$ /$$__  $$|_  $$_/  | $$| $$_  $$_  $$ /$$__  $$
| $$  | $$| $$  \ $$  | $$    | $$| $$ \ $$ \ $$| $$$$$$$$
| $$  | $$| $$  | $$  | $$ /$$| $$| $$ | $$ | $$| $$_____/
|  $$$$$$/| $$$$$$$/  |  $$$$/| $$| $$ | $$ | $$|  $$$$$$$
 \______/ | $$____/    \___/  |__/|__/ |__/ |__/ \_______/
          | $$                                            
          | $$                                            
          |__/                                            

A Python Script that shows the response time from a website

"""


)

file_path = f"{datetime.datetime.now().strftime('%Y-%m-%d')}_Site.log"


def fetch_url(url):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = requests.get(url)
    status_code = response.status_code
    response_time = response.elapsed.total_seconds()

    with open(file_path, "a") as file:
        if status_code == 200 and response_time < 0.5:
            file.write(
                f"{current_time}: Status Code: {status_code}, Response Time: {response_time}\n"
            )
        else:
            file.write(
                f"TOOK TOO LONG: Status Code: {status_code}, Response Time: {response_time}\n"
            )


site_URL = input("Enter a site to get metrics for: ")

file1 = open(file_path, 'w')
file1.write(f"GETTING SITE DATA FOR: {site_URL}\n")
file1.close()


#print(f"GETTING SITE DATA FOR: {site_URL}")

schedule.every(0.5).seconds.do(fetch_url, site_URL)

while True:
    schedule.run_pending()
