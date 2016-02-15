python-haproxy
==============

Read or write to the HAProxy stats socket.

This is a fork of https://github.com/nl5887/python-haproxy

## CLI Usage

This provides a `hapctl` command.

```bash
# See the help menu
hapctl --help

# Run a command against the socket
hapctl --socket=/path/to/socket "<command here>"
```

For example:

```bash
hapctl --socket=/run/haproxy/admin.sock "show info"
```

*Note* that the command `"show info"` is quoted, as it includes spaces.

## Python Usage

You can it it in code directly:

```python
from hapctl import haproxy

stats = haproxy.HAProxyStats('/run/haproxy/admin.sock')

stats.execute('show info')

# Yields:
[u'Name: HAProxy', u'Version: 1.4.18', u'Release_date: 2011/09/16', u'Nbproc: 1', u'Process_num: 1', u'Pid: 19234', u'Uptime: 0d 6h18m11s', u'Uptime_sec: 22691', u'Memmax_MB: 0', u'Ulimit-n: 8210', u'Maxsock: 8210', u'Maxconn: 4096', u'Maxpipes: 0', u'CurrConns: 1', u'PipesUsed: 0', u'PipesFree: 0', u'Tasks: 7', u'Run_queue: 1', u'node: ip-10-0-0-45', u'description: ', u'']
```

## Available Commands

Commands can be seein under section **9.2 "Unix Socket commands"** in the Haproxy 1.6 (current stable version) [management docs](http://www.haproxy.org/download/1.6/doc/configuration.txt).

Some common ones are shown here:

```
clear counters : clear max statistics counters (add 'all' for all counters)
help           : HAProxy help message, which lists available commands
prompt         : toggle interactive mode with prompt
quit           : disconnect
show info      : report information about the running process
show stat      : report counters for each proxy and server
show errors    : report last request and response errors for each proxy
show sess [id] : report the list of current sessions or dump this session
get weight     : report a server's current weight
set weight     : change a server's weight  
set timeout    : change a timeout setting
disable server : set a server in maintenance mode
enable server  : re-enable a server that was previously in maintenance mode
```

