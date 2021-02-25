import requests
email = "rekiker958@edultry.com"

# TODO: update to login to this thing to get the jwt
cookies = {
    'jwt': 'eyJraWQiOiJ2NSIsImFsZyI6IkhTMjU2In0.eyJzdWIiOiIyMDAwMTQzNDM2NjEiLCJleHAiOjE2MTQyOTU2MTIsImlhdCI6MTYxNDI5MzgxMiwiaXNzIjoid2FsZ3JlZW5zLmNvbSIsImF1ZCI6ImRvdGNvbSIsImp0aSI6ImQ2MjdiYzJhLThjYzAtNGYwMS05ZWNkLTEyNWY1ZTZmNDRlZiJ9.RYOlkzTUEYUfEaeqksuyjyvQ_cZmE75ba6lSZivcUhg',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json; charset=utf-8',
    'X-XSRF-TOKEN': 'VgAxjCvBiwQS/w==.vtK6y8MuwZUE5klYghRrkeZLcU+eRpbN4F9dhlYEYlI=',
    'Origin': 'https://www.walgreens.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.walgreens.com/findcare/vaccination/covid-19/location-screening',
    'Sec-GPC': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

data = '{"serviceId":"99","position":{"latitude":41.6882419,"longitude":-93.7943157},"appointmentAvailability":{"startDateTime":"2021-02-26"},"radius":25}'

response = requests.post('https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability', headers=headers, cookies=cookies, data=data)
print(response.json())

