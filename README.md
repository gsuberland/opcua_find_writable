# Find Writable OPC UA Variables

`opcua_find_writable.py` is a simple tool to find writable variables on [OPC UA](https://en.wikipedia.org/wiki/OPC_Unified_Architecture) servers. It enumerates all nodes in the tree and prints the path of each variable that is writable by the current user.

Usage: `python3 opcua_find_writable.py [server]`, where `[server]` is an OPC UA connection string, like `opc.tcp://10.1.2.3:4840/`

It depends on [python-opcua](https://github.com/FreeOpcUa/python-opcua).

Released under MIT License.
