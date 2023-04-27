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

class FilterModule(object):
    def filters(self):
        return {
            'nested_service_interfaces': nested_service_interfaces
        }
