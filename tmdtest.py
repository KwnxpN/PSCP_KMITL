import requests
import json

url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/place"

querystring = {"province":u"สมุทรปราการ", "amphoe":u"เมืองสมุทรปราการ", "tambon":u"สำโรงเหนือ", "fields":"tc_max,rh", "date":"2023-09-16", "hour":"8", "duration":"2"}

headers = {
    'accept': "application/json",
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImU1OGY1Zjc1ZTAwMDcwNzg3OWJiZDJmYmZhN2RjNmU5NjkyZWMwZGI2MmQ1MjUwN2QzMzVlZDAzZDM1MDVjOGMyNmE1ZjQ4MGVkMWU1ZThlIn0.eyJhdWQiOiIyIiwianRpIjoiZTU4ZjVmNzVlMDAwNzA3ODc5YmJkMmZiZmE3ZGM2ZTk2OTJlYzBkYjYyZDUyNTA3ZDMzNWVkMDNkMzUwNWM4YzI2YTVmNDgwZWQxZTVlOGUiLCJpYXQiOjE2OTQ4NzI3MzMsIm5iZiI6MTY5NDg3MjczMywiZXhwIjoxNzI2NDk1MTMzLCJzdWIiOiIyNzYwIiwic2NvcGVzIjpbXX0.JXAGBO6YDx3l_bWGywWZw9W-ivNGGo4vjs5hJvEfKqCbiXvNCzldYTzbvlfXcgfMFwP6qIam_lRrPq-xvuFZXXkZSQiE2s78cfYnCuSXrVRFl7MYQySNdimks0sdl0F-nWGvHBg-STnsNUAiIooNtHkAJmb0xR5CPLba8TzEJ-yXIXIKwfhBGna__g9Shzw4W7BoVWqs-CzpFj4FE3Vm_w6luIdr_o3Dm8cEmDkoskqdOnxqsJRh3I7CN3hbqw5f1a7Cq_h7IyBdOi_aq57vjxH1LksDuBQCfHfOl7HE9jZUvNf31d7qNkl-WgQJ8hz0JwSELHsVePBfj4XW4B47KICq66oiYBd_mXjF-4Dk0dyntc-OnbdQcqXn6U_Ns1CgOV5eieQtjPiVj12Pd6QbB1ROZMXYtPm5wLODOxp_uFtfKkUmgTn5_LwKSmS6PYDi-9KSgazkye2J-kJlOuTkekITddD4KuovypUj4XMFWI62A-Y_9HoWxmnr1Pm0iBA6AxXgpKCMW1wfjCHfcuMNGJtf0AC8-oJi0LzADsoPOF8Px9pN04ynwasgJiunQA9tiNO9KYJ02umTracUkFfKYhPYj1ku2P_yV6zNUG7VlUoega0nw0YhajRy6vj3TJakLfQPBFVWKPPmfLTHoUa7nfeUqlpBZqQNehrZoULbvKQ",
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(json.loads(response.text))
