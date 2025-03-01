## The import below is what happens when you organize things into folders after class. Move these files to the main directory to run them properly :D :3

from Notes.TestsNotes.TestStrings.hello import hello

def test_default():
    assert hello() == "hello, world"

def test_case():
        assert hello("David") == "hello, David"
