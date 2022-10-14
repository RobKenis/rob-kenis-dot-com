FROM klakegg/hugo as build

WORKDIR /build

COPY ./ ./

RUN hugo -d out/ --environment development

FROM nginx

COPY --from=build /build/out/ /usr/share/nginx/html
