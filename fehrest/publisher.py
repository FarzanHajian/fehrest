from slugify import slugify
from . import validator
from . import errors
from . import helper
import os
import os.path


class Publisher:
    def __init__(self, working_path: str):
        self.__working_path = working_path

    def publish(self):
        if not validator.validate_working_path(self.__working_path):
            errors.raise_error(errors.INVALID_WORKING_DIR)
        self.__generate_artifacts()
        helper.publish(self.__working_path)

    def __generate_artifacts(self):
        walker = os.walk(f'{self.__working_path}/content/files')
        walker.__next__()   # skipping the 'files" folder

        page_info = []  # List of tuples (folder name, folder slug)
        for folder in walker:
            if folder[2]:
                page_info.append(self.__create_page(folder))

        if page_info:
            self.__update_home_page(page_info)
        else:
            errors.raise_error(errors.NO_FILES)

    def __create_page(self, folder: tuple) -> tuple[str, str]:
        # Return type is tuple(folder name, folder slug)
        page_name = os.path.basename(folder[0])
        page_slug = slugify(page_name)
        page_file = f'{self.__working_path}/content/pages/{page_name}.md'
        lines = [f'Title: {page_name}\n', f'Slug: {page_slug}\n']

        for fname in folder[2]:
            lines.append(
                f'\n[{fname}]({{static}}/files/{page_name}/{fname})\n')

        with open(page_file, mode='w+', encoding="utf-8") as f:
            f.writelines(lines)

        return (page_name, page_slug)

    def __update_home_page(self, page_info: list[tuple[str, str]]):
        markdown = []
        for info in page_info:
            new_line = '\n' if markdown else ''
            markdown.append(f'{new_line}[{info[0]}](/pages/{info[1]}.html)\n')

        home_file = f'{self.__working_path}/content/pages/home.md'
        with open(home_file, mode="r", encoding="utf-8") as f:
            content = f.readlines()

        is_inside = False
        with open(home_file, mode="w", encoding="utf-8") as f:
            for line in content:
                if is_inside:
                    if line.strip() == "[]: # 'End of Links region'":
                        is_inside = False
                        f.write(line)
                else:
                    if line.strip() == "[]: # 'Links region'":
                        is_inside = True
                        f.write(line)
                        f.writelines(markdown)
                    else:
                        f.write(line)
