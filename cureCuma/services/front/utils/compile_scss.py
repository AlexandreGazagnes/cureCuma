import os
import sass


from src import logger

# declare directories
SCSS = "app/assets/scss"
CSS = "app/static/css"


def compile_scss():

    logger.info("called")

    # asset
    assert os.path.isdir(SCSS)
    assert os.path.isdir(CSS)

    # compile
    sass.compile(dirname=(SCSS, CSS),)  # output_style="compressed")


if __name__ == "__main__":
    compile_scss()
