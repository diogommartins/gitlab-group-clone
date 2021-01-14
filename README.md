# Gitlab Group Cloner - GGC

Você é novo em um time que adora microserviços? Acha um saco ter que passar por 
cada um dos projetos, tendo o trabalho de clonar cada um dos repositórios 
antes de começar a trabalhar? Seus problemas acabaram!

A app utiliza a API do Gitlab, percorre os projetos de um grupo e clona eles pra você 😊

# Installation

```shell
pip install pipenv 
pipenv install
```

# Run
Para clonar todos os projetos do grupo [accounts](https://gitlab.olxbr.io/accounts), por exemplo:

```shell
pipenv run clone accounts
```

Todos os projetos desse grupo serão clonados em `./output/accounts/`

Precisa de ajuda?

```shell
pipenv run clone --help
```

# Configuration

A configuração funciona através das seguintes variáveis de ambiente

- `GITLAB_URL` - Default `https://gitlab.olxbr.io/`
- `GITLAB_TOKEN` - Personal Access Token. Leia mais: [https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)  
- `OUTPUT_PATH` - Output path que será usado como prefixo para git clones. Default `./output`
- `MAX_CONCURRENCY` - Máximo de git clones concorrentes. Defaults `4`
