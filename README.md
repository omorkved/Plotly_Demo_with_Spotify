# Plotly Demo with Spotify
Quick demo from summer 2019 -- was testing Plotly capabilities on my spotify data to do a plotly proof-of-concept.
(Yes, this is was a pretty rushed thing, but I thought it worth it to throw up on Git)

# To test demo:

Option one -- Bash:

Make `init.py` executable 

Run: 

`./init.sh` (this installs Plotly, so activate a virtual env if desired)

This will show a demo graph of spotify usage

Option two -- run yourself:
  `pip install -r requirements`
  
  `python readdata.py SampleStreamingHistory.json` 
  
  
# Test your own spotify data:

Download your streaming data
https://www.makeuseof.com/tag/download-privacy-data-spotify/

(Have to wait a few days, sorry! That's why I've included sample data in this repo!)

Your downloadable data will include a json file entitled StreamingHistory.json


Run:
`python readdata.py /path/to/your/StreamingHistory.json`
  
# A note:
Did this summer primarily to test out Plotly as a viable Matplotlib alternative, and not to create a cool Spotify feature.
I've since then realized there's a pretty comprehensive Spotify Web API and am planning to mess around with it on this repo once 
the academic quarter ends :)

