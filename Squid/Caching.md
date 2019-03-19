# How Squid caching

In this documents will analyze the many of directives which can use in `squid.conf` to control how squid is caching.
The most of information we use the book [Squid Proxy Server 3.1: Beginner's Guid]() as the Squid site is suggested.

## Installation 
For installation of `Squid` we can see [here](https://github.com/spartakos87/my_thesis/tree/master/ProxyServer), in
section `Setup Squid`.

## Caching directives

Squid use the `RAM` either hard disk to caching `web documenets`. As we know the web documents which caching in RAM they
can be served more quickly than the ones which be caching in hard disk. But the disadvantage of caching in the RAM is 
the limited storage space. So, the strategy which should follow is to caching the most poplular `objects` in RAM which
have high probability of being requested again.

For Squid there two kind of objects which it caching
* Hot/popular objects. These objects or web documents are popular and are requested quite frequently compared to
others
* Negatively cached objects. Negatively cached objects are error messages which Squid has encountered while fetching
a page or web document on behalf of a client.

First we start with directives about RAM

* `cache_mem`. This define the size of RAM memory Squid is free to use.How to use is,
```buildoutcfg
cache_mem [integer number] [unit bytes/KB/MB/GB]
```
For example,
```buildoutcfg
cache_mem 100 MB
```

* `maximum_object_size_in_memory`. It defines the size of each object which can cache in RAM.

  For example,
  ```buildoutcfg
   maximum_object_size_in_memory 1 MB
  ```

### Memory cache mode
Squid give us the ability to choose which objext ot keep in memory-RAM cache for optimize reasons. For this we have to 
use the directive `memory_cache_mode`.  There are three modes which can be used.
*`always`. Keep all the the most recently fetched objects that can fit in the available space. `DEFAULT OPTION`
*`disk`. Only the objects which are already cached on a HD(hard disk) and have a `HTI` (meaning they were requested subsequently after being
cached), will be stored in the memory cache.
*`network`. Only the objects which have been fetched from the network (including neighbors)
are kept in the memory cache.

An example of use this directive,
```buildoutcfg
memory_cache_mode disk
```

### Using HD for caching
