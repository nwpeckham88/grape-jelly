28 Resampler Options
29 Scaler Options
30 Filtering Introduction
31 graph2dot
32 Filtergraph description
32.1 Filtergraph syntax
32.2 Notes on filtergraph escaping
33 Timeline editing
34 Changing options at runtime with a command
35 Options for filters with several inputs (framesync)

28 Resampler Options
The audio resampler supports the following named options.
Options may be set by specifying -option value in the
FFmpeg tools, option=value for the aresample filter,
by setting the value explicitly in the
SwrContext options or using the libavutil/opt.h API for
programmatic use.
uchl, used_chlayout
Set used input channel layout. Default is unset. This option is
only used for special remapping.
isr, in_sample_rate
Set the input sample rate. Default value is 0.
osr, out_sample_rate
Set the output sample rate. Default value is 0.
isf, in_sample_fmt
Specify the input sample format. It is set by default to none.
osf, out_sample_fmt
Specify the output sample format. It is set by default to none.
tsf, internal_sample_fmt
Set the internal sample format. Default value is none.
This will automatically be chosen when it is not explicitly set.
ichl, in_chlayout
ochl, out_chlayout
Set the input/output channel layout.
See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual
for the required syntax.
clev, center_mix_level
Set the center mix level. It is a value expressed in deciBel, and must be
in the interval [-32,32].
slev, surround_mix_level
Set the surround mix level. It is a value expressed in deciBel, and must
be in the interval [-32,32].
lfe_mix_level
Set LFE mix into non LFE level. It is used when there is a LFE input but no
LFE output. It is a value expressed in deciBel, and must
be in the interval [-32,32].
rmvol, rematrix_volume
Set rematrix volume. Default value is 1.0.
rematrix_maxval
Set maximum output value for rematrixing.
This can be used to prevent clipping vs. preventing volume reduction.
A value of 1.0 prevents clipping.
flags, swr_flags
Set flags used by the converter. Default value is 0.
It supports the following individual flags:
res
force resampling, this flag forces resampling to be used even when the
input and output sample rates match.
dither_scale
Set the dither scale. Default value is 1.
dither_method
Set dither method. Default value is 0.
Supported values:
‘rectangular’
select rectangular dither
‘triangular’
select triangular dither
‘triangular_hp’
select triangular dither with high pass
‘lipshitz’
select Lipshitz noise shaping dither.
‘shibata’
select Shibata noise shaping dither.
‘low_shibata’
select low Shibata noise shaping dither.
‘high_shibata’
select high Shibata noise shaping dither.
‘f_weighted’
select f-weighted noise shaping dither
‘modified_e_weighted’
select modified-e-weighted noise shaping dither
‘improved_e_weighted’
select improved-e-weighted noise shaping dither
resampler
Set resampling engine. Default value is swr.
Supported values:
‘swr’
select the native SW Resampler; filter options precision and cheby are not
applicable in this case.
‘soxr’
select the SoX Resampler (where available); compensation, and filter options
filter_size, phase_shift, exact_rational, filter_type & kaiser_beta, are not
applicable in this case.
filter_size
For swr only, set resampling filter size, default value is 32.
phase_shift
For swr only, set resampling phase shift, default value is 10, and must be in
the interval [0,30].
linear_interp
Use linear interpolation when enabled (the default). Disable it if you want
to preserve speed instead of quality when exact_rational fails.
exact_rational
For swr only, when enabled, try to use exact phase_count based on input and
output sample rate. However, if it is larger than 1 << phase_shift,
the phase_count will be 1 << phase_shift as fallback. Default is enabled.
cutoff
Set cutoff frequency (swr: 6dB point; soxr: 0dB point) ratio; must be a float
value between 0 and 1.  Default value is 0.97 with swr, and 0.91 with soxr
(which, with a sample-rate of 44100, preserves the entire audio band to 20kHz).
precision
For soxr only, the precision in bits to which the resampled signal will be
calculated.  The default value of 20 (which, with suitable dithering, is
appropriate for a destination bit-depth of 16) gives SoX’s ’High Quality’; a
value of 28 gives SoX’s ’Very High Quality’.
cheby
For soxr only, selects passband rolloff none (Chebyshev) & higher-precision
approximation for ’irrational’ ratios. Default value is 0.
async
For swr only, simple 1 parameter audio sync to timestamps using stretching,
squeezing, filling and trimming. Setting this to 1 will enable filling and
trimming, larger values represent the maximum amount in samples that the data
may be stretched or squeezed for each second.
Default value is 0, thus no compensation is applied to make the samples match
the audio timestamps.
first_pts
For swr only, assume the first pts should be this value. The time unit is 1 / sample rate.
This allows for padding/trimming at the start of stream. By default, no
assumption is made about the first frame’s expected pts, so no padding or
trimming is done. For example, this could be set to 0 to pad the beginning with
silence if an audio stream starts after the video stream or to trim any samples
with a negative pts due to encoder delay.
min_comp
For swr only, set the minimum difference between timestamps and audio data (in
seconds) to trigger stretching/squeezing/filling or trimming of the
data to make it match the timestamps. The default is that
stretching/squeezing/filling and trimming is disabled
(min_comp = FLT_MAX).
min_hard_comp
For swr only, set the minimum difference between timestamps and audio data (in
seconds) to trigger adding/dropping samples to make it match the
timestamps.  This option effectively is a threshold to select between
hard (trim/fill) and soft (squeeze/stretch) compensation. Note that
all compensation is by default disabled through min_comp.
The default is 0.1.
comp_duration
For swr only, set duration (in seconds) over which data is stretched/squeezed
to make it match the timestamps. Must be a non-negative double float value,
default value is 1.0.
max_soft_comp
For swr only, set maximum factor by which data is stretched/squeezed to make it
match the timestamps. Must be a non-negative double float value, default value
is 0.
matrix_encoding
Select matrixed stereo encoding.
It accepts the following values:
‘none’
select none
‘dolby’
select Dolby
‘dplii’
select Dolby Pro Logic II
Default value is none.
filter_type
For swr only, select resampling filter type. This only affects resampling
operations.
It accepts the following values:
‘cubic’
select cubic
‘blackman_nuttall’
select Blackman Nuttall windowed sinc
‘kaiser’
select Kaiser windowed sinc
kaiser_beta
For swr only, set Kaiser window beta value. Must be a double float value in the
interval [2,16], default value is 9.
output_sample_bits
For swr only, set number of used output sample bits for dithering. Must be an integer in the
interval [0,64], default value is 0, which means it’s not used.
29 Scaler Options
The video scaler supports the following named options.
Options may be set by specifying -option value in the
FFmpeg tools, with a few API-only exceptions noted below.
For programmatic use, they can be set explicitly in the
SwsContext options or through the libavutil/opt.h API.
sws_flags
Set the scaler flags. This is also used to set the scaling
algorithm. Only a single algorithm should be selected. Default
value is ‘bicubic’.
It accepts the following values:
‘fast_bilinear’
Select fast bilinear scaling algorithm.
‘bilinear’
Select bilinear scaling algorithm.
‘bicubic’
Select bicubic scaling algorithm.
‘experimental’
Select experimental scaling algorithm.
‘neighbor’
Select nearest neighbor rescaling algorithm.
‘area’
Select averaging area rescaling algorithm.
‘bicublin’
Select bicubic scaling algorithm for the luma component, bilinear for
chroma components.
‘gauss’
Select Gaussian rescaling algorithm.
‘sinc’
Select sinc rescaling algorithm.
‘lanczos’
Select Lanczos rescaling algorithm. The default width (alpha) is 3 and can be
changed by setting param0.
‘spline’
Select natural bicubic spline rescaling algorithm.
‘print_info’
Enable printing/debug logging.
‘accurate_rnd’
Enable accurate rounding.
‘full_chroma_int’
Enable full chroma interpolation.
‘full_chroma_inp’
Select full chroma input.
‘bitexact’
Enable bitexact output.
srcw (API only)
Set source width.
srch (API only)
Set source height.
dstw (API only)
Set destination width.
dsth (API only)
Set destination height.
src_format (API only)
Set source pixel format (must be expressed as an integer).
dst_format (API only)
Set destination pixel format (must be expressed as an integer).
src_range (boolean)
If value is set to 1, indicates source is full range. Default value is
0, which indicates source is limited range.
dst_range (boolean)
If value is set to 1, enable full range for destination. Default value
is 0, which enables limited range.
param0, param1
Set scaling algorithm parameters. The specified values are specific of
some scaling algorithms and ignored by others. The specified values
are floating point number values.
sws_dither
Set the dithering algorithm. Accepts one of the following
values. Default value is ‘auto’.
‘auto’
automatic choice
‘none’
no dithering
‘bayer’
bayer dither
‘ed’
error diffusion dither
‘a_dither’
arithmetic dither, based using addition
‘x_dither’
arithmetic dither, based using xor (more random/less apparent patterning that
a_dither).
alphablend
Set the alpha blending to use when the input has alpha but the output does not.
Default value is ‘none’.
‘uniform_color’
Blend onto a uniform background color
‘checkerboard’
Blend onto a checkerboard
‘none’
No blending
30 Filtering Introduction
Filtering in FFmpeg is enabled through the libavfilter library.
In libavfilter, a filter can have multiple inputs and multiple
outputs.
To illustrate the sorts of things that are possible, we consider the
following filtergraph.
[main]
input --> split ---------------------> overlay --> output
|                             ^
|[tmp]                  [flip]|
+-----> crop --> vflip -------+
This filtergraph splits the input stream in two streams, then sends one
stream through the crop filter and the vflip filter, before merging it
back with the other stream by overlaying it on top. You can use the
following command to achieve this:
ffmpeg -i INPUT -vf "split [main][tmp]; [tmp] crop=iw:ih/2:0:0, vflip [flip]; [main][flip] overlay=0:H/2" OUTPUT
The result will be that the top half of the video is mirrored
onto the bottom half of the output video.
Filters in the same linear chain are separated by commas, and distinct
linear chains of filters are separated by semicolons. In our example,
crop,vflip are in one linear chain, split and
overlay are separately in another. The points where the linear
chains join are labelled by names enclosed in square brackets. In the
example, the split filter generates two outputs that are associated to
the labels [main] and [tmp].
The stream sent to the second output of split, labelled as
[tmp], is processed through the crop filter, which crops
away the lower half part of the video, and then vertically flipped. The
overlay filter takes in input the first unchanged output of the
split filter (which was labelled as [main]), and overlay on its
lower half the output generated by the crop,vflip filterchain.
Some filters take in input a list of parameters: they are specified
after the filter name and an equal sign, and are separated from each other
by a colon.
There exist so-called source filters that do not have an
audio/video input, and sink filters that will not have audio/video
output.
31 graph2dot
The graph2dot program included in the FFmpeg tools
directory can be used to parse a filtergraph description and issue a
corresponding textual representation in the dot language.
Invoke the command:
graph2dot -h
to see how to use graph2dot.
You can then pass the dot description to the dot program (from
the graphviz suite of programs) and obtain a graphical representation
of the filtergraph.
For example the sequence of commands:
echo GRAPH_DESCRIPTION | \
tools/graph2dot -o graph.tmp && \
dot -Tpng graph.tmp -o graph.png && \
display graph.png
can be used to create and display an image representing the graph
described by the GRAPH_DESCRIPTION string. Note that this string must be
a complete self-contained graph, with its inputs and outputs explicitly defined.
For example if your command line is of the form:
ffmpeg -i infile -vf scale=640:360 outfile
your GRAPH_DESCRIPTION string will need to be of the form:
nullsrc,scale=640:360,nullsink
you may also need to set the nullsrc parameters and add a format
filter in order to simulate a specific input file.
32 Filtergraph description
A filtergraph is a directed graph of connected filters. It can contain
cycles, and there can be multiple links between a pair of
filters. Each link has one input pad on one side connecting it to one
filter from which it takes its input, and one output pad on the other
side connecting it to one filter accepting its output.
Each filter in a filtergraph is an instance of a filter class
registered in the application, which defines the features and the
number of input and output pads of the filter.
A filter with no input pads is called a "source", and a filter with no
output pads is called a "sink".
32.1 Filtergraph syntax
A filtergraph has a textual representation, which is recognized by the
-filter/-vf/-af and
-filter_complex options in ffmpeg and
-vf/-af in ffplay, and by the
avfilter_graph_parse_ptr() function defined in
libavfilter/avfilter.h.
A filterchain consists of a sequence of connected filters, each one
connected to the previous one in the sequence. A filterchain is
represented by a list of ","-separated filter descriptions.
A filtergraph consists of a sequence of filterchains. A sequence of
filterchains is represented by a list of ";"-separated filterchain
descriptions.
A filter is represented by a string of the form:
[in_link_1]...[in_link_N]filter_name@id=arguments[out_link_1]...[out_link_M]
filter_name is the name of the filter class of which the
described filter is an instance of, and has to be the name of one of
the filter classes registered in the program optionally followed by "@id".
The name of the filter class is optionally followed by a string
"=arguments".
arguments is a string which contains the parameters used to
initialize the filter instance. It may have one of two forms:
A ’:’-separated list of key=value pairs.
A ’:’-separated list of value. In this case, the keys are assumed to be
the option names in the order they are declared. E.g. the fade filter
declares three options in this order – type, start_frame and
nb_frames. Then the parameter list in:0:30 means that the value
in is assigned to the option type, 0 to
start_frame and 30 to nb_frames.
A ’:’-separated list of mixed direct value and long key=value
pairs. The direct value must precede the key=value pairs, and
follow the same constraints order of the previous point. The following
key=value pairs can be set in any preferred order.
If the option value itself is a list of items (e.g. the format filter
takes a list of pixel formats), the items in the list are usually separated by
‘|’.
The list of arguments can be quoted using the character ‘'’ as initial
and ending mark, and the character ‘\’ for escaping the characters
within the quoted text; otherwise the argument string is considered
terminated when the next special character (belonging to the set
‘[]=;,’) is encountered.
A special syntax implemented in the ffmpeg CLI tool allows loading
option values from files. This is done be prepending a slash ’/’ to the option
name, then the supplied value is interpreted as a path from which the actual
value is loaded. E.g.
ffmpeg -i <INPUT> -vf drawtext=/text=/tmp/some_text <OUTPUT>
will load the text to be drawn from /tmp/some_text. API users wishing to
implement a similar feature should use the avfilter_graph_segment_*()
functions together with custom IO code.
The name and arguments of the filter are optionally preceded and
followed by a list of link labels.
A link label allows one to name a link and associate it to a filter output
or input pad. The preceding labels in_link_1
... in_link_N, are associated to the filter input pads,
the following labels out_link_1 ... out_link_M, are
associated to the output pads.
When two link labels with the same name are found in the
filtergraph, a link between the corresponding input and output pad is
created.
If an output pad is not labelled, it is linked by default to the first
unlabelled input pad of the next filter in the filterchain.
For example in the filterchain
nullsrc, split[L1], [L2]overlay, nullsink
the split filter instance has two output pads, and the overlay filter
instance two input pads. The first output pad of split is labelled
"L1", the first input pad of overlay is labelled "L2", and the second
output pad of split is linked to the second input pad of overlay,
which are both unlabelled.
In a filter description, if the input label of the first filter is not
specified, "in" is assumed; if the output label of the last filter is not
specified, "out" is assumed.
In a complete filterchain all the unlabelled filter input and output
pads must be connected. A filtergraph is considered valid if all the
filter input and output pads of all the filterchains are connected.
Leading and trailing whitespaces (space, tabs, or line feeds) separating tokens
in the filtergraph specification are ignored. This means that the filtergraph
can be expressed using empty lines and spaces to improve redability.
For example, the filtergraph:
testsrc,split[L1],hflip[L2];[L1][L2] hstack
can be represented as:
testsrc,
split [L1], hflip [L2];
[L1][L2] hstack
Libavfilter will automatically insert scale filters where format
conversion is required. It is possible to specify swscale flags
for those automatically inserted scalers by prepending
sws_flags=flags;
to the filtergraph description.
Here is a BNF description of the filtergraph syntax:
NAME             ::= sequence of alphanumeric characters and '_'
FILTER_NAME      ::= NAME["@"NAME]
LINKLABEL        ::= "[" NAME "]"
LINKLABELS       ::= LINKLABEL [LINKLABELS]
FILTER_ARGUMENTS ::= sequence of chars (possibly quoted)
FILTER           ::= [LINKLABELS] FILTER_NAME ["=" FILTER_ARGUMENTS] [LINKLABELS]
FILTERCHAIN      ::= FILTER [,FILTERCHAIN]
FILTERGRAPH      ::= [sws_flags=flags;] FILTERCHAIN [;FILTERGRAPH]
32.2 Notes on filtergraph escaping
Filtergraph description composition entails several levels of
escaping. See (ffmpeg-utils)the "Quoting and escaping"
section in the ffmpeg-utils(1) manual for more
information about the employed escaping procedure.
A first level escaping affects the content of each filter option
value, which may contain the special character : used to
separate values, or one of the escaping characters \'.
A second level escaping affects the whole filter description, which
may contain the escaping characters \' or the special
characters [],; used by the filtergraph description.
Finally, when you specify a filtergraph on a shell commandline, you
need to perform a third level escaping for the shell special
characters contained within it.
For example, consider the following string to be embedded in
the drawtext filter description text value:
this is a 'string': may contain one, or more, special characters
This string contains the ' special escaping character, and the
: special character, so it needs to be escaped in this way:
text=this is a \'string\'\: may contain one, or more, special characters
A second level of escaping is required when embedding the filter
description in a filtergraph description, in order to escape all the
filtergraph special characters. Thus the example above becomes:
drawtext=text=this is a \\\'string\\\'\\: may contain one\, or more\, special characters
(note that in addition to the \' escaping special characters,
also , needs to be escaped).
Finally an additional level of escaping is needed when writing the
filtergraph description in a shell command, which depends on the
escaping rules of the adopted shell. For example, assuming that
\ is special and needs to be escaped with another \, the
previous string will finally result in:
-vf "drawtext=text=this is a \\\\\\'string\\\\\\'\\\\: may contain one\\, or more\\, special characters"
In order to avoid cumbersome escaping when using a commandline tool accepting a
filter specification as input, it is advisable to avoid direct inclusion of the
filter or options specification in the shell.
For example, in case of the drawtext filter, you might prefer to
use the textfile option in place of text to specify the text
to render.
33 Timeline editing
Some filters support a generic enable option. For the filters
supporting timeline editing, this option can be set to an expression which is
evaluated before sending a frame to the filter. If the evaluation is non-zero,
the filter will be enabled, otherwise the frame will be sent unchanged to the
next filter in the filtergraph.
The expression accepts the following values:
‘t’
timestamp expressed in seconds, NAN if the input timestamp is unknown
‘n’
sequential number of the input frame, starting from 0
‘pos’
the position in the file of the input frame, NAN if unknown; deprecated, do
not use
‘w’
‘h’
width and height of the input frame if video
Additionally, these filters support an enable command that can be used
to re-define the expression.
Like any other filtering option, the enable option follows the same
rules.
For example, to enable a blur filter (smartblur) from 10 seconds to 3
minutes, and a curves filter starting at 3 seconds:
smartblur = enable='between(t,10,3*60)',
curves    = enable='gte(t,3)' : preset=cross_process
See ffmpeg -filters to view which filters have timeline support.
34 Changing options at runtime with a command
Some options can be changed during the operation of the filter using
a command. These options are marked ’T’ on the output of
ffmpeg -h filter=<name of filter>.
The name of the command is the name of the option and the argument is
the new value.
35 Options for filters with several inputs (framesync)
Some filters with several inputs support a common set of options.
These options can only be set by name, not with the short notation.
eof_action
The action to take when EOF is encountered on the secondary input; it accepts
one of the following values:
repeat
Repeat the last frame (the default).
endall
End both streams.
pass
Pass the main input through.
shortest
If set to 1, force the output to terminate when the shortest input
terminates. Default value is 0.
repeatlast
If set to 1, force the filter to extend the last frame of secondary streams
until the end of the primary stream. A value of 0 disables this behavior.
Default value is 1.
ts_sync_mode
How strictly to sync streams based on secondary input timestamps; it accepts
one of the following values:
default
Frame from secondary input with the nearest lower or equal timestamp to the
primary input frame.
nearest
Frame from secondary input with the absolute nearest timestamp to the primary
input frame.