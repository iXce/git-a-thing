from dulwich.repo import Repo
from dulwich.objects import Blob, Tree, Commit
import time
import os

import gitathing_git.settings as settings

def do_commit(repo, tree, blobs, message, author, ref = "master"):
    commit = Commit()
    commit.tree = tree.id
    commit.author = commit.committer = author
    commit.commit_time = commit.author_time = int(time.time())
    tz = time.timezone if (time.daylight == 0) else time.altzone
    commit.commit_timezone = commit.author_timezone = tz
    commit.encoding = "UTF-8"
    commit.message = message
    for blob in blobs:
        repo.object_store.add_object(blob)
    repo.object_store.add_object(tree)
    repo.object_store.add_object(commit)
    repo.refs['refs/heads/%s' % ref] = commit.id

def create_repo(design, initialize):
    full_path = os.path.join(settings.GIT_ROOT, design.repo_path)
    os.makedirs(full_path)
    repo = Repo.init_bare(full_path)
    if initialize:
        blob = Blob.from_string(str("%s Git-a-thing design repository\n" % design.name))
        tree = Tree()
        tree.add("README", 0100644, blob.id)
        do_commit(repo, tree, [blob], "Initialize repository", settings.GITATHING_COMMITER)
