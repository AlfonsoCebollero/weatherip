# weatherip
## Deploying the app
1. Edit /app/properties.py to add your weather API Token in the field TOKEN. It is not included by default for security reasons.
2. From the project base directory run:
    - docker build -t weatherip .
    - docker run -d --name weatheripc -p 80:80 weatherip

## Making a query
**http://127.0.0.1/weather/24.48.0.1**

Expected response:

{"weather": [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}], "main": {"temp": 261.73, "feels_like": 255.7, "temp_min": 256.35, "temp_max": 263.83, "pressure": 1015, "humidity": 76, "sea_level": 1015, "grnd_level": 1001}, "visibility": 10000, "wind": {"speed": 3.19, "deg": 168, "gust": 8.44}, "clouds": {"all": 100}, "name": "Montreal"}
