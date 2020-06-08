FROM  vorakl/alpine-pelican:latest

# https://github.com/Difegue/TVC-16/blob/master/.github/action-pelican/Dockerfile
LABEL "name"="nick-website-build"
LABEL "version"="0.0.1"

LABEL "com.github.actions.name"="Build My Website"
LABEL "com.github.actions.description"="Runs pelican to build master branch"
LABEL "com.github.actions.icon"="eye"
LABEL "com.github.actions.color"="green"

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN pip install pelican-jupyter

ENTRYPOINT ["/entrypoint.sh"]