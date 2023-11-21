"""
Test für die Klasse Warenkorb werden hier implementiert
"""
from pytest import fixture
from pytest import raises

# pylint: disable= redefined-outer-name, missing-function-docstring

from warenkorb import Warenkorb

def test_can_instantiate_class():
    warenkorb = Warenkorb()
    assert warenkorb != None

def test_can_add_price_to_artikel():
    pass




def test_can_add_artikel_to_warenkorb():
    warenkorb = Warenkorb()
    warenkorb.addartikel("shirt")                   #warentkorb.getartikel()            -> um auf privates objekt zuzugreifen
    assert warenkorb.getartikel() == ["shirt"]

def test_total():
    warenkorb = Warenkorb()
    warenkorb.addartikel("shirt")
    assert warenkorb.getprice() == 20
    warenkorb.addartikel("shirt")
    warenkorb.addartikel("hose")
    #assert warenkorb.getartikel() == ["shirt", "shirt", "hose"]
    assert warenkorb.getprice() == 75

def test_discount():
    warenkorb = Warenkorb()
    warenkorb.addartikel("shirt")
    warenkorb.addartikel("shirt")
    warenkorb.addartikel("shirt")
    warenkorb.addartikel("shirt")
    warenkorb.addartikel("shirt")
    warenkorb.addartikel("shirt")
    warenkorb.addartikel("shirt")
    #assert warenkorb.calcdiscount() == 120
    warenkorb.addartikel("hose")
    warenkorb.addartikel("hose")
    warenkorb.addartikel("hose")
    warenkorb.addartikel("hose")
    warenkorb.addartikel("hose")
    warenkorb.addartikel("hose")
    assert warenkorb.calcdiscount() == 6 * 32 + 120

def test_can_call_preis():
    pass

