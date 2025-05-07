from git import Repo

def commit_and_push(repo_path):
    repo = Repo(repo_path)
    repo.git.add('--all')
    repo.index.commit("Fix: Auto-patch CI workflow")
    origin = repo.remote(name='origin')
    origin.push()
