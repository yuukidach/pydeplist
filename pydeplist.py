import sys
import os
import logging
import subprocess

from distutils.core import run_setup

PACK_DIR = ""
SETUP_FOLDER = ".setup_py_tmp"
USER = ""
PASSWD = ""
TAB_SPACE = 4

all_setup_file = []
dep_tree = {}

def goto_pack_dir(pack_folder):
    ''' Go to package's directory.

    # Args:
        pack_folder: Packages' folder.
    '''
    os.chdir(pack_folder)


def get_setup_py(dir, name):
    return (f"{dir}/{name}.py")


def get_deps(setup_py):
    ''' Get dependecies list from `setup.py'

    # Args:
        setup_py: obsolute path for `setup.py' file

    # Return:
        deps: Denpedencies list in `setup.py'
    '''
    try:
        setup = run_setup(setup_py, stop_after="config")
        logging.info(setup)
        deps = setup.install_requires

        logging.debug(f"Dependencies in {setup_py}:")
        for dep in deps:
            logging.debug("    - "+dep)

        return deps
    except:
        return []


def is_git_dep(dep):
    if "git" in str(dep):
        return True
    else:
        return False


def get_git_dep_info(dep):
    ''' If the dependency is in GitHub, get its information

    # Args:
        dep: Denpendency.
    
    # Return:
        pack_name: Package name.
        pack_ver: Package version.
        git_url: The URL for git repo.
    '''
    info_piece = str(dep).split("@")

    pack_name = info_piece[0]
    pack_ver = info_piece[-1].split("#")[0]
    git_url = info_piece[2]         # github.com/[Organizaiton]/[repo-path]/setup.py

    return (pack_name, pack_ver, git_url)


def get_raw_url(repo_url, ver):
    url = "https://raw.githubusercontent.com/" \
          + repo_url.split("/", 1)[1] + "/"    \
          + ver                                \
          + "/setup.py"
    logging.debug(url)
    return url


def download_setup_py(pack_name, url):
    os.makedirs(SETUP_FOLDER, exist_ok=True)
    fname = SETUP_FOLDER + "/" + pack_name + ".py"
    user = USER + ":" + PASSWD
    # if file exisy, do not download again
    if os.path.isfile(fname):
        return
    try:
        subprocess.check_call(["curl",
                               "--user", user,
                               "-o", fname,
                               url])
    except:
        pass


def get_dep_tree(DIR, pack_name):
    
    if pack_name in all_setup_file:
        return
    
    all_setup_file.append(pack_name)
    logging.debug(all_setup_file)

    proj_setup_py = get_setup_py(DIR, pack_name)
    deps = get_deps(proj_setup_py)
    for dep in deps:
        if is_git_dep(dep):
            (name, ver, link) = get_git_dep_info(dep)
            url = get_raw_url(link, ver)
            
            if pack_name in dep_tree:
                dep_tree[pack_name].append(name)
            else:
                dep_tree[pack_name] = [name]

            download_setup_py(name, url)
            get_dep_tree(SETUP_FOLDER, name)
            

def draw_dep_grah(dep_dict, node, depth):
    depth += 1
    for pack in dep_dict[node]:
        line = " " * depth * TAB_SPACE \
               + "- "                  \
               + pack
        print(line)
        if pack in dep_dict:
            draw_dep_grah(dep_dict, pack, depth)
            

def main():
    log_format = "[%(asctime)s] [%(levelname)8s]  %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=log_format)    

    goto_pack_dir(PACK_DIR)
    get_dep_tree(PACK_DIR, "setup")

    print("\n- setup")
    draw_dep_grah(dep_tree, "setup", 0)


if __name__ == "__main__":
    sys.exit(main())