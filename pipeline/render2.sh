# usage: bash render2.sh week_ro.json list.txt   (list: "<id> <musicVariant>" per line) — run from pipeline/
export NODE_PATH=$(npm root -g)
J=$1; mkdir -p out
while read id m; do
  [ -f out/$id.mp4 ] && continue
  rm -rf tmp_$id; mkdir -p tmp_$id
  node reel2.js $id 22 $J 25 tmp_$id >/dev/null 2>&1 && ffmpeg -v error -y -framerate 25 -i tmp_$id/f%04d.jpg -i lm$m.wav -c:v libx264 -pix_fmt yuv420p -crf 21 -c:a aac -b:a 160k -shortest -movflags +faststart out/$id.mp4 && ffmpeg -v error -y -ss 0.2 -i out/$id.mp4 -frames:v 1 -vf scale=270:-1 out/$id.thumb.jpg
  rm -rf tmp_$id
done < $2
