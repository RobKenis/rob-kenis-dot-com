FROM docker.io/klakegg/hugo as build

WORKDIR /build

COPY ./ ./

RUN hugo -d out/ --environment development

FROM docker.io/nginx

COPY --from=build /build/out/ /usr/share/nginx/html
