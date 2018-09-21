# readme.md

place domains in same host/vhost, generate nginx configs by this image.

## how to generate domain content

use markdown to write articles.

use sphinx to generate the site.



```
# hint: change the aaa.dom to your site domain
docker run --rm -v ${YOUR_ROOT_1}/aaa.dom:/data -w /data lua511/sphinx make html
# you need run for all sites on the host/vhost.
```

## how to generate config

```
docker run --rm -v ${YOUR_ROOT_1}/wroot:/wwwroot -v ${YOUR_ROOT_2}/wconf:/wwwconfig lua511/gen-nginx-sites
```

## build image
```
docker build -t gen-nginx-sites .
```