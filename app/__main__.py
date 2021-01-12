import gitlab
import argparse

from .gitlab import clone, get_projects
from .settings import settings


parser = argparse.ArgumentParser(description='Clone projetos de um grupo do gitlab.')
parser.add_argument("group", type=str, help="Nome do grupo no gitlab")
args = parser.parse_args()

gl = gitlab.Gitlab(settings.GITLAB_URL, private_token=settings.GITLAB_TOKEN, **settings.pagination_config)

projects = get_projects(gl, args.group)
clone(projects)
