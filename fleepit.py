# Copyright 2024 pegasko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Requirements: xclip, xdotool

import subprocess
import argparse
import typing
import json


# Built-in langsets
LANGSETS = {
    'qwerty-en-ru': (
        r"""`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,.~!#%&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>""",
        r"""ё1234567890-=йцукенгшщзхъ\фывапролджэячсмитьбюЁ!№%?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ""",
    ),
}


def make_langset_dict(langset: typing.Tuple[str, str]) -> typing.Dict[str, str]:
    flipper = {}

    if len(langset) != 2 or len(langset[0]) != len(langset[1]):
        raise ValueError("langset alternatives not matching")

    for (a, b) in zip(*langset):
        if a in flipper:
            raise ValueError(f'alternative for "{ a }" already exists')
        if b in flipper:
            raise ValueError(f'alternative for "{ b }" already exists')

        flipper[a] = b
        flipper[b] = a
    return flipper


def flip_langset(clip: str, conv: typing.Dict[str, str]) -> str:
    return ''.join([conv[c] if c in conv else c for c in clip])


def do_x11(args: argparse.Namespace):
    # Extract selection
    result = subprocess.run([ 'xclip', '-o', '-selection', 'primary', '-target', 'UTF8_STRING' ], capture_output=True, text=True)
    result.check_returncode()
    clip = result.stdout
    if clip.strip() == '':
        if args.verbose:
            print(f'clipboard is empty')
        return

    if args.verbose:
        print(f'clipboard: "{ clip }"')

    # Clear selection
    result = subprocess.run([ 'xclip', '-i', '-selection', 'primary' ], text=True, input='')
    result.check_returncode()

    # Do convert
    if args.langset:
        conv = make_langset_dict(LANGSETS[args.langset])
    else:
        with open(args.langset_file, 'r') as f:
            conv = make_langset_dict(json.load(f)['langset'])
    converted = flip_langset(clip, conv)

    if args.verbose:
        print(f'converted: "{ converted }"')

    # Write selection
    result = subprocess.run([ 'xclip', '-i', '-selection', 'clipboard' ], text=True, input=converted)
    result.check_returncode()

    # Paste
    result = subprocess.run([ 'xdotool', 'key', 'ctrl+v' ])
    result.check_returncode()


def main():
    parser = argparse.ArgumentParser('fleep')
    parser.add_argument(
        '-m', '--mode',
        type=str,
        choices=[
            'x11',
            'wayland',
        ],
        help='compositor compatibility mode',
        required=True,
    )
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging ',
        action='store_true',
    )
    langset_group = parser.add_mutually_exclusive_group(required=True)
    langset_group.add_argument(
        '-l', '--langset',
        help='use one of embedded langsets',
        type=str,
        choices=list(LANGSETS.keys()),
    )
    langset_group.add_argument(
        '-f', '--langset-file',
        help='use langset from json file containing',
        type=str,
    )
    args = parser.parse_args()

    if args.mode == 'x11':
        do_x11(args)
    else:
        raise NotImplementedError()


if __name__ == '__main__':
    main()
