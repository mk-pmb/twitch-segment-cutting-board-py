
<!--#echo json="package.json" key="name" underline="=" -->
twitch-segment-cutting-board
============================
<!--/#echo -->

<!--#echo json="package.json" key="description" -->
Split/ select/ merge/ write individual MPEG-TS (transport stream) segments in
ways that help old VLC cope with Twitch.
<!--/#echo -->



Motivation
----------

Twitch streams as received by [streamlink][sl-official],
especially using my [streamlink-ubuntu-native][sl-ubunative] hack,
often contain system messages – white text on a slowly swirling
blue-purple background. This causes several problems:


#### Confusing timestamps

The system messages are sent with timestamps on their own timeline,
which doesn't fit the timeline of the timestamps of the actual content
segments sent by the streamer.
This confuses some players like Ubuntu's (slightly old) version of VLC.


#### Initial behind-the-scenes stories

Some streams start with a sequence of pseudo-funny messages telling a
tale of what Twitch servers or Twitch staff might be doing in order to
prepare the upcoming transmission.
Those come with music that is probably meant to be for audio testing.

It might be helpful in some exotic situations, but when you start a new
stream in the background and want to continue watching your current stream
until the new one actually arrives, that music is an annoyance.
It would be nice if we could cut it out.


#### "Commercial break in progress"

Fortunately, this message has no music. Rather, it is entirely silent.
Unfortunately, that also includes muting the real content's audio.

Since that message is meant to be advertisement or at least a stand-in
for something actually profitable, as not-logged-in users we'll have to
accept this disruption of service.

However, there are some aspects that we should be able to improve:

* __Predict the schedule.__
  This can then help you postpone any participation for which you want
  to see the reaction to until after the next ad break.
  * Twitch itself probably won't ever implement anything for that,
    as they probably hope the frustration helps convince you to at least
    identify yourself so you can enjoy the benefits of a potential gifted
    subscription. (Or maybe the bullying might even make you pay yourself.)
* __Cut it out from recordings.__
  However, when cutting it out completely (as streamlink would try when
  you enable its adblock option), any live-playing player in the output
  chain cannot discern it from a network outage.
  In those situations, a good compromise could be to let the first few
  frames pass through. That way, the interruption in non-live playback will
  be negligible, while a quick glance at the suddenly-mute live player
  still will immediately clarify the type of outage.
  * If we could reliably inject a custom notification sound,
    I wouldn't even have to glance at the player for clarification.
  * While a very short timeline anomaly in non-live VLC probably won't be
    much of a problem, it would be even nicer if we could fix up the
    timestamps nonetheless.
* __Use ad breaks as a cue to "switch tape",__
  i.e. begin a new file for the next part of the stream.
  This way, you can record by default (e.g. for pause-and-resume or
  instant replay) and still have a convenient way to release disk space
  for the parts that you're done watching.



Strategy
--------

This project targets embedded devices like my NAS.
Thus, we won't load a fancy MPEG TS parser.
Rather, we'll try and find low-level byte sequences that can give us a
good educated guess about where to cut the stream parts.

In order to handle binary data on stdio reliably, I'll use python3.






Usage
-----

:TODO:



<!--#toc stop="scan" -->



Known issues
------------

* Needs more/better tests and docs.




  [sl-official]: https://github.com/streamlink/streamlink
  [sl-ubunative]: https://github.com/mk-pmb/streamlink-ubuntu-native
  [wp-mpeg-ts]: https://en.wikipedia.org/wiki/MPEG_transport_stream


&nbsp;

License
-------
<!--#echo json="package.json" key=".license" -->
ISC
<!--/#echo -->
