9 Codec Options
10 Decoders
11 Video Decoders
11.1 av1
11.1.1 Options
11.2 hevc
11.2.1 Options
11.3 rawvideo
11.3.1 Options
11.4 libdav1d
11.4.1 Options
11.5 libdavs2
11.6 libuavs3d
11.6.1 Options
11.7 libxevd
11.7.1 Options
11.8 QSV Decoders
11.8.1 Common Options
11.8.2 HEVC Options
11.9 v210
11.9.1 Options
12 Audio Decoders
12.1 ac3
12.1.1 AC-3 Decoder Options
12.2 flac
12.2.1 FLAC Decoder options
12.3 ffwavesynth
12.4 libcelt
12.5 libgsm
12.6 libilbc
12.6.1 Options
12.7 libopencore-amrnb
12.8 libopencore-amrwb
12.9 libopus
13 Subtitles Decoders
13.1 libaribb24
13.1.1 libaribb24 Decoder Options
13.2 libaribcaption
13.2.1 libaribcaption Decoder Options
13.2.2 libaribcaption decoder usage examples
13.3 dvbsub
13.3.1 Options
13.4 dvdsub
13.4.1 Options
13.5 libzvbi-teletext
13.5.1 Options



9 Codec Options
libavcodec provides some generic global options, which can be set on
all the encoders and decoders. In addition, each codec may support
so-called private options, which are specific for a given codec.
Sometimes, a global option may only affect a specific kind of codec,
and may be nonsensical or ignored by another, so you need to be aware
of the meaning of the specified options. Also some options are
meant only for decoding or encoding.
Options may be set by specifying -option value in the
FFmpeg tools, or by setting the value explicitly in the
AVCodecContext options or using the libavutil/opt.h API
for programmatic use.
The list of supported options follow:
b integer (encoding,audio,video)
Set bitrate in bits/s. Default value is 200K.
ab integer (encoding,audio)
Set audio bitrate (in bits/s). Default value is 128K.
bt integer (encoding,video)
Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate
tolerance specifies how far ratecontrol is willing to deviate from the
target average bitrate value. This is not related to min/max
bitrate. Lowering tolerance too much has an adverse effect on quality.
flags flags (decoding/encoding,audio,video,subtitles)
Set generic flags.
Possible values:
‘mv4’
Use four motion vector by macroblock (mpeg4).
‘qpel’
Use 1/4 pel motion compensation.
‘loop’
Use loop filter.
‘qscale’
Use fixed qscale.
‘pass1’
Use internal 2pass ratecontrol in first pass mode.
‘pass2’
Use internal 2pass ratecontrol in second pass mode.
‘gray’
Only decode/encode grayscale.
‘psnr’
Set error[?] variables during encoding.
‘truncated’
Input bitstream might be randomly truncated.
‘drop_changed’
Don’t output frames whose parameters differ from first decoded frame in stream.
Error AVERROR_INPUT_CHANGED is returned when a frame is dropped.
‘ildct’
Use interlaced DCT.
‘low_delay’
Force low delay.
‘global_header’
Place global headers in extradata instead of every keyframe.
‘bitexact’
Only write platform-, build- and time-independent data. (except (I)DCT).
This ensures that file and data checksums are reproducible and match between
platforms. Its primary use is for regression testing.
‘aic’
Apply H263 advanced intra coding / mpeg4 ac prediction.
‘ilme’
Apply interlaced motion estimation.
‘cgop’
Use closed gop.
‘output_corrupt’
Output even potentially corrupted frames.
time_base rational number
Set codec time base.
It is the fundamental unit of time (in seconds) in terms of which
frame timestamps are represented. For fixed-fps content, timebase
should be 1 / frame_rate and timestamp increments should be
identically 1.
g integer (encoding,video)
Set the group of picture (GOP) size. Default value is 12.
ar integer (decoding/encoding,audio)
Set audio sampling rate (in Hz).
ac integer (decoding/encoding,audio)
Set number of audio channels.
cutoff integer (encoding,audio)
Set cutoff bandwidth. (Supported only by selected encoders, see
their respective documentation sections.)
frame_size integer (encoding,audio)
Set audio frame size.
Each submitted frame except the last must contain exactly frame_size
samples per channel. May be 0 when the codec has
CODEC_CAP_VARIABLE_FRAME_SIZE set, in that case the frame size is not
restricted. It is set by some decoders to indicate constant frame
size.
frame_number integer
Set the frame number.
delay integer
qcomp float (encoding,video)
Set video quantizer scale compression (VBR). It is used as a constant
in the ratecontrol equation. Recommended range for default rc_eq:
0.0-1.0.
qblur float (encoding,video)
Set video quantizer scale blur (VBR).
qmin integer (encoding,video)
Set min video quantizer scale (VBR). Must be included between -1 and
69, default value is 2.
qmax integer (encoding,video)
Set max video quantizer scale (VBR). Must be included between -1 and
1024, default value is 31.
qdiff integer (encoding,video)
Set max difference between the quantizer scale (VBR).
bf integer (encoding,video)
Set max number of B frames between non-B-frames.
Must be an integer between -1 and 16. 0 means that B-frames are
disabled. If a value of -1 is used, it will choose an automatic value
depending on the encoder.
Default value is 0.
b_qfactor float (encoding,video)
Set qp factor between P and B frames.
codec_tag integer
bug flags (decoding,video)
Workaround not auto detected encoder bugs.
Possible values:
‘autodetect’
‘xvid_ilace’
Xvid interlacing bug (autodetected if fourcc==XVIX)
‘ump4’
(autodetected if fourcc==UMP4)
‘no_padding’
padding bug (autodetected)
‘amv’
‘qpel_chroma’
‘std_qpel’
old standard qpel (autodetected per fourcc/version)
‘qpel_chroma2’
‘direct_blocksize’
direct-qpel-blocksize bug (autodetected per fourcc/version)
‘edge’
edge padding bug (autodetected per fourcc/version)
‘hpel_chroma’
‘dc_clip’
‘ms’
Workaround various bugs in microsoft broken decoders.
‘trunc’
trancated frames
strict integer (decoding/encoding,audio,video)
Specify how strictly to follow the standards.
Possible values:
‘very’
strictly conform to an older more strict version of the spec or reference software
‘strict’
strictly conform to all the things in the spec no matter what consequences
‘normal’
‘unofficial’
allow unofficial extensions
‘experimental’
allow non standardized experimental things, experimental
(unfinished/work in progress/not well tested) decoders and encoders.
Note: experimental decoders can pose a security risk, do not use this for
decoding untrusted input.
b_qoffset float (encoding,video)
Set QP offset between P and B frames.
err_detect flags (decoding,audio,video)
Set error detection flags.
Possible values:
‘crccheck’
verify embedded CRCs
‘bitstream’
detect bitstream specification deviations
‘buffer’
detect improper bitstream length
‘explode’
abort decoding on minor error detection
‘ignore_err’
ignore decoding errors, and continue decoding.
This is useful if you want to analyze the content of a video and thus want
everything to be decoded no matter what. This option will not result in a video
that is pleasing to watch in case of errors.
‘careful’
consider things that violate the spec and have not been seen in the wild as errors
‘compliant’
consider all spec non compliancies as errors
‘aggressive’
consider things that a sane encoder should not do as an error
has_b_frames integer
block_align integer
rc_override_count integer
maxrate integer (encoding,audio,video)
Set max bitrate tolerance (in bits/s). Requires bufsize to be set.
minrate integer (encoding,audio,video)
Set min bitrate tolerance (in bits/s). Most useful in setting up a CBR
encode. It is of little use elsewise.
bufsize integer (encoding,audio,video)
Set ratecontrol buffer size (in bits).
i_qfactor float (encoding,video)
Set QP factor between P and I frames.
i_qoffset float (encoding,video)
Set QP offset between P and I frames.
dct integer (encoding,video)
Set DCT algorithm.
Possible values:
‘auto’
autoselect a good one (default)
‘fastint’
fast integer
‘int’
accurate integer
‘mmx’
‘altivec’
‘faan’
floating point AAN DCT
lumi_mask float (encoding,video)
Compress bright areas stronger than medium ones.
tcplx_mask float (encoding,video)
Set temporal complexity masking.
scplx_mask float (encoding,video)
Set spatial complexity masking.
p_mask float (encoding,video)
Set inter masking.
dark_mask float (encoding,video)
Compress dark areas stronger than medium ones.
idct integer (decoding/encoding,video)
Select IDCT implementation.
Possible values:
‘auto’
‘int’
‘simple’
‘simplemmx’
‘simpleauto’
Automatically pick a IDCT compatible with the simple one
‘arm’
‘altivec’
‘sh4’
‘simplearm’
‘simplearmv5te’
‘simplearmv6’
‘simpleneon’
‘xvid’
‘faani’
floating point AAN IDCT
slice_count integer
ec flags (decoding,video)
Set error concealment strategy.
Possible values:
‘guess_mvs’
iterative motion vector (MV) search (slow)
‘deblock’
use strong deblock filter for damaged MBs
‘favor_inter’
favor predicting from the previous frame instead of the current
bits_per_coded_sample integer
aspect rational number (encoding,video)
Set sample aspect ratio.
sar rational number (encoding,video)
Set sample aspect ratio. Alias to aspect.
debug flags (decoding/encoding,audio,video,subtitles)
Print specific debug info.
Possible values:
‘pict’
picture info
‘rc’
rate control
‘bitstream’
‘mb_type’
macroblock (MB) type
‘qp’
per-block quantization parameter (QP)
‘dct_coeff’
‘green_metadata’
display complexity metadata for the upcoming frame, GoP or for a given duration.
‘skip’
‘startcode’
‘er’
error recognition
‘mmco’
memory management control operations (H.264)
‘bugs’
‘buffers’
picture buffer allocations
‘thread_ops’
threading operations
‘nomc’
skip motion compensation
cmp integer (encoding,video)
Set full pel me compare function.
Possible values:
‘sad’
sum of absolute differences, fast (default)
‘sse’
sum of squared errors
‘satd’
sum of absolute Hadamard transformed differences
‘dct’
sum of absolute DCT transformed differences
‘psnr’
sum of squared quantization errors (avoid, low quality)
‘bit’
number of bits needed for the block
‘rd’
rate distortion optimal, slow
‘zero’
0
‘vsad’
sum of absolute vertical differences
‘vsse’
sum of squared vertical differences
‘nsse’
noise preserving sum of squared differences
‘w53’
5/3 wavelet, only used in snow
‘w97’
9/7 wavelet, only used in snow
‘dctmax’
‘chroma’
subcmp integer (encoding,video)
Set sub pel me compare function.
Possible values:
‘sad’
sum of absolute differences, fast (default)
‘sse’
sum of squared errors
‘satd’
sum of absolute Hadamard transformed differences
‘dct’
sum of absolute DCT transformed differences
‘psnr’
sum of squared quantization errors (avoid, low quality)
‘bit’
number of bits needed for the block
‘rd’
rate distortion optimal, slow
‘zero’
0
‘vsad’
sum of absolute vertical differences
‘vsse’
sum of squared vertical differences
‘nsse’
noise preserving sum of squared differences
‘w53’
5/3 wavelet, only used in snow
‘w97’
9/7 wavelet, only used in snow
‘dctmax’
‘chroma’
mbcmp integer (encoding,video)
Set macroblock compare function.
Possible values:
‘sad’
sum of absolute differences, fast (default)
‘sse’
sum of squared errors
‘satd’
sum of absolute Hadamard transformed differences
‘dct’
sum of absolute DCT transformed differences
‘psnr’
sum of squared quantization errors (avoid, low quality)
‘bit’
number of bits needed for the block
‘rd’
rate distortion optimal, slow
‘zero’
0
‘vsad’
sum of absolute vertical differences
‘vsse’
sum of squared vertical differences
‘nsse’
noise preserving sum of squared differences
‘w53’
5/3 wavelet, only used in snow
‘w97’
9/7 wavelet, only used in snow
‘dctmax’
‘chroma’
ildctcmp integer (encoding,video)
Set interlaced dct compare function.
Possible values:
‘sad’
sum of absolute differences, fast (default)
‘sse’
sum of squared errors
‘satd’
sum of absolute Hadamard transformed differences
‘dct’
sum of absolute DCT transformed differences
‘psnr’
sum of squared quantization errors (avoid, low quality)
‘bit’
number of bits needed for the block
‘rd’
rate distortion optimal, slow
‘zero’
0
‘vsad’
sum of absolute vertical differences
‘vsse’
sum of squared vertical differences
‘nsse’
noise preserving sum of squared differences
‘w53’
5/3 wavelet, only used in snow
‘w97’
9/7 wavelet, only used in snow
‘dctmax’
‘chroma’
dia_size integer (encoding,video)
Set diamond type & size for motion estimation.
‘(1024, INT_MAX)’
full motion estimation(slowest)
‘(768, 1024]’
umh motion estimation
‘(512, 768]’
hex motion estimation
‘(256, 512]’
l2s diamond motion estimation
‘[2,256]’
var diamond motion estimation
‘(-1,  2)’
small diamond motion estimation
‘-1’
funny diamond motion estimation
‘(INT_MIN, -1)’
sab diamond motion estimation
last_pred integer (encoding,video)
Set amount of motion predictors from the previous frame.
precmp integer (encoding,video)
Set pre motion estimation compare function.
Possible values:
‘sad’
sum of absolute differences, fast (default)
‘sse’
sum of squared errors
‘satd’
sum of absolute Hadamard transformed differences
‘dct’
sum of absolute DCT transformed differences
‘psnr’
sum of squared quantization errors (avoid, low quality)
‘bit’
number of bits needed for the block
‘rd’
rate distortion optimal, slow
‘zero’
0
‘vsad’
sum of absolute vertical differences
‘vsse’
sum of squared vertical differences
‘nsse’
noise preserving sum of squared differences
‘w53’
5/3 wavelet, only used in snow
‘w97’
9/7 wavelet, only used in snow
‘dctmax’
‘chroma’
pre_dia_size integer (encoding,video)
Set diamond type & size for motion estimation pre-pass.
subq integer (encoding,video)
Set sub pel motion estimation quality.
me_range integer (encoding,video)
Set limit motion vectors range (1023 for DivX player).
global_quality integer (encoding,audio,video)
slice_flags integer
mbd integer (encoding,video)
Set macroblock decision algorithm (high quality mode).
Possible values:
‘simple’
use mbcmp (default)
‘bits’
use fewest bits
‘rd’
use best rate distortion
rc_init_occupancy integer (encoding,video)
Set number of bits which should be loaded into the rc buffer before
decoding starts.
flags2 flags (decoding/encoding,audio,video,subtitles)
Possible values:
‘fast’
Allow non spec compliant speedup tricks.
‘noout’
Skip bitstream encoding.
‘ignorecrop’
Ignore cropping information from sps.
‘local_header’
Place global headers at every keyframe instead of in extradata.
‘chunks’
Frame data might be split into multiple chunks.
‘showall’
Show all frames before the first keyframe.
‘export_mvs’
Export motion vectors into frame side-data (see AV_FRAME_DATA_MOTION_VECTORS)
for codecs that support it. See also doc/examples/export_mvs.c.
‘skip_manual’
Do not skip samples and export skip information as frame side data.
‘ass_ro_flush_noop’
Do not reset ASS ReadOrder field on flush.
‘icc_profiles’
Generate/parse embedded ICC profiles from/to colorimetry tags.
export_side_data flags (decoding/encoding,audio,video,subtitles)
Possible values:
‘mvs’
Export motion vectors into frame side-data (see AV_FRAME_DATA_MOTION_VECTORS)
for codecs that support it. See also doc/examples/export_mvs.c.
‘prft’
Export encoder Producer Reference Time into packet side-data (see AV_PKT_DATA_PRFT)
for codecs that support it.
‘venc_params’
Export video encoding parameters through frame side data (see AV_FRAME_DATA_VIDEO_ENC_PARAMS)
for codecs that support it. At present, those are H.264 and VP9.
‘film_grain’
Export film grain parameters through frame side data (see AV_FRAME_DATA_FILM_GRAIN_PARAMS).
Supported at present by AV1 decoders.
‘enhancements’
Export picture enhancement metadata through frame side data, e.g. LCEVC (see AV_FRAME_DATA_LCEVC).
threads integer (decoding/encoding,video)
Set the number of threads to be used, in case the selected codec
implementation supports multi-threading.
Possible values:
‘auto, 0’
automatically select the number of threads to set
Default value is ‘auto’.
dc integer (encoding,video)
Set intra_dc_precision.
nssew integer (encoding,video)
Set nsse weight.
skip_top integer (decoding,video)
Set number of macroblock rows at the top which are skipped.
skip_bottom integer (decoding,video)
Set number of macroblock rows at the bottom which are skipped.
profile integer (encoding,audio,video)
Set encoder codec profile. Default value is ‘unknown’. Encoder specific
profiles are documented in the relevant encoder documentation.
level integer (encoding,audio,video)
Set the encoder level. This level depends on the specific codec, and
might correspond to the profile level. It is set by default to
‘unknown’.
Possible values:
‘unknown’
lowres integer (decoding,audio,video)
Decode at 1= 1/2, 2=1/4, 3=1/8 resolutions.
mblmin integer (encoding,video)
Set min macroblock lagrange factor (VBR).
mblmax integer (encoding,video)
Set max macroblock lagrange factor (VBR).
skip_loop_filter integer (decoding,video)
skip_idct        integer (decoding,video)
skip_frame       integer (decoding,video)
Make decoder discard processing depending on the frame type selected
by the option value.
skip_loop_filter skips frame loop filtering, skip_idct
skips frame IDCT/dequantization, skip_frame skips decoding.
Possible values:
‘none’
Discard no frame.
‘default’
Discard useless frames like 0-sized frames.
‘noref’
Discard all non-reference frames.
‘bidir’
Discard all bidirectional frames.
‘nokey’
Discard all frames excepts keyframes.
‘nointra’
Discard all frames except I frames.
‘all’
Discard all frames.
Default value is ‘default’.
bidir_refine integer (encoding,video)
Refine the two motion vectors used in bidirectional macroblocks.
keyint_min integer (encoding,video)
Set minimum interval between IDR-frames.
refs integer (encoding,video)
Set reference frames to consider for motion compensation.
trellis integer (encoding,audio,video)
Set rate-distortion optimal quantization.
mv0_threshold integer (encoding,video)
compression_level integer (encoding,audio,video)
bits_per_raw_sample integer
channel_layout integer (decoding/encoding,audio)
See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual
for the required syntax.
rc_max_vbv_use float (encoding,video)
rc_min_vbv_use float (encoding,video)
color_primaries integer (decoding/encoding,video)
Possible values:
‘bt709’
BT.709
‘bt470m’
BT.470 M
‘bt470bg’
BT.470 BG
‘smpte170m’
SMPTE 170 M
‘smpte240m’
SMPTE 240 M
‘film’
Film
‘bt2020’
BT.2020
‘smpte428’
‘smpte428_1’
SMPTE ST 428-1
‘smpte431’
SMPTE 431-2
‘smpte432’
SMPTE 432-1
‘jedec-p22’
JEDEC P22
color_trc integer (decoding/encoding,video)
Possible values:
‘bt709’
BT.709
‘gamma22’
BT.470 M
‘gamma28’
BT.470 BG
‘smpte170m’
SMPTE 170 M
‘smpte240m’
SMPTE 240 M
‘linear’
Linear
‘log’
‘log100’
Log
‘log_sqrt’
‘log316’
Log square root
‘iec61966_2_4’
‘iec61966-2-4’
IEC 61966-2-4
‘bt1361’
‘bt1361e’
BT.1361
‘iec61966_2_1’
‘iec61966-2-1’
IEC 61966-2-1
‘bt2020_10’
‘bt2020_10bit’
BT.2020 - 10 bit
‘bt2020_12’
‘bt2020_12bit’
BT.2020 - 12 bit
‘smpte2084’
SMPTE ST 2084
‘smpte428’
‘smpte428_1’
SMPTE ST 428-1
‘arib-std-b67’
ARIB STD-B67
colorspace integer (decoding/encoding,video)
Possible values:
‘rgb’
RGB
‘bt709’
BT.709
‘fcc’
FCC
‘bt470bg’
BT.470 BG
‘smpte170m’
SMPTE 170 M
‘smpte240m’
SMPTE 240 M
‘ycocg’
YCOCG
‘bt2020nc’
‘bt2020_ncl’
BT.2020 NCL
‘bt2020c’
‘bt2020_cl’
BT.2020 CL
‘smpte2085’
SMPTE 2085
‘chroma-derived-nc’
Chroma-derived NCL
‘chroma-derived-c’
Chroma-derived CL
‘ictcp’
ICtCp
color_range integer (decoding/encoding,video)
If used as input parameter, it serves as a hint to the decoder, which
color_range the input has.
Possible values:
‘tv’
‘mpeg’
‘limited’
MPEG (219*2^(n-8))
‘pc’
‘jpeg’
‘full’
JPEG (2^n-1)
chroma_sample_location integer (decoding/encoding,video)
Possible values:
‘left’
‘center’
‘topleft’
‘top’
‘bottomleft’
‘bottom’
log_level_offset integer
Set the log level offset.
slices integer (encoding,video)
Number of slices, used in parallelized encoding.
thread_type flags (decoding/encoding,video)
Select which multithreading methods to use.
Use of ‘frame’ will increase decoding delay by one frame per
thread, so clients which cannot provide future frames should not use
it.
Possible values:
‘slice’
Decode more than one part of a single frame at once.
Multithreading using slices works only when the video was encoded with
slices.
‘frame’
Decode more than one frame at once.
Default value is ‘slice+frame’.
audio_service_type integer (encoding,audio)
Set audio service type.
Possible values:
‘ma’
Main Audio Service
‘ef’
Effects
‘vi’
Visually Impaired
‘hi’
Hearing Impaired
‘di’
Dialogue
‘co’
Commentary
‘em’
Emergency
‘vo’
Voice Over
‘ka’
Karaoke
request_sample_fmt sample_fmt (decoding,audio)
Set sample format audio decoders should prefer. Default value is
none.
pkt_timebase rational number
sub_charenc encoding (decoding,subtitles)
Set the input subtitles character encoding.
field_order  field_order (video)
Set/override the field order of the video.
Possible values:
‘progressive’
Progressive video
‘tt’
Interlaced video, top field coded and displayed first
‘bb’
Interlaced video, bottom field coded and displayed first
‘tb’
Interlaced video, top coded first, bottom displayed first
‘bt’
Interlaced video, bottom coded first, top displayed first
skip_alpha bool (decoding,video)
Set to 1 to disable processing alpha (transparency). This works like the
‘gray’ flag in the flags option which skips chroma information
instead of alpha. Default is 0.
codec_whitelist list (input)
"," separated list of allowed decoders. By default all are allowed.
dump_separator string (input)
Separator used to separate the fields printed on the command line about the
Stream parameters.
For example, to separate the fields with newlines and indentation:
ffprobe -dump_separator "
"  -i ~/videos/matrixbench_mpeg2.mpg
max_pixels integer (decoding/encoding,video)
Maximum number of pixels per image. This value can be used to avoid out of
memory failures due to large images.
apply_cropping bool (decoding,video)
Enable cropping if cropping parameters are multiples of the required
alignment for the left and top parameters. If the alignment is not met the
cropping will be partially applied to maintain alignment.
Default is 1 (enabled).
Note: The required alignment depends on if AV_CODEC_FLAG_UNALIGNED is set and the
CPU. AV_CODEC_FLAG_UNALIGNED cannot be changed from the command line. Also hardware
decoders will not apply left/top Cropping.
10 Decoders
Decoders are configured elements in FFmpeg which allow the decoding of
multimedia streams.
When you configure your FFmpeg build, all the supported native decoders
are enabled by default. Decoders requiring an external library must be enabled
manually via the corresponding --enable-lib option. You can list all
available decoders using the configure option --list-decoders.
You can disable all the decoders with the configure option
--disable-decoders and selectively enable / disable single decoders
with the options --enable-decoder=DECODER /
--disable-decoder=DECODER.
The option -decoders of the ff* tools will display the list of
enabled decoders.
11 Video Decoders
A description of some of the currently available video decoders
follows.
11.1 av1
AOMedia Video 1 (AV1) decoder.
11.1.1 Options
operating_point
Select an operating point of a scalable AV1 bitstream (0 - 31). Default is 0.
11.2 hevc
HEVC (AKA ITU-T H.265 or ISO/IEC 23008-2) decoder.
The decoder supports MV-HEVC multiview streams with at most two views. Views to
be output are selected by supplying a list of view IDs to the decoder (the
view_ids option). This option may be set either statically before
decoder init, or from the get_format() callback - useful for the case
when the view count or IDs change dynamically during decoding.
Only the base layer is decoded by default.
Note that if you are using the ffmpeg CLI tool, you should be using view
specifiers as documented in its manual, rather than the options documented here.
11.2.1 Options
view_ids (MV-HEVC)
Specify a list of view IDs that should be output. This option can also be set to
a single ’-1’, which will cause all views defined in the VPS to be decoded and
output.
view_ids_available (MV-HEVC)
This option may be read by the caller to retrieve an array of view IDs available
in the active VPS. The array is empty for single-layer video.
The value of this option is guaranteed to be accurate when read from the
get_format() callback. It may also be set at other times (e.g. after
opening the decoder), but the value is informational only and may be incorrect
(e.g. when the stream contains multiple distinct VPS NALUs).
view_pos_available (MV-HEVC)
This option may be read by the caller to retrieve an array of view positions
(left, right, or unspecified) available in the active VPS, as
AVStereo3DView values. When the array is available, its elements apply to
the corresponding elements of view_ids_available, i.e.
view_pos_available[i] contains the position of view with ID
view_ids_available[i].
Same validity restrictions as for view_ids_available apply to
this option.
11.3 rawvideo
Raw video decoder.
This decoder decodes rawvideo streams.
11.3.1 Options
top top_field_first
Specify the assumed field type of the input video.
-1
the video is assumed to be progressive (default)
0
bottom-field-first is assumed
1
top-field-first is assumed
11.4 libdav1d
dav1d AV1 decoder.
libdav1d allows libavcodec to decode the AOMedia Video 1 (AV1) codec.
Requires the presence of the libdav1d headers and library during configuration.
You need to explicitly configure the build with --enable-libdav1d.
11.4.1 Options
The following options are supported by the libdav1d wrapper.
framethreads
Set amount of frame threads to use during decoding. The default value is 0 (autodetect).
This option is deprecated for libdav1d >= 1.0 and will be removed in the future. Use the
option max_frame_delay and the global option threads instead.
tilethreads
Set amount of tile threads to use during decoding. The default value is 0 (autodetect).
This option is deprecated for libdav1d >= 1.0 and will be removed in the future. Use the
global option threads instead.
max_frame_delay
Set max amount of frames the decoder may buffer internally. The default value is 0
(autodetect).
filmgrain
Apply film grain to the decoded video if present in the bitstream. Defaults to the
internal default of the library.
This option is deprecated and will be removed in the future. See the global option
export_side_data to export Film Grain parameters instead of applying it.
oppoint
Select an operating point of a scalable AV1 bitstream (0 - 31). Defaults to the
internal default of the library.
alllayers
Output all spatial layers of a scalable AV1 bitstream. The default value is false.
11.5 libdavs2
AVS2-P2/IEEE1857.4 video decoder wrapper.
This decoder allows libavcodec to decode AVS2 streams with davs2 library.
11.6 libuavs3d
AVS3-P2/IEEE1857.10 video decoder.
libuavs3d allows libavcodec to decode AVS3 streams.
Requires the presence of the libuavs3d headers and library during configuration.
You need to explicitly configure the build with --enable-libuavs3d.
11.6.1 Options
The following option is supported by the libuavs3d wrapper.
frame_threads
Set amount of frame threads to use during decoding. The default value is 0 (autodetect).
11.7 libxevd
eXtra-fast Essential Video Decoder (XEVD) MPEG-5 EVC decoder wrapper.
This decoder requires the presence of the libxevd headers and library
during configuration. You need to explicitly configure the build with
--enable-libxevd.
The xevd project website is at https://github.com/mpeg5/xevd.
11.7.1 Options
The following options are supported by the libxevd wrapper.
The xevd-equivalent options or values are listed in parentheses for easy migration.
To get a more accurate and extensive documentation of the libxevd options,
invoke the command  xevd_app --help or consult the libxevd documentation.
threads (threads)
Force to use a specific number of threads
11.8 QSV Decoders
The family of Intel QuickSync Video decoders (VC1, MPEG-2, H.264, HEVC,
JPEG/MJPEG, VP8, VP9, AV1, VVC).
11.8.1 Common Options
The following options are supported by all qsv decoders.
async_depth
Internal parallelization depth, the higher the value the higher the latency.
gpu_copy
A GPU-accelerated copy between video and system memory
‘default’
‘on’
‘off’
11.8.2 HEVC Options
Extra options for hevc_qsv.
load_plugin
A user plugin to load in an internal session
‘none’
‘hevc_sw’
‘hevc_hw’
load_plugins
A :-separate list of hexadecimal plugin UIDs to load in an internal session
11.9 v210
Uncompressed 4:2:2 10-bit decoder.
11.9.1 Options
custom_stride
Set the line size of the v210 data in bytes. The default value is 0
(autodetect). You can use the special -1 value for a strideless v210 as seen in
BOXX files.
12 Audio Decoders
A description of some of the currently available audio decoders
follows.
12.1 ac3
AC-3 audio decoder.
This decoder implements part of ATSC A/52:2010 and ETSI TS 102 366, as well as
the undocumented RealAudio 3 (a.k.a. dnet).
12.1.1 AC-3 Decoder Options
-drc_scale value
Dynamic Range Scale Factor. The factor to apply to dynamic range values
from the AC-3 stream. This factor is applied exponentially. The default value is 1.
There are 3 notable scale factor ranges:
drc_scale == 0
DRC disabled. Produces full range audio.
0 < drc_scale <= 1
DRC enabled.  Applies a fraction of the stream DRC value.
Audio reproduction is between full range and full compression.
drc_scale > 1
DRC enabled. Applies drc_scale asymmetrically.
Loud sounds are fully compressed.  Soft sounds are enhanced.
12.2 flac
FLAC audio decoder.
This decoder aims to implement the complete FLAC specification from Xiph.
12.2.1 FLAC Decoder options
-use_buggy_lpc
The lavc FLAC encoder used to produce buggy streams with high lpc values
(like the default value). This option makes it possible to decode such streams
correctly by using lavc’s old buggy lpc logic for decoding.
12.3 ffwavesynth
Internal wave synthesizer.
This decoder generates wave patterns according to predefined sequences. Its
use is purely internal and the format of the data it accepts is not publicly
documented.
12.4 libcelt
libcelt decoder wrapper.
libcelt allows libavcodec to decode the Xiph CELT ultra-low delay audio codec.
Requires the presence of the libcelt headers and library during configuration.
You need to explicitly configure the build with --enable-libcelt.
12.5 libgsm
libgsm decoder wrapper.
libgsm allows libavcodec to decode the GSM full rate audio codec. Requires
the presence of the libgsm headers and library during configuration. You need
to explicitly configure the build with --enable-libgsm.
This decoder supports both the ordinary GSM and the Microsoft variant.
12.6 libilbc
libilbc decoder wrapper.
libilbc allows libavcodec to decode the Internet Low Bitrate Codec (iLBC)
audio codec. Requires the presence of the libilbc headers and library during
configuration. You need to explicitly configure the build with
--enable-libilbc.
12.6.1 Options
The following option is supported by the libilbc wrapper.
enhance
Enable the enhancement of the decoded audio when set to 1. The default
value is 0 (disabled).
12.7 libopencore-amrnb
libopencore-amrnb decoder wrapper.
libopencore-amrnb allows libavcodec to decode the Adaptive Multi-Rate
Narrowband audio codec. Using it requires the presence of the
libopencore-amrnb headers and library during configuration. You need to
explicitly configure the build with --enable-libopencore-amrnb.
An FFmpeg native decoder for AMR-NB exists, so users can decode AMR-NB
without this library.
12.8 libopencore-amrwb
libopencore-amrwb decoder wrapper.
libopencore-amrwb allows libavcodec to decode the Adaptive Multi-Rate
Wideband audio codec. Using it requires the presence of the
libopencore-amrwb headers and library during configuration. You need to
explicitly configure the build with --enable-libopencore-amrwb.
An FFmpeg native decoder for AMR-WB exists, so users can decode AMR-WB
without this library.
12.9 libopus
libopus decoder wrapper.
libopus allows libavcodec to decode the Opus Interactive Audio Codec.
Requires the presence of the libopus headers and library during
configuration. You need to explicitly configure the build with
--enable-libopus.
An FFmpeg native decoder for Opus exists, so users can decode Opus
without this library.
13 Subtitles Decoders
13.1 libaribb24
ARIB STD-B24 caption decoder.
Implements profiles A and C of the ARIB STD-B24 standard.
13.1.1 libaribb24 Decoder Options
-aribb24-base-path path
Sets the base path for the libaribb24 library. This is utilized for reading of
configuration files (for custom unicode conversions), and for dumping of
non-text symbols as images under that location.
Unset by default.
-aribb24-skip-ruby-text boolean
Tells the decoder wrapper to skip text blocks that contain half-height ruby
text.
Enabled by default.
13.2 libaribcaption
Yet another ARIB STD-B24 caption decoder using external libaribcaption
library.
Implements profiles A and C of the Japanse ARIB STD-B24 standard,
Brazilian ABNT NBR 15606-1, and Philippines version of ISDB-T.
Requires the presence of the libaribcaption headers and library
(https://github.com/xqq/libaribcaption) during configuration.
You need to explicitly configure the build with --enable-libaribcaption.
If both libaribb24 and libaribcaption are enabled, libaribcaption
decoder precedes.
13.2.1 libaribcaption Decoder Options
-sub_type subtitle_type
Specifies the format of the decoded subtitles.
‘bitmap’
Graphical image.
‘ass’
ASS formatted text.
‘text’
Simple text based output without formatting.
The default is ass as same as libaribb24 decoder.
Some present players (e.g., mpv) expect ASS format for ARIB caption.
-caption_encoding encoding_scheme
Specifies the encoding scheme of input subtitle text.
‘auto’
Automatically detect text encoding (default).
‘jis’
8bit-char JIS encoding defined in ARIB STD B24.
This encoding used in Japan for ISDB captions.
‘utf8’
UTF-8 encoding defined in ARIB STD B24.
This encoding is used in Philippines for ISDB-T captions.
‘latin’
Latin character encoding defined in ABNT NBR 15606-1.
This encoding is used in South America for SBTVD / ISDB-Tb captions.
-font font_name[,font_name2,...]
Specify comma-separated list of font family names to be used for bitmap
or ass type subtitle rendering.
Only first font name is used for ass type subtitle.
If not specified, use internaly defined default font family.
-ass_single_rect boolean
ARIB STD-B24 specifies that some captions may be displayed at different
positions at a time (multi-rectangle subtitle).
Since some players (e.g., old mpv) can’t handle multiple ASS rectangles
in a single AVSubtitle, or multiple ASS rectangles of indeterminate duration
with the same start timestamp, this option can change the behavior so that
all the texts are displayed in a single ASS rectangle.
The default is false.
If your player cannot handle AVSubtitles with multiple ASS rectangles properly,
set this option to true or define ASS_SINGLE_RECT=1 to change
default behavior at compilation.
-force_outline_text boolean
Specify whether always render outline text for all characters regardless of
the indication by charactor style.
The default is false.
-outline_width number (0.0 - 3.0)
Specify width for outline text, in dots (relative).
The default is 1.5.
-ignore_background boolean
Specify whether to ignore background color rendering.
The default is false.
-ignore_ruby boolean
Specify whether to ignore rendering for ruby-like (furigana) characters.
The default is false.
-replace_drcs boolean
Specify whether to render replaced DRCS characters as Unicode characters.
The default is true.
-replace_msz_ascii boolean
Specify whether to replace MSZ (Middle Size; half width) fullwidth
alphanumerics with halfwidth alphanumerics.
The default is true.
-replace_msz_japanese boolean
Specify whether to replace some MSZ (Middle Size; half width) fullwidth
japanese special characters with halfwidth ones.
The default is true.
-replace_msz_glyph boolean
Specify whether to replace MSZ (Middle Size; half width) characters
with halfwidth glyphs if the fonts supports it.
This option works under FreeType or DirectWrite renderer
with Adobe-Japan1 compliant fonts.
e.g., IBM Plex Sans JP, Morisawa BIZ UDGothic, Morisawa BIZ UDMincho,
Yu Gothic, Yu Mincho, and Meiryo.
The default is true.
-canvas_size image_size
Specify the resolution of the canvas to render subtitles to; usually, this
should be frame size of input video.
This only applies when -subtitle_type is set to bitmap.
The libaribcaption decoder assumes input frame size for bitmap rendering as below:
PROFILE_A : 1440 x 1080 with SAR (PAR) 4:3
PROFILE_C : 320 x 180 with SAR (PAR) 1:1
If actual frame size of input video does not match above assumption,
the rendered captions may be distorted.
To make the captions undistorted, add -canvas_size option to specify
actual input video size.
Note that the -canvas_size option is not required for video with
different size but same aspect ratio.
In such cases, the caption will be stretched or shrunk to actual video size
if -canvas_size option is not specified.
If -canvas_size option is specified with different size,
the caption will be stretched or shrunk as specified size with calculated SAR.
13.2.2 libaribcaption decoder usage examples
Display MPEG-TS file with ARIB subtitle by ffplay tool:
ffplay -sub_type bitmap MPEG.TS
Display MPEG-TS file with input frame size 1920x1080 by ffplay tool:
ffplay -sub_type bitmap -canvas_size 1920x1080 MPEG.TS
Embed ARIB subtitle in transcoded video:
ffmpeg -sub_type bitmap -i src.m2t -filter_complex "[0:v][0:s]overlay" -vcodec h264 dest.mp4
13.3 dvbsub
13.3.1 Options
compute_clut
-2
Compute clut once if no matching CLUT is in the stream.
-1
Compute clut if no matching CLUT is in the stream.
0
Never compute CLUT
1
Always compute CLUT and override the one provided in the stream.
dvb_substream
Selects the dvb substream, or all substreams if -1 which is default.
13.4 dvdsub
This codec decodes the bitmap subtitles used in DVDs; the same subtitles can
also be found in VobSub file pairs and in some Matroska files.
13.4.1 Options
palette
Specify the global palette used by the bitmaps. When stored in VobSub, the
palette is normally specified in the index file; in Matroska, the palette is
stored in the codec extra-data in the same format as in VobSub. In DVDs, the
palette is stored in the IFO file, and therefore not available when reading
from dumped VOB files.
The format for this option is a string containing 16 24-bits hexadecimal
numbers (without 0x prefix) separated by commas, for example 0d00ee,
ee450d, 101010, eaeaea, 0ce60b, ec14ed, ebff0b, 0d617a, 7b7b7b, d1d1d1,
7b2a0e, 0d950c, 0f007b, cf0dec, cfa80c, 7c127b.
ifo_palette
Specify the IFO file from which the global palette is obtained.
(experimental)
forced_subs_only
Only decode subtitle entries marked as forced. Some titles have forced
and non-forced subtitles in the same track. Setting this flag to 1
will only keep the forced subtitles. Default value is 0.
13.5 libzvbi-teletext
Libzvbi allows libavcodec to decode DVB teletext pages and DVB teletext
subtitles. Requires the presence of the libzvbi headers and library during
configuration. You need to explicitly configure the build with
--enable-libzvbi.
13.5.1 Options
txt_page
List of teletext page numbers to decode. Pages that do not match the specified
list are dropped. You may use the special * string to match all pages,
or subtitle to match all subtitle pages.
Default value is *.
txt_default_region
Set default character set used for decoding, a value between 0 and 87 (see
ETS 300 706, Section 15, Table 32). Default value is -1, which does not
override the libzvbi default. This option is needed for some legacy level 1.0
transmissions which cannot signal the proper charset.
txt_chop_top
Discards the top teletext line. Default value is 1.
txt_format
Specifies the format of the decoded subtitles.
bitmap
The default format, you should use this for teletext pages, because certain
graphics and colors cannot be expressed in simple text or even ASS.
text
Simple text based output without formatting.
ass
Formatted ASS output, subtitle pages and teletext pages are returned in
different styles, subtitle pages are stripped down to text, but an effort is
made to keep the text alignment and the formatting.
txt_left
X offset of generated bitmaps, default is 0.
txt_top
Y offset of generated bitmaps, default is 0.
txt_chop_spaces
Chops leading and trailing spaces and removes empty lines from the generated
text. This option is useful for teletext based subtitles where empty spaces may
be present at the start or at the end of the lines or empty lines may be
present between the subtitle lines because of double-sized teletext characters.
Default value is 1.
txt_duration
Sets the display duration of the decoded teletext pages or subtitles in
milliseconds. Default value is -1 which means infinity or until the next
subtitle event comes.
txt_transparent
Force transparent background of the generated teletext bitmaps. Default value
is 0 which means an opaque background.
txt_opacity
Sets the opacity (0-255) of the teletext background. If
txt_transparent is not set, it only affects characters between a start
box and an end box, typically subtitles. Default value is 0 if
txt_transparent is set, 255 otherwise.