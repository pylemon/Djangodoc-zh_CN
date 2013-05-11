Djangodoc-zh_CN
===============

django documentation chinese version

* Use django opensource project to get the latest content for translations

submodules
==========
* django
  django source code use latest stable version tags/1.5.1
  This is where the sphinx content comes from. make sure it is using the same version with the django-docs-translations.
  
* django-docs-translations
  django translations project use the branch stable/1.5.x
  This is where the pot files comes from. make sure it is on the right   branch.

Steps
=====

# TODO
* try to make these steps into a python script.

1. setup the django and django-docs-translations to the right version.

    $ git submodules update --init --rebase
    $ cd django
    $ git checkout 1.5.1
    $ cd ../
    $ cd django-docs-translations
    $ git checkout stable/1.5.x
    $ cd ../

1. copy all the pot files from django-docs-translations to pots folder.

    $ cp django-docs-translations/pots/* pots/
    $ cp pots/* translations/zh_CN/
    
1. change the filenames in translateions/zh_CN from *.pot to *.po

    $ cd translations/zh_CN
    $ for filename, ext in <this folder>
    $ !mv filename+ext filename+'.po'
    
1. translate the po files.
   
    edit the po files to make strings translated.


Make a readable doc on RTD
==========================

1. copy the docs from django project.

    $ cp -a django/docs .
    
1. make mo files.
   
    $ for filename, ext in translations/zh_CN/*.po
    $ msgfmt "filename + ext" -o "translated/zh_CN/LC_MESSAGES/filename + .mo"

1. update config file for sphinx.

    open docs/conf.py:find language = None
    update lines:
    language = "zh_CN"
    locale_dirs = ['../translated/']

1. make html using sphinx

    $ cd docs
    $ make html

1. the final docs will be in folder

    ~/Djangodoc-zh_CN/docs/_build/html/index.html


Get all the translations from online
====================================

1. get all the translations from online. this updates the `translations/zh_CN/LC_MESSAGES/*.po`

    $ tx pull -a

1. you can also edit the po files from local machine. then upload them to online.

    $ tx push -t
    
    
