ls | grep ".png" | cat -n | while read n f; do mv "$f" "$n.png"; done 
