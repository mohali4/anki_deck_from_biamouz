import genanki
from random import randint
from pathlib import Path


idgen = lambda : randint(10**10,10**11-1)
model_id =  24105438792
model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<h3 style="text-align: center;">{{Question}}</h3>',
      'afmt': '{{FrontSide}}<hr id="answer"><h3 style="text-align: center;">{{Answer}}</h3>',
    },
  ])

def create_deck (name:str,words:list,path_to_save):


    if not isinstance(path_to_save,Path): path_to_save = Path(path_to_save)
    write_file_path = str(path_to_save/f'{name}.apkg')

    print(f"Creating deck named {name} and saving to {write_file_path} with {words.__len__()} words ...")

    # Generate Anki cards and add them to a deck
    deck_id = idgen()
    deck = genanki.Deck(deck_id, name)

    for english_w, mean in words:
        note = genanki.Note(model=model, fields=[english_w, mean])
        deck.add_note(note)

    # Save the deck to an Anki package (*.apkg) file

    genanki.Package(deck).write_to_file(write_file_path)

    print('Saving deck')

    return write_file_path