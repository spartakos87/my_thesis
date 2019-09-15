"""An example of constructing a profile with four physical nodes connected by a Link.

Instructions:
Wait for the profile instance to start, and then log in to either host.

This file will upload to powder to recreate the topology
"""

import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create four raw "PC" nodes
client_1 = request.RawPC("client1")
client_2 = request.RawPC("client2")
client_3 = request.RawPC("client3")
client_4 = request.RawPC("client4")
switch_1 = request.RawPC("switch1")
switch_2 = request.RawPC("switch2")
switch_3 = request.RawPC("switch3")  # This is the master switch which connect switch 1 & 2
controller = request.RawPC("controller")

# Proxy server will run inside switches 1 & 2
# proxy_server_1 = request.RawPC("proxy_server1")
# proxy_server_2 = request.RawPC("proxy_server2")

# Set up servers which clients will ping
server_1 = request.RawPC("server1")
server_2 = request.RawPC("server2")
# Setup python servers in server_1 and server_2


# Install Squid in proxy_server
install_squid = "sudo apt-get --assume-yes install squid"
update = "sudo apt-get update"

# proxy_server_1.addService(rspec.Execute(shell="bash", command=update+"; "+install_squid))
# proxy_server_2.addService(rspec.Execute(shell="bash", command=update+"; "+install_squid))


# Install POX in controller node 

cmd = "cd /home && sudo mkdir POX && sudo  git clone http://github.com/noxrepo/pox"
controller.addService(rspec.Execute(shell="bash", command=cmd))

# Controller will be out of net
# link1 = request.Link(members=[switch_1, controller])
# link2 = request.Link(members=[switch_2, controller])

link3 = request.Link(members=[client_1, switch_1])
link4 = request.Link(members=[client_2, switch_1])
link5 = request.Link(members=[client_3, switch_2])
link6 = request.Link(members=[client_4, switch_2])
# link7 = request.Link(members=[proxy_server_2, switch_2])
# link8 = request.Link(members=[proxy_server_1, switch_1])

# Switches and Proxy serves will be lingked with servers
# link9 = request.Link(members=[proxy_server_1, server_1])
# link10 = request.Link(members=[proxy_server_1, server_2])
# link11 = request.Link(members=[proxy_server_2, server_1])
# link12 = request.Link(members=[proxy_server_2, server_2])
# link = request.Link(members=[switch_1, server_1])
# link10 = request.Link(members=[switch_2, server_2])


# Link only switch3 with servers
link7 = request.Link(members=[switch_3, server_1])
link8 = request.Link(members=[switch_3, server_2])

# After linked
# Install ovs in switches
ovs_install = "sudo apt-get --assume-yes install openvswitch-switch"
# Setup the switch and run it
get_py_config_file = "wget https://github.com/spartakos87/my_thesis/blob/master/powderwireless/setup_switch1.py"
run_py_script = "python setup_switch1.py "
# Additionally must install the Squid
switch_1.addService(rspec.Execute(shell="bash", command=update+" && "+ovs_install+ " && "+ get_py_config_file+ " && "
                                                        +run_py_script+"0" + " && " + install_squid))
switch_2.addService(rspec.Execute(shell="bash", command=update+" && "+ovs_install+" && "+get_py_config_file+" && "
                                                        +run_py_script+"1" + " && " + install_squid))

# In switch3 install, at least at first , only the ovs, create new py file to make the connects
switch_3.addService(rspec.Execute(shell="bash", command=update+" && "+ovs_install))
link9 = request.Link(members=[switch_3, switch_1])
link10 = request.Link(members=[switch_3, switch_2])
portal.context.printRequestRSpec()
