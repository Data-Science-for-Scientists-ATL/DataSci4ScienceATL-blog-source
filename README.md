based on the Jake Vanderplas approach: 
<https://github.com/jakevdp/jakevdp.github.io-source>

Install required packages:

```bash
$ conda create -n pelican-blog python=3.5 jupyter notebook
$ source activate pelican-blog
$ pip install pelican Markdown ghp-import
$ pelican-quickstart
$ git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
$ git submodule add git://github.com/getpelican/pelican-plugins.git plugins/pelican-plugins
```

If you clone this repo, you'll need to pull in the submodules with an update:
`$ git submodule update --init --recursive`

The Makefile (also adapated from Jake Vanderplas) enables one-liners for 
viewing changes locally and for pushing to the Github pages repo from the source repo.
To see how:
`$ Makefile help`

On Windows you can run `view-local.bat` and one of the  `push-to-github.bat` 
scripts to achieve approximately the same thing.