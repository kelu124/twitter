# echOpen processing tweets (ept tool)

Using the graph. Get all the tweets from gdrive to tsv files (an archive is provided)

> usage : python ept.py tweets.tsv > graph.gdf

Remove all echopenorg mentions? Just 

> sed "/@echopenorg/d" ./graph.gdf > ./graph_clean.gdf



Patched up together by @kelu124 to help visualize echopen.org twittosphere
