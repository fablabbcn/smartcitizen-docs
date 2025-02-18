import pytest
import subprocess
import os

def test_links():
    out = 0
    try:
        out = subprocess.call([os.path.join(os.getcwd(), "links.sh")])
    except:
        pass

    print (out)
    assert out == 0
