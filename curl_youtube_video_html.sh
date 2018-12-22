#time curl -s https://www.youtube.com/watch?v=UAor3YnvcQ4 | grep "\" title=\"" | grep alternate | tail -n 1 | perl -pe 's/.*="//g;s/".*//g'
#time curl -s https://www.youtube.com/watch?v=UAor3YnvcQ4 | grep "\" title=\"" | grep alternate | tail -n 1 
#   <link rel="alternate" type="text/xml+oembed" href="http://www.youtube.com/oembed?format=xml&amp;url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DUAor3YnvcQ4" title="Making Lemon Cordial">
#time curl -s https://www.youtube.com/watch?v=UAor3YnvcQ4 | grep "\" title=\"" | grep alternate 
# <link rel="manifest" href="/manifest.json"><link rel="shortlink" href="https://youtu.be/UAor3YnvcQ4"><link rel="search" type="application/opensearchdescription+xml" href="https://www.youtube.com/opensearch?locale=de_DE" title="YouTube-Videosuche"><link rel="shortcut icon" href="https://s.ytimg.com/yts/img/favicon-vfl8qSV2F.ico" type="image/x-icon">     <link rel="icon" href="/yts/img/favicon_32-vflOogEID.png" sizes="32x32"><link rel="icon" href="/yts/img/favicon_48-vflVjB_Qk.png" sizes="48x48"><link rel="icon" href="/yts/img/favicon_96-vflW9Ec0w.png" sizes="96x96"><link rel="icon" href="/yts/img/favicon_144-vfliLAfaB.png" sizes="144x144"><meta name="theme-color" content="#ff0000">        <link rel="alternate" href="android-app://com.google.android.youtube/http/www.youtube.com/watch?v=UAor3YnvcQ4">
#       <link rel="alternate" type="application/json+oembed" href="http://www.youtube.com/oembed?format=json&amp;url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DUAor3YnvcQ4" title="Making Lemon Cordial">
#   <link rel="alternate" type="text/xml+oembed" href="http://www.youtube.com/oembed?format=xml&amp;url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DUAor3YnvcQ4" title="Making Lemon Cordial">
#time curl -s https://www.youtube.com/watch?v=UAor3YnvcQ4 | grep "\" title=\"" 
time curl -s https://www.youtube.com/watch?v=UAor3YnvcQ4 


