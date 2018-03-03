class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        current_path_parts = self.current_path.split('/')
       
        new_path_parts = new_path.split('/')
        print (new_path_parts)
       
        for p in new_path_parts:
            if (p == '..'):
                current_path_parts.pop()
            else:
                current_path_parts.append(p)
       
        #rejoin the current path parts
        print (current_path_parts)
        self.current_path = '/'.join(current_path_parts)

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)

