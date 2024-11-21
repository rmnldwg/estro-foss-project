# ESTRO FOSS Project

[`copier`] template for starting a free and open source (FOSS) project as recommended by [ESTRO].

[`copier`]: https://copier.readthedocs.io
[ESTRO]: https://estro.org

## Installing the Requirements

First, let's install [`pipx`](https://pipx.pypa.io/stable/), a great tool to install Python command line tools, such as the templating machinery of [`copier`].

```bash
pip install --user pipx
pipx install copier
```

To run our particular template, some additional Python packages are necessary. They are easily installed by running the following command:

```bash
pipx runpip copier install $(curl https://raw.githubusercontent.com/rmnldwg/estro-foss-project/refs/heads/main/requirements.in)
```

## Using the Template

```bash
copier copy https://github.com/rmnldwg/estro-foss-project your-project-dir
# answer questions...
cd your-project-dir
git init .
git add .
git commit -m "initialize project from template"
```
