set -e
D="/mnt/user-data/uploads/Marketing Department Ola/Video Photo Ola"
R=/tmp/claude-0/-home-claude/16b815b6-6568-5797-a585-2ec6af0bf98e/scratchpad/reels
k=$1; name=$2; hook="$3"
(cd $R && python3 hook.py "$hook" /tmp/claude-0/-home-claude/16b815b6-6568-5797-a585-2ec6af0bf98e/scratchpad/vbatch/h_$name.png)
ffmpeg -v error -y -i "$D/$k.mp4" -i h_$name.png -i $R/logo.png -filter_complex "[0:v]scale=1080:1920,setsar=1,ass=$k.ass[c];[c][2:v]overlay=0:0[a];[a][1:v]overlay=0:0:enable='lt(t,3.5)',fps=30,format=yuv420p[v];[0:a]aresample=44100,aformat=channel_layouts=stereo[au]" -map "[v]" -map "[au]" -c:v libx264 -crf 22 -preset fast -c:a aac -b:a 160k m_$name.mp4
printf "file 'm_$name.mp4'\nfile '../video/end.mp4'\n" > l_$name.txt
ffmpeg -v error -y -f concat -safe 0 -i l_$name.txt -c:v libx264 -crf 23 -preset fast -maxrate 4000k -bufsize 8000k -c:a aac -b:a 160k -movflags +faststart $name.mp4
echo done $name
