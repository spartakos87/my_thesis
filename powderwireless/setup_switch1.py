# Get the ip when I ping
#ping google.com -c1 | head -1 | grep -Eo '[0-9.]{4,}'

# Get eth from ifconfig
#ip addr show | awk -F '[: ]+' '  /^[^ ]/      { iface=$2 }  $2 == "inet" { print iface ": " $3 }'

import  sys

if __name__ == '__main__':
    print type(sys.argv[-1])