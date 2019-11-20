import sys, json
import plotly.graph_objects as go

color0 = '#CCCC00'
color1 = '#00CC66'
color2 = '#00CCCC'
color3 = '#0066CC'
color4 = '#0000CC'
datafile = sys.argv[1]

with open(datafile,'r', encoding='utf8') as json_file:
    data = json.loads(json_file.read())

artistdict = {}

for entry in data:
    artist = entry["artistName"]
    track = entry["trackName"]
    try:
        num_plays = artistdict[artist][0] + 1
        artistdict[artist][0] = num_plays
    except:
        artistdict[artist] = [1, track]
    if track not in artistdict[artist]:
        artistdict[artist].append(track)

# print(artistdict)

artistname = []
artistplays = []
artisttracks = []
for key, entry in artistdict.items():
    if entry[0] > 5:
        artistname.append(key)
        artistplays.append(entry[0])
        num_tracks = len(entry) - 1
        if num_tracks > 15:
            artisttracks.append(color4)
        elif num_tracks >= 10:
            artisttracks.append(color3)
        elif num_tracks >= 5:
            artisttracks.append(color2)
        elif num_tracks > 1:
            artisttracks.append(color1)
        else:
            artisttracks.append(color0)
fig = go.Figure([go.Bar(x=artistname, y=artistplays, marker_color = artisttracks)])   
fig.update_layout(
    title=go.layout.Title(
        text="Title",
        font=dict(
            size=26
            ),
        xref="paper",
        x=0
        ),
     xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Song",
            font=dict(
                size=16,
                color="#7f7f7f"
                )
            )
        ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Plays",
            font=dict(
                size=16,
                color="#7f7f7f"
                )
            )
        )
)

fig.show()
