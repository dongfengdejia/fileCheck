import unittest
import fileCheck


fileName = "README.md"
hashCode = "1bf6a31098979ef8d126c7603def5b8149c0146ef21f636a2324e85b35ad6014"

class TestFileCheck(unittest.TestCase):

    def test_fileCheck(self):
        fileMap = fileCheck.calcCheckSum([fileName])
        print "+++",fileMap
        checkSum = fileMap["*" + fileName]
        self.assertEquals(checkSum, hashCode)
    
    
if __name__ == "__main__":
    unittest.main()