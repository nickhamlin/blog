# nickhamlin.com  

## About

My personal website was old, hard to update, and less useful than it could be. I want to be able to:

- Add content quickly and easily without having to worry about deploying
- Retain a lot of control over how things looked and worked
- Write in both markdown and jupyter notebooks
- Have a (somewhat) polished landing page for traditional portfolio purposes as well as a separate place for whatever incomplete ideas I might have
- Store structured career portfolio info in a structured way so that I could easily remix it into whatever format/structure I might want in the future

Pelican (a python-based static site generator) forms the core of site and uses a custom theme to support the more heavily styled portfolio pages. The [pelican-jupyter](https://github.com/danielfrg/pelican-jupyter) plugin allows for jupyter notebook support. 

## Writing

New posts should be added in the `content` directory and organized into subdirectories based on category. Posts should have the following metadata either at the top of the markdown document or in the first cell of the jupyter notebook.

- `Title`: Post title, lower-skewer-case version will be used as the url
- `Date`: Should be in MMMM-YY-DD format and will determine order on `archives` page
- `Template`: Should usually be `article`, except in rare situations that haven't really come up yet
- `Homepage`: if `True`, then the post will appear on the main portfolio page
- `image`: Name of file in `theme/static/images` to use as homepage tile. Only required for posts appearing on the homepage.

Metadata not yet implemented/confirmed functional:

- `Tags`
- `Status`

Metadata deliberately not used:

- `Author`

## Running Locally

`pelican -l --autoreload` will run a server on [localhost:8000] and automatically rebuild when something is saved

Additional commands that might be useful but will rarely be necessary:

`pelican content`  
`pelican -D content` (debug mode)  
`pelican content -s pelicanconf.py` (dev)  
`pelican content -s publishconf.py` (prod)  

## Deploying

Pushing to master will trigger a github action that will automatically build all the pelican files and deploy to s3

## Useful References

- https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/
- https://tvc-16.science/blogopolis-docker.html
