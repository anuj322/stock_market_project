import requests

cookies = {
    'AKA_A2': 'A',
    'nsit': 'ax1ZP0WqP_n0n-oXMnfP6eKf',
    'bm_mi': '76053D8B9E32E13BB351E921E10F8E02~YAAQb106F04BJ5uQAQAAhZFvphihe0KxmHcHKrfWJADb2mKR2zHeWxWQuwLJsQQCEFMUgg3n/pb8M+44zPUW0T1AU6ba6zfOq7AbkO1lbzs+yTgDpwpOBXGwJES0ybNw9jRL8f9zSAPb/fR9KQSPofs2fyEEjDypWA9Qe7N4tBS1Ccha7Qtsmp5EEiYmMPRjtYAxlud0MKLviCq0FI0RliHhcrd03DNMwdz6WQ83C44JpCy9fUa989NUgrGnrRzlqM1VTveChOlhdEhmeh9vhdjNlagT8IzOvo+wiDj6Q9Qx6qrJ/UGshYmXzAWX3w4jX2//v1h7hqUznSwuypk=~1',
    'defaultLang': 'en',
    '_ga': 'GA1.1.1283185097.1720779252',
    'ak_bmsc': 'C0C0A40F00F93E27EE763F482D1D17A9~000000000000000000000000000000~YAAQb106F+gBJ5uQAQAAb59vphhHFpty60ABtTmxrrD9CoC3d6942VOCDCw+8zOjXjZwcoCs2/90dWss6uQ7lOb2ycXbrLd1OKfKpE8mYzltxsEklB+ZlQRDv9KF5tLWmgbrHjIQiju8Tjax/4PyceKo606LVEN/5DgyeGAHJIART+5GBdkfgIFyh8MfFhtcun6uLHpFlhKTRGaRiN3CYmRTkpk+JYe0zETIL4cLTmhvz0inplqSzdhzXPCeayat71XaFbK/O6ugeyXCpnMcGfaU9Vb0lzcfFbEJYwlWJDM0gAyI7kiA47d5CYGHkum2SL9VW1215iFf2CwKIpfhPmAi99+hBlJ31qjP3H2UhHUAsE2nLx0VfW0PCBYr+/xPwQLJRvG4u4FiyvASYqEKBZtU+1Lc8Lv9VsSTaxaSCRrYodCv2nsa71zAQEJ3F8OCLO0a4o4p1JKQS1nTncSHOIENduz3YZD6J9fOJ/v8TxGGnBjUwSTBauzxUDftYap/',
    '_abck': '515594A6AE4AC0897F80D6E223F01ADD~0~YAAQb106FyACJ5uQAQAAHaRvpgzv1waQnKCi7YoHiL4QxE2EQ+aJcGVeTWp3DAdpzbvCUZR+C76FkbLSMrItlo/CvTdGnua8NZXdthQK09uxAbI+avT7Ggc5J+47r5BXxMOupBeNqhastxJXg1O9FSh1mG2jzcRDN+4cSVsnWW8oA83OLa0KjQLMj86xBMWzXU0tH3QiR1K0yp11U7VK1hKI5ldB0AR4UvLqV8lcHoqi7VgMYUkuwZu6e4XXTSb7Ah+jXtqQVHHUoSJBtD6GY18i11FsK+A6APrxg+BU5ADIGrm9+8xXMKOeGPQG7Zz7cpe+/nkmZ5lKmN4YoNL4/bzWn0jFQSQGt162Nrp9JlQKA5aVdLdDpfY+Tm4ZmjRIyOPehi6DMACN3kqvAPqeRXYHqoXxzdWE7CBR~-1~-1~-1',
    'nseappid': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcyMDc3OTI2MCwiZXhwIjoxNzIwNzg2NDYwfQ.YhbpwYyORgBeZ1H1rC2oWiNdCyQK3alIF5UCGzI6Bnw',
    'bm_sz': 'DC4919550CE1AD53C3AECEF5FCD8A905~YAAQb106FzUDJ5uQAQAAtsBvphiBmBbFuNjStP2ojHLGXV8ZfO5lTh7Y8blfCXXD3YXtVcqUGw2+vwGJhGl6WNqd3B0Ctqz5OthN+HvFP63UpUyojCwR4w84+6ceEeL4wqW6HzGuO6IQmJQGr8SHVBlh7vAFR0YESLBMsuwbjpx1piZegfhVBBnPpGnq77W/LKglLe0mrGSCUKfx+v/99p+k5/iuM+d8VS/bhgRj5PNS4Jm9PAQSZcIAJU7fkcNvap+jmBZoau+CjRGvE2GiAKyBPHxMk9B9NjnHLR8kaGtVGlVfMpl0un5a0usBaM7CVfrpahE16+oZyRW8UFoFJyVRa013wFyfM9YVwm22SLEW31FZLucQr6Pv9ujeXsZtCMbcCzfH4i34ozat3p3TkG4xqkbSXKTDuZgT+OTj3CQ9xkiyQROn3jI=~3551300~3617329',
    'nseQuoteSymbols': '[{"symbol":"IREDA","identifier":null,"type":"equity"},{"symbol":"75IREDA34","identifier":null,"type":"bonds"}]',
    'bm_sv': 'B735F6325C50AAB6D70C242A8936FC83~YAAQb106FyYFJ5uQAQAAYQBwphhM/feZv9A/uZaoXMR63MqDhQVjD7xN4+ydO2gr8rLypJDBbLKGC6fxehyZoxOGR1AGXatTjrnLY/02OMShpfXdKUWr9bH0T1IMtHVVz2F3F7oM30J2M6HJ4J3HsaSeB/ewc8PS0rL2eEsn6u9zWYLEu7UwSBNmEkaqCoeSKxn89ikRsGzY+nscSaCKYO2tbwbWs8diNAMGLNCa8RRRjHsXOtfQ8MzY/uyl4XmVozZb~1',
    'RT': '"z=1&dm=nseindia.com&si=f4624fa8-d67f-4b57-a754-f35ec3a71c28&ss=lyijj99x&sl=2&se=8c&tt=40k&bcn=%2F%2F684d0d43.akstat.io%2F&ld=7gw&nu=4qwisfbs&cl=9k3&ul=43g1&hd=43gh"',
    '_ga_87M7PJ3R97': 'GS1.1.1720779251.1.1.1720779438.57.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'AKA_A2=A; nsit=ax1ZP0WqP_n0n-oXMnfP6eKf; bm_mi=76053D8B9E32E13BB351E921E10F8E02~YAAQb106F04BJ5uQAQAAhZFvphihe0KxmHcHKrfWJADb2mKR2zHeWxWQuwLJsQQCEFMUgg3n/pb8M+44zPUW0T1AU6ba6zfOq7AbkO1lbzs+yTgDpwpOBXGwJES0ybNw9jRL8f9zSAPb/fR9KQSPofs2fyEEjDypWA9Qe7N4tBS1Ccha7Qtsmp5EEiYmMPRjtYAxlud0MKLviCq0FI0RliHhcrd03DNMwdz6WQ83C44JpCy9fUa989NUgrGnrRzlqM1VTveChOlhdEhmeh9vhdjNlagT8IzOvo+wiDj6Q9Qx6qrJ/UGshYmXzAWX3w4jX2//v1h7hqUznSwuypk=~1; defaultLang=en; _ga=GA1.1.1283185097.1720779252; ak_bmsc=C0C0A40F00F93E27EE763F482D1D17A9~000000000000000000000000000000~YAAQb106F+gBJ5uQAQAAb59vphhHFpty60ABtTmxrrD9CoC3d6942VOCDCw+8zOjXjZwcoCs2/90dWss6uQ7lOb2ycXbrLd1OKfKpE8mYzltxsEklB+ZlQRDv9KF5tLWmgbrHjIQiju8Tjax/4PyceKo606LVEN/5DgyeGAHJIART+5GBdkfgIFyh8MfFhtcun6uLHpFlhKTRGaRiN3CYmRTkpk+JYe0zETIL4cLTmhvz0inplqSzdhzXPCeayat71XaFbK/O6ugeyXCpnMcGfaU9Vb0lzcfFbEJYwlWJDM0gAyI7kiA47d5CYGHkum2SL9VW1215iFf2CwKIpfhPmAi99+hBlJ31qjP3H2UhHUAsE2nLx0VfW0PCBYr+/xPwQLJRvG4u4FiyvASYqEKBZtU+1Lc8Lv9VsSTaxaSCRrYodCv2nsa71zAQEJ3F8OCLO0a4o4p1JKQS1nTncSHOIENduz3YZD6J9fOJ/v8TxGGnBjUwSTBauzxUDftYap/; _abck=515594A6AE4AC0897F80D6E223F01ADD~0~YAAQb106FyACJ5uQAQAAHaRvpgzv1waQnKCi7YoHiL4QxE2EQ+aJcGVeTWp3DAdpzbvCUZR+C76FkbLSMrItlo/CvTdGnua8NZXdthQK09uxAbI+avT7Ggc5J+47r5BXxMOupBeNqhastxJXg1O9FSh1mG2jzcRDN+4cSVsnWW8oA83OLa0KjQLMj86xBMWzXU0tH3QiR1K0yp11U7VK1hKI5ldB0AR4UvLqV8lcHoqi7VgMYUkuwZu6e4XXTSb7Ah+jXtqQVHHUoSJBtD6GY18i11FsK+A6APrxg+BU5ADIGrm9+8xXMKOeGPQG7Zz7cpe+/nkmZ5lKmN4YoNL4/bzWn0jFQSQGt162Nrp9JlQKA5aVdLdDpfY+Tm4ZmjRIyOPehi6DMACN3kqvAPqeRXYHqoXxzdWE7CBR~-1~-1~-1; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcyMDc3OTI2MCwiZXhwIjoxNzIwNzg2NDYwfQ.YhbpwYyORgBeZ1H1rC2oWiNdCyQK3alIF5UCGzI6Bnw; bm_sz=DC4919550CE1AD53C3AECEF5FCD8A905~YAAQb106FzUDJ5uQAQAAtsBvphiBmBbFuNjStP2ojHLGXV8ZfO5lTh7Y8blfCXXD3YXtVcqUGw2+vwGJhGl6WNqd3B0Ctqz5OthN+HvFP63UpUyojCwR4w84+6ceEeL4wqW6HzGuO6IQmJQGr8SHVBlh7vAFR0YESLBMsuwbjpx1piZegfhVBBnPpGnq77W/LKglLe0mrGSCUKfx+v/99p+k5/iuM+d8VS/bhgRj5PNS4Jm9PAQSZcIAJU7fkcNvap+jmBZoau+CjRGvE2GiAKyBPHxMk9B9NjnHLR8kaGtVGlVfMpl0un5a0usBaM7CVfrpahE16+oZyRW8UFoFJyVRa013wFyfM9YVwm22SLEW31FZLucQr6Pv9ujeXsZtCMbcCzfH4i34ozat3p3TkG4xqkbSXKTDuZgT+OTj3CQ9xkiyQROn3jI=~3551300~3617329; nseQuoteSymbols=[{"symbol":"IREDA","identifier":null,"type":"equity"},{"symbol":"75IREDA34","identifier":null,"type":"bonds"}]; bm_sv=B735F6325C50AAB6D70C242A8936FC83~YAAQb106FyYFJ5uQAQAAYQBwphhM/feZv9A/uZaoXMR63MqDhQVjD7xN4+ydO2gr8rLypJDBbLKGC6fxehyZoxOGR1AGXatTjrnLY/02OMShpfXdKUWr9bH0T1IMtHVVz2F3F7oM30J2M6HJ4J3HsaSeB/ewc8PS0rL2eEsn6u9zWYLEu7UwSBNmEkaqCoeSKxn89ikRsGzY+nscSaCKYO2tbwbWs8diNAMGLNCa8RRRjHsXOtfQ8MzY/uyl4XmVozZb~1; RT="z=1&dm=nseindia.com&si=f4624fa8-d67f-4b57-a754-f35ec3a71c28&ss=lyijj99x&sl=2&se=8c&tt=40k&bcn=%2F%2F684d0d43.akstat.io%2F&ld=7gw&nu=4qwisfbs&cl=9k3&ul=43g1&hd=43gh"; _ga_87M7PJ3R97=GS1.1.1720779251.1.1.1720779438.57.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0',
}

params = {
    'index': 'SECURITIES IN F&O',
}

response = requests.get('https://www.nseindia.com/api/equity-stockIndices', params=params, cookies=cookies, headers=headers)
print(response.text)