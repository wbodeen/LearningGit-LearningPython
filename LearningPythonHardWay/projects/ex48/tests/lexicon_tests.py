from unittest import *
import sys
sys.path.append('C:\\Users\\wbode\\Documents\\GitHubRepo\\LearningPythonHardWay\\projects\\ex48')
import ex48.lexicon

def test_directions(self):
    a
    assertEqual(ex48.lexicon.scan("north"), [('direction','north')])   
    result = ex48.lexicon.scan("north south east")
    self.assertEqual(result, [('direction', 'north'),
                            ('direction', 'south'),
                            ('direction', 'east')])


test_directions()


stuff = input('> ')
words = stuff.split()
i=0

while i < len(words):
    output = ex48.lexicon.lexiScan(words[i])
    i = i+1
    print(output)


    
if __name__ == '__main__':
    unittest.main()