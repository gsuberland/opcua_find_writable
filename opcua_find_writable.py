import sys
import opcua
from opcua import Client
from opcua import ua

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Tool to find writable variables on OPC UA servers.")
		print("GitHub: https://github.com/gsuberland/opcua_find_writable")
		print("")
		print("Usage: python3 opcua_find_writable.py [server]")
		print("")
		print("    server: OPC string, e.g. opc.tcp://10.1.2.3:4840/")
		print("")
		exit()
	connectString = sys.argv[1]
	client = Client(connectString)
	try:
		print("Connecting to server...")
		client.connect()
		print("Loading type definitions...")
		client.load_type_definitions()
		print("Getting root node...")
		root = client.get_root_node()
		print("Root node is: ", root)
		objects = client.get_objects_node()
		print("Objects node is: ", objects)
		print("Walking nodes for user-writable variables...")
		walk_nodes = []
		walk_nodes.append(root)
		while len(walk_nodes) > 0:
			node = walk_nodes.pop(0)
			try:
				if ua.AccessLevel.CurrentWrite in node.get_user_access_level():
					print("Writable node: ", node.get_path(as_string=True))
			except opcua.ua.uaerrors._auto.BadAttributeIdInvalid:
				_foo = None # do nothing
			children = node.get_children()
			walk_nodes.extend(children)

		print("Done.");
	finally:
		client.disconnect()
