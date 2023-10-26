from netmiko import ConnectHandler
import pprint
device = {
          'device_type': 'cisco_xr',
          'ip': '10.1.230.131',
          'username': 'admin',
          'password': 'P@ssw0rd',
      }
with ConnectHandler(**device) as net_connect:
          output = net_connect.send_command('show interfaces', use_textfsm=True)
          pprint.pprint(output)