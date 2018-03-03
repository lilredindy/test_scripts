class FileOwners:

    @staticmethod
    def group_by_owners(files):
        d = {}
        
        for k in files:
            if (files[k] not in d):
                d[files[k]] = []
            d[files[k]].append(k)
        
        return d

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))