git-a-thing
===========

git-based distributed design sharing platform

Basic architecture :
- Authentification through django-social-auth
- DBMS storing users (just a few profile infos), things and likes/made, and distribution information
- The files related to each design are stored in a git repository (Dulwich package is used for git handling in python)
- Users can clone the git repos (over http/git protocol or ssh) and push to them through ssh through a gitosis/gitolite-like system
- Derivatives are handled as github forks (starting from a clone of the original repo)
- Disqus for comments

How distribution works ?
- Clustered DBMS if needed (though a single DBMS node can probably handle the load)
- Web frontends can be set on several federated instances (i.e. anyone can set up a read only instance, and people can get their instance to be able to read-write by getting known and trusted ; this can probably be improved though)
- git repos can be on any instance, and the central instance has a table listing which known instance has which repo

Dependencies
============
- Dulwich, for python-git interaction http://www.samba.org/~jelmer/dulwich/
- django-social-auth for authentication handling https://github.com/omab/django-social-auth
- django-rest-framework for the RESTful API http://django-rest-framework.org/
