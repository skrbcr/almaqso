import sys
sys.path.append('../almaqso')
from almaqso.search_archive import search_archive

def test_search_archive():
    search_archive(4, 'catalog/test_2.json')
