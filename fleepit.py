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


LANGSETS = {
    'qwerty-en-ru': (
        r"""`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,.~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>""",
        r"""ё1234567890-=йцукенгшщзхъ\фывапролджэячсмитьбюЁ!"№;%:?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ""",
    ),
}


def make_langset_dict(langset: str) -> typing.Dict[str, str]:
    ls = LANGSETS[langset]
    flipper = {}
    for (a, b) in zip(*ls):
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
    conv = make_langset_dict(args.langset)
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
        required=True,
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
    )
    parser.add_argument(
        '-l', '--langset',
        type=str,
        choices=list(LANGSETS.keys()),
        required=True,
    )
    args = parser.parse_args()

    if args.mode == 'x11':
        do_x11(args)
    else:
        raise NotImplementedError()


if __name__ == '__main__':
    main()
