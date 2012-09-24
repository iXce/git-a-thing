git-a-thing
===========

git-based distributed design sharing platform

Basic architecture :
- Authentification through django-social-auth
- DBMS storing users (just a few profile infos), things (including multi-parent derivative information) and likes/made, and distribution information
- The files related to each design are stored in a git repository (Dulwich package is used for git handling in python)
- Users can clone the git repos (over http/git protocol or ssh) and push to them through ssh through a gitosis/gitolite-like system
- Git branches are handled as derivatives from the same user
- Git tags can be used to publish new major versions of the design
- Derivatives of designs owned by other users are handled as github forks (starting from a clone of the original repo)
- Disqus for comments
- All user repos can also be referenced in a master git repo as git submodules for an easy clone of the whole infrastructure, though this might not very well work with the instance model described below (what happens if two instances have the same repo, but one is in a state where it cannot be merged into the other or vice-versa ? which do you select for being in the master git ?)

How distribution works ?
- Clustered DBMS if needed (though a single DBMS node can probably handle the load)
- Web frontends can be set on several federated instances (i.e. anyone can set up a read only instance, and people can get their instance to be able to read-write by getting known and trusted ; this can probably be improved though)
- git repos can be on any instance, and the central instance has a table listing which known instance has which repo
- When a user accesses a design which is not available on the current instance, they get redirected to an instance which has the corresponding repo

Included external dependencies
==============================
- Twitter Bootstrap, for CSS magic http://twitter.github.com/bootstrap/

External dependencies
=====================
- Dulwich, for python-git interaction http://www.samba.org/~jelmer/dulwich/
- django-social-auth, for authentication handling https://github.com/omab/django-social-auth
- django-rest-framework, for the RESTful API http://django-rest-framework.org/
- django-licenses, for License management http://bitbucket.org/jezdez/django-licenses/
- django-bootstrap-form, for prettier forms https://github.com/tzangms/django-bootstrap-form
