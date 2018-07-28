mogrify -verbose -path ../_data_3 -filter Lanczos -format png -resize "500x500^" -gravity center -crop 500x500+0+0 +repage *.jpg
