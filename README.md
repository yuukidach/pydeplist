# pydeplist

## Description

This is a command line tool to list all remote GitHub dependencies for a python package.

The dependencies will stop be listed until we have no access to the repo **OR** there is no more dependency is needed.

**NOTICE:** Now, this is only used for show dependencies which are in GitHub. But in the future, I'll try to extend it to packages in Pypi.

## Installation

``` Shell
# cd pydeplist
pip3 install .
```

## Usage

``` Shell
cd [package folder]
pydeplist --user [user name for GitHub] --passwd [password]

# or

pydeplist --dir [package folder] --user [user name for GitHub] --passwd [password]
```

## Example Output

``` shell
- setup
    - mcubn
    - upctl
    - aclient
    - testassis
    - kball
        - timeutil
        - pve
            - func
            - math
        - aclient
        - cpylua
            - mcubn
            - upctl
    - pve
        - func
        - math
```

The dependency tree node ends at `func` and `math`, because we have no access for `func` and `math`, so we cannot go on. And it ens at `mcubn` because it does not depend in another GitHub repo.
