# nickhamlin.com  

## About

My personal website was old, hard to update, and less useful than it could be. I want to be able to:

- Add content quickly and easily without having to worry about deploying
- Retain a lot of control over how things looked and worked
- Write in both markdown and jupyter notebooks
- Have a (somewhat) polished landing page for traditional portfolio purposes as well as a separate place for whatever incomplete ideas I might have
- Store structured career portfolio info in a structured way so that I could easily remix it into whatever format/structure I might want in the future

Pelican (a python-based static site generator) forms the core of site and uses a custom theme to support the more heavily styled portfolio pages. The [pelican-jupyter](https://github.com/danielfrg/pelican-jupyter) plugin allows for jupyter notebook support. 

## Compiling

`pelican content`  
`pelican -D content` (debug mode)  
`pelican content -s pelicanconf.py` (dev)  
`pelican content -s publishconf.py` (prod)  

## Running Locally

`pelican -l` will run a server on [localhost:8000]

## Deploying

Pushing to master will trigger a github action that will automatically build all the pelican files and deploy to s3

## Useful References

- https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/
- https://tvc-16.science/blogopolis-docker.html
