1 Synopsis
2 Description
3 Detailed description
3.1 Streamcopy
3.2 Trancoding
3.3 Filtering
3.3.1 Simple filtergraphs
3.3.2 Complex filtergraphs
3.4 Loopback decoders


1 Synopsis
ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...
2 Description
ffmpeg is a universal media converter. It can read a wide variety of
inputs - including live grabbing/recording devices - filter, and transcode them
into a plethora of output formats.
ffmpeg reads from an arbitrary number of inputs (which can be regular
files, pipes, network streams, grabbing devices, etc.), specified by the
-i option, and writes to an arbitrary number of outputs, which are
specified by a plain output url. Anything found on the command line which cannot
be interpreted as an option is considered to be an output url.
Each input or output can, in principle, contain any number of elementary streams
of different types (video/audio/subtitle/attachment/data), though the allowed
stream counts and/or types may be limited by the container format. Selecting
which streams from which inputs will go into which output is either done
automatically or with the -map option (see the Stream selection
chapter).
To refer to inputs/outputs in options, you must use their indices (0-based).
E.g. the first input is 0, the second is 1, etc. Similarly,
streams within an input/output are referred to by their indices. E.g. 2:3
refers to the fourth stream in the third input or output. Also see the
Stream specifiers chapter.
As a general rule, options are applied to the next specified
file. Therefore, order is important, and you can have the same
option on the command line multiple times. Each occurrence is
then applied to the next input or output file.
Exceptions from this rule are the global options (e.g. verbosity level),
which should be specified first.
Do not mix input and output files – first specify all input files, then all
output files. Also do not mix options which belong to different files. All
options apply ONLY to the next input or output file and are reset between files.
Some simple examples follow.
Convert an input media file to a different format, by re-encoding media streams:
ffmpeg -i input.avi output.mp4
Set the video bitrate of the output file to 64 kbit/s:
ffmpeg -i input.avi -b:v 64k -bufsize 64k output.mp4
Force the frame rate of the output file to 24 fps:
ffmpeg -i input.avi -r 24 output.mp4
Force the frame rate of the input file (valid for raw formats only) to 1 fps and
the frame rate of the output file to 24 fps:
ffmpeg -r 1 -i input.m2v -r 24 output.mp4
The format option may be needed for raw input files.
3 Detailed description
ffmpeg builds a transcoding pipeline out of the components listed
below. The program’s operation then consists of input data chunks flowing from
the sources down the pipes towards the sinks, while being transformed by the
components they encounter along the way.
The following kinds of components are available:
Demuxers (short for "demultiplexers") read an input source in order to
extract
global properties such as metadata or chapters;
list of input elementary streams and their properties
One demuxer instance is created for each -i option, and sends encoded
packets to decoders or muxers.
In other literature, demuxers are sometimes called splitters, because
their main function is splitting a file into elementary streams (though some
files only contain one elementary stream).
A schematic representation of a demuxer looks like this:
┌──────────┬───────────────────────┐
│ demuxer  │                       │ packets for stream 0
╞══════════╡ elementary stream 0   ├──────────────────────►
│          │                       │
│  global  ├───────────────────────┤
│properties│                       │ packets for stream 1
│   and    │ elementary stream 1   ├──────────────────────►
│ metadata │                       │
│          ├───────────────────────┤
│          │                       │
│          │     ...........       │
│          │                       │
│          ├───────────────────────┤
│          │                       │ packets for stream N
│          │ elementary stream N   ├──────────────────────►
│          │                       │
└──────────┴───────────────────────┘
▲
│
│ read from file, network stream,
│     grabbing device, etc.
│
Decoders receive encoded (compressed) packets for an audio, video,
or subtitle elementary stream, and decode them into raw frames (arrays of
pixels for video, PCM for audio). A decoder is typically associated with (and
receives its input from) an elementary stream in a demuxer, but sometimes
may also exist on its own (see Loopback decoders).
A schematic representation of a decoder looks like this:
┌─────────┐
packets  │         │ raw frames
─────────►│ decoder ├────────────►
│         │
└─────────┘
Filtergraphs process and transform raw audio or video frames. A
filtergraph consists of one or more individual filters linked into a
graph. Filtergraphs come in two flavors - simple and complex,
configured with the -filter and -filter_complex options,
respectively.
A simple filtergraph is associated with an output elementary stream; it
receives the input to be filtered from a decoder and sends filtered
output to that output stream’s encoder.
A simple video filtergraph that performs deinterlacing (using the yadif
deinterlacer) followed by resizing (using the scale filter) can look like
this:
┌────────────────────────┐
│  simple filtergraph    │
frames from ╞════════════════════════╡ frames for
a decoder   │  ┌───────┐  ┌───────┐  │ an encoder
────────────►├─►│ yadif ├─►│ scale ├─►│────────────►
│  └───────┘  └───────┘  │
└────────────────────────┘
A complex filtergraph is standalone and not associated with any specific stream.
It may have multiple (or zero) inputs, potentially of different types (audio or
video), each of which receiving data either from a decoder or another complex
filtergraph’s output. It also has one or more outputs that feed either an
encoder or another complex filtergraph’s input.
The following example diagram represents a complex filtergraph with 3 inputs and
2 outputs (all video):
┌─────────────────────────────────────────────────┐
│               complex filtergraph               │
╞═════════════════════════════════════════════════╡
frames   ├───────┐  ┌─────────┐      ┌─────────┐  ┌────────┤ frames
─────────►│input 0├─►│ overlay ├─────►│ overlay ├─►│output 0├────────►
├───────┘  │         │      │         │  └────────┤
frames   ├───────┐╭►│         │    ╭►│         │           │
─────────►│input 1├╯ └─────────┘    │ └─────────┘           │
├───────┘                 │                       │
frames   ├───────┐ ┌─────┐ ┌─────┬─╯              ┌────────┤ frames
─────────►│input 2├►│scale├►│split├───────────────►│output 1├────────►
├───────┘ └─────┘ └─────┘                └────────┤
└─────────────────────────────────────────────────┘
Frames from second input are overlaid over those from the first. Frames from the
third input are rescaled, then the duplicated into two identical streams. One of
them is overlaid over the combined first two inputs, with the result exposed as
the filtergraph’s first output. The other duplicate ends up being the
filtergraph’s second output.
Encoders receive raw audio, video, or subtitle frames and encode
them into encoded packets. The encoding (compression) process is
typically lossy - it degrades stream quality to make the output smaller;
some encoders are lossless, but at the cost of much higher output size. A
video or audio encoder receives its input from some filtergraph’s output,
subtitle encoders receive input from a decoder (since subtitle filtering is not
supported yet). Every encoder is associated with some muxer’s output
elementary stream and sends its output to that muxer.
A schematic representation of an encoder looks like this:
┌─────────┐
raw frames  │         │ packets
────────────►│ encoder ├─────────►
│         │
└─────────┘
Muxers (short for "multiplexers") receive encoded packets for
their elementary streams from encoders (the transcoding path) or directly
from demuxers (the streamcopy path), interleave them (when there is more
than one elementary stream), and write the resulting bytes into the output file
(or pipe, network stream, etc.).
A schematic representation of a muxer looks like this:
┌──────────────────────┬───────────┐
packets for stream 0  │                      │   muxer   │
──────────────────────►│  elementary stream 0 ╞═══════════╡
│                      │           │
├──────────────────────┤  global   │
packets for stream 1  │                      │properties │
──────────────────────►│  elementary stream 1 │   and     │
│                      │ metadata  │
├──────────────────────┤           │
│                      │           │
│     ...........      │           │
│                      │           │
├──────────────────────┤           │
packets for stream N  │                      │           │
──────────────────────►│  elementary stream N │           │
│                      │           │
└──────────────────────┴─────┬─────┘
│
write to file, network stream, │
grabbing device, etc.      │
│
▼
3.1 Streamcopy
The simplest pipeline in ffmpeg is single-stream
streamcopy, that is copying one input elementary stream’s packets
without decoding, filtering, or encoding them. As an example, consider an input
file called INPUT.mkv with 3 elementary streams, from which we take the
second and write it to file OUTPUT.mp4. A schematic representation of
such a pipeline looks like this:
┌──────────┬─────────────────────┐
│ demuxer  │                     │ unused
╞══════════╡ elementary stream 0 ├────────╳
│          │                     │
│INPUT.mkv ├─────────────────────┤          ┌──────────────────────┬───────────┐
│          │                     │ packets  │                      │   muxer   │
│          │ elementary stream 1 ├─────────►│  elementary stream 0 ╞═══════════╡
│          │                     │          │                      │OUTPUT.mp4 │
│          ├─────────────────────┤          └──────────────────────┴───────────┘
│          │                     │ unused
│          │ elementary stream 2 ├────────╳
│          │                     │
└──────────┴─────────────────────┘
The above pipeline can be constructed with the following commandline:
ffmpeg -i INPUT.mkv -map 0:1 -c copy OUTPUT.mp4
In this commandline
there is a single input INPUT.mkv;
there are no input options for this input;
there is a single output OUTPUT.mp4;
there are two output options for this output:
-map 0:1 selects the input stream to be used - from input with index 0
(i.e. the first one) the stream with index 1 (i.e. the second one);
-c copy selects the copy encoder, i.e. streamcopy with no decoding
or encoding.
Streamcopy is useful for changing the elementary stream count, container format,
or modifying container-level metadata. Since there is no decoding or encoding,
it is very fast and there is no quality loss. However, it might not work in some
cases because of a variety of factors (e.g. certain information required by the
target container is not available in the source). Applying filters is obviously
also impossible, since filters work on decoded frames.
More complex streamcopy scenarios can be constructed - e.g. combining streams
from two input files into a single output:
┌──────────┬────────────────────┐         ┌────────────────────┬───────────┐
│ demuxer 0│                    │ packets │                    │   muxer   │
╞══════════╡elementary stream 0 ├────────►│elementary stream 0 ╞═══════════╡
│INPUT0.mkv│                    │         │                    │OUTPUT.mp4 │
└──────────┴────────────────────┘         ├────────────────────┤           │
┌──────────┬────────────────────┐         │                    │           │
│ demuxer 1│                    │ packets │elementary stream 1 │           │
╞══════════╡elementary stream 0 ├────────►│                    │           │
│INPUT1.aac│                    │         └────────────────────┴───────────┘
└──────────┴────────────────────┘
that can be built by the commandline
ffmpeg -i INPUT0.mkv -i INPUT1.aac -map 0:0 -map 1:0 -c copy OUTPUT.mp4
The output -map option is used twice here, creating two streams in the
output file - one fed by the first input and one by the second. The single
instance of the -c option selects streamcopy for both of those streams.
You could also use multiple instances of this option together with
Stream specifiers to apply different values to each stream, as will be
demonstrated in following sections.
A converse scenario is splitting multiple streams from a single input into
multiple outputs:
┌──────────┬─────────────────────┐          ┌───────────────────┬───────────┐
│ demuxer  │                     │ packets  │                   │ muxer 0   │
╞══════════╡ elementary stream 0 ├─────────►│elementary stream 0╞═══════════╡
│          │                     │          │                   │OUTPUT0.mp4│
│INPUT.mkv ├─────────────────────┤          └───────────────────┴───────────┘
│          │                     │ packets  ┌───────────────────┬───────────┐
│          │ elementary stream 1 ├─────────►│                   │ muxer 1   │
│          │                     │          │elementary stream 0╞═══════════╡
└──────────┴─────────────────────┘          │                   │OUTPUT1.mp4│
└───────────────────┴───────────┘
built with
ffmpeg -i INPUT.mkv -map 0:0 -c copy OUTPUT0.mp4 -map 0:1 -c copy OUTPUT1.mp4
Note how a separate instance of the -c option is needed for every
output file even though their values are the same. This is because non-global
options (which is most of them) only apply in the context of the file before
which they are placed.
These  examples can of course be further generalized into arbitrary remappings
of any number of inputs into any number of outputs.
3.2 Trancoding
Transcoding is the process of decoding a stream and then encoding it
again. Since encoding tends to be computationally expensive and in most cases
degrades the stream quality (i.e. it is lossy), you should only transcode
when you need to and perform streamcopy otherwise. Typical reasons to transcode
are:
applying filters - e.g. resizing, deinterlacing, or overlaying video; resampling
or mixing audio;
you want to feed the stream to something that cannot decode the original codec.
Note that ffmpeg will transcode all audio, video, and subtitle streams
unless you specify -c copy for them.
Consider an example pipeline that reads an input file with one audio and one
video stream, transcodes the video and copies the audio into a single output
file. This can be schematically represented as follows
┌──────────┬─────────────────────┐
│ demuxer  │                     │       audio packets
╞══════════╡ stream 0 (audio)    ├─────────────────────────────────────╮
│          │                     │                                     │
│INPUT.mkv ├─────────────────────┤ video    ┌─────────┐     raw        │
│          │                     │ packets  │  video  │ video frames   │
│          │ stream 1 (video)    ├─────────►│ decoder ├──────────────╮ │
│          │                     │          │         │              │ │
└──────────┴─────────────────────┘          └─────────┘              │ │
▼ ▼
│ │
┌──────────┬─────────────────────┐ video    ┌─────────┐              │ │
│ muxer    │                     │ packets  │  video  │              │ │
╞══════════╡ stream 0 (video)    │◄─────────┤ encoder ├──────────────╯ │
│          │                     │          │(libx264)│                │
│OUTPUT.mp4├─────────────────────┤          └─────────┘                │
│          │                     │                                     │
│          │ stream 1 (audio)    │◄────────────────────────────────────╯
│          │                     │
└──────────┴─────────────────────┘
and implemented with the following commandline:
ffmpeg -i INPUT.mkv -map 0:v -map 0:a -c:v libx264 -c:a copy OUTPUT.mp4
Note how it uses stream specifiers :v and :a to select input
streams and apply different values of the -c option to them; see the
Stream specifiers section for more details.
3.3 Filtering
When transcoding, audio and video streams can be filtered before encoding, with
either a simple or complex filtergraph.
3.3.1 Simple filtergraphs
Simple filtergraphs are those that have exactly one input and output, both of
the same type (audio or video). They are configured with the per-stream
-filter option (with -vf and -af aliases for
-filter:v (video) and -filter:a (audio) respectively). Note
that simple filtergraphs are tied to their output stream, so e.g. if you have
multiple audio streams, -af will create a separate filtergraph for each
one.
Taking the trancoding example from above, adding filtering (and omitting audio,
for clarity) makes it look like this:
┌──────────┬───────────────┐
│ demuxer  │               │          ┌─────────┐
╞══════════╡ video stream  │ packets  │  video  │ frames
│INPUT.mkv │               ├─────────►│ decoder ├─────►───╮
│          │               │          └─────────┘         │
└──────────┴───────────────┘                              │
╭───────────◄───────────╯
│   ┌────────────────────────┐
│   │  simple filtergraph    │
│   ╞════════════════════════╡
│   │  ┌───────┐  ┌───────┐  │
╰──►├─►│ yadif ├─►│ scale ├─►├╮
│  └───────┘  └───────┘  ││
└────────────────────────┘│
│
│
┌──────────┬───────────────┐ video    ┌─────────┐               │
│ muxer    │               │ packets  │  video  │               │
╞══════════╡ video stream  │◄─────────┤ encoder ├───────◄───────╯
│OUTPUT.mp4│               │          │         │
│          │               │          └─────────┘
└──────────┴───────────────┘
3.3.2 Complex filtergraphs
Complex filtergraphs are those which cannot be described as simply a linear
processing chain applied to one stream. This is the case, for example, when the
graph has more than one input and/or output, or when output stream type is
different from input. Complex filtergraphs are configured with the
-filter_complex option. Note that this option is global, since a
complex filtergraph, by its nature, cannot be unambiguously associated with a
single stream or file. Each instance of -filter_complex creates a new
complex filtergraph, and there can be any number of them.
A trivial example of a complex filtergraph is the overlay filter, which
has two video inputs and one video output, containing one video overlaid on top
of the other. Its audio counterpart is the amix filter.
3.4 Loopback decoders
While decoders are normally associated with demuxer streams, it is also possible
to create "loopback" decoders that decode the output from some encoder and allow
it to be fed back to complex filtergraphs. This is done with the -dec
directive, which takes as a parameter the index of the output stream that should
be decoded. Every such directive creates a new loopback decoder, indexed with
successive integers starting at zero. These indices should then be used to refer
to loopback decoders in complex filtergraph link labels, as described in the
documentation for -filter_complex.
Decoding AVOptions can be passed to loopback decoders by placing them before
-dec, analogously to input/output options.
E.g. the following example:
ffmpeg -i INPUT                                        \
-map 0:v:0 -c:v libx264 -crf 45 -f null -            \
-threads 3 -dec 0:0                                  \
-filter_complex '[0:v][dec:0]hstack[stack]'          \
-map '[stack]' -c:v ffv1 OUTPUT
reads an input video and
(line 2) encodes it with libx264 at low quality;
(line 3) decodes this encoded stream using 3 threads;
(line 4) places decoded video side by side with the original input video;
(line 5) combined video is then losslessly encoded and written into
OUTPUT.
Such a transcoding pipeline can be represented with the following diagram:
┌──────────┬───────────────┐
│ demuxer  │               │   ┌─────────┐            ┌─────────┐    ┌────────────────────┐
╞══════════╡ video stream  │   │  video  │            │  video  │    │ null muxer         │
│   INPUT  │               ├──►│ decoder ├──┬────────►│ encoder ├─┬─►│(discards its input)│
│          │               │   └─────────┘  │         │(libx264)│ │  └────────────────────┘
└──────────┴───────────────┘                │         └─────────┘ │
╭───────◄──╯   ┌─────────┐       │
│              │loopback │       │
│ ╭─────◄──────┤ decoder ├────◄──╯
│ │            └─────────┘
│ │
│ │
│ │  ┌───────────────────┐
│ │  │complex filtergraph│
│ │  ╞═══════════════════╡
│ │  │  ┌─────────────┐  │
╰─╫─►├─►│   hstack    ├─►├╮
╰─►├─►│             │  ││
│  └─────────────┘  ││
└───────────────────┘│
│
┌──────────┬───────────────┐  ┌─────────┐                  │
│ muxer    │               │  │  video  │                  │
╞══════════╡ video stream  │◄─┤ encoder ├───────◄──────────╯
│  OUTPUT  │               │  │ (ffv1)  │
│          │               │  └─────────┘
└──────────┴───────────────┘