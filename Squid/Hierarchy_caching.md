##Hierarchy Caching

We can have more than one Squid proxy servers. The serves can communicate with the others and share content.
The Squid give us the directive `cache_peer` which define the type of cache peer and others.

# Case which use this kind of caching


# Directive cache_peer

```python
cache_peer HOSTNAME TYPE HTTP_PORT ICP_OR_HTCP_PORT [OPTIONS]
```

* `HOSTNAME`: IP address or domain of the proxy server
* `TYPE`: There are three types, `parent`, `sibling` and `multicast`.
* `HTTP_PORT`: specifies the port on which a neighbor or peer accepts HTTP request.
The default is `3128`
* `ICP_OR_HTCP_PORT`: specifies the port for ICP or HTCP communication.


Example of the directive,

```python
cache_peer parent.example.com parent 3128 3130 default
cache_peer sib.example.com sibling 3128 3130 proxy-only
```
