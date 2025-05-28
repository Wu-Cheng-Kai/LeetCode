def simplifyPath(path: str) -> str:
    if path == "/":
        return "/"
    else:
        folder = []
        
        for i in path.split("/"):
            if i == "..":
                if folder:
                    folder.pop()
            elif i and i != ".":
                folder.append(i)

    return "/" + "/".join(folder)

path = "/../"
ans = simplifyPath(path)
print(ans)