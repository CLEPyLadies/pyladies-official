Title: Contribute Content
Date: 2018-09-16 13:49
Modified: 2018-09-16 13:50
Category: Blog
Tags: Open-Source, Contribute, Pull Requests, Newbies, First PR, Write, Code
Slug: get-started
Authors: Cleveland PyLadies, Marissa Utterberg
Summary: Some helpful info for first-time contributors.
Image: images/ResourcesBanner.png


# So you want to make a PR

GREAT! We love pull requests.
The easiest way to get involved is to write about your experiences with Python and PyLadies on our blog.
Here are a few steps to help you get started:

1. Decide what you will write. It may be helpful to draft it out in your word processor or text editor of choice first.

2. Fork this repo!

3. Clone your fork to a directory on your machine so that you can develop in your text editor of choice.

4. Add a .md file with your post in the 'content' folder **on branch master**. Your file needs to have a line with the title
`Title: {{ your awesome title here }}`
and may have any/all of the following metadata:

`Date: 2010-12-03 10:20`

`Modified: 2020-12-05 19:30`

`Category: Blog # PLEASE CHOOSE AN EXISTING CATEGORY - We may edit your category if it does not match our menu bar.`

`Tags: pelican, publishing # Choose any tags you like! Tag it up!`

`Slug: my-super-post # Defaults to your title, but you may set it directly.`

`Authors: Cleveland PyLadies, Floaty McFloatFace # Own it, lady!`

`Summary: Short version for index and feeds # Again all of these are optional.`

Your super content goes below your metadata block. Remember to commit changes with meaningful messages before moving on!

You can preview changes you've saved locally with the following steps:
 - open a terminal and run `cd pyladies-official` (the location of your cloned fork)
 - (run `python -m venv myvenv` if you haven't already done so in that directory)
 - run `source myvenv/bin/activate` to activate the virtual environment you created for this project
 - (run `pip install --upgrade pip` and then `pip install -r requirements.txt` if this is the first time you've activated this virtual environment)
 - run `pelican content` to generate the site html files locally
 - run `./develop_server.sh start` to make your version of the site available locally
 - Check it out by opening `http://localhost:8000` in your internet browser of choice.

When you are satisfied with the look of your article or other change:

5. Check to see if your fork is behind the main repo by any number of commits. These may cause problems if merge commits emerge between fork and PR.

6. Make a new pull request **from [the main repo](https://github.com/CLEPyLadies/pyladies-official)** by selecting `compare across forks`, setting your fork master as the head, giving your PR a meaningful title, and submitting your request.

7. BOOM! You're officially an open-source contributor. We may ask for changes before merging your fork, but you've successfully gotten started!
Shoot us an email or get at us on social if more than a week goes by and we haven't addressed your PR. We are very encouraging of new contributors, so give it a shot!
