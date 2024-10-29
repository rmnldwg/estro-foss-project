# ESTRO FOSS Project

[`copier`] template for starting a free and open source (FOSS) project as recommended by [ESTRO].

[`copier`]: https://copier.readthedocs.io
[ESTRO]: https://estro.org

## Installing the Requirements

```bash
pip install --user pipx

pipx install copier
pipx runpip copier install -r requirements.txt
```

## Using the Template

```bash
mkdir your-project-dir
cd your-project-dir
git init .

copier copy https://github.com/rmnldwg/estro-foss-project .
# answer questions...
git add .
git commit -m "initialize project from template"
```
