import parser
import constants

results = parser.parse(constants.URL)
file = open(constants.FILENAME, 'w')
file.write('\n'.join(results))
file.close()
