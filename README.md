# SkyCast - Your Modern Weather Companion
#### Video Demo: [Your Video URL Here]

## Description:
Welcome to SkyCast, a sleek and modern web app designed to keep you informed about the current weather and the forecast for the next 7 days. Developed by Mohammed Taha Rafi Farooqui as the final project for CS50, SkyCast offers a user-friendly interface and accurate weather data, making it your go-to weather companion.

## Project Structure:

### helpers.py
This file contains the backend functionality of SkyCast. It utilizes the `requests` library to interact with the [WeatherAPI](http://api.weatherapi.com/) and fetch real-time weather information. The `get_weather` function retrieves the current weather for a given country and city, while the `get_forecast` function fetches the 7-day forecast. The `get_icon` function maps weather condition codes to corresponding icons, enhancing the visual appeal of the app.

### app.py
The heart of SkyCast, `app.py`, leverages Flask, a Python web framework, to create a seamless user experience. The two main routes, "/" and "/weather," handle the rendering of the homepage and the weather information page, respectively. The `weather` route dynamically fetches and displays weather and forecast data based on user input, providing a personalized experience.

## Usage:
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/MTahaRF/SkyCast
   ```

2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Set up a virtual environment and run the Flask app.
   ```bash
   flask run
   ```

4. Access the app in your browser at [http://localhost:5000/](http://localhost:5000/).

## Design Choices:
- **Modern Theme**: The app's design follows a modern and intuitive layout, enhancing the user experience and making weather information easily accessible.

- **Weather Icons**: Weather conditions are visually represented with icons, providing a quick and recognizable way to understand the forecast.

- **Error Handling**: The code includes robust error handling to address issues such as incorrect country or city input, ensuring a smooth user experience.

## Conclusion:
SkyCast is more than just a weather app; it's a culmination of coding skills demonstrated through the CS50 course. Explore the code, try out the app, and embrace the simplicity and elegance of SkyCast. Your weather updates have never looked this good!

Feel free to watch the [demo video](Your Video URL Here) for a visual walkthrough of SkyCast and its features.

Happy coding!
