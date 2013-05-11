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



    
    
    
    