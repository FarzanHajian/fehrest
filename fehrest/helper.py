import subprocess
import argparse
import sys


def publish(working_path: str):
    subprocess.run(["pelican"], cwd=working_path)


def apply_template_values(file_path: str, add_quotes=True, **kwargs):
    with open(file_path, mode="r", encoding="utf-8") as f:
        content = f.read()

    for k in kwargs:
        value = kwargs[k]
        if add_quotes and isinstance(value, str):
            value = f"'{kwargs[k]}'"
        content = content.replace('{{$$'+k+'$$}}', value)

    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(content)


def parse_args() -> argparse.Namespace:
    def check_commands(args: argparse.Namespace) -> str:
        initialize = True if args.initialize else False
        publish = True if args.publish else False
        count = int(initialize)+int(publish)
        if count == 0:
            return 'No command is specified'
        if count > 1:
            return 'Only on command must be specified'
        return None

    parser = argparse.ArgumentParser(exit_on_error=True)

    cmd_group = parser.add_mutually_exclusive_group()
    cmd_group.add_argument('--init', dest='initialize', action='store_true',
                           help='initializes an empty project inside the folder specified by --path switch')
    parser.add_argument('-o', '--output', required='--initialize' in " ".join(
        sys.argv), help='sets destination of the new site to be initialized')
    parser.add_argument('-n', '--name', required='--initialize' in " ".join(
        sys.argv), help='sets name of the new site to be initialized')
    cmd_group.add_argument('--publish', metavar="PATH",
                           help='creates output files for the site pointed to by PATH')
    cmd_group.add_argument('--version', action='version',
                           version='%(prog)s 0.1')

    args = parser.parse_args()

    if error := check_commands(args):
        parser.error(error)

    return args
