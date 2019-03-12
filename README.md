# A JS console log redirecter

Sometimes is it usefull to extract javascript console logs from the browser, to easilly analyse them elsewhere.
This is a basic and hacky tool to allow just that.

It has two parts: the first is a short js script that should be injected into the page that you want to monitor.
This script will capture the console log output and send it via ajax to a local server.
This server is a basic Flask app in docker, that does nothing but capture the dat and store it in a local mongodb (that is also in a container).
This app can be extended to allow some log parsing for instance.
