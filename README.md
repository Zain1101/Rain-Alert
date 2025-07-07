# Rain Alert System

This Python script checks the weather forecast using the OpenWeatherMap API and sends an SMS alert if it's going to rain — using Twilio.

## Features

- Uses [OpenWeatherMap](https://openweathermap.org/forecast5) 5-day/3-hour forecast
- Analyzes upcoming weather to detect rain
- Sends an SMS via [Twilio](https://www.twilio.com/) if rain is predicted

## How It Works

1. Gets forecast for the next 12 hours (via `cnt=4`)
2. Checks for weather condition codes `< 700` (indicating rain)
3. Sends an alert message if rain is expected

## Tech Stack

- Python
- `requests` library
- `twilio` Python package
- `python-dotenv` for secrets
- OpenWeatherMap API
- Twilio API

## Example Output

```bash
It is going to rain. Remember to carry the umbrella
