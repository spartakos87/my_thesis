"""An example of constructing a profile with four physical nodes connected by a Link.

Instructions:
Wait for the profile instance to start, and then log in to either host.
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
controller = request.RawPC("controller")
proxy_server_1 = request.RawPC("proxy_server1")
proxy_server_2 = request.RawPC("proxy_server2")
# server = request.RawPC("server")

# Install Squid in proxy_server
install_squid = "sudo apt-get --assume-yes install squid"
update = "sudo apt-get update"
proxy_server_1.addService(rspec.Execute(shell="bash", command=update+"; "+install_squid))
proxy_server_2.addService(rspec.Execute(shell="bash", command=update+"; "+install_squid))

# Install ovs in switches
ovs_install = "sudo apt-get --assume-yes install openvswitch-switch"
switch_1.addService(rspec.Execute(shell="bash", command=update+"&& "+ovs_install))
switch_2.addService(rspec.Execute(shell="bash", command=update+"&& "+ovs_install))

# Install POX in controller node 

cmd = "cd /home && sudo mkdir POX && sudo  git clone http://github.com/noxrepo/pox"
controller.addService(rspec.Execute(shell="bash", command=cmd))


link1 = request.Link(members = [switch_1, controller])
link2 = request.Link(members = [switch_2, controller])
link3 = request.Link(members = [client_1, switch_1])
link4 = request.Link(members = [client_2, switch_1])
link5 = request.Link(members = [client_3, switch_2])
link6 = request.Link(members = [client_4, switch_2])
link7 = request.Link(members = [proxy_server_2, switch_2])
link8 = request.Link(members = [proxy_server_1, switch_1])


portal.context.printRequestRSpec()
