#!/usr/bin/python


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        """

        :return:
        """
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
    # def build(self, n=2):
        switch = self.addSwitch('s1')
        host1 = self.addHost('h1',
                            defaultRoute='via 172.17.0.1:3128')
        self.addLink(host1, switch)
        host2 = self.addHost('h2')
        self.addLink(host2, switch)
        # # Python's range(N) generates 0..N-1
        # for h in range(n):
        #     host = self.addHost('h%s' % (h + 1))
        #     self.addLink(host, switch)


def simpleTest():
    "Create and test a simple network"
    # topo = SingleSwitchTopo(n=10000)
    topo = SingleSwitchTopo()
    net = Mininet(topo)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()


if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
