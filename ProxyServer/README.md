# Proxy server topology
Here I implement topology of proxy server. In this case I have two hosts ( `clients` ) and one switch. 
I want to connect my hosts with my proxy server, for that I set a default gateway the ip address where 
my proxy is running. For proxy I use `Squid`.  The one host is the client and the other one will represent
the "site".

![picture1](/images/Proxy_server.jpg)


In our example we don't need a switch we set up only two hosts in `mininet` and use one as `client` and the other 
as `server- web site` . But first we need to set up our proxy server. For that we use the [`Squid`](http://www.squid-cache.org/) .

The command for installing the `Squid` in `Ubuntu` is,

```
$ sudo apt -y install squid
```

After the installation a folder is created in path `/etc/squid` . There is located the file `squid.conf`.
We use this configuration file to change and define the process in `Squid`.

There are three mainly commands for `Squid`
* `start`, start the `Squid` 
  ```
  $ service squid start

  ```

* `stop`,  stop the `Squid`
   ```
   $ service squid stop

  ``` 
  
 * `status`, give us information about the status of `Squid`
   ```
   $ service squid status
   
   ```


When we finish with the setup of `Squid` we continue with our network.
==>
 

