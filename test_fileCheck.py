import unittest
import fileCheck


fileName = "README.md"
hashCode = "604fbb506f13bd7dc338ee8468b4ef13204ba26e8872c8475ac55fc564f7f7f6"

class TestFileCheck(unittest.TestCase):

    def test_fileCheck(self):
        fileMap = fileCheck.calcCheckSum([fileName])
        checkSum = fileMap["*" + fileName]
        self.assertEquals(checkSum, hashCode)
    
    
if __name__ == "__main__":
    unittest.main()