Project Setup
=============

setting up django is very easy. Real pain is given by nodejs, webpack and frontend stuffs. Do the following: 

- install node and npm
- run `npm install` [This will install things from package.json]
- run `npm install typings -g`
- run `typings install`
- copy zone.js from node_modules to assets/lib/js/
- include bundle.js and zone.js in html file, after the body tag (inside head will cause problems as DOM is not ready)

That should work
