import json
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as bars_file:
            parsed_json = json.loads(bars_file.read())
        return parsed_json
    except IOError:
        raise IOError('Could not open file bars.json!')
    except ValueError:
        raise ValueError('Wrong JSON!')


def pretty_print_json(parsed_json):
    print(json.dumps(
        parsed_json,
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )
    )


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            bars_dict = load_data(str(sys.argv[1]))
            pretty_print_json(bars_dict)
        else:
            print('File path not found!')
    except ValueError as exc_text:
        print(exc_text)
    except IOError:
        print("Could not open file!")
