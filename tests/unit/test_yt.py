import pytest
from onipynbrenderer import get_time_info
from onipynbrenderer.custom_exception import InvalidURLException

good_URL_data = [
    ("https://youtu.be/roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", 42),
    ("https://www.youtube.com/watch?v=q6IEA26hvXc&list=PLot-Xpze53letfIu9dMzIIO7na_sqvl0w&index=1" , 0),
    ("https://youtu.be/q6IEA26hvXc?list=PLot-Xpze53letfIu9dMzIIO7na_sqvl0w",0),
    ("https://youtu.be/q6IEA26hvXc?list=PLot-Xpze53letfIu9dMzIIO7na_sqvl0w&t=637",637),
    ("https://youtu.be/NMP3nRPyX5g?list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO&t=258",258)
]


URL_id_bad_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),  # exception
]


@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response

@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)