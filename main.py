
def run (args) :

    from biamouz_data import get_data
    from anki import create_deck

    print('fetching data')
    data = get_data(*args.URLS)
    print('Fetch data finished')
    deck_path = create_deck(args.NAME,data,args.DECK_SAVE_PATH)

    print(f'A deck created and saved to {deck_path}')