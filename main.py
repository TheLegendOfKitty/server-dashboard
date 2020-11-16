import argparse
import asyncio
from mcutil import mcutil
import flask
app = flask.Flask(__name__)
# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port", type=int)
parser.add_argument("password")
args = parser.parse_args()

util = mcutil(args.host, args.port, args.password)
print(asyncio.run(util.get_online_players()))

