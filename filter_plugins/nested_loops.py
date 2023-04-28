from ansible.errors import AnsibleFilterError

def nested_service_interfaces(services):
    try:
        result = []
        for service in services:
            for side_key, side_value in service['sides'].items():
                for interface in side_value['interfaces']:
                    result.append((service, interface))
        return result
    except Exception as e:
        raise AnsibleFilterError(f"Error in nested_service_interfaces filter: {str(e)}")

def filter_router_interfaces(services, router_side):
    try:
        result = []
        for service in services:
            for side_key, side_value in service['sides'].items():
                if side_key == router_side:
                    for interface in side_value['interfaces']:
                        if "." in interface['name']:
                            vlan_id = interface['name'].split(".")[1]
                            interface_info = {
                                'name': interface['name'],
                                'ip': interface['ip'],
                                'vlan_id': vlan_id
                            }
                        else:
                            interface_info = {
                                'name': interface['name'],
                                'ip': interface['ip']
                            }
                        result.append((service, interface_info))
        return result
    except Exception as e:
        raise AnsibleFilterError(f"Error in filter_router_interfaces filter: {str(e)}")

class FilterModule(object):
    def filters(self):
        return {
            'nested_service_interfaces': nested_service_interfaces,
            'filter_router_interfaces': filter_router_interfaces
        }