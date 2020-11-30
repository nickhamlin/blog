Title: Todos and improvements to this site
Date: 2020-11-29
Template: article

Last Updated: 2020-11-29

## Improvements

- Audit page load time and make optimizations accordingly
    - Shrink unnecessarily large images - DONE
    - Preload CSS - DONE
- Remove unnecessary JS/CSS
    - Serve fontawesome from CDN
    - Serve fonts from CDN
    - Remove flexslider dependency
    - Potentially remove all jQuery dependencies, if not, at least upgrade it and deliver via CDN
- Consider whether or not implementing tags is worth it. Would it be useful to have/actually add something new?

## Issues

- Fix problem with extra vertical space going into the footer instead of main page body
- "Back to top" button doesn't work without a #home anchor