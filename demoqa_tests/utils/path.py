from pathlib import Path
from selene.support.shared import browser
import resources


def upload(relative_path):
    path = str(Path(resources.__file__).parent.joinpath(relative_path).absolute())
    browser.element('#uploadPicture').send_keys(path)
