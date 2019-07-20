#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class ProxyTopo(Topo):
    """
    Topology with n hosts. At each host set defaultRoute via Squid proxy server
    """
    def build(self, n=4):
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1)

                                # defaultRoute='via 172.17.0.1:3128'
                                )

def simpleTest():
    """
    Create and test a simple network
    :return:
    """
    topo = ProxyTopo(n=4)
    net = Mininet(topo)
    net.start()
    h1 = net.get('h1')
    h2 = net.get('h2')
    h1.cmd("route add default gw 172.17.0.1:3128")
    print h1.cmd("route -n")
    print h2.cmd("route -n")
    # print "PPP"
    print h1.cmd('ping -c1 10.0.0.2' )
    # print "Dumping host connections"
    # dumpNodeConnections(net.hosts)
    # print "Testing network connectivity"
    # net.pingAll()
    net.stop()



if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
