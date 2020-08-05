import request
import sys
import glob
import smbus
import socket

hostname = socket.gethostname()

def i2c():
        bus = smbus.SMBus(1)
        array = ["kein geraet gefunden"]
        for device in range(128):
                try:
                        bus.read_byte(device)
                        array.append(str(hex(device)))
                except:
                        pass
        if not array == ["kein geraet gefunden"]:
                del array[0]
        return array

iquadc = i2c()


def pserial():

  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial
serial = pserial()
r = requests.post("http://www.google.de", data={'hostname': hostname, 'i2c': iquadc, 'serial': serial})
