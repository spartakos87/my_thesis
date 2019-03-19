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
*`cache_dir`. Declare the space on HD which Squid use to stor or cache the web documents. It syntax is,
```buildoutcfg
cache_dir STORAGE_TYPE DIRECTORY SIZE_IN_Mbytes L1 L2 [OPTIONS]
```

`STORAGE_TYPE` has three options,

*`ufs`. Is good for servers with less load and high speed disks but is not really preferable for busy caches

*`aufs`. Is `ufs` with asynchronous I/O support if we have the `pthreads` lib support on our OS we should always go for
`aufs`, especialy for heavily loaded proxy servers.

*`diskd`(Disk Daemon). Similar to `aufs`, only different is that uses an external process for I/O transactions instead
for threads. Involves quering system. May get overloaded over time in a busy proxy server. Has two additional options to 
`cache_dir`. In this case the syntax of directive will be,
```buildoutcfg
cache_dir diskd DIRECTORY SIZE_Mbytes L1 L2 [OPTIONS] [Q1=n] [Q2=n]
```
*`Q1`. Signifies the number of pending messages in the queue beyond which Squid will not place new requests for I/O
 transactions. The default value is 64. 

*`Q2`. Signifies the number of pending messages in the queue beyond which Squid will cease the operate and will go in to
block mode.  The default value is 72.
 
 
 ### Cache object size limits
 There are two directives which declare the minimum and maximum size of objects which can be stored,
 * `minimum_object_size`
 
 *`maximum_object_size`
 
 An example of this directive, 
 ```buildoutcfg
maximum_object_size 10 MB
```


### Cache replacement policied