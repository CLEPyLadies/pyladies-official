# home

The [Cleveland PyLadies website](https://clepyladies.github.io/pyladies-official){: aria-label='Cleveland PyLadies' } is built on Pelican, a Python-based static site generator. To contribute content posts: fork this repo, create your post as amarkdown file in the content folder, and make a pull request. We love community contributions and happily accept pull requests from first-time contributors! Don't know where to start? Attend a meetup and we'll help you get started!

Organizer notes:

* Can we put together a video walkthrough of making a PR to this site? I'd love to have a custom YouTube resource to help familiarize newbies with the process.

* The site build is automated by Travis-CI on any merges or commits to master.

* Check to see if your fork is ## commits **behind** master before submitting pull requests. (Behind master could end up being problematic, depending on your change.) You can compare across forks and `git pull` from the original repo directly on GitHub, if necessary. Note that you may lose changes if your fork is behind the site repo, so make changes in small increments.

* The format for adding custom attributes to markdown elements is `{: attribute='value' }` . We may want to do this on all elements to include aria-label for screen reader accessibility. For example, the raw example above would translate to `<a aria-label='Cleveland PyLadies' href='https://clepyladies.github.io/pyladies-official'>Cleveland PyLadies website</a>` upon build.
