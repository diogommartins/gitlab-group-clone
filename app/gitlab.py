import subprocess
from multiprocessing.pool import ThreadPool as Pool
from typing import Iterable

from gitlab import Gitlab

from app.models import Project
from app.settings import settings


pool = Pool(settings.MAX_CONCURRENCY)


def _do_clone(project: Project):
    print(f"git clone {project.ssh_url} {project.path}", flush=True)
    return subprocess.run(['git', 'clone', project.ssh_url, f"{settings.OUTPUT_PATH}{project.path}"])


def clone(projects: Iterable[Project]):
    for project in projects:
        pool.apply_async(_do_clone, (project,))
    pool.close()
    pool.join()


# se um grupo tiver subgrupos dentro de subgrupos,
# não vai pegar. Não sei se isso existe no gitlab,
# mas caso exista, o fix é tratar isso como uma árvore
def get_projects(gl: Gitlab, group: str):
    group = gl.groups.get(group)
    for project in group.projects.list():
        yield Project(
            ssh_url=project.ssh_url_to_repo,
            path=project.path_with_namespace
        )

    for subgroup in group.subgroups.list():
        group = gl.groups.get(subgroup.id)
        for project in group.projects.list():
            yield Project(
                ssh_url=project.ssh_url_to_repo,
                path=project.path_with_namespace
            )