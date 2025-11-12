(add logo here when i make one)

(add map here)

## Context 

This is a project I started because of my university dissertation on the presence of US bases in Okinawa, Japan, and one of the sections is about the geographical areas of where the territorial boundaries are located and analysing the data.

I spent approximately 50 hours in total manually mapping the areas while binge listening to Nujabes (10/10 experience btw, would recommend). I did lose around 2 days worth of work due to a saving error and I'm probably on some sort of watchlist by now, but it was all worth it :trollface:


<br>

## Sources

I found that many sources have missing bases, inaccurate borders, and conflicting reports. A lot of previously done maps on this topic have their problems as well with the aforementioned issues. Even the official Japanese Ministry of Defense website had errors such as wrong military base names and designated borders that makes no sense, and mismatched borders between the reports and reality. 

So to accompany this, I did my best to compile the correct details and discarded the incorrect ones from each source I could find to make it as accurate as possible. 


<br>

## Mapping methodology

Most of the mapping was done by viewing previous maps to view the general shape and area of the target base, then trace the borders through installations of the fences using a combination of google maps, google streetview, a bit of python scripting, and ArcGIS. 

The satellite imagery was sometimes fuzzy and impossible to view with the human eye, but google maps and ArcGIS both have varying clarity depending on the area and time. The difference in time when it was taken is also a very important detail, because the sun is casting shadows at different angles, and sometimes the fences can be found and identified this way.

(show example here)


## What is included and what is omitted
There's many categories that I can classify for what was mapped:
  1. Fully enclosed within fences
  2. Enclosed with an unfenced coastline
  3. Island territory with no fences and nothing on it
  4. Designated territory with no fences and nothing on it (I'll explain below)
  5. Maritime territory

I didn't include the many territories that were "designated" but publicly accessible. For example:

| Mod website | Google streetview | Explanation |
(show examples of this phenomenon with the Ie Jima road and the parking lot in Kadena I think)

The only exception to this is Kume Jima Range, because despite being tiny, unfenced, and desolate, it has its own unique entry in the Japanese MoD website unlike the examples I showed above.

## Data for nerds:
