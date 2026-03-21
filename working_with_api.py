import requests

# Bengaluru coordinates
latitude = 12.9716
longitude = 77.5946

# Build the API URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

data["current"]["temperature_2m"]

#writing functions to extract what we need
def get_current_temperature(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temperature_2m"]
paris_temp = get_current_temperature(48.8566, 2.3522)  # Paris coordinates
bengaluru_temp = get_current_temperature(12.9716, 77.5946)  # Bengaluru coordinates
delhi_temp = get_current_temperature(28.7041, 77.1025)  # Delhi coordinates


print(f"Paris: {paris_temp}°C")
print(f"Bengaluru: {bengaluru_temp}°C")
print(f"Delhi: {delhi_temp}°C")