# nickhamlin.com  

(the new version)

Compiling:  
`pelican content`  
`pelican -D content` (debug mode)  
`pelican content -s pelicanconf.py`  (dev)
`pelican content -s publishconf.py`  (prod)


Running Locally:  
'pelican -l' will run a server on [localhost:8000]

Deploying:  
Pushing to master will trigger a github action to automatically p

Accessing:  
http://nh-pelican-test.s3-website-us-east-1.amazonaws.com

Useful References
- https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/
- https://tvc-16.science/blogopolis-docker.html

Other notes:
This setup uses the [pelican-jupyter](https://github.com/danielfrg/pelican-jupyter) plugin (via git submodule) to allow for easy building of pages out of notebooks