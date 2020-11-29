Title: The Internet Is Complicated
Date: 2020-11-28
Template: article

I just spent the afternoon doing a little sprucing up on this site to make it easier to [cultivate my digital garden](/garden). I'm using a custom pelican theme that I'm slowly implementing as I need new features, so I figured this should be pretty straightforward. Adding a simple list of post categories to a blog should be super simple, right?

### Here's what I had to do to make that happen

- Figure out the difference between categories and tags in Pelican
- Think through how to categorize my other posts in a way that Future Me wouldn't hate
- Realize that Pelican already has patterns for this and I can probably just modify some out-of-the-box examples
- Create Jinja templates for both `categories` and `category`
- While doing that, realize many of my current other templates look a little ugly and need some tweaks. Make them.
- Figure out why the links weren't working between those two new pages (answer: [Pelican has lots of URL config options](https://docs.getpelican.com/en/stable/settings.html#url-settings))
- Figure out why those new pages couldn't load any CSS (answer: missing leading slashes in my base template)
- Remember that I want to refer to this as "garden" in the structure of the site. Futz with the pelican settings more to allow that.
- Discover that the github action responsible for the deploy stopped working due to an underlying dependency failure in the upstream docker image
- [Fix that dependency failure](https://stackoverflow.com/questions/51915174/how-to-install-pyzmq-on-a-alpine-linux-container)
- Get the site to deploy, but wonder why nothing works
- Realize that in order to display static sites without trailing `.html` extensions on everything, [S3 needs to have `text/html` filetypes explicitly set](https://stackoverflow.com/questions/23463679/s3-static-pages-without-html-extension) and must not have any files with that extension
- Realize that removing the `.html` extension from files causes naming collisions with certain folders. Rethink the file structure yet again until I come up with something new that works.
- Figure out [how to set the html filetypes via a flag on the sync command](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
- Get that working, but now see that everything loads without styling again
- Realize that S3 needs other specific types specified for CSS/JS
- Learn [there's not really a good way to specify multiple filetypes in one copy step](https://github.com/aws/aws-cdk/issues/7090)
- Add separate steps to the github action to deploy each different filetype separately


### Bonus additional steps

- Write all these steps down in this post
- Preview the post, discover my styling somehow doesn't add any tickmarks to bulleted lists, rendering the list above impossible to read
- Look up [all the different list style options](https://www.w3schools.com/cssref/tryit.asp?filename=trycss_list-style-type_all)
- Find the place in my css where that should be added and insert it
- Notice that now the indentation is off
- Go back and add some extra margin to get everything to line up right (after initially forgetting the difference between margin and padding)
- Make mental plans to link to this post the next time I hear anyone say "I'm not a real coder, I always have to look so much stuff up!"

