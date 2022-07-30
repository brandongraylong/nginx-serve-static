# Nginx Server Static
Jinja2-templated nginx.conf to serve static files.

## Requirements
Python 3.x and Nginx or Docker.

## Examples
### Python
- Run `python main.py --listen 80 --server-name "example.org www.example.org" --location / --root /www/data --index index.html`
- If on Linux, run `sudo nginx.conf /etc/nginx/nginx.conf`
- Copy static files to `/www/data`
- Restart nginx

### Docker
- Create .env file in root of project:
```
LISTEN=80
SERVER_NAME=example.org www.example.org
LOCATION=/
ROOT=/www/data
INDEX=index.html
```
- Place static files in ./static/* (make sure to include at least an `index.html`)
- Run `docker build -t nginx-serve-static . --build-arg STATIC_LOCAL_DIR=./static --build-arg STATIC_DOCKER_DIR=/www/data`
- Run `docker run -p 9999:80 nginx-serve-static:latest`

## TODO
- Maybe change from rendering a single server section to rendering any number of server sections based on a yaml config file? So you can have as many server directives you want.
- Add more places to render arbitrary lines.
