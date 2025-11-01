# Send-data-dht11-to-Raspberry-Pi-and-display-it-on-CircusOfThings
Send data dht11 to a Raspberry Pi and display it on CircusOfThings, then display it on the CircusOfThings platform. We used HTTP requests.
- Install the following libraries: requests, json, and W1ThermSensor

- Create a circusofthings.com account

- In https://circusofthings.com/workshop, create a new signal and name it temp_c and temp_f
- Key: 28440 for temp_c (example)
- Key: 28441 for temp_f (example)

- Go to https://circusofthings.com/dashboard,

- Click on View: Add a view to monitor the value of an existing signal.

- Choose temp_c and temp_f

- Run the code; it will display the sensor values ​​on the dashboard.
