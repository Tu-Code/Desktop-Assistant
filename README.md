# Desktop-Assistant
What it does:
1. Executable python application that uses voice-recognition software to listen for, and execute commands (runs on any device) 💻
1. Monitors desktop resources (on-site or remotely) in real-time and returns stats to user 📝
1. Comes with REST-API and web-socket channel
### How to use it:
 Make sure you have python 3.8+ installed
 Create a virtual environment
 run `pip install -r requirements.txt` to install the required modules
 run `python -m app` in the terminal/command-prompt
 To test resource monitor, run the python script in tests/rest_client.py
 Feel free to change the host and port
 -To test voice-recognition through executable: Navigate to the dist folder and execute the .exe file to run your personal desktop assistant or run through voice.py
 ### Routes
 1. GET /
 This route to is to get all information about PC

 2. GET /battery
 This returns the PC's battery percent

 3. GET /memory
 This returns the PC's memory information

 4. GET /network
 This returns the PC's information about it's connected network devices

 5. GET /processor
 This returns a list of processes and their information
 
 Example of how to check usign voice recognition: "what's my battery percent", "show connected devices", "show all computer resources", etc.
