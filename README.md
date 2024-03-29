#  Demonstrator for Controls through Web-based Application and Drawing Robot
This is a Streamlit app that provides a library of number theory patterns that can be sent to a Raspberry Pi robot to print out. The patterns are based on various number theory concepts and can be customized with different parameters to create unique designs.

## How it Works

The app is built using the Streamlit Python library and communicates with the Raspberry Pi robot via a Bluetooth using the socket library. Users can select from a variety of pre-defined number theory patterns or create their own by adjusting parameters.

Once a pattern is selected, the app sends an array of points to the Raspberry Pi robot, which uses a movement algorithm to follow the desired path, accelerating and deccelerating when necessary. The user can then watch as the pattern is drawn in real time.

## Website
https://capstoneproject.streamlit.app/

## How to Run the App

To run the app, you'll need to follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Run the app using the command `streamlit run Test.py` or `python -m streamlit run Test.py`.
4. Connect your Raspberry Pi to your computer via Bluetooth.
5. Open the `Backend/SendData.py` file and change line 19/20 to the MAC address of your Raspberry Pi.
6. Open your web browser and navigate to `http://localhost:8501` to view the app.
7. On your Raspberry Pi, uncomment and run the `RPI/Movement.py` file.
8. Once you have chosen a pattern, press the print button to send the data to the robot.
9. Click the button on the robot to start the print!

Note: You can adjust the size of the print by scaling the points in the Transform function in `Backend/SendData.py`

Note: You may need to adjust the port argument in the `bot.motorRun(port, speed)` call in the `set_wheel_speed` function in `RPI/Movement.py` based on which port each motor is plugged into.
Use the follow graphic as a reference:

![MegaPi Board Ports](https://github.com/GarPorter/Capstone/blob/Streamlit/Images/megapi.jpg?raw=true)

## Capstone Poster

![Capstone Poster](https://github.com/GarPorter/Capstone/blob/Streamlit/Images/Capstone_Poster_JPEG.jpg)
[PDF Copy](https://github.com/GarPorter/Capstone/blob/Streamlit/Images/Capstone_Poster_2023.pptx.pdf)
