# ESTRO FOSS Project Template

A [`copier`] template for starting a free and open source (FOSS) project as recommended by [ESTRO].

> [!CAUTION]
> This is still in its very early stages and NOT yet officially endorsed by [ESTRO]!
>
> The idea is that this will eventually become a template to set up such a FOSS project according to best practices that are commonly used and needed in the radiation oncology community (or beyond that).

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
```

Then you will be asked a series of questions. After answering them, you should have a directory `your-project-dir` with an initialized structure and pre-filled files.

We strongly recommend to track this directory using [git]. That way, it is even possible to update the repo's contents when you want to e.g. change some of the provided answers or new features become available in this template repository.

Here is how to initialize a [git] repo and commit what [`copier`] set up for you:

```bash
cd your-project-dir
git init .
git add .
git commit -m "initialize project from template"
```

[git]: https://git-scm.com
