# https://www.testdome.com/questions/python/file-owners/94848


def group_by_owners(files):
    result = {}
    for key, value in files.items():
        result[value] = result.get(value, [])
        result[value].append(key)

    return result


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))
