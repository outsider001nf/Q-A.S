#++++++++++++VARIABLES_AND_ARRAYS
users = ["root"]
selected_user = "none"
log_func = False
motd_file = False
lib_folder = False
#++++++++++++VARIABLES_AND_ARRAYS_END
#????????????WRITED_MODULES_ZONE
try:
  from lib import *
  lib_folder = True
except ModuleNotFoundError:
  def red_text(text):
    print("\033[31m {}" .format(text))
  print(red_text("'lib' folder is not found"))
import datetime
now = datetime.datetime.now()
import threading
import os
#????????????WRITED_MODULES_ZONE_END
#!!!!!!!!!!!!FUNCTION_CLASSES_ZONE
def scan():
  scan = open("scan.py", "w")
  scan.write("import os\nprint(os.listdir('lib'))")
  scan.close()
  os.system("python scan.py > scan_result.txt")
def purple_text(text):
  print("\033[35m {}" .format(text))
def green_text(text):
  print("\033[32m {}" .format(text))
#!!!!!!!!!!!!FUNCTION_CLASSES_ZONE_END
try:
  motd = open("txt/motd.txt", "r")
  motd_file = True
  print(purple_text(motd.read()))
  motd.close()
except FileNotFoundError:
  print(red_text("'motd' file not found"))
try:
  log = open("log/inp_log.txt", "w")
  log_func = True
except FileNotFoundError:
  log_func = False
  print(red_text("log function is unreachable"))
#write scanner of installed cli_applicaton
if lib_folder == True:
  print(green_text("'lib' folder connected"))
  scan()
  if motd_file == True:
    print(green_text("'motd' file is enabled"))
    if log_func == True:
      print(green_text("log function is enabled"))
while True:
  scan_result = open("scan_result.txt", "r")
  usr_inp = input("user -> Q-A.S--> ")
  if log_func == True:
    log.write(now.strftime("%H:%M:%S on %A, %B the %dth, %Y: " + usr_inp + "\n"))
  if usr_inp == "exit":
    if log_func == True:
      log.close()
    break
  if usr_inp == "reboot_lib_view":
    scan()
  if usr_inp in scan_result.read():
    os.system("cd lib && python " + usr_inp)
