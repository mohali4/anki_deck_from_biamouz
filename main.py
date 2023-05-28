from args import *
from biamouz_data import get_data
from anki import create_deck

print('fetching data')
data = get_data(*URLS)
print('Fetch data finished')
deck_path = create_deck(NAME,data,DECK_SAVE_PATH)

print(f'A deck created and saved to {deck_path}')