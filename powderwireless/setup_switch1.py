"""
Basic to this tutorila
https://viveksubbarao.wordpress.com/2015/11/17/how-to-setup-a-sdn-using-openvswitch-and-odl-controller/ set up ovs
"""
# Get the ip when I ping
#ping google.com -c1 | head -1 | grep -Eo '[0-9.]{4,}'

# Get eth from ifconfig
#ip addr show | awk -F '[: ]+' '  /^[^ ]/      { iface=$2 }  $2 == "inet" { print iface ": " $3 }'

import  sys
import os

def inc_ip(ip):
    ip = ip.split(".")
    ip[-1] = int(ip[-1])+1
    return ".".join(ip)

def set_up(n):
    """

    :param n: is the number of switch, from tha will find the clients
    :return:
    """
    clients_lst = ['client'+str(1+int(n)), 'client'+str(2+int(n))]
    proxy_lst = ["proxy_server"+n]
    pings_lst = list(map(lambda client: "ping "+clients_lst[0]+"  -c1~ | head -1 | grep -Eo '[0-9.]{4,}'", clients_lst+
                         proxy_lst))
    localIPs = list(map(lambda ping:os.popen(ping), pings_lst))
    localIPs = list(map(lambda ip: inc_ip(ip), localIPs))
    eth_lst = os.popen("""ip addr show | awk -F '[: ]+' '  /^[^ ]/      { iface=$2 }  $2 == "inet" { print iface ": " $3 }'""").read()
    eth_lst = eth_lst.split("\n")[-1]
    eth_dic = {} # Dict with key the ip and value the port
    for i in eth_lst:
        temp = i.split(":")
        eth_lst[temp[-1].split("/")[0]] = temp[0]

    # Configure the switch
    os.system("ovs-vsctl add-br br0")
    os.system("ovs-vsctl set-fail-mode br0 secure")
    ports_lst = []
    for ip in localIPs:
        if eth_lst.get(ip):
            ports_lst.append(eth_lst[ip])
            os.system("ovs-vsctl add-port br0 " + eth_lst[ip])
    # Manually set up the ip of controller
    # ovs-vsctl set-controller br0 tcp:<controllers ip>:6633
    # After this make sure to enable all the interfaces that form part of the above bridge, else you won’t be able to
    # run traffic from one host to another
    map(lambda port: os.system("ifconfig "+port + " up"), ports_lst)


if __name__ == '__main__':
    set_up(sys.argv[-1])