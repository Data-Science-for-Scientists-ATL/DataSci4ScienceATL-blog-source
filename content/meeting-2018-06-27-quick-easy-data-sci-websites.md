Title: Quick and Easy Data Science Websites
Date: 2018-06-27
Category: posts
Author: David Nicholson

# Quick and Easy Data Science Websites

At our last meeting, I gave a demo of how to make websites about what you're up to in data science. My demo followed the method that Jake Vanderplas uses, and that other famous totally awesome data scientists use, such as Christine Doig, and, uh, me. To be meta, I am now writing a blog post about that demo of how to make a blog. And to be even more meta, I made a website for our group by following my own demo. This blog post includes, as a bonus, stuff I remembered and/or figured out as I went through the process of setting up this site.

## high-level overview

Here's a high-level overview of how this will work, in list form.

1. **follow instructions for set up**
2. **write your posts**
3. **follow instructions to update after you write post**
4. tweet out your blog posts and hope someone reads them
5. repeat steps 2 through 4 as needed
6. ...
7. become a famous data scientist (sexiest job, 2014-present)
8. publish a book and / or start a podcast, e.g. "Make Your Own Data Science Playing Cards From Scratch"

Some of the items in the list are more tongue-in-cheek then others.

## instructions for set up

Apparently I like lists. Here's another! I'll give detail for each step below. Note again that my instructions here are based on the Jake Vanderplas approach, as he outlines in [this blog post](https://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/) and in the README for the source code for his blog, which he has helpfully made public in a [Github repository](https://github.com/jakevdp/jakevdp.github.io-source).

1. make sure you have git installed for version control, and so you can take advantage of Github
2. make a virtual environment for the software libraries you'll use to blog
  - pelican: a static website generator written in Python
  - jupyter to create notebooks
  - ghp-import: a script that lets you use Github Pages to host your site by doing all the work for you
  - some other tools that make it easy to use pelican and jupyter (Markdown, etc.)
3. set up a folder that will contain your blog, and initialize a git repository inside it
4. use `pelican-quickstart` command to quickly start a project (your blog)

None of the items in that list were tongue-in-cheek. I wouldn't want to try your patience.  
Okay, let's walk through each step in more detail.  

1. make sure you have git installed (us

2. ... and install the software libraries you'll use (with pip)


(pelican-blog) $ pip install pelican Markdown ghp-import
ing conda)
`$ conda install git`

2. make an environment (using conda) ...
```
$ conda create -n pelican-blog python=3.6 jupyter notebook
$ source activate pelican-blog
```

... and install the software libraries you'll use (with pip)

`(pelican-blog) $ pip install pelican Markdown ghp-import`

3. create a directory that will contain your blog, and initialize a git repository inside it
```
(pelican-blog) $ mkdir your-blog
(pelican-blog) $ cd your-blog
(pelican-blog) $ git init
```

Below are a couple more steps you need to execute *inside* the directory after you create it, although they fall under the category of "install the software libraries you'll use"
```
(pelican-blog) $ git submodule add https://github.com/danielfrg/pelican-ipynb
(pelican-blog) $ git submodule add https://github.com/getpelican/pelican-plugins
```
What you're doing here is some git voodoo that, as I understand it, makes these plugins part of your repository, but in such a way that you could still pull from them if their maintainers made some changes to the code.
Recent versions of git should get the actual code from these repos off Github and put it inside your local copy. But you might need to update your submodules, for example if you copy your own blog's repo off your Github profile onto another computer besides the one where you started the repo. In that case git doesn't pull in the code automatically so you need to execute:
`git submodule update --init --recursive`

4. use `pelican-quickstart` command to quickly start a project (your blog)
`(pelican-blog) $ pelican-quickstart`
Pelican will ask you a series questions about your site. You can safely accept all the defaults by just hitting enter--everything in this tutorial should work with those defaults.

## write your posts
I like to write in Markdown, like so ...

```Markdown
Title: Red, A Network Analysis Library
Date: 2018-06-27
Category: test

## Introduction
I just released the first version of a [network analysis library, Red](github/YourUserName/red.git).    

## How-To
Here's an example script in Python:
```Python
import red

twitter_data = red.datasets.twitter
red = RedCreador(twitter_data)

```

... although hardcore Pythonistas have the option of writing in RestructuredText.

### instructions to update after you write your post

1. use pelican to convert your Markdown post into html that browsers know how to read
`(pelican-blog) $ pelican content -o output -s pelicanconf.py`

2. use ghp-import to publish your Pelican site on Github, as either a Project Page or a User Page
```
(pelican-blog) $ ghp-import output
(pelican-blog) $ git push origin gh-pages
```
For a User Page, you need to "push" the content from the output directory to the master branch of a repository named Username.github.io. (So you should make one, replacing Username with your actual user name on Github,)
Github automagically converts a repository with such a name into a website.
Step-by-step instructions for this on the command line are on the next slide.

Note that this means you need a separate repository for your source code!
For example we have the source code for the group's blog in: https://github.com/Data-Science-for-Scientists-ATL/DataSci4ScienceATL-blog-source
And the "output" gets pushed to a different repository: https://github.com/Data-Science-for-Scientists-ATL/Data-Science-for-Scientists-ATL.github.io

so once you have set up the separate repository for your User Page, you'd push to it like so:
```
(pelican-blog) $ pelican content -o output -s pelicanconf.py
(pelican-blog) $ ghp-import output
(pelican-blog) $ git push https://github.com/Data-Science-for-Scientists-ATL/Data-Science-for-Scientists-ATL.github.io gh-pages:master
```
In the last line above, you are using git to *push* to your separate repository, specifically you're pushing the contents of the `gh-pages` branch of your **source** repository **to** the `master` branch of your `Username.github.io` repository. That's why at the end of the line you write `gh-pages:master`. Explaining the concept of git branches is beyond the scope of what I feel like writing right now :) but you can read about it in the "helpful links / more reading" section at the end of this post.

if pushing fails, e.g. because you already have content in the repository, you can force it with the -f flag, although be warned that this will write over everything:
`(pelican-blog) $ git push -f https://github.com/Data-Science-for-Scientists-ATL/Data-Science-for-Scientists-ATL.github.io gh-pages:master`

## Stylin'
One thing I didn't address much in my demo was how to apply themes.
I always find this confusing for Pelican; it comes with a tool to upload themes but then it basically copies them all to your computer, in such a way that they're not part of any one project.
I have a feeling that almost everyone modifies themes to some extent, so what would seem more natural to me would be a tool that would copy one individual theme into your project, in a themes subdirectory, so that you could then go ahead and modify it.
But currently there's no built-in tool to do that, as I remembered after staring at the docs, so I did what some other part of the docs suggests instead, which was to copy all the themes myself to some other place on my computer, and then copy one of those themes to my project folder.  
I went with `pelican-bootstrap3` because it has a lot of bells and whistles.
I very much recommmend reading the README.md for `pelican-bootstrap3`. In particular note that you need to add the following lines to your `pelicanconf.py` file:
```Python
PLUGIN_PATHS = ['path/to/plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
```
If you don't do this, you will get a very helpful error message:

Apparently, I am not the first person to experience this: https://github.com/getpelican/pelican-themes/issues/482

Anyhow, I based my decision to use `pelican-bootstrap3` in part on this handy blog post from Christine Doig that explains in detail how she modified her theme. Lots of good ideas there:
https://chdoig.github.io/create-pelican-blog.html

## Summary
Okay, now you've read a blog post about the meeting of our data science group yesterday about how you set up a your own data science blog, based on a bunch of data science blogs! Now you can set up your own blog and blog about data science blogging! Please let us know when your book comes out and look for much less meta posts from the future, unless this is the only post we ever write.

## Helpful links + more reading
- get Anaconda here, with the conda command-line tool for managing packages and installing libraries (including many scientific libraries): https://www.anaconda.com/download/
- good example of why you would use virtual environments: https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
- all about Markdown: https://daringfireball.net/projects/markdown/
- using ghp-import to publish to Github (from Pelican docs): http://docs.getpelican.com/en/stable/tips.html#publishing-to-github
- branching: what is it? https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
- pelican themes: http://pelicanthemes.com/
- how to use themes: https://github.com/getpelican/pelican-themes#using-themes

