# nickhamlin.com  

(the new version)

Compiling:  
`pelican content`
`pelican -D content` (debug mode)
`pelican content -s publishconf.py`  
`pelican content -s pelicanconf.py`  

Running Locally:  
From inside the `output` folder: `python -m pelican.server` will run a server on [localhost:8000]

Deploying:  
Pushing to master will trigger a github action to automatically p

Accessing:  
http://nh-pelican-test.s3-website-us-east-1.amazonaws.com

Useful References
- https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/
- https://tvc-16.science/blogopolis-docker.html

