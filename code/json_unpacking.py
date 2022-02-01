from itertools import chain, starmap


def iterative_json_unpacking(dictionary):
    """Flatten a nested json file"""

    def unpack(parent_key, parent_value):
        """Unpack one level of nesting in json file"""

        if isinstance(parent_value, dict):
            for key, value in parent_value.items():
                temp1 = f'{parent_key}_{key}'
                yield temp1, value
        elif isinstance(parent_value, list):
            for value in parent_value:
                temp2 = parent_key
                yield temp2, value
        else:
            yield parent_key, parent_value

    while True:
        # Keep unpacking the json file until all values are atomic elements (not dictionary or list)
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
        # Terminate condition: not any value in the json file is dictionary or list
        if not any(isinstance(value, dict) for value in dictionary.values()) and \
                not any(isinstance(value, list) for value in dictionary.values()):
            break
    return dictionary
