"""An example of constructing a profile with four physical nodes connected by a Link.

Instructions:
Wait for the profile instance to start, and then log in to either host.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create four raw "PC" nodes
client = request.RawPC("client")
controller = request.RawPC("controller")
proxy_server = request.RawPC("proxy_server")
server = request.RawPC("server")

# Install Squid in proxy_server
install_squid = "sudo apt-get --assume-yes install squid"
update = "sudo apt-get update"
proxy_server.addService(rspec.Execute(shell="bash", command=update+"; "+install_squid))

# Install POX in controller node 

cmd = "cd /home && sudo mkdir POX && sudo  git clone http://github.com/noxrepo/pox"
controller.addService(rspec.Execute(shell="bash", command=cmd))

# Create a link between them
link1 = request.Link(members = [client, controller])
link2 = request.Link(members = [controller, proxy_server])
link3 = request.Link(members = [proxy_server, server])

portal.context.printRequestRSpec()
