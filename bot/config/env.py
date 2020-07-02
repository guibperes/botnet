import sys
import getopt

class Env:
    def __init__(self):
        self.env = self.parse_env()

    def parse_env(self):
        variables = dict(getopt.getopt(args=sys.argv[1:], shortopts='t:u:')[0])

        return {
            'threads': int(variables.get('-t')),
            'url': variables.get('-u')
        }

    def get(self, argument):
        return self.env.get(argument)
