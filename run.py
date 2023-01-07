from git import Repo
from repos import repos

update_count = 0

class c:
    reset = '\033[0m'
    update = '\033[92m\033[01m'
    red = '\033[91m'

for path in repos:
    repo = Repo(path)
    last_commit = repo.head.commit

    repo.git.reset('--hard')

    remote = repo.remote('origin')
    remote.fetch()
    remote.pull()

    name = remote.url.split('.git')[0].split('/')[-1]
    if last_commit != repo.head.commit:
        update_count += 1
        print(f'[{name}] {c.update}Fetching changes...{c.reset}')
    else:
        print(f'[{name}] {c.red}No changes found{c.reset}')

print(f'Fetched changes from {c.update}{update_count}{c.reset}/{len(repos)} repositories')
