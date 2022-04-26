"""
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
 

Example 1:


Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
 

Constraints:

1 <= path.length, filePath.length <= 100
path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
1 <= content.length <= 50
At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.
"""

class FileSystem:

    def __init__(self):
        self.file_system = {"root":{}}

    def ls(self, path: str) -> List[str]:
        #print(self.file_system)
        curr = self.file_system["root"]
        paths = path.split("/")[1:]
        if paths[0] == '':
            paths = paths[1:]
        #print(paths)
        for each in paths:
            if each not in curr:
                return []
            if type(curr[each]) == str:
                return [each]
            curr = curr[each]
        #print(self.file_system)
        res = list(curr.keys())
        res.sort()
        return res

    def mkdir(self, path: str) -> None:
        curr = self.file_system["root"]
        paths = path.split("/")[1:]
        for each in paths:
            if each not in curr:
                curr[each] = {}
            curr = curr[each]
        

            
    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.file_system["root"]
        paths = filePath.split("/")[1:]
        for i in range(len(paths)-1):
            each = paths[i]
            if each not in curr:
                curr[each] = {}
            curr = curr[each]
        if paths[-1] not in curr:
            curr[paths[-1]] = ""
        curr[paths[-1]] += content
        
    def readContentFromFile(self, filePath: str) -> str:
        curr = self.file_system["root"]
        paths = filePath.split("/")[1:]
        for i in range(len(paths)-1):
            each = paths[i]
            if each not in curr:
                curr[each] = {}
            curr = curr[each]
        return curr[paths[-1]]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
