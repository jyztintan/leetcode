class Solution:
    def removeSubfolders(self, folder):
        seen = set()
        ans = []
        folder.sort()
        for fold in folder:
            path = tuple(fold[1:].split('/'))
            check = ()
            is_subfolder = False
            for super_folder in path:
                if check in seen:
                    is_subfolder = True
                    break
                check += (super_folder,)

            if not is_subfolder:
                ans.append(fold)
                seen.add(path)
        return ans

# folder = ["/ah/al/am","/ah/al"]
# print(Solution().removeSubfolders(folder))  # ["/a","/c/d","/c/f"]