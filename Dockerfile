FROM python:3.9-alpine as nginx-serve-static-build
WORKDIR /nginx-serve-static
COPY . /nginx-serve-static
RUN pip install --no-cache-dir -r requirements.txt
RUN python main.py

FROM nginx:latest
ARG STATIC_LOCAL_DIR
ARG STATIC_DOCKER_DIR
COPY ${STATIC_LOCAL_DIR} ${STATIC_DOCKER_DIR}
COPY --from=nginx-serve-static-build /nginx-serve-static/nginx.conf /etc/nginx/nginx.conf
