import requests
import csv
import json

gist_url = 'https://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiNjE2ODIxOCIsImRlbGl2ZXJ5X2lkIjoiNXM0dG00dHQ1am9lYnl6a2h1MWMiLCJ1cmwiOiJodHRwczovL2dpc3QuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3JldXZlbi83N2VkYmIwMjkyOTAxZjM1MDE5ZjE3ZWRiOTc5NDM1OC9yYXcvMmJmMjU4NzYzY2RkZGQ3MDRmOGZmZDNlYTlhM2U4MWQyNWUyYzZmNi9jaXRpZXMuanNvbj9fX3M9cXBqZmE2NWVmbXdwZDUyZHdnaHBcdTAwMjZ1dG1fc291cmNlPWRyaXBcdTAwMjZ1dG1fbWVkaXVtPWVtYWlsXHUwMDI2dXRtX2NhbXBhaWduPVdQRSsyMDIwK0IxK1x1MDAyNnV0bV9jb250ZW50PSU1QldlZWtseStQeXRob24rRXhlcmNpc2UrMjAyMCtCMSU1RCtFeGVyY2lzZSslMjM1KyVFMiU4MCU5NCtCaWcrY2l0aWVzIn0'

def cities_to_csv(url, filename):
    try:
        body = json.loads(requests.get(url).text)

        with open(filename, mode='w') as city_file:
            fieldnames = ['city', 'state', 'rank', 'population']
            writer = csv.DictWriter(city_file, fieldnames=fieldnames, delimiter='\t')
            #writer.writeheader()
            for each in body:
                writer.writerow({'city': each['city'], 'state': each['state'], 'rank': each['rank'], 'population': each['population']})
    except:
        print('Invalid URL')
