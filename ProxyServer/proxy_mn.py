#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class ProxyTopo(Topo):
    """
    Topology with for hosts.
    The host number one will "play" the role of the proxy
    In host number1 will running the Squid proxy server
    All the host will be connected only with host one
    """
    def build(self, n=4):
        proxy_host = self.addHost('h0')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, proxy_host)

def simpleTest():
    """
    Create and test a simple network
    :return:
    """
    topo = ProxyTopo(n=4)
    net = Mininet(topo)
    net.start()
    proxy_host = net.get('h0')
    proxy_host.cmd('service squid start')
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
