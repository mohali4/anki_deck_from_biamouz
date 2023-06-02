import args
from biamouz_data import fetch_countainer
from main import run

args.URLS = fetch_countainer(args.COUNTAINER_URL)
run(args)