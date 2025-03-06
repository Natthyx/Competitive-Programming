class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)
        stack = []
        for i in range(len(path)):
            if path[i]=="":
                continue
            elif path[i]=="..":
                if stack:
                    stack.pop()
            elif path[i]==".":
                continue
            else:
                stack.append(path[i])

        return "/"+"/".join(stack)

            