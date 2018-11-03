# home

The [Cleveland PyLadies website](https://clepyladies.github.io/pyladies-official) is built on Pelican, a Python-based static site generator. To contribute content posts: fork this repo, create your post as a markdown file (`.md`) in the `content` folder, and make a pull request. We love community contributions and happily accept pull requests from first-time contributors! Don't know where to start? Attend a meetup and we'll help you get started!

Organizer notes:

* The site build is automated by Travis-CI on any merges or commits to master.

* Check to see if your fork is ## commits **behind** master before submitting pull requests. (Behind master could end up being problematic, depending on your change.) You can compare across forks and `git fetch upstream master` from your fork's local clone, if necessary. Note that you may lose changes if your fork is behind the site repo, so make changes in small increments.

* The format for adding custom attributes to markdown elements is `{: attribute='value' }` .
