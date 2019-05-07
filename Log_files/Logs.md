
### Log files of Squid

All the log files are locate in `/var/log/squid`.

First of all, we have the [*cache.log*](https://wiki.squid-cache.org/SquidFaq/SquidLogs?action=fullsearch&context=180&value=store.log&titlesearch=Titles#cache.log) file, we can say this is the debug log file of Squid. Here we can see all the 
error and debugging messages.

Another one important log files is the [*access.log*](https://wiki.squid-cache.org/SquidFaq/SquidLogs?action=fullsearch&context=180&value=store.log&titlesearch=Titles#access.log) file where Squid give use information about who is accessing our
proxy server and information about the status of requests and replies.


Example,
```python
1555349363.485    468 192.168.1.4 TCP_MISS/200 1024 POST http://ocsp.sectigo.com/ - HIER_DIRECT/2a02:582:a00::d4cd:7e98 application
/ocsp-response
```

[*store.log*](https://wiki.squid-cache.org/SquidFaq/SquidLogs?action=fullsearch&context=180&value=store.log&titlesearch=Titles#store.log)
