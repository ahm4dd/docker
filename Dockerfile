FROM debian:stable-slim

# COPY source destination
COPY docker /bin/docker

ENV PORT=8991

CMD ["/bin/docker"]

