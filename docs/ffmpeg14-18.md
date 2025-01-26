14 Encoders
15 Audio Encoders
15.1 aac
15.1.1 Options
15.2 ac3 and ac3_fixed
15.2.1 AC-3 Metadata
15.2.1.1 Metadata Control Options
15.2.1.2 Downmix Levels
15.2.1.3 Audio Production Information
15.2.1.4 Other Metadata Options
15.2.2 Extended Bitstream Information
15.2.2.1 Extended Bitstream Information - Part 1
15.2.2.2 Extended Bitstream Information - Part 2
15.2.3 Other AC-3 Encoding Options
15.2.4 Floating-Point-Only AC-3 Encoding Options
15.3 ffv1
15.3.1 Options
15.4 flac
15.4.1 Options
15.5 opus
15.5.1 Options
15.6 libfdk_aac
15.6.1 Options
15.6.2 Examples
15.7 liblc3
15.7.1 Options
15.8 libmp3lame
15.8.1 Options
15.9 libopencore-amrnb
15.9.1 Options
15.10 libopus
15.10.1 Option Mapping
15.11 libshine
15.11.1 Options
15.12 libtwolame
15.12.1 Options
15.13 libvo-amrwbenc
15.13.1 Options
15.14 libvorbis
15.14.1 Options
15.15 mjpeg
15.15.1 Options
15.16 wavpack
15.16.1 Options
15.16.1.1 Shared options
15.16.1.2 Private options
16 Video Encoders
16.1 a64_multi, a64_multi5
16.2 Cinepak
16.2.1 Options
16.3 GIF
16.3.1 Options
16.4 Hap
16.4.1 Options
16.5 jpeg2000
16.5.1 Options
16.6 librav1e
16.6.1 Options
16.7 libaom-av1
16.7.1 Options
16.8 libsvtav1
16.8.1 Options
16.9 libjxl
16.9.1 Options
16.10 libkvazaar
16.10.1 Options
16.11 libopenh264
16.11.1 Options
16.12 libtheora
16.12.1 Options
16.12.2 Examples
16.13 libvpx
16.13.1 Options
16.14 libvvenc
16.14.1 Supported Pixel Formats
16.14.2 Options
16.15 libwebp
16.15.1 Pixel Format
16.15.2 Options
16.16 libx264, libx264rgb
16.16.1 Supported Pixel Formats
16.16.2 Options
16.17 libx265
16.17.1 Options
16.18 libxavs2
16.18.1 Options
16.19 libxeve
16.19.1 Options
16.20 libxvid
16.20.1 Options
16.21 MediaFoundation
16.22 Microsoft RLE
16.22.1 Options
16.23 mpeg2
16.23.1 Options
16.24 png
16.24.1 Private options
16.25 ProRes
16.25.1 Private Options for prores-ks
16.25.2 Speed considerations
16.26 QSV Encoders
16.26.1 Ratecontrol Method
16.26.2 Global Options -> MSDK Options
16.26.3 Common Options
16.26.4 Runtime Options
16.26.5 H264 options
16.26.6 HEVC Options
16.26.7 MPEG2 Options
16.26.8 VP9 Options
16.26.9 AV1 Options
16.27 snow
16.27.1 Options
16.28 VAAPI encoders
16.29 vbn
16.29.1 Options
16.30 vc2
16.30.1 Options
17 Subtitles Encoders
17.1 dvdsub
17.1.1 Options
18 Bitstream Filters
18.1 aac_adtstoasc
18.2 av1_metadata
18.3 chomp
18.4 dca_core
18.5 dovi_rpu
18.6 dump_extra
18.7 dv_error_marker
18.8 eac3_core
18.9 extract_extradata
18.10 filter_units
18.11 hapqa_extract
18.12 h264_metadata
18.13 h264_mp4toannexb
18.14 h264_redundant_pps
18.15 hevc_metadata
18.16 hevc_mp4toannexb
18.17 imxdump
18.18 mjpeg2jpeg
18.19 mjpegadump
18.20 mov2textsub
18.21 mpeg2_metadata
18.22 mpeg4_unpack_bframes
18.23 noise
18.23.1 Examples
18.24 null
18.25 pcm_rechunk
18.26 pgs_frame_merge
18.27 prores_metadata
18.28 remove_extra
18.29 setts
18.30 showinfo
18.31 text2movsub
18.32 trace_headers
18.33 truehd_core
18.34 vp9_metadata
18.35 vp9_superframe
18.36 vp9_superframe_split
18.37 vp9_raw_reorder


14 Encoders
Encoders are configured elements in FFmpeg which allow the encoding of
multimedia streams.
When you configure your FFmpeg build, all the supported native encoders
are enabled by default. Encoders requiring an external library must be enabled
manually via the corresponding --enable-lib option. You can list all
available encoders using the configure option --list-encoders.
You can disable all the encoders with the configure option
--disable-encoders and selectively enable / disable single encoders
with the options --enable-encoder=ENCODER /
--disable-encoder=ENCODER.
The option -encoders of the ff* tools will display the list of
enabled encoders.
15 Audio Encoders
A description of some of the currently available audio encoders
follows.
15.1 aac
Advanced Audio Coding (AAC) encoder.
This encoder is the default AAC encoder, natively implemented into FFmpeg.
15.1.1 Options
b
Set bit rate in bits/s. Setting this automatically activates constant bit rate
(CBR) mode. If this option is unspecified it is set to 128kbps.
q
Set quality for variable bit rate (VBR) mode. This option is valid only using
the ffmpeg command-line tool. For library interface users, use
global_quality.
cutoff
Set cutoff frequency. If unspecified will allow the encoder to dynamically
adjust the cutoff to improve clarity on low bitrates.
aac_coder
Set AAC encoder coding method. Possible values:
‘twoloop’
Two loop searching (TLS) method. This is the default method.
This method first sets quantizers depending on band thresholds and then tries
to find an optimal combination by adding or subtracting a specific value from
all quantizers and adjusting some individual quantizer a little.  Will tune
itself based on whether aac_is, aac_ms and aac_pns
are enabled.
‘anmr’
Average noise to mask ratio (ANMR) trellis-based solution.
This is an experimental coder which currently produces a lower quality, is more
unstable and is slower than the default twoloop coder but has potential.
Currently has no support for the aac_is or aac_pns options.
Not currently recommended.
‘fast’
Constant quantizer method.
Uses a cheaper version of twoloop algorithm that doesn’t try to do as many
clever adjustments. Worse with low bitrates (less than 64kbps), but is better
and much faster at higher bitrates.
aac_ms
Sets mid/side coding mode. The default value of "auto" will automatically use
M/S with bands which will benefit from such coding. Can be forced for all bands
using the value "enable", which is mainly useful for debugging or disabled using
"disable".
aac_is
Sets intensity stereo coding tool usage. By default, it’s enabled and will
automatically toggle IS for similar pairs of stereo bands if it’s beneficial.
Can be disabled for debugging by setting the value to "disable".
aac_pns
Uses perceptual noise substitution to replace low entropy high frequency bands
with imperceptible white noise during the decoding process. By default, it’s
enabled, but can be disabled for debugging purposes by using "disable".
aac_tns
Enables the use of a multitap FIR filter which spans through the high frequency
bands to hide quantization noise during the encoding process and is reverted
by the decoder. As well as decreasing unpleasant artifacts in the high range
this also reduces the entropy in the high bands and allows for more bits to
be used by the mid-low bands. By default it’s enabled but can be disabled for
debugging by setting the option to "disable".
aac_ltp
Enables the use of the long term prediction extension which increases coding
efficiency in very low bandwidth situations such as encoding of voice or
solo piano music by extending constant harmonic peaks in bands throughout
frames. This option is implied by profile:a aac_low and is incompatible with
aac_pred. Use in conjunction with -ar to decrease the samplerate.
aac_pred
Enables the use of a more traditional style of prediction where the spectral
coefficients transmitted are replaced by the difference of the current
coefficients minus the previous "predicted" coefficients. In theory and sometimes
in practice this can improve quality for low to mid bitrate audio.
This option implies the aac_main profile and is incompatible with aac_ltp.
profile
Sets the encoding profile, possible values:
‘aac_low’
The default, AAC "Low-complexity" profile. Is the most compatible and produces
decent quality.
‘mpeg2_aac_low’
Equivalent to -profile:a aac_low -aac_pns 0. PNS was introduced with the
MPEG4 specifications.
‘aac_ltp’
Long term prediction profile, is enabled by and will enable the aac_ltp
option. Introduced in MPEG4.
‘aac_main’
Main-type prediction profile, is enabled by and will enable the aac_pred
option. Introduced in MPEG2.
If this option is unspecified it is set to ‘aac_low’.
15.2 ac3 and ac3_fixed
AC-3 audio encoders.
These encoders implement part of ATSC A/52:2010 and ETSI TS 102 366.
The ac3 encoder uses floating-point math, while the ac3_fixed
encoder only uses fixed-point integer math. This does not mean that one is
always faster, just that one or the other may be better suited to a
particular system. The ac3_fixed encoder is not the default codec for
any of the output formats, so it must be specified explicitly using the option
-acodec ac3_fixed in order to use it.
15.2.1 AC-3 Metadata
The AC-3 metadata options are used to set parameters that describe the audio,
but in most cases do not affect the audio encoding itself. Some of the options
do directly affect or influence the decoding and playback of the resulting
bitstream, while others are just for informational purposes. A few of the
options will add bits to the output stream that could otherwise be used for
audio data, and will thus affect the quality of the output. Those will be
indicated accordingly with a note in the option list below.
These parameters are described in detail in several publicly-available
documents.
A/52:2010 - Digital Audio Compression (AC-3) (E-AC-3) Standard
A/54 - Guide to the Use of the ATSC Digital Television Standard
Dolby Metadata Guide
Dolby Digital Professional Encoding Guidelines
15.2.1.1 Metadata Control Options
-per_frame_metadata boolean
Allow Per-Frame Metadata. Specifies if the encoder should check for changing
metadata for each frame.
0
The metadata values set at initialization will be used for every frame in the
stream. (default)
1
Metadata values can be changed before encoding each frame.
15.2.1.2 Downmix Levels
-center_mixlev level
Center Mix Level. The amount of gain the decoder should apply to the center
channel when downmixing to stereo. This field will only be written to the
bitstream if a center channel is present. The value is specified as a scale
factor. There are 3 valid values:
0.707
Apply -3dB gain
0.595
Apply -4.5dB gain (default)
0.500
Apply -6dB gain
-surround_mixlev level
Surround Mix Level. The amount of gain the decoder should apply to the surround
channel(s) when downmixing to stereo. This field will only be written to the
bitstream if one or more surround channels are present. The value is specified
as a scale factor.  There are 3 valid values:
0.707
Apply -3dB gain
0.500
Apply -6dB gain (default)
0.000
Silence Surround Channel(s)
15.2.1.3 Audio Production Information
Audio Production Information is optional information describing the mixing
environment.  Either none or both of the fields are written to the bitstream.
-mixing_level number
Mixing Level. Specifies peak sound pressure level (SPL) in the production
environment when the mix was mastered. Valid values are 80 to 111, or -1 for
unknown or not indicated. The default value is -1, but that value cannot be
used if the Audio Production Information is written to the bitstream. Therefore,
if the room_type option is not the default value, the mixing_level
option must not be -1.
-room_type type
Room Type. Describes the equalization used during the final mixing session at
the studio or on the dubbing stage. A large room is a dubbing stage with the
industry standard X-curve equalization; a small room has flat equalization.
This field will not be written to the bitstream if both the mixing_level
option and the room_type option have the default values.
0
notindicated
Not Indicated (default)
1
large
Large Room
2
small
Small Room
15.2.1.4 Other Metadata Options
-copyright boolean
Copyright Indicator. Specifies whether a copyright exists for this audio.
0
off
No Copyright Exists (default)
1
on
Copyright Exists
-dialnorm value
Dialogue Normalization. Indicates how far the average dialogue level of the
program is below digital 100% full scale (0 dBFS). This parameter determines a
level shift during audio reproduction that sets the average volume of the
dialogue to a preset level. The goal is to match volume level between program
sources. A value of -31dB will result in no volume level change, relative to
the source volume, during audio reproduction. Valid values are whole numbers in
the range -31 to -1, with -31 being the default.
-dsur_mode mode
Dolby Surround Mode. Specifies whether the stereo signal uses Dolby Surround
(Pro Logic). This field will only be written to the bitstream if the audio
stream is stereo. Using this option does NOT mean the encoder will actually
apply Dolby Surround processing.
0
notindicated
Not Indicated (default)
1
off
Not Dolby Surround Encoded
2
on
Dolby Surround Encoded
-original boolean
Original Bit Stream Indicator. Specifies whether this audio is from the
original source and not a copy.
0
off
Not Original Source
1
on
Original Source (default)
15.2.2 Extended Bitstream Information
The extended bitstream options are part of the Alternate Bit Stream Syntax as
specified in Annex D of the A/52:2010 standard. It is grouped into 2 parts.
If any one parameter in a group is specified, all values in that group will be
written to the bitstream.  Default values are used for those that are written
but have not been specified.  If the mixing levels are written, the decoder
will use these values instead of the ones specified in the center_mixlev
and surround_mixlev options if it supports the Alternate Bit Stream
Syntax.
15.2.2.1 Extended Bitstream Information - Part 1
-dmix_mode mode
Preferred Stereo Downmix Mode. Allows the user to select either Lt/Rt
(Dolby Surround) or Lo/Ro (normal stereo) as the preferred stereo downmix mode.
0
notindicated
Not Indicated (default)
1
ltrt
Lt/Rt Downmix Preferred
2
loro
Lo/Ro Downmix Preferred
-ltrt_cmixlev level
Lt/Rt Center Mix Level. The amount of gain the decoder should apply to the
center channel when downmixing to stereo in Lt/Rt mode.
1.414
Apply +3dB gain
1.189
Apply +1.5dB gain
1.000
Apply 0dB gain
0.841
Apply -1.5dB gain
0.707
Apply -3.0dB gain
0.595
Apply -4.5dB gain (default)
0.500
Apply -6.0dB gain
0.000
Silence Center Channel
-ltrt_surmixlev level
Lt/Rt Surround Mix Level. The amount of gain the decoder should apply to the
surround channel(s) when downmixing to stereo in Lt/Rt mode.
0.841
Apply -1.5dB gain
0.707
Apply -3.0dB gain
0.595
Apply -4.5dB gain
0.500
Apply -6.0dB gain (default)
0.000
Silence Surround Channel(s)
-loro_cmixlev level
Lo/Ro Center Mix Level. The amount of gain the decoder should apply to the
center channel when downmixing to stereo in Lo/Ro mode.
1.414
Apply +3dB gain
1.189
Apply +1.5dB gain
1.000
Apply 0dB gain
0.841
Apply -1.5dB gain
0.707
Apply -3.0dB gain
0.595
Apply -4.5dB gain (default)
0.500
Apply -6.0dB gain
0.000
Silence Center Channel
-loro_surmixlev level
Lo/Ro Surround Mix Level. The amount of gain the decoder should apply to the
surround channel(s) when downmixing to stereo in Lo/Ro mode.
0.841
Apply -1.5dB gain
0.707
Apply -3.0dB gain
0.595
Apply -4.5dB gain
0.500
Apply -6.0dB gain (default)
0.000
Silence Surround Channel(s)
15.2.2.2 Extended Bitstream Information - Part 2
-dsurex_mode mode
Dolby Surround EX Mode. Indicates whether the stream uses Dolby Surround EX
(7.1 matrixed to 5.1). Using this option does NOT mean the encoder will actually
apply Dolby Surround EX processing.
0
notindicated
Not Indicated (default)
1
on
Dolby Surround EX Off
2
off
Dolby Surround EX On
-dheadphone_mode mode
Dolby Headphone Mode. Indicates whether the stream uses Dolby Headphone
encoding (multi-channel matrixed to 2.0 for use with headphones). Using this
option does NOT mean the encoder will actually apply Dolby Headphone
processing.
0
notindicated
Not Indicated (default)
1
on
Dolby Headphone Off
2
off
Dolby Headphone On
-ad_conv_type type
A/D Converter Type. Indicates whether the audio has passed through HDCD A/D
conversion.
0
standard
Standard A/D Converter (default)
1
hdcd
HDCD A/D Converter
15.2.3 Other AC-3 Encoding Options
-stereo_rematrixing boolean
Stereo Rematrixing. Enables/Disables use of rematrixing for stereo input. This
is an optional AC-3 feature that increases quality by selectively encoding
the left/right channels as mid/side. This option is enabled by default, and it
is highly recommended that it be left as enabled except for testing purposes.
cutoff frequency
Set lowpass cutoff frequency. If unspecified, the encoder selects a default
determined by various other encoding parameters.
15.2.4 Floating-Point-Only AC-3 Encoding Options
These options are only valid for the floating-point encoder and do not exist
for the fixed-point encoder due to the corresponding features not being
implemented in fixed-point.
-channel_coupling boolean
Enables/Disables use of channel coupling, which is an optional AC-3 feature
that increases quality by combining high frequency information from multiple
channels into a single channel. The per-channel high frequency information is
sent with less accuracy in both the frequency and time domains. This allows
more bits to be used for lower frequencies while preserving enough information
to reconstruct the high frequencies. This option is enabled by default for the
floating-point encoder and should generally be left as enabled except for
testing purposes or to increase encoding speed.
-1
auto
Selected by Encoder (default)
0
off
Disable Channel Coupling
1
on
Enable Channel Coupling
-cpl_start_band number
Coupling Start Band. Sets the channel coupling start band, from 1 to 15. If a
value higher than the bandwidth is used, it will be reduced to 1 less than the
coupling end band. If auto is used, the start band will be determined by
the encoder based on the bit rate, sample rate, and channel layout. This option
has no effect if channel coupling is disabled.
-1
auto
Selected by Encoder (default)
15.3 ffv1
FFv1 Encoder
15.3.1 Options
The following options are supported by FFmpeg’s FFv1 encoder.
context
Sets the context size, 0 (default) is small, 1 is big.
coder
Set the coder,
‘rice’
Golomb rice coder
‘range_def’
Range coder with default table
‘range_tab’
Range coder with custom table
slicecrc
-1 (default, automatic), 1 use crc with zero initial and final state, 2 use crc with non zero initial and final state
qtable
‘default’
default, automatic
‘8bit’
use 8bit default
‘greater8bit’
use >8bit default
15.4 flac
FLAC (Free Lossless Audio Codec) Encoder
15.4.1 Options
The following options are supported by FFmpeg’s flac encoder.
compression_level
Sets the compression level, which chooses defaults for many other options
if they are not set explicitly. Valid values are from 0 to 12, 5 is the
default.
frame_size
Sets the size of the frames in samples per channel.
lpc_coeff_precision
Sets the LPC coefficient precision, valid values are from 1 to 15, 15 is the
default.
lpc_type
Sets the first stage LPC algorithm
‘none’
LPC is not used
‘fixed’
fixed LPC coefficients
‘levinson’
‘cholesky’
lpc_passes
Number of passes to use for Cholesky factorization during LPC analysis
min_partition_order
The minimum partition order
max_partition_order
The maximum partition order
prediction_order_method
‘estimation’
‘2level’
‘4level’
‘8level’
‘search’
Bruteforce search
‘log’
ch_mode
Channel mode
‘auto’
The mode is chosen automatically for each frame
‘indep’
Channels are independently coded
‘left_side’
‘right_side’
‘mid_side’
exact_rice_parameters
Chooses if rice parameters are calculated exactly or approximately.
if set to 1 then they are chosen exactly, which slows the code down slightly and
improves compression slightly.
multi_dim_quant
Multi Dimensional Quantization. If set to 1 then a 2nd stage LPC algorithm is
applied after the first stage to finetune the coefficients. This is quite slow
and slightly improves compression.
15.5 opus
Opus encoder.
This is a native FFmpeg encoder for the Opus format. Currently, it’s in development and
only implements the CELT part of the codec. Its quality is usually worse and at best
is equal to the libopus encoder.
15.5.1 Options
b
Set bit rate in bits/s. If unspecified it uses the number of channels and the layout
to make a good guess.
opus_delay
Sets the maximum delay in milliseconds. Lower delays than 20ms will very quickly
decrease quality.
15.6 libfdk_aac
libfdk-aac AAC (Advanced Audio Coding) encoder wrapper.
The libfdk-aac library is based on the Fraunhofer FDK AAC code from
the Android project.
Requires the presence of the libfdk-aac headers and library during
configuration. You need to explicitly configure the build with
--enable-libfdk-aac. The library is also incompatible with GPL,
so if you allow the use of GPL, you should configure with
--enable-gpl --enable-nonfree --enable-libfdk-aac.
This encoder has support for the AAC-HE profiles.
VBR encoding, enabled through the vbr or flags
+qscale options, is experimental and only works with some
combinations of parameters.
Support for encoding 7.1 audio is only available with libfdk-aac 0.1.3 or
higher.
For more information see the fdk-aac project at
http://sourceforge.net/p/opencore-amr/fdk-aac/.
15.6.1 Options
The following options are mapped on the shared FFmpeg codec options.
b
Set bit rate in bits/s. If the bitrate is not explicitly specified, it
is automatically set to a suitable value depending on the selected
profile.
In case VBR mode is enabled the option is ignored.
ar
Set audio sampling rate (in Hz).
channels
Set the number of audio channels.
flags +qscale
Enable fixed quality, VBR (Variable Bit Rate) mode.
Note that VBR is implicitly enabled when the vbr value is
positive.
cutoff
Set cutoff frequency. If not specified (or explicitly set to 0) it
will use a value automatically computed by the library. Default value
is 0.
profile
Set audio profile.
The following profiles are recognized:
‘aac_low’
Low Complexity AAC (LC)
‘aac_he’
High Efficiency AAC (HE-AAC)
‘aac_he_v2’
High Efficiency AAC version 2 (HE-AACv2)
‘aac_ld’
Low Delay AAC (LD)
‘aac_eld’
Enhanced Low Delay AAC (ELD)
If not specified it is set to ‘aac_low’.
The following are private options of the libfdk_aac encoder.
afterburner
Enable afterburner feature if set to 1, disabled if set to 0. This
improves the quality but also the required processing power.
Default value is 1.
eld_sbr
Enable SBR (Spectral Band Replication) for ELD if set to 1, disabled
if set to 0.
Default value is 0.
eld_v2
Enable ELDv2 (LD-MPS extension for ELD stereo signals) for ELDv2 if set to 1,
disabled if set to 0.
Note that option is available when fdk-aac version (AACENCODER_LIB_VL0.AACENCODER_LIB_VL1.AACENCODER_LIB_VL2) > (4.0.0).
Default value is 0.
signaling
Set SBR/PS signaling style.
It can assume one of the following values:
‘default’
choose signaling implicitly (explicit hierarchical by default,
implicit if global header is disabled)
‘implicit’
implicit backwards compatible signaling
‘explicit_sbr’
explicit SBR, implicit PS signaling
‘explicit_hierarchical’
explicit hierarchical signaling
Default value is ‘default’.
latm
Output LATM/LOAS encapsulated data if set to 1, disabled if set to 0.
Default value is 0.
header_period
Set StreamMuxConfig and PCE repetition period (in frames) for sending
in-band configuration buffers within LATM/LOAS transport layer.
Must be a 16-bits non-negative integer.
Default value is 0.
vbr
Set VBR mode, from 1 to 5. 1 is lowest quality (though still pretty
good) and 5 is highest quality. A value of 0 will disable VBR, and CBR
(Constant Bit Rate) is enabled.
Currently only the ‘aac_low’ profile supports VBR encoding.
VBR modes 1-5 correspond to roughly the following average bit rates:
‘1’
32 kbps/channel
‘2’
40 kbps/channel
‘3’
48-56 kbps/channel
‘4’
64 kbps/channel
‘5’
about 80-96 kbps/channel
Default value is 0.
frame_length
Set the audio frame length in samples. Default value is the internal
default of the library. Refer to the library’s documentation for information
about supported values.
15.6.2 Examples
Use ffmpeg to convert an audio file to VBR AAC in an M4A (MP4)
container:
ffmpeg -i input.wav -codec:a libfdk_aac -vbr 3 output.m4a
Use ffmpeg to convert an audio file to CBR 64k kbps AAC, using the
High-Efficiency AAC profile:
ffmpeg -i input.wav -c:a libfdk_aac -profile:a aac_he -b:a 64k output.m4a
15.7 liblc3
liblc3 LC3 (Low Complexity Communication Codec) encoder wrapper.
Requires the presence of the liblc3 headers and library during configuration.
You need to explicitly configure the build with --enable-liblc3.
This encoder has support for the Bluetooth SIG LC3 codec for the LE Audio
protocol, and the following features of LC3plus:
Frame duration of 2.5 and 5ms.
High-Resolution mode, 48 KHz, and 96 kHz sampling rates.
For more information see the liblc3 project at
https://github.com/google/liblc3.
15.7.1 Options
The following options are mapped on the shared FFmpeg codec options.
b bitrate
Set the bit rate in bits/s. This will determine the fixed size of the encoded
frames, for a selected frame duration.
ar frequency
Set the audio sampling rate (in Hz).
channels
Set the number of audio channels.
frame_duration
Set the audio frame duration in milliseconds. Default value is 10ms.
Allowed frame durations are 2.5ms, 5ms, 7.5ms and 10ms.
LC3 (Bluetooth LE Audio), allows 7.5ms and 10ms; and LC3plus 2.5ms, 5ms
and 10ms.
The 10ms frame duration is available in LC3 and LC3 plus standard.
In this mode, the produced bitstream can be referenced either as LC3 or LC3plus.
high_resolution boolean
Enable the high-resolution mode if set to 1. The high-resolution mode is
available with all LC3plus frame durations and for a sampling rate of 48 KHz,
and 96 KHz.
The encoder automatically turns off this mode at lower sampling rates and
activates it at 96 KHz.
This mode should be preferred at high bitrates. In this mode, the audio
bandwidth is always up to the Nyquist frequency, compared to LC3 at 48 KHz,
which limits the bandwidth to 20 KHz.
15.8 libmp3lame
LAME (Lame Ain’t an MP3 Encoder) MP3 encoder wrapper.
Requires the presence of the libmp3lame headers and library during
configuration. You need to explicitly configure the build with
--enable-libmp3lame.
See libshine for a fixed-point MP3 encoder, although with a
lower quality.
15.8.1 Options
The following options are supported by the libmp3lame wrapper. The
lame-equivalent of the options are listed in parentheses.
b (-b)
Set bitrate expressed in bits/s for CBR or ABR. LAME bitrate is
expressed in kilobits/s.
q (-V)
Set constant quality setting for VBR. This option is valid only
using the ffmpeg command-line tool. For library interface
users, use global_quality.
compression_level (-q)
Set algorithm quality. Valid arguments are integers in the 0-9 range,
with 0 meaning highest quality but slowest, and 9 meaning fastest
while producing the worst quality.
cutoff (--lowpass)
Set lowpass cutoff frequency. If unspecified, the encoder dynamically
adjusts the cutoff.
reservoir
Enable use of bit reservoir when set to 1. Default value is 1. LAME
has this enabled by default, but can be overridden by use
--nores option.
joint_stereo (-m j)
Enable the encoder to use (on a frame by frame basis) either L/R
stereo or mid/side stereo. Default value is 1.
abr (--abr)
Enable the encoder to use ABR when set to 1. The lame
--abr sets the target bitrate, while this options only
tells FFmpeg to use ABR still relies on b to set bitrate.
copyright (-c)
Set MPEG audio copyright flag when set to 1. The default value is 0
(disabled).
original (-o)
Set MPEG audio original flag when set to 1. The default value is 1
(enabled).
15.9 libopencore-amrnb
OpenCORE Adaptive Multi-Rate Narrowband encoder.
Requires the presence of the libopencore-amrnb headers and library during
configuration. You need to explicitly configure the build with
--enable-libopencore-amrnb --enable-version3.
This is a mono-only encoder. Officially it only supports 8000Hz sample rate,
but you can override it by setting strict to ‘unofficial’ or
lower.
15.9.1 Options
b
Set bitrate in bits per second. Only the following bitrates are supported,
otherwise libavcodec will round to the nearest valid bitrate.
4750
5150
5900
6700
7400
7950
10200
12200
dtx
Allow discontinuous transmission (generate comfort noise) when set to 1. The
default value is 0 (disabled).
15.10 libopus
libopus Opus Interactive Audio Codec encoder wrapper.
Requires the presence of the libopus headers and library during
configuration. You need to explicitly configure the build with
--enable-libopus.
15.10.1 Option Mapping
Most libopus options are modelled after the opusenc utility from
opus-tools. The following is an option mapping chart describing options
supported by the libopus wrapper, and their opusenc-equivalent
in parentheses.
b (bitrate)
Set the bit rate in bits/s.  FFmpeg’s b option is
expressed in bits/s, while opusenc’s bitrate in
kilobits/s.
vbr (vbr, hard-cbr, and cvbr)
Set VBR mode. The FFmpeg vbr option has the following
valid arguments, with the opusenc equivalent options
in parentheses:
‘off (hard-cbr)’
Use constant bit rate encoding.
‘on (vbr)’
Use variable bit rate encoding (the default).
‘constrained (cvbr)’
Use constrained variable bit rate encoding.
compression_level (comp)
Set encoding algorithm complexity. Valid options are integers in
the 0-10 range. 0 gives the fastest encodes but lower quality, while 10
gives the highest quality but slowest encoding. The default is 10.
frame_duration (framesize)
Set maximum frame size, or duration of a frame in milliseconds. The
argument must be exactly the following: 2.5, 5, 10, 20, 40, 60. Smaller
frame sizes achieve lower latency but less quality at a given bitrate.
Sizes greater than 20ms are only interesting at fairly low bitrates.
The default is 20ms.
packet_loss (expect-loss)
Set expected packet loss percentage. The default is 0.
fec (n/a)
Enable inband forward error correction. packet_loss must be non-zero
to take advantage - frequency of FEC ’side-data’ is proportional to expected packet loss.
Default is disabled.
application (N.A.)
Set intended application type. Valid options are listed below:
‘voip’
Favor improved speech intelligibility.
‘audio’
Favor faithfulness to the input (the default).
‘lowdelay’
Restrict to only the lowest delay modes by disabling voice-optimized
modes.
cutoff (N.A.)
Set cutoff bandwidth in Hz. The argument must be exactly one of the
following: 4000, 6000, 8000, 12000, or 20000, corresponding to
narrowband, mediumband, wideband, super wideband, and fullband
respectively. The default is 0 (cutoff disabled). Note that libopus
forces a wideband cutoff for bitrates < 15 kbps, unless CELT-only
(application set to ‘lowdelay’) mode is used.
mapping_family (mapping_family)
Set channel mapping family to be used by the encoder. The default value of -1
uses mapping family 0 for mono and stereo inputs, and mapping family 1
otherwise. The default also disables the surround masking and LFE bandwidth
optimzations in libopus, and requires that the input contains 8 channels or
fewer.
Other values include 0 for mono and stereo, 1 for surround sound with masking
and LFE bandwidth optimizations, and 255 for independent streams with an
unspecified channel layout.
apply_phase_inv (N.A.) (requires libopus >= 1.2)
If set to 0, disables the use of phase inversion for intensity stereo,
improving the quality of mono downmixes, but slightly reducing normal stereo
quality. The default is 1 (phase inversion enabled).
15.11 libshine
Shine Fixed-Point MP3 encoder wrapper.
Shine is a fixed-point MP3 encoder. It has a far better performance on
platforms without an FPU, e.g. armel CPUs, and some phones and tablets.
However, as it is more targeted on performance than quality, it is not on par
with LAME and other production-grade encoders quality-wise. Also, according to
the project’s homepage, this encoder may not be free of bugs as the code was
written a long time ago and the project was dead for at least 5 years.
This encoder only supports stereo and mono input. This is also CBR-only.
The original project (last updated in early 2007) is at
http://sourceforge.net/projects/libshine-fxp/. We only support the
updated fork by the Savonet/Liquidsoap project at https://github.com/savonet/shine.
Requires the presence of the libshine headers and library during
configuration. You need to explicitly configure the build with
--enable-libshine.
See also libmp3lame.
15.11.1 Options
The following options are supported by the libshine wrapper. The
shineenc-equivalent of the options are listed in parentheses.
b (-b)
Set bitrate expressed in bits/s for CBR. shineenc -b option
is expressed in kilobits/s.
15.12 libtwolame
TwoLAME MP2 encoder wrapper.
Requires the presence of the libtwolame headers and library during
configuration. You need to explicitly configure the build with
--enable-libtwolame.
15.12.1 Options
The following options are supported by the libtwolame wrapper. The
twolame-equivalent options follow the FFmpeg ones and are in
parentheses.
b (-b)
Set bitrate expressed in bits/s for CBR. twolame b
option is expressed in kilobits/s. Default value is 128k.
q (-V)
Set quality for experimental VBR support. Maximum value range is
from -50 to 50, useful range is from -10 to 10. The higher the
value, the better the quality. This option is valid only using the
ffmpeg command-line tool. For library interface users,
use global_quality.
mode (--mode)
Set the mode of the resulting audio. Possible values:
‘auto’
Choose mode automatically based on the input. This is the default.
‘stereo’
Stereo
‘joint_stereo’
Joint stereo
‘dual_channel’
Dual channel
‘mono’
Mono
psymodel (--psyc-mode)
Set psychoacoustic model to use in encoding. The argument must be
an integer between -1 and 4, inclusive. The higher the value, the
better the quality. The default value is 3.
energy_levels (--energy)
Enable energy levels extensions when set to 1. The default value is
0 (disabled).
error_protection (--protect)
Enable CRC error protection when set to 1. The default value is 0
(disabled).
copyright (--copyright)
Set MPEG audio copyright flag when set to 1. The default value is 0
(disabled).
original (--original)
Set MPEG audio original flag when set to 1. The default value is 0
(disabled).
15.13 libvo-amrwbenc
VisualOn Adaptive Multi-Rate Wideband encoder.
Requires the presence of the libvo-amrwbenc headers and library during
configuration. You need to explicitly configure the build with
--enable-libvo-amrwbenc --enable-version3.
This is a mono-only encoder. Officially it only supports 16000Hz sample
rate, but you can override it by setting strict to
‘unofficial’ or lower.
15.13.1 Options
b
Set bitrate in bits/s. Only the following bitrates are supported, otherwise
libavcodec will round to the nearest valid bitrate.
‘6600’
‘8850’
‘12650’
‘14250’
‘15850’
‘18250’
‘19850’
‘23050’
‘23850’
dtx
Allow discontinuous transmission (generate comfort noise) when set to 1. The
default value is 0 (disabled).
15.14 libvorbis
libvorbis encoder wrapper.
Requires the presence of the libvorbisenc headers and library during
configuration. You need to explicitly configure the build with
--enable-libvorbis.
15.14.1 Options
The following options are supported by the libvorbis wrapper. The
oggenc-equivalent of the options are listed in parentheses.
To get a more accurate and extensive documentation of the libvorbis
options, consult the libvorbisenc’s and oggenc’s documentations.
See http://xiph.org/vorbis/,
http://wiki.xiph.org/Vorbis-tools, and oggenc(1).
b (-b)
Set bitrate expressed in bits/s for ABR. oggenc -b is
expressed in kilobits/s.
q (-q)
Set constant quality setting for VBR. The value should be a float
number in the range of -1.0 to 10.0. The higher the value, the better
the quality. The default value is ‘3.0’.
This option is valid only using the ffmpeg command-line tool.
For library interface users, use global_quality.
cutoff (--advanced-encode-option lowpass_frequency=N)
Set cutoff bandwidth in Hz, a value of 0 disables cutoff. oggenc’s
related option is expressed in kHz. The default value is ‘0’ (cutoff
disabled).
minrate (-m)
Set minimum bitrate expressed in bits/s. oggenc -m is
expressed in kilobits/s.
maxrate (-M)
Set maximum bitrate expressed in bits/s. oggenc -M is
expressed in kilobits/s. This only has effect on ABR mode.
iblock (--advanced-encode-option impulse_noisetune=N)
Set noise floor bias for impulse blocks. The value is a float number from
-15.0 to 0.0. A negative bias instructs the encoder to pay special attention
to the crispness of transients in the encoded audio. The tradeoff for better
transient response is a higher bitrate.
15.15 mjpeg
Motion JPEG encoder.
15.15.1 Options
huffman
Set the huffman encoding strategy. Possible values:
‘default’
Use the default huffman tables. This is the default strategy.
‘optimal’
Compute and use optimal huffman tables.
15.16 wavpack
WavPack lossless audio encoder.
15.16.1 Options
The equivalent options for wavpack command line utility are listed in
parentheses.
15.16.1.1 Shared options
The following shared options are effective for this encoder. Only special notes
about this particular encoder will be documented here. For the general meaning
of the options, see the Codec Options chapter.
frame_size (--blocksize)
For this encoder, the range for this option is between 128 and 131072. Default
is automatically decided based on sample rate and number of channel.
For the complete formula of calculating default, see
libavcodec/wavpackenc.c.
compression_level (-f, -h, -hh, and -x)
15.16.1.2 Private options
joint_stereo (-j)
Set whether to enable joint stereo. Valid values are:
‘on (1)’
Force mid/side audio encoding.
‘off (0)’
Force left/right audio encoding.
‘auto’
Let the encoder decide automatically.
optimize_mono
Set whether to enable optimization for mono. This option is only effective for
non-mono streams. Available values:
‘on’
enabled
‘off’
disabled

16 Video Encoders
A description of some of the currently available video encoders
follows.
16.1 a64_multi, a64_multi5
A64 / Commodore 64 multicolor charset encoder. a64_multi5 is extended with 5th color (colram).
16.2 Cinepak
Cinepak aka CVID encoder.
Compatible with Windows 3.1 and vintage MacOS.
16.2.1 Options
g integer
Keyframe interval.
A keyframe is inserted at least every -g frames, sometimes sooner.
q:v integer
Quality factor. Lower is better. Higher gives lower bitrate.
The following table lists bitrates when encoding akiyo_cif.y4m for various values of -q:v with -g 100:
-q:v 1 1918 kb/s
-q:v 2 1735 kb/s
-q:v 4 1500 kb/s
-q:v 10 1041 kb/s
-q:v 20 826 kb/s
-q:v 40 553 kb/s
-q:v 100 394 kb/s
-q:v 200 312 kb/s
-q:v 400 266 kb/s
-q:v 1000 237 kb/s
max_extra_cb_iterations integer
Max extra codebook recalculation passes, more is better and slower.
skip_empty_cb boolean
Avoid wasting bytes, ignore vintage MacOS decoder.
max_strips integer
min_strips integer
The minimum and maximum number of strips to use.
Wider range sometimes improves quality.
More strips is generally better quality but costs more bits.
Fewer strips tend to yield more keyframes.
Vintage compatible is 1..3.
strip_number_adaptivity integer
How much number of strips is allowed to change between frames.
Higher is better but slower.
16.3 GIF
GIF image/animation encoder.
16.3.1 Options
gifflags integer
Sets the flags used for GIF encoding.
offsetting
Enables picture offsetting.
Default is enabled.
transdiff
Enables transparency detection between frames.
Default is enabled.
gifimage integer
Enables encoding one full GIF image per frame, rather than an animated GIF.
Default value is 0.
global_palette integer
Writes a palette to the global GIF header where feasible.
If disabled, every frame will always have a palette written, even if there
is a global palette supplied.
Default value is 1.
16.4 Hap
Vidvox Hap video encoder.
16.4.1 Options
format integer
Specifies the Hap format to encode.
hap
hap_alpha
hap_q
Default value is hap.
chunks integer
Specifies the number of chunks to split frames into, between 1 and 64. This
permits multithreaded decoding of large frames, potentially at the cost of
data-rate. The encoder may modify this value to divide frames evenly.
Default value is 1.
compressor integer
Specifies the second-stage compressor to use. If set to none,
chunks will be limited to 1, as chunked uncompressed frames offer no
benefit.
none
snappy
Default value is snappy.
16.5 jpeg2000
The native jpeg 2000 encoder is lossy by default, the -q:v
option can be used to set the encoding quality. Lossless encoding
can be selected with -pred 1.
16.5.1 Options
format integer
Can be set to either j2k or jp2 (the default) that
makes it possible to store non-rgb pix_fmts.
tile_width integer
Sets tile width. Range is 1 to 1073741824. Default is 256.
tile_height integer
Sets tile height. Range is 1 to 1073741824. Default is 256.
pred integer
Allows setting the discrete wavelet transform (DWT) type
dwt97int (Lossy)
dwt53 (Lossless)
Default is dwt97int
sop boolean
Enable this to add SOP marker at the start of each packet. Disabled by default.
eph boolean
Enable this to add EPH marker at the end of each packet header. Disabled by default.
prog integer
Sets the progression order to be used by the encoder.
Possible values are:
lrcp
rlcp
rpcl
pcrl
cprl
Set to lrcp by default.
layer_rates string
By default, when this option is not used, compression is done using the quality metric.
This option allows for compression using compression ratio. The compression ratio for each
level could be specified. The compression ratio of a layer l species the what ratio of
total file size is contained in the first l layers.
Example usage:
ffmpeg -i input.bmp -c:v jpeg2000 -layer_rates "100,10,1" output.j2k
This would compress the image to contain 3 layers, where the data contained in the
first layer would be compressed by 1000 times, compressed by 100 in the first two layers,
and shall contain all data while using all 3 layers.
16.6 librav1e
rav1e AV1 encoder wrapper.
Requires the presence of the rav1e headers and library during configuration.
You need to explicitly configure the build with --enable-librav1e.
16.6.1 Options
qmax
Sets the maximum quantizer to use when using bitrate mode.
qmin
Sets the minimum quantizer to use when using bitrate mode.
qp
Uses quantizer mode to encode at the given quantizer (0-255).
speed
Selects the speed preset (0-10) to encode with.
tiles
Selects how many tiles to encode with.
tile-rows
Selects how many rows of tiles to encode with.
tile-columns
Selects how many columns of tiles to encode with.
rav1e-params
Set rav1e options using a list of key=value pairs separated
by ":". See rav1e --help for a list of options.
For example to specify librav1e encoding options with -rav1e-params:
ffmpeg -i input -c:v librav1e -b:v 500K -rav1e-params speed=5:low_latency=true output.mp4
16.7 libaom-av1
libaom AV1 encoder wrapper.
Requires the presence of the libaom headers and library during
configuration.  You need to explicitly configure the build with
--enable-libaom.
16.7.1 Options
The wrapper supports the following standard libavcodec options:
b
Set bitrate target in bits/second.  By default this will use
variable-bitrate mode.  If maxrate and minrate are
also set to the same value then it will use constant-bitrate mode,
otherwise if crf is set as well then it will use
constrained-quality mode.
g keyint_min
Set key frame placement.  The GOP size sets the maximum distance between
key frames; if zero the output stream will be intra-only.  The minimum
distance is ignored unless it is the same as the GOP size, in which case
key frames will always appear at a fixed interval.  Not set by default,
so without this option the library has completely free choice about
where to place key frames.
qmin qmax
Set minimum/maximum quantisation values.  Valid range is from 0 to 63
(warning: this does not match the quantiser values actually used by AV1
- divide by four to map real quantiser values to this range).  Defaults
to min/max (no constraint).
minrate maxrate bufsize rc_init_occupancy
Set rate control buffering parameters.  Not used if not set - defaults
to unconstrained variable bitrate.
threads
Set the number of threads to use while encoding.  This may require the
tiles or row-mt options to also be set to actually
use the specified number of threads fully. Defaults to the number of
hardware threads supported by the host machine.
profile
Set the encoding profile.  Defaults to using the profile which matches
the bit depth and chroma subsampling of the input.
The wrapper also has some specific options:
cpu-used
Set the quality/encoding speed tradeoff.  Valid range is from 0 to 8,
higher numbers indicating greater speed and lower quality.  The default
value is 1, which will be slow and high quality.
auto-alt-ref
Enable use of alternate reference frames.  Defaults to the internal
default of the library.
arnr-max-frames (frames)
Set altref noise reduction max frame count. Default is -1.
arnr-strength (strength)
Set altref noise reduction filter strength. Range is -1 to 6. Default is -1.
aq-mode (aq-mode)
Set adaptive quantization mode. Possible values:
‘none (0)’
Disabled.
‘variance (1)’
Variance-based.
‘complexity (2)’
Complexity-based.
‘cyclic (3)’
Cyclic refresh.
tune (tune)
Set the distortion metric the encoder is tuned with. Default is psnr.
‘psnr (0)’
‘ssim (1)’
lag-in-frames
Set the maximum number of frames which the encoder may keep in flight
at any one time for lookahead purposes.  Defaults to the internal
default of the library.
error-resilience
Enable error resilience features:
default
Improve resilience against losses of whole frames.
Not enabled by default.
crf
Set the quality/size tradeoff for constant-quality (no bitrate target)
and constrained-quality (with maximum bitrate target) modes. Valid
range is 0 to 63, higher numbers indicating lower quality and smaller
output size.  Only used if set; by default only the bitrate target is
used.
static-thresh
Set a change threshold on blocks below which they will be skipped by
the encoder.  Defined in arbitrary units as a nonnegative integer,
defaulting to zero (no blocks are skipped).
drop-threshold
Set a threshold for dropping frames when close to rate control bounds.
Defined as a percentage of the target buffer - when the rate control
buffer falls below this percentage, frames will be dropped until it
has refilled above the threshold.  Defaults to zero (no frames are
dropped).
denoise-noise-level (level)
Amount of noise to be removed for grain synthesis. Grain synthesis is disabled if
this option is not set or set to 0.
denoise-block-size (pixels)
Block size used for denoising for grain synthesis. If not set, AV1 codec
uses the default value of 32.
undershoot-pct (pct)
Set datarate undershoot (min) percentage of the target bitrate. Range is -1 to 100.
Default is -1.
overshoot-pct (pct)
Set datarate overshoot (max) percentage of the target bitrate. Range is -1 to 1000.
Default is -1.
minsection-pct (pct)
Minimum percentage variation of the GOP bitrate from the target bitrate. If minsection-pct
is not set, the libaomenc wrapper computes it as follows: (minrate * 100 / bitrate).
Range is -1 to 100. Default is -1 (unset).
maxsection-pct (pct)
Maximum percentage variation of the GOP bitrate from the target bitrate. If maxsection-pct
is not set, the libaomenc wrapper computes it as follows: (maxrate * 100 / bitrate).
Range is -1 to 5000. Default is -1 (unset).
frame-parallel (boolean)
Enable frame parallel decodability features. Default is true.
tiles
Set the number of tiles to encode the input video with, as columns x
rows.  Larger numbers allow greater parallelism in both encoding and
decoding, but may decrease coding efficiency.  Defaults to the minimum
number of tiles required by the size of the input video (this is 1x1
(that is, a single tile) for sizes up to and including 4K).
tile-columns tile-rows
Set the number of tiles as log2 of the number of tile rows and columns.
Provided for compatibility with libvpx/VP9.
row-mt (Requires libaom >= 1.0.0-759-g90a15f4f2)
Enable row based multi-threading. Disabled by default.
enable-cdef (boolean)
Enable Constrained Directional Enhancement Filter. The libaom-av1
encoder enables CDEF by default.
enable-restoration (boolean)
Enable Loop Restoration Filter. Default is true for libaom-av1.
enable-global-motion (boolean)
Enable the use of global motion for block prediction. Default is true.
enable-intrabc (boolean)
Enable block copy mode for intra block prediction. This mode is
useful for screen content. Default is true.
enable-rect-partitions (boolean) (Requires libaom >= v2.0.0)
Enable rectangular partitions. Default is true.
enable-1to4-partitions (boolean) (Requires libaom >= v2.0.0)
Enable 1:4/4:1 partitions. Default is true.
enable-ab-partitions (boolean) (Requires libaom >= v2.0.0)
Enable AB shape partitions. Default is true.
enable-angle-delta (boolean) (Requires libaom >= v2.0.0)
Enable angle delta intra prediction. Default is true.
enable-cfl-intra (boolean) (Requires libaom >= v2.0.0)
Enable chroma predicted from luma intra prediction. Default is true.
enable-filter-intra (boolean) (Requires libaom >= v2.0.0)
Enable filter intra predictor. Default is true.
enable-intra-edge-filter (boolean) (Requires libaom >= v2.0.0)
Enable intra edge filter. Default is true.
enable-smooth-intra (boolean) (Requires libaom >= v2.0.0)
Enable smooth intra prediction mode. Default is true.
enable-paeth-intra (boolean) (Requires libaom >= v2.0.0)
Enable paeth predictor in intra prediction. Default is true.
enable-palette (boolean) (Requires libaom >= v2.0.0)
Enable palette prediction mode. Default is true.
enable-flip-idtx (boolean) (Requires libaom >= v2.0.0)
Enable extended transform type, including FLIPADST_DCT, DCT_FLIPADST,
FLIPADST_FLIPADST, ADST_FLIPADST, FLIPADST_ADST, IDTX, V_DCT, H_DCT,
V_ADST, H_ADST, V_FLIPADST, H_FLIPADST. Default is true.
enable-tx64 (boolean) (Requires libaom >= v2.0.0)
Enable 64-pt transform. Default is true.
reduced-tx-type-set (boolean) (Requires libaom >= v2.0.0)
Use reduced set of transform types. Default is false.
use-intra-dct-only (boolean) (Requires libaom >= v2.0.0)
Use DCT only for INTRA modes. Default is false.
use-inter-dct-only (boolean) (Requires libaom >= v2.0.0)
Use DCT only for INTER modes. Default is false.
use-intra-default-tx-only (boolean) (Requires libaom >= v2.0.0)
Use Default-transform only for INTRA modes. Default is false.
enable-ref-frame-mvs (boolean) (Requires libaom >= v2.0.0)
Enable temporal mv prediction. Default is true.
enable-reduced-reference-set (boolean) (Requires libaom >= v2.0.0)
Use reduced set of single and compound references. Default is false.
enable-obmc (boolean) (Requires libaom >= v2.0.0)
Enable obmc. Default is true.
enable-dual-filter (boolean) (Requires libaom >= v2.0.0)
Enable dual filter. Default is true.
enable-diff-wtd-comp (boolean) (Requires libaom >= v2.0.0)
Enable difference-weighted compound. Default is true.
enable-dist-wtd-comp (boolean) (Requires libaom >= v2.0.0)
Enable distance-weighted compound. Default is true.
enable-onesided-comp (boolean) (Requires libaom >= v2.0.0)
Enable one sided compound. Default is true.
enable-interinter-wedge (boolean) (Requires libaom >= v2.0.0)
Enable interinter wedge compound. Default is true.
enable-interintra-wedge (boolean) (Requires libaom >= v2.0.0)
Enable interintra wedge compound. Default is true.
enable-masked-comp (boolean) (Requires libaom >= v2.0.0)
Enable masked compound. Default is true.
enable-interintra-comp (boolean) (Requires libaom >= v2.0.0)
Enable interintra compound. Default is true.
enable-smooth-interintra (boolean) (Requires libaom >= v2.0.0)
Enable smooth interintra mode. Default is true.
aom-params
Set libaom options using a list of key=value pairs separated
by ":". For a list of supported options, see aomenc --help under the
section "AV1 Specific Options".
For example to specify libaom encoding options with -aom-params:
ffmpeg -i input -c:v libaom-av1 -b:v 500K -aom-params tune=psnr:enable-tpl-model=1 output.mp4
16.8 libsvtav1
SVT-AV1 encoder wrapper.
Requires the presence of the SVT-AV1 headers and library during configuration.
You need to explicitly configure the build with --enable-libsvtav1.
16.8.1 Options
profile
Set the encoding profile.
‘main’
‘high’
‘professional’
level
Set the operating point level. For example: ’4.0’
hielevel
Set the Hierarchical prediction levels.
‘3level’
‘4level’
This is the default.
tier
Set the operating point tier.
‘main’
This is the default.
‘high’
qmax
Set the maximum quantizer to use when using a bitrate mode.
qmin
Set the minimum quantizer to use when using a bitrate mode.
crf
Constant rate factor value used in crf rate control mode (0-63).
qp
Set the quantizer used in cqp rate control mode (0-63).
sc_detection
Enable scene change detection.
la_depth
Set number of frames to look ahead (0-120).
preset
Set the quality-speed tradeoff, in the range 0 to 13.  Higher values are
faster but lower quality.
tile_rows
Set log2 of the number of rows of tiles to use (0-6).
tile_columns
Set log2 of the number of columns of tiles to use (0-4).
svtav1-params
Set SVT-AV1 options using a list of key=value pairs separated
by ":". See the SVT-AV1 encoder user guide for a list of accepted parameters.
16.9 libjxl
libjxl JPEG XL encoder wrapper.
Requires the presence of the libjxl headers and library during
configuration. You need to explicitly configure the build with
--enable-libjxl.
16.9.1 Options
The libjxl wrapper supports the following options:
distance
Set the target Butteraugli distance. This is a quality setting: lower
distance yields higher quality, with distance=1.0 roughly comparable to
libjpeg Quality 90 for photographic content. Setting distance=0.0 yields
true lossless encoding. Valid values range between 0.0 and 15.0, and sane
values rarely exceed 5.0. Setting distance=0.1 usually attains
transparency for most input. The default is 1.0.
effort
Set the encoding effort used. Higher effort values produce more consistent
quality and usually produces a better quality/bpp curve, at the cost of
more CPU time required. Valid values range from 1 to 9, and the default is 7.
modular
Force the encoder to use Modular mode instead of choosing automatically. The
default is to use VarDCT for lossy encoding and Modular for lossless. VarDCT
is generally superior to Modular for lossy encoding but does not support
lossless encoding.
16.10 libkvazaar
Kvazaar H.265/HEVC encoder.
Requires the presence of the libkvazaar headers and library during
configuration. You need to explicitly configure the build with
--enable-libkvazaar.
16.10.1 Options
b
Set target video bitrate in bit/s and enable rate control.
kvazaar-params
Set kvazaar parameters as a list of name=value pairs separated
by commas (,). See kvazaar documentation for a list of options.
16.11 libopenh264
Cisco libopenh264 H.264/MPEG-4 AVC encoder wrapper.
This encoder requires the presence of the libopenh264 headers and
library during configuration. You need to explicitly configure the
build with --enable-libopenh264. The library is detected using
pkg-config.
For more information about the library see
http://www.openh264.org.
16.11.1 Options
The following FFmpeg global options affect the configurations of the
libopenh264 encoder.
b
Set the bitrate (as a number of bits per second).
g
Set the GOP size.
maxrate
Set the max bitrate (as a number of bits per second).
flags +global_header
Set global header in the bitstream.
slices
Set the number of slices, used in parallelized encoding. Default value
is 0. This is only used when slice_mode is set to
‘fixed’.
loopfilter
Enable loop filter, if set to 1 (automatically enabled). To disable
set a value of 0.
profile
Set profile restrictions. If set to the value of ‘main’ enable
CABAC (set the SEncParamExt.iEntropyCodingModeFlag flag to 1).
max_nal_size
Set maximum NAL size in bytes.
allow_skip_frames
Allow skipping frames to hit the target bitrate if set to 1.
16.12 libtheora
libtheora Theora encoder wrapper.
Requires the presence of the libtheora headers and library during
configuration. You need to explicitly configure the build with
--enable-libtheora.
For more information about the libtheora project see
http://www.theora.org/.
16.12.1 Options
The following global options are mapped to internal libtheora options
which affect the quality and the bitrate of the encoded stream.
b
Set the video bitrate in bit/s for CBR (Constant Bit Rate) mode.  In
case VBR (Variable Bit Rate) mode is enabled this option is ignored.
flags
Used to enable constant quality mode (VBR) encoding through the
qscale flag, and to enable the pass1 and pass2
modes.
g
Set the GOP size.
global_quality
Set the global quality as an integer in lambda units.
Only relevant when VBR mode is enabled with flags +qscale. The
value is converted to QP units by dividing it by FF_QP2LAMBDA,
clipped in the [0 - 10] range, and then multiplied by 6.3 to get a
value in the native libtheora range [0-63]. A higher value corresponds
to a higher quality.
q
Enable VBR mode when set to a non-negative value, and set constant
quality value as a double floating point value in QP units.
The value is clipped in the [0-10] range, and then multiplied by 6.3
to get a value in the native libtheora range [0-63].
This option is valid only using the ffmpeg command-line
tool. For library interface users, use global_quality.
16.12.2 Examples
Set maximum constant quality (VBR) encoding with ffmpeg:
ffmpeg -i INPUT -codec:v libtheora -q:v 10 OUTPUT.ogg
Use ffmpeg to convert a CBR 1000 kbps Theora video stream:
ffmpeg -i INPUT -codec:v libtheora -b:v 1000k OUTPUT.ogg
16.13 libvpx
VP8/VP9 format supported through libvpx.
Requires the presence of the libvpx headers and library during configuration.
You need to explicitly configure the build with --enable-libvpx.
16.13.1 Options
The following options are supported by the libvpx wrapper. The
vpxenc-equivalent options or values are listed in parentheses
for easy migration.
To reduce the duplication of documentation, only the private options
and some others requiring special attention are documented here. For
the documentation of the undocumented generic options, see
the Codec Options chapter.
To get more documentation of the libvpx options, invoke the command
ffmpeg -h encoder=libvpx, ffmpeg -h encoder=libvpx-vp9 or
vpxenc --help. Further information is available in the libvpx API
documentation.
b (target-bitrate)
Set bitrate in bits/s. Note that FFmpeg’s b option is
expressed in bits/s, while vpxenc’s target-bitrate is in
kilobits/s.
g (kf-max-dist)
keyint_min (kf-min-dist)
qmin (min-q)
Minimum (Best Quality) Quantizer.
qmax (max-q)
Maximum (Worst Quality) Quantizer.
Can be changed per-frame.
bufsize (buf-sz, buf-optimal-sz)
Set ratecontrol buffer size (in bits). Note vpxenc’s options are
specified in milliseconds, the libvpx wrapper converts this value as follows:
buf-sz = bufsize * 1000 / bitrate,
buf-optimal-sz = bufsize * 1000 / bitrate * 5 / 6.
rc_init_occupancy (buf-initial-sz)
Set number of bits which should be loaded into the rc buffer before decoding
starts. Note vpxenc’s option is specified in milliseconds, the libvpx
wrapper converts this value as follows:
rc_init_occupancy * 1000 / bitrate.
undershoot-pct
Set datarate undershoot (min) percentage of the target bitrate.
overshoot-pct
Set datarate overshoot (max) percentage of the target bitrate.
skip_threshold (drop-frame)
qcomp (bias-pct)
maxrate (maxsection-pct)
Set GOP max bitrate in bits/s. Note vpxenc’s option is specified as a
percentage of the target bitrate, the libvpx wrapper converts this value as
follows: (maxrate * 100 / bitrate).
minrate (minsection-pct)
Set GOP min bitrate in bits/s. Note vpxenc’s option is specified as a
percentage of the target bitrate, the libvpx wrapper converts this value as
follows: (minrate * 100 / bitrate).
minrate, maxrate, b end-usage=cbr
(minrate == maxrate == bitrate).
crf (end-usage=cq, cq-level)
tune (tune)
‘psnr (psnr)’
‘ssim (ssim)’
quality, deadline (deadline)
‘best’
Use best quality deadline. Poorly named and quite slow, this option should be
avoided as it may give worse quality output than good.
‘good’
Use good quality deadline. This is a good trade-off between speed and quality
when used with the cpu-used option.
‘realtime’
Use realtime quality deadline.
speed, cpu-used (cpu-used)
Set quality/speed ratio modifier. Higher values speed up the encode at the cost
of quality.
nr (noise-sensitivity)
static-thresh
Set a change threshold on blocks below which they will be skipped by the
encoder.
slices (token-parts)
Note that FFmpeg’s slices option gives the total number of partitions,
while vpxenc’s token-parts is given as
log2(partitions).
max-intra-rate
Set maximum I-frame bitrate as a percentage of the target bitrate. A value of 0
means unlimited.
force_key_frames
VPX_EFLAG_FORCE_KF
Alternate reference frame related
auto-alt-ref
Enable use of alternate reference frames (2-pass only).
Values greater than 1 enable multi-layer alternate reference frames (VP9 only).
arnr-maxframes
Set altref noise reduction max frame count.
arnr-type
Set altref noise reduction filter type: backward, forward, centered.
arnr-strength
Set altref noise reduction filter strength.
rc-lookahead, lag-in-frames (lag-in-frames)
Set number of frames to look ahead for frametype and ratecontrol.
min-gf-interval
Set minimum golden/alternate reference frame interval (VP9 only).
error-resilient
Enable error resiliency features.
sharpness integer
Increase sharpness at the expense of lower PSNR.
The valid range is [0, 7].
ts-parameters
Sets the temporal scalability configuration using a :-separated list of
key=value pairs. For example, to specify temporal scalability parameters
with ffmpeg:
ffmpeg -i INPUT -c:v libvpx -ts-parameters ts_number_layers=3:\
ts_target_bitrate=250,500,1000:ts_rate_decimator=4,2,1:\
ts_periodicity=4:ts_layer_id=0,2,1,2:ts_layering_mode=3 OUTPUT
Below is a brief explanation of each of the parameters, please
refer to struct vpx_codec_enc_cfg in vpx/vpx_encoder.h for more
details.
ts_number_layers
Number of temporal coding layers.
ts_target_bitrate
Target bitrate for each temporal layer (in kbps).
(bitrate should be inclusive of the lower temporal layer).
ts_rate_decimator
Frame rate decimation factor for each temporal layer.
ts_periodicity
Length of the sequence defining frame temporal layer membership.
ts_layer_id
Template defining the membership of frames to temporal layers.
ts_layering_mode
(optional) Selecting the temporal structure from a set of pre-defined temporal layering modes.
Currently supports the following options.
0
No temporal layering flags are provided internally,
relies on flags being passed in using metadata field in AVFrame
with following keys.
vp8-flags
Sets the flags passed into the encoder to indicate the referencing scheme for
the current frame.
Refer to function vpx_codec_encode in vpx/vpx_encoder.h for more
details.
temporal_id
Explicitly sets the temporal id of the current frame to encode.
2
Two temporal layers. 0-1...
3
Three temporal layers. 0-2-1-2...; with single reference frame.
4
Same as option "3", except there is a dependency between
the two temporal layer 2 frames within the temporal period.
VP8-specific options
screen-content-mode
Screen content mode, one of: 0 (off), 1 (screen), 2 (screen with more aggressive rate control).
VP9-specific options
lossless
Enable lossless mode.
tile-columns
Set number of tile columns to use. Note this is given as
log2(tile_columns). For example, 8 tile columns would be requested by
setting the tile-columns option to 3.
tile-rows
Set number of tile rows to use. Note this is given as log2(tile_rows).
For example, 4 tile rows would be requested by setting the tile-rows
option to 2.
frame-parallel
Enable frame parallel decodability features.
aq-mode
Set adaptive quantization mode (0: off (default), 1: variance 2: complexity, 3:
cyclic refresh, 4: equator360).
colorspace color-space
Set input color space. The VP9 bitstream supports signaling the following
colorspaces:
‘rgb’ sRGB
‘bt709’ bt709
‘unspecified’ unknown
‘bt470bg’ bt601
‘smpte170m’ smpte170
‘smpte240m’ smpte240
‘bt2020_ncl’ bt2020
row-mt boolean
Enable row based multi-threading.
tune-content
Set content type: default (0), screen (1), film (2).
corpus-complexity
Corpus VBR mode is a variant of standard VBR where the complexity distribution
midpoint is passed in rather than calculated for a specific clip or chunk.
The valid range is [0, 10000]. 0 (default) uses standard VBR.
enable-tpl boolean
Enable temporal dependency model.
ref-frame-config
Using per-frame metadata, set members of the structure vpx_svc_ref_frame_config_t in vpx/vp8cx.h to fine-control referencing schemes and frame buffer management.
Use a :-separated list of key=value pairs.
For example,
av_dict_set(&av_frame->metadata, "ref-frame-config", \
"rfc_update_buffer_slot=7:rfc_lst_fb_idx=0:rfc_gld_fb_idx=1:rfc_alt_fb_idx=2:rfc_reference_last=0:rfc_reference_golden=0:rfc_reference_alt_ref=0");
rfc_update_buffer_slot
Indicates the buffer slot number to update
rfc_update_last
Indicates whether to update the LAST frame
rfc_update_golden
Indicates whether to update GOLDEN frame
rfc_update_alt_ref
Indicates whether to update ALT_REF frame
rfc_lst_fb_idx
LAST frame buffer index
rfc_gld_fb_idx
GOLDEN frame buffer index
rfc_alt_fb_idx
ALT_REF frame buffer index
rfc_reference_last
Indicates whether to reference LAST frame
rfc_reference_golden
Indicates whether to reference GOLDEN frame
rfc_reference_alt_ref
Indicates whether to reference ALT_REF frame
rfc_reference_duration
Indicates frame duration
For more information about libvpx see:
http://www.webmproject.org/
16.14 libvvenc
VVenC H.266/VVC encoder wrapper.
This encoder requires the presence of the libvvenc headers and library
during configuration. You need to explicitly configure the build with
--enable-libvvenc.
The VVenC project website is at
https://github.com/fraunhoferhhi/vvenc.
16.14.1 Supported Pixel Formats
VVenC supports only 10-bit color spaces as input. But the internal (encoded)
bit depth can be set to 8-bit or 10-bit at runtime.
16.14.2 Options
b
Sets target video bitrate.
g
Set the GOP size. Currently support for g=1 (Intra only) or default.
preset
Set the VVenC preset.
levelidc
Set level idc.
tier
Set vvc tier.
qp
Set constant quantization parameter.
subopt boolean
Set subjective (perceptually motivated) optimization. Default is 1 (on).
bitdepth8 boolean
Set 8bit coding mode instead of using 10bit. Default is 0 (off).
period
set (intra) refresh period in seconds.
vvenc-params
Set vvenc options using a list of key=value couples separated
by ":". See vvencapp --fullhelp or vvencFFapp --fullhelp for a list of options.
For example, the options might be provided as:
intraperiod=64:decodingrefreshtype=idr:poc0idr=1:internalbitdepth=8
For example the encoding options might be provided with -vvenc-params:
ffmpeg -i input -c:v libvvenc -b 1M -vvenc-params intraperiod=64:decodingrefreshtype=idr:poc0idr=1:internalbitdepth=8 output.mp4
16.15 libwebp
libwebp WebP Image encoder wrapper
libwebp is Google’s official encoder for WebP images. It can encode in either
lossy or lossless mode. Lossy images are essentially a wrapper around a VP8
frame. Lossless images are a separate codec developed by Google.
16.15.1 Pixel Format
Currently, libwebp only supports YUV420 for lossy and RGB for lossless due
to limitations of the format and libwebp. Alpha is supported for either mode.
Because of API limitations, if RGB is passed in when encoding lossy or YUV is
passed in for encoding lossless, the pixel format will automatically be
converted using functions from libwebp. This is not ideal and is done only for
convenience.
16.15.2 Options
-lossless boolean
Enables/Disables use of lossless mode. Default is 0.
-compression_level integer
For lossy, this is a quality/speed tradeoff. Higher values give better quality
for a given size at the cost of increased encoding time. For lossless, this is
a size/speed tradeoff. Higher values give smaller size at the cost of increased
encoding time. More specifically, it controls the number of extra algorithms
and compression tools used, and varies the combination of these tools. This
maps to the method option in libwebp. The valid range is 0 to 6.
Default is 4.
-quality float
For lossy encoding, this controls image quality. For lossless encoding, this
controls the effort and time spent in compression.
Range is 0 to 100. Default is 75.
-preset type
Configuration preset. This does some automatic settings based on the general
type of the image.
none
Do not use a preset.
default
Use the encoder default.
picture
Digital picture, like portrait, inner shot
photo
Outdoor photograph, with natural lighting
drawing
Hand or line drawing, with high-contrast details
icon
Small-sized colorful images
text
Text-like
16.16 libx264, libx264rgb
x264 H.264/MPEG-4 AVC encoder wrapper.
This encoder requires the presence of the libx264 headers and library
during configuration. You need to explicitly configure the build with
--enable-libx264.
libx264 supports an impressive number of features, including 8x8 and
4x4 adaptive spatial transform, adaptive B-frame placement, CAVLC/CABAC
entropy coding, interlacing (MBAFF), lossless mode, psy optimizations
for detail retention (adaptive quantization, psy-RD, psy-trellis).
Many libx264 encoder options are mapped to FFmpeg global codec
options, while unique encoder options are provided through private
options. Additionally the x264opts and x264-params
private options allows one to pass a list of key=value tuples as accepted
by the libx264 x264_param_parse function.
The x264 project website is at
http://www.videolan.org/developers/x264.html.
The libx264rgb encoder is the same as libx264, except it accepts packed RGB
pixel formats as input instead of YUV.
16.16.1 Supported Pixel Formats
x264 supports 8- to 10-bit color spaces. The exact bit depth is controlled at
x264’s configure time.
16.16.2 Options
The following options are supported by the libx264 wrapper. The
x264-equivalent options or values are listed in parentheses
for easy migration.
To reduce the duplication of documentation, only the private options
and some others requiring special attention are documented here. For
the documentation of the undocumented generic options, see
the Codec Options chapter.
To get a more accurate and extensive documentation of the libx264
options, invoke the command x264 --fullhelp or consult
the libx264 documentation.
In the list below, note that the x264 option name is shown
in parentheses after the libavcodec corresponding name, in case there
is a direct mapping.
b (bitrate)
Set bitrate in bits/s. Note that FFmpeg’s b option is
expressed in bits/s, while x264’s bitrate is in
kilobits/s.
bf (bframes)
Number of B-frames between I and P-frames
g (keyint)
Maximum GOP size
qmin (qpmin)
Minimum quantizer scale
qmax (qpmax)
Maximum quantizer scale
qdiff (qpstep)
Maximum difference between quantizer scales
qblur (qblur)
Quantizer curve blur
qcomp (qcomp)
Quantizer curve compression factor
refs (ref)
Number of reference frames each P-frame can use. The range is 0-16.
level (level)
Set the x264_param_t.i_level_idc value in case the value is
positive, it is ignored otherwise.
This value can be set using the AVCodecContext API (e.g. by
setting the AVCodecContext value directly), and is specified as
an integer mapped on a corresponding level (e.g. the value 31 maps
to H.264 level IDC "3.1", as defined in the x264_levels
table). It is ignored when set to a non positive value.
Alternatively it can be set as a private option, overriding the value
set in AVCodecContext, and in this case must be specified as
the level IDC identifier (e.g. "3.1"), as defined by H.264 Annex A.
sc_threshold (scenecut)
Sets the threshold for the scene change detection.
trellis (trellis)
Performs Trellis quantization to increase efficiency. Enabled by default.
nr (nr)
Noise reduction
me_range (merange)
Maximum range of the motion search in pixels.
me_method (me)
Set motion estimation method. Possible values in the decreasing order
of speed:
‘dia (dia)’
‘epzs (dia)’
Diamond search with radius 1 (fastest). ‘epzs’ is an alias for
‘dia’.
‘hex (hex)’
Hexagonal search with radius 2.
‘umh (umh)’
Uneven multi-hexagon search.
‘esa (esa)’
Exhaustive search.
‘tesa (tesa)’
Hadamard exhaustive search (slowest).
forced-idr
Normally, when forcing a I-frame type, the encoder can select any type
of I-frame. This option forces it to choose an IDR-frame.
subq (subme)
Sub-pixel motion estimation method.
b_strategy (b-adapt)
Adaptive B-frame placement decision algorithm. Use only on first-pass.
keyint_min (min-keyint)
Minimum GOP size.
coder
Set entropy encoder. Possible values:
‘ac’
Enable CABAC.
‘vlc’
Enable CAVLC and disable CABAC. It generates the same effect as
x264’s --no-cabac option.
cmp
Set full pixel motion estimation comparison algorithm. Possible values:
‘chroma’
Enable chroma in motion estimation.
‘sad’
Ignore chroma in motion estimation. It generates the same effect as
x264’s --no-chroma-me option.
threads (threads)
Number of encoding threads.
thread_type
Set multithreading technique. Possible values:
‘slice’
Slice-based multithreading. It generates the same effect as
x264’s --sliced-threads option.
‘frame’
Frame-based multithreading.
flags
Set encoding flags. It can be used to disable closed GOP and enable
open GOP by setting it to -cgop. The result is similar to
the behavior of x264’s --open-gop option.
rc_init_occupancy (vbv-init)
Initial VBV buffer occupancy
preset (preset)
Set the encoding preset.
tune (tune)
Set tuning of the encoding params.
profile (profile)
Set profile restrictions.
fastfirstpass
Enable fast settings when encoding first pass, when set to 1. When set
to 0, it has the same effect of x264’s
--slow-firstpass option.
crf (crf)
Set the quality for constant quality mode.
crf_max (crf-max)
In CRF mode, prevents VBV from lowering quality beyond this point.
qp (qp)
Set constant quantization rate control method parameter.
aq-mode (aq-mode)
Set AQ method. Possible values:
‘none (0)’
Disabled.
‘variance (1)’
Variance AQ (complexity mask).
‘autovariance (2)’
Auto-variance AQ (experimental).
aq-strength (aq-strength)
Set AQ strength, reduce blocking and blurring in flat and textured areas.
psy
Use psychovisual optimizations when set to 1. When set to 0, it has the
same effect as x264’s --no-psy option.
psy-rd (psy-rd)
Set strength of psychovisual optimization, in
psy-rd:psy-trellis format.
rc-lookahead (rc-lookahead)
Set number of frames to look ahead for frametype and ratecontrol.
weightb
Enable weighted prediction for B-frames when set to 1. When set to 0,
it has the same effect as x264’s --no-weightb option.
weightp (weightp)
Set weighted prediction method for P-frames. Possible values:
‘none (0)’
Disabled
‘simple (1)’
Enable only weighted refs
‘smart (2)’
Enable both weighted refs and duplicates
ssim (ssim)
Enable calculation and printing SSIM stats after the encoding.
intra-refresh (intra-refresh)
Enable the use of Periodic Intra Refresh instead of IDR frames when set
to 1.
avcintra-class (class)
Configure the encoder to generate AVC-Intra.
Valid values are 50, 100 and 200
bluray-compat (bluray-compat)
Configure the encoder to be compatible with the bluray standard.
It is a shorthand for setting "bluray-compat=1 force-cfr=1".
b-bias (b-bias)
Set the influence on how often B-frames are used.
b-pyramid (b-pyramid)
Set method for keeping of some B-frames as references. Possible values:
‘none (none)’
Disabled.
‘strict (strict)’
Strictly hierarchical pyramid.
‘normal (normal)’
Non-strict (not Blu-ray compatible).
mixed-refs
Enable the use of one reference per partition, as opposed to one
reference per macroblock when set to 1. When set to 0, it has the
same effect as x264’s --no-mixed-refs option.
8x8dct
Enable adaptive spatial transform (high profile 8x8 transform)
when set to 1. When set to 0, it has the same effect as
x264’s --no-8x8dct option.
fast-pskip
Enable early SKIP detection on P-frames when set to 1. When set
to 0, it has the same effect as x264’s
--no-fast-pskip option.
aud (aud)
Enable use of access unit delimiters when set to 1.
mbtree
Enable use macroblock tree ratecontrol when set to 1. When set
to 0, it has the same effect as x264’s
--no-mbtree option.
deblock (deblock)
Set loop filter parameters, in alpha:beta form.
cplxblur (cplxblur)
Set fluctuations reduction in QP (before curve compression).
partitions (partitions)
Set partitions to consider as a comma-separated list of values.
Possible values in the list:
‘p8x8’
8x8 P-frame partition.
‘p4x4’
4x4 P-frame partition.
‘b8x8’
4x4 B-frame partition.
‘i8x8’
8x8 I-frame partition.
‘i4x4’
4x4 I-frame partition.
(Enabling ‘p4x4’ requires ‘p8x8’ to be enabled. Enabling
‘i8x8’ requires adaptive spatial transform (8x8dct
option) to be enabled.)
‘none (none)’
Do not consider any partitions.
‘all (all)’
Consider every partition.
direct-pred (direct)
Set direct MV prediction mode. Possible values:
‘none (none)’
Disable MV prediction.
‘spatial (spatial)’
Enable spatial predicting.
‘temporal (temporal)’
Enable temporal predicting.
‘auto (auto)’
Automatically decided.
slice-max-size (slice-max-size)
Set the limit of the size of each slice in bytes. If not specified
but RTP payload size (ps) is specified, that is used.
stats (stats)
Set the file name for multi-pass stats.
nal-hrd (nal-hrd)
Set signal HRD information (requires vbv-bufsize to be set).
Possible values:
‘none (none)’
Disable HRD information signaling.
‘vbr (vbr)’
Variable bit rate.
‘cbr (cbr)’
Constant bit rate (not allowed in MP4 container).
x264opts opts
x264-params opts
Override the x264 configuration using a :-separated list of key=value
options.
The argument for both options is a list of key=value
couples separated by ":". With x264opts the value can be
omitted, and the value 1 is assumed in that case.
For filter and psy-rd options values that use ":" as a
separator themselves, use "," instead. They accept it as well since
long ago but this is kept undocumented for some reason.
For example, the options might be provided as:
level=30:bframes=0:weightp=0:cabac=0:ref=1:vbv-maxrate=768:vbv-bufsize=2000:analyse=all:me=umh:no-fast-pskip=1:subq=6:8x8dct=0:trellis=0
For example to specify libx264 encoding options with ffmpeg:
ffmpeg -i foo.mpg -c:v libx264 -x264opts keyint=123:min-keyint=20 -an out.mkv
To get the complete list of the libx264 options, invoke the command
x264 --fullhelp or consult the libx264 documentation.
a53cc boolean
Import closed captions (which must be ATSC compatible format) into output.
Only the mpeg2 and h264 decoders provide these. Default is 1 (on).
udu_sei boolean
Import user data unregistered SEI if available into output. Default is 0 (off).
mb_info boolean
Set mb_info data through AVFrameSideData, only useful when used from the
API. Default is 0 (off).
Encoding ffpresets for common usages are provided so they can be used with the
general presets system (e.g. passing the pre option).
16.17 libx265
x265 H.265/HEVC encoder wrapper.
This encoder requires the presence of the libx265 headers and library
during configuration. You need to explicitly configure the build with
--enable-libx265.
16.17.1 Options
b
Sets target video bitrate.
bf
g
Set the GOP size.
keyint_min
Minimum GOP size.
refs
Number of reference frames each P-frame can use. The range is from 1-16.
preset
Set the x265 preset.
tune
Set the x265 tune parameter.
profile
Set profile restrictions.
crf
Set the quality for constant quality mode.
qp
Set constant quantization rate control method parameter.
qmin
Minimum quantizer scale.
qmax
Maximum quantizer scale.
qdiff
Maximum difference between quantizer scales.
qblur
Quantizer curve blur
qcomp
Quantizer curve compression factor
i_qfactor
b_qfactor
forced-idr
Normally, when forcing a I-frame type, the encoder can select any type
of I-frame. This option forces it to choose an IDR-frame.
udu_sei boolean
Import user data unregistered SEI if available into output. Default is 0 (off).
x265-params
Set x265 options using a list of key=value couples separated
by ":". See x265 --help for a list of options.
For example to specify libx265 encoding options with -x265-params:
ffmpeg -i input -c:v libx265 -x265-params crf=26:psy-rd=1 output.mp4
16.18 libxavs2
xavs2 AVS2-P2/IEEE1857.4 encoder wrapper.
This encoder requires the presence of the libxavs2 headers and library
during configuration. You need to explicitly configure the build with
--enable-libxavs2.
The following standard libavcodec options are used:
b / bit_rate
g / gop_size
bf / max_b_frames
The encoder also has its own specific options:
16.18.1 Options
lcu_row_threads
Set the number of parallel threads for rows from 1 to 8 (default 5).
initial_qp
Set the xavs2 quantization parameter from 1 to 63 (default 34). This is
used to set the initial qp for the first frame.
qp
Set the xavs2 quantization parameter from 1 to 63 (default 34). This is
used to set the qp value under constant-QP mode.
max_qp
Set the max qp for rate control from 1 to 63 (default 55).
min_qp
Set the min qp for rate control from 1 to 63 (default 20).
speed_level
Set the Speed level from 0 to 9 (default 0). Higher is better but slower.
log_level
Set the log level from -1 to 3 (default 0). -1: none, 0: error,
1: warning, 2: info, 3: debug.
xavs2-params
Set xavs2 options using a list of key=value couples separated
by ":".
For example to specify libxavs2 encoding options with -xavs2-params:
ffmpeg -i input -c:v libxavs2 -xavs2-params RdoqLevel=0 output.avs2
16.19 libxeve
eXtra-fast Essential Video Encoder (XEVE) MPEG-5 EVC encoder wrapper.
The xeve-equivalent options or values are listed in parentheses for easy migration.
This encoder requires the presence of the libxeve headers and library
during configuration. You need to explicitly configure the build with
--enable-libxeve.
Many libxeve encoder options are mapped to FFmpeg global codec options,
while unique encoder options are provided through private options.
Additionally the xeve-params private options allows one to pass a list
of key=value tuples as accepted by the libxeve parse_xeve_params function.
The xeve project website is at https://github.com/mpeg5/xeve.
16.19.1 Options
The following options are supported by the libxeve wrapper.
The xeve-equivalent options or values are listed in parentheses for easy migration.
To reduce the duplication of documentation, only the private options
and some others requiring special attention are documented here. For
the documentation of the undocumented generic options, see
the Codec Options chapter.
To get a more accurate and extensive documentation of the libxeve options,
invoke the command  xeve_app --help or consult the libxeve documentation.
b (bitrate)
Set target video bitrate in bits/s.
Note that FFmpeg’s b option is expressed in bits/s, while xeve’s bitrate is in kilobits/s.
bf (bframes)
Set the maximum number of B frames (1,3,7,15).
g (keyint)
Set the GOP size (I-picture period).
preset (preset)
Set the xeve preset.
Set the encoder preset value to determine encoding speed [fast, medium, slow, placebo]
tune (tune)
Set the encoder tune parameter [psnr, zerolatency]
profile (profile)
Set the encoder profile [0: baseline; 1: main]
crf (crf)
Set the quality for constant quality mode.
Constant rate factor <10..49> [default: 32]
qp (qp)
Set constant quantization rate control method parameter.
Quantization parameter qp <0..51> [default: 32]
threads (threads)
Force to use a specific number of threads
16.20 libxvid
Xvid MPEG-4 Part 2 encoder wrapper.
This encoder requires the presence of the libxvidcore headers and library
during configuration. You need to explicitly configure the build with
--enable-libxvid --enable-gpl.
The native mpeg4 encoder supports the MPEG-4 Part 2 format, so
users can encode to this format without this library.
16.20.1 Options
The following options are supported by the libxvid wrapper. Some of
the following options are listed but are not documented, and
correspond to shared codec options. See the Codec
Options chapter for their documentation. The other shared options
which are not listed have no effect for the libxvid encoder.
b
g
qmin
qmax
mpeg_quant
threads
bf
b_qfactor
b_qoffset
flags
Set specific encoding flags. Possible values:
‘mv4’
Use four motion vector by macroblock.
‘aic’
Enable high quality AC prediction.
‘gray’
Only encode grayscale.
‘qpel’
Enable quarter-pixel motion compensation.
‘cgop’
Enable closed GOP.
‘global_header’
Place global headers in extradata instead of every keyframe.
gmc
Enable the use of global motion compensation (GMC).  Default is 0
(disabled).
me_quality
Set motion estimation quality level. Possible values in decreasing order of
speed and increasing order of quality:
‘0’
Use no motion estimation (default).
‘1, 2’
Enable advanced diamond zonal search for 16x16 blocks and half-pixel
refinement for 16x16 blocks.
‘3, 4’
Enable all of the things described above, plus advanced diamond zonal
search for 8x8 blocks and half-pixel refinement for 8x8 blocks, also
enable motion estimation on chroma planes for P and B-frames.
‘5, 6’
Enable all of the things described above, plus extended 16x16 and 8x8
blocks search.
mbd
Set macroblock decision algorithm. Possible values in the increasing
order of quality:
‘simple’
Use macroblock comparing function algorithm (default).
‘bits’
Enable rate distortion-based half pixel and quarter pixel refinement for
16x16 blocks.
‘rd’
Enable all of the things described above, plus rate distortion-based
half pixel and quarter pixel refinement for 8x8 blocks, and rate
distortion-based search using square pattern.
lumi_aq
Enable lumi masking adaptive quantization when set to 1. Default is 0
(disabled).
variance_aq
Enable variance adaptive quantization when set to 1. Default is 0
(disabled).
When combined with lumi_aq, the resulting quality will not
be better than any of the two specified individually. In other
words, the resulting quality will be the worse one of the two
effects.
trellis
Set rate-distortion optimal quantization.
ssim
Set structural similarity (SSIM) displaying method. Possible values:
‘off’
Disable displaying of SSIM information.
‘avg’
Output average SSIM at the end of encoding to stdout. The format of
showing the average SSIM is:
Average SSIM: %f
For users who are not familiar with C, %f means a float number, or
a decimal (e.g. 0.939232).
‘frame’
Output both per-frame SSIM data during encoding and average SSIM at
the end of encoding to stdout. The format of per-frame information
is:
SSIM: avg: %1.3f min: %1.3f max: %1.3f
For users who are not familiar with C, %1.3f means a float number
rounded to 3 digits after the dot (e.g. 0.932).
ssim_acc
Set SSIM accuracy. Valid options are integers within the range of
0-4, while 0 gives the most accurate result and 4 computes the
fastest.
16.21 MediaFoundation
This provides wrappers to encoders (both audio and video) in the
MediaFoundation framework. It can access both SW and HW encoders.
Video encoders can take input in either of nv12 or yuv420p form
(some encoders support both, some support only either - in practice,
nv12 is the safer choice, especially among HW encoders).
16.22 Microsoft RLE
Microsoft RLE aka MSRLE encoder.
Only 8-bit palette mode supported.
Compatible with Windows 3.1 and Windows 95.
16.22.1 Options
g integer
Keyframe interval.
A keyframe is inserted at least every -g frames, sometimes sooner.
16.23 mpeg2
MPEG-2 video encoder.
16.23.1 Options
profile
Select the mpeg2 profile to encode:
‘422’
‘high’
‘ss’
Spatially Scalable
‘snr’
SNR Scalable
‘main’
‘simple’
level
Select the mpeg2 level to encode:
‘high’
‘high1440’
‘main’
‘low’
seq_disp_ext integer
Specifies if the encoder should write a sequence_display_extension to the
output.
-1
auto
Decide automatically to write it or not (this is the default) by checking if
the data to be written is different from the default or unspecified values.
0
never
Never write it.
1
always
Always write it.
video_format integer
Specifies the video_format written into the sequence display extension
indicating the source of the video pictures. The default is ‘unspecified’,
can be ‘component’, ‘pal’, ‘ntsc’, ‘secam’ or ‘mac’.
For maximum compatibility, use ‘component’.
a53cc boolean
Import closed captions (which must be ATSC compatible format) into output.
Default is 1 (on).
16.24 png
PNG image encoder.
16.24.1 Private options
dpi integer
Set physical density of pixels, in dots per inch, unset by default
dpm integer
Set physical density of pixels, in dots per meter, unset by default
16.25 ProRes
Apple ProRes encoder.
FFmpeg contains 2 ProRes encoders, the prores-aw and prores-ks encoder.
The used encoder can be chosen with the -vcodec option.
16.25.1 Private Options for prores-ks
profile integer
Select the ProRes profile to encode
‘proxy’
‘lt’
‘standard’
‘hq’
‘4444’
‘4444xq’
quant_mat integer
Select quantization matrix.
‘auto’
‘default’
‘proxy’
‘lt’
‘standard’
‘hq’
If set to auto, the matrix matching the profile will be picked.
If not set, the matrix providing the highest quality, default, will be
picked.
bits_per_mb integer
How many bits to allot for coding one macroblock. Different profiles use
between 200 and 2400 bits per macroblock, the maximum is 8000.
mbs_per_slice integer
Number of macroblocks in each slice (1-8); the default value (8)
should be good in almost all situations.
vendor string
Override the 4-byte vendor ID.
A custom vendor ID like apl0 would claim the stream was produced by
the Apple encoder.
alpha_bits integer
Specify number of bits for alpha component.
Possible values are 0, 8 and 16.
Use 0 to disable alpha plane coding.
16.25.2 Speed considerations
In the default mode of operation the encoder has to honor frame constraints
(i.e. not produce frames with size bigger than requested) while still making
output picture as good as possible.
A frame containing a lot of small details is harder to compress and the encoder
would spend more time searching for appropriate quantizers for each slice.
Setting a higher bits_per_mb limit will improve the speed.
For the fastest encoding speed set the qscale parameter (4 is the
recommended value) and do not set a size constraint.
16.26 QSV Encoders
The family of Intel QuickSync Video encoders (MPEG-2, H.264, HEVC, JPEG/MJPEG,
VP9, AV1)
16.26.1 Ratecontrol Method
The ratecontrol method is selected as follows:
When global_quality is specified, a quality-based mode is used.
Specifically this means either
- CQP - constant quantizer scale, when the qscale codec flag is
also set (the -qscale ffmpeg option).
- LA_ICQ - intelligent constant quality with lookahead, when the
look_ahead option is also set.
- ICQ – intelligent constant quality otherwise. For the ICQ modes, global
quality range is 1 to 51, with 1 being the best quality.
Otherwise when the desired average bitrate is specified with the b
option, a bitrate-based mode is used.
- LA - VBR with lookahead, when the look_ahead option is specified.
- VCM - video conferencing mode, when the vcm option is set.
- CBR - constant bitrate, when maxrate is specified and equal to
the average bitrate.
- VBR - variable bitrate, when maxrate is specified, but is higher
than the average bitrate.
- AVBR - average VBR mode, when maxrate is not specified, both
avbr_accuracy and avbr_convergence are set to non-zero. This
mode is available for H264 and HEVC on Windows.
Otherwise the default ratecontrol method CQP is used.
Note that depending on your system, a different mode than the one you specified
may be selected by the encoder. Set the verbosity level to verbose or
higher to see the actual settings used by the QSV runtime.
16.26.2 Global Options -> MSDK Options
Additional libavcodec global options are mapped to MSDK options as follows:
g/gop_size -> GopPicSize
bf/max_b_frames+1 -> GopRefDist
rc_init_occupancy/rc_initial_buffer_occupancy ->
InitialDelayInKB
slices -> NumSlice
refs -> NumRefFrame
b_strategy/b_frame_strategy -> BRefType
cgop/CLOSED_GOP codec flag -> GopOptFlag
For the CQP mode, the i_qfactor/i_qoffset and
b_qfactor/b_qoffset set the difference between QPP and QPI,
and QPP and QPB respectively.
Setting the coder option to the value vlc will make the H.264
encoder use CAVLC instead of CABAC.
16.26.3 Common Options
Following options are used by all qsv encoders.
async_depth
Specifies how many asynchronous operations an application performs
before the application explicitly synchronizes the result. If zero,
the value is not specified.
preset
This option itemizes a range of choices from veryfast (best speed) to veryslow
(best quality).
‘veryfast’
‘faster’
‘fast’
‘medium’
‘slow’
‘slower’
‘veryslow’
forced_idr
Forcing I frames as IDR frames.
low_power
For encoders set this flag to ON to reduce power consumption and GPU usage.
16.26.4 Runtime Options
Following options can be used durning qsv encoding.
global_quality
i_quant_factor
i_quant_offset
b_quant_factor
b_quant_offset
Supported in h264_qsv and hevc_qsv.
Change these value to reset qsv codec’s qp configuration.
max_frame_size
Supported in h264_qsv and hevc_qsv.
Change this value to reset qsv codec’s MaxFrameSize configuration.
gop_size
Change this value to reset qsv codec’s gop configuration.
int_ref_type
int_ref_cycle_size
int_ref_qp_delta
int_ref_cycle_dist
Supported in h264_qsv and hevc_qsv.
Change these value to reset qsv codec’s Intra Refresh configuration.
qmax
qmin
max_qp_i
min_qp_i
max_qp_p
min_qp_p
max_qp_b
min_qp_b
Supported in h264_qsv.
Change these value to reset qsv codec’s max/min qp configuration.
low_delay_brc
Supported in h264_qsv, hevc_qsv and av1_qsv.
Change this value to reset qsv codec’s low_delay_brc configuration.
framerate
Change this value to reset qsv codec’s framerate configuration.
bit_rate
rc_buffer_size
rc_initial_buffer_occupancy
rc_max_rate
Change these value to reset qsv codec’s bitrate control configuration.
pic_timing_sei
Supported in h264_qsv and hevc_qsv.
Change this value to reset qsv codec’s pic_timing_sei configuration.
qsv_params
Set QSV encoder parameters as a colon-separated list of key-value pairs.
The qsv_params should be formatted as key1=value1:key2=value2:....
These parameters are passed directly to the underlying Intel Quick Sync Video (QSV) encoder using the MFXSetParameter function.
Example:
ffmpeg -i input.mp4 -c:v h264_qsv -qsv_params "CodingOption1=1:CodingOption2=2" output.mp4
This option allows fine-grained control over various encoder-specific settings provided by the QSV encoder.
16.26.5 H264 options
These options are used by h264_qsv
extbrc
Extended bitrate control.
recovery_point_sei
Set this flag to insert the recovery point SEI message at the beginning of every
intra refresh cycle.
rdo
Enable rate distortion optimization.
max_frame_size
Maximum encoded frame size in bytes.
max_frame_size_i
Maximum encoded frame size for I frames in bytes. If this value is set as larger
than zero, then for I frames the value set by max_frame_size is ignored.
max_frame_size_p
Maximum encoded frame size for P frames in bytes. If this value is set as larger
than zero, then for P frames the value set by max_frame_size is ignored.
max_slice_size
Maximum encoded slice size in bytes.
bitrate_limit
Toggle bitrate limitations.
Modifies bitrate to be in the range imposed by the QSV encoder. Setting this
flag off may lead to violation of HRD conformance. Mind that specifying bitrate
below the QSV encoder range might significantly affect quality. If on this
option takes effect in non CQP modes: if bitrate is not in the range imposed
by the QSV encoder, it will be changed to be in the range.
mbbrc
Setting this flag enables macroblock level bitrate control that generally
improves subjective visual quality. Enabling this flag may have negative impact
on performance and objective visual quality metric.
low_delay_brc
Setting this flag turns on or off LowDelayBRC feautre in qsv plugin, which provides
more accurate bitrate control to minimize the variance of bitstream size frame
by frame. Value: -1-default 0-off 1-on
adaptive_i
This flag controls insertion of I frames by the QSV encoder. Turn ON this flag
to allow changing of frame type from P and B to I.
adaptive_b
This flag controls changing of frame type from B to P.
p_strategy
Enable P-pyramid: 0-default 1-simple 2-pyramid(bf need to be set to 0).
b_strategy
This option controls usage of B frames as reference.
dblk_idc
This option disable deblocking. It has value in range 0~2.
cavlc
If set, CAVLC is used; if unset, CABAC is used for encoding.
vcm
Video conferencing mode, please see ratecontrol method.
idr_interval
Distance (in I-frames) between IDR frames.
pic_timing_sei
Insert picture timing SEI with pic_struct_syntax element.
single_sei_nal_unit
Put all the SEI messages into one NALU.
max_dec_frame_buffering
Maximum number of frames buffered in the DPB.
look_ahead
Use VBR algorithm with look ahead.
look_ahead_depth
Depth of look ahead in number frames.
look_ahead_downsampling
Downscaling factor for the frames saved for the lookahead analysis.
‘unknown’
‘auto’
‘off’
‘2x’
‘4x’
int_ref_type
Specifies intra refresh type. The major goal of intra refresh is improvement of
error resilience without significant impact on encoded bitstream size caused by
I frames. The SDK encoder achieves this by encoding part of each frame in
refresh cycle using intra MBs. none means no refresh. vertical means
vertical refresh, by column of MBs. horizontal means horizontal refresh,
by rows of MBs. slice means horizontal refresh by slices without
overlapping. In case of slice, in_ref_cycle_size is ignored. To enable
intra refresh, B frame should be set to 0.
int_ref_cycle_size
Specifies number of pictures within refresh cycle starting from 2. 0 and 1 are
invalid values.
int_ref_qp_delta
Specifies QP difference for inserted intra MBs. This is signed value in
[-51, 51] range if target encoding bit-depth for luma samples is 8 and this
range is [-63, 63] for 10 bit-depth or [-75, 75] for 12 bit-depth respectively.
int_ref_cycle_dist
Distance between the beginnings of the intra-refresh cycles in frames.
profile
‘unknown’
‘baseline’
‘main’
‘high’
a53cc
Use A53 Closed Captions (if available).
aud
Insert the Access Unit Delimiter NAL.
mfmode
Multi-Frame Mode.
‘off’
‘auto’
repeat_pps
Repeat pps for every frame.
max_qp_i
Maximum video quantizer scale for I frame.
min_qp_i
Minimum video quantizer scale for I frame.
max_qp_p
Maximum video quantizer scale for P frame.
min_qp_p
Minimum video quantizer scale for P frame.
max_qp_b
Maximum video quantizer scale for B frame.
min_qp_b
Minimum video quantizer scale for B frame.
scenario
Provides a hint to encoder about the scenario for the encoding session.
‘unknown’
‘displayremoting’
‘videoconference’
‘archive’
‘livestreaming’
‘cameracapture’
‘videosurveillance’
‘gamestreaming’
‘remotegaming’
avbr_accuracy
Accuracy of the AVBR ratecontrol (unit of tenth of percent).
avbr_convergence
Convergence of the AVBR ratecontrol (unit of 100 frames)
The parameters avbr_accuracy and avbr_convergence are for the
average variable bitrate control (AVBR) algorithm.
The algorithm focuses on overall encoding quality while meeting the specified
bitrate, target_bitrate, within the accuracy range avbr_accuracy,
after a avbr_Convergence period. This method does not follow HRD and the
instant bitrate is not capped or padded.
skip_frame
Use per-frame metadata "qsv_skip_frame" to skip frame when encoding. This option
defines the usage of this metadata.
‘no_skip’
Frame skipping is disabled.
‘insert_dummy’
Encoder inserts into bitstream frame where all macroblocks are encoded as
skipped.
‘insert_nothing’
Similar to insert_dummy, but encoder inserts nothing into bitstream. The skipped
frames are still used in brc. For example, gop still include skipped frames, and
the frames after skipped frames will be larger in size.
‘brc_only’
skip_frame metadata indicates the number of missed frames before the current
frame.
16.26.6 HEVC Options
These options are used by hevc_qsv
extbrc
Extended bitrate control.
recovery_point_sei
Set this flag to insert the recovery point SEI message at the beginning of every
intra refresh cycle.
rdo
Enable rate distortion optimization.
max_frame_size
Maximum encoded frame size in bytes.
max_frame_size_i
Maximum encoded frame size for I frames in bytes. If this value is set as larger
than zero, then for I frames the value set by max_frame_size is ignored.
max_frame_size_p
Maximum encoded frame size for P frames in bytes. If this value is set as larger
than zero, then for P frames the value set by max_frame_size is ignored.
max_slice_size
Maximum encoded slice size in bytes.
mbbrc
Setting this flag enables macroblock level bitrate control that generally
improves subjective visual quality. Enabling this flag may have negative impact
on performance and objective visual quality metric.
low_delay_brc
Setting this flag turns on or off LowDelayBRC feautre in qsv plugin, which provides
more accurate bitrate control to minimize the variance of bitstream size frame
by frame. Value: -1-default 0-off 1-on
adaptive_i
This flag controls insertion of I frames by the QSV encoder. Turn ON this flag
to allow changing of frame type from P and B to I.
adaptive_b
This flag controls changing of frame type from B to P.
p_strategy
Enable P-pyramid: 0-default 1-simple 2-pyramid(bf need to be set to 0).
b_strategy
This option controls usage of B frames as reference.
dblk_idc
This option disable deblocking. It has value in range 0~2.
idr_interval
Distance (in I-frames) between IDR frames.
‘begin_only’
Output an IDR-frame only at the beginning of the stream.
load_plugin
A user plugin to load in an internal session.
‘none’
‘hevc_sw’
‘hevc_hw’
load_plugins
A :-separate list of hexadecimal plugin UIDs to load in
an internal session.
look_ahead_depth
Depth of look ahead in number frames, available when extbrc option is enabled.
profile
Set the encoding profile (scc requires libmfx >= 1.32).
‘unknown’
‘main’
‘main10’
‘mainsp’
‘rext’
‘scc’
tier
Set the encoding tier (only level >= 4 can support high tier).
This option only takes effect when the level option is specified.
‘main’
‘high’
gpb
1: GPB (generalized P/B frame)
0: regular P frame.
tile_cols
Number of columns for tiled encoding.
tile_rows
Number of rows for tiled encoding.
aud
Insert the Access Unit Delimiter NAL.
pic_timing_sei
Insert picture timing SEI with pic_struct_syntax element.
transform_skip
Turn this option ON to enable transformskip. It is supported on platform equal
or newer than ICL.
int_ref_type
Specifies intra refresh type. The major goal of intra refresh is improvement of
error resilience without significant impact on encoded bitstream size caused by
I frames. The SDK encoder achieves this by encoding part of each frame in
refresh cycle using intra MBs. none means no refresh. vertical means
vertical refresh, by column of MBs. horizontal means horizontal refresh,
by rows of MBs. slice means horizontal refresh by slices without
overlapping. In case of slice, in_ref_cycle_size is ignored. To enable
intra refresh, B frame should be set to 0.
int_ref_cycle_size
Specifies number of pictures within refresh cycle starting from 2. 0 and 1 are
invalid values.
int_ref_qp_delta
Specifies QP difference for inserted intra MBs. This is signed value in
[-51, 51] range if target encoding bit-depth for luma samples is 8 and this
range is [-63, 63] for 10 bit-depth or [-75, 75] for 12 bit-depth respectively.
int_ref_cycle_dist
Distance between the beginnings of the intra-refresh cycles in frames.
max_qp_i
Maximum video quantizer scale for I frame.
min_qp_i
Minimum video quantizer scale for I frame.
max_qp_p
Maximum video quantizer scale for P frame.
min_qp_p
Minimum video quantizer scale for P frame.
max_qp_b
Maximum video quantizer scale for B frame.
min_qp_b
Minimum video quantizer scale for B frame.
scenario
Provides a hint to encoder about the scenario for the encoding session.
‘unknown’
‘displayremoting’
‘videoconference’
‘archive’
‘livestreaming’
‘cameracapture’
‘videosurveillance’
‘gamestreaming’
‘remotegaming’
avbr_accuracy
Accuracy of the AVBR ratecontrol (unit of tenth of percent).
avbr_convergence
Convergence of the AVBR ratecontrol (unit of 100 frames)
The parameters avbr_accuracy and avbr_convergence are for the
average variable bitrate control (AVBR) algorithm.
The algorithm focuses on overall encoding quality while meeting the specified
bitrate, target_bitrate, within the accuracy range avbr_accuracy,
after a avbr_Convergence period. This method does not follow HRD and the
instant bitrate is not capped or padded.
skip_frame
Use per-frame metadata "qsv_skip_frame" to skip frame when encoding. This option
defines the usage of this metadata.
‘no_skip’
Frame skipping is disabled.
‘insert_dummy’
Encoder inserts into bitstream frame where all macroblocks are encoded as
skipped.
‘insert_nothing’
Similar to insert_dummy, but encoder inserts nothing into bitstream. The skipped
frames are still used in brc. For example, gop still include skipped frames, and
the frames after skipped frames will be larger in size.
‘brc_only’
skip_frame metadata indicates the number of missed frames before the current
frame.
16.26.7 MPEG2 Options
These options are used by mpeg2_qsv
profile
‘unknown’
‘simple’
‘main’
‘high’
16.26.8 VP9 Options
These options are used by vp9_qsv
profile
‘unknown’
‘profile0’
‘profile1’
‘profile2’
‘profile3’
tile_cols
Number of columns for tiled encoding (requires libmfx >= 1.29).
tile_rows
Number of rows for tiled encoding (requires libmfx  >= 1.29).
16.26.9 AV1 Options
These options are used by av1_qsv (requires libvpl).
profile
‘unknown’
‘main’
tile_cols
Number of columns for tiled encoding.
tile_rows
Number of rows for tiled encoding.
adaptive_i
This flag controls insertion of I frames by the QSV encoder. Turn ON this flag
to allow changing of frame type from P and B to I.
adaptive_b
This flag controls changing of frame type from B to P.
b_strategy
This option controls usage of B frames as reference.
extbrc
Extended bitrate control.
look_ahead_depth
Depth of look ahead in number frames, available when extbrc option is enabled.
low_delay_brc
Setting this flag turns on or off LowDelayBRC feautre in qsv plugin, which provides
more accurate bitrate control to minimize the variance of bitstream size frame
by frame. Value: -1-default 0-off 1-on
max_frame_size
Set the allowed max size in bytes for each frame. If the frame size exceeds
the limitation, encoder will adjust the QP value to control the frame size.
Invalid in CQP rate control mode.
max_frame_size_i
Maximum encoded frame size for I frames in bytes. If this value is set as larger
than zero, then for I frames the value set by max_frame_size is ignored.
max_frame_size_p
Maximum encoded frame size for P frames in bytes. If this value is set as larger
than zero, then for P frames the value set by max_frame_size is ignored.
16.27 snow
16.27.1 Options
iterative_dia_size
dia size for the iterative motion estimation
16.28 VAAPI encoders
Wrappers for hardware encoders accessible via VAAPI.
These encoders only accept input in VAAPI hardware surfaces.  If you have input
in software frames, use the hwupload filter to upload them to the GPU.
The following standard libavcodec options are used:
g / gop_size
bf / max_b_frames
profile
If not set, this will be determined automatically from the format of the input
frames and the profiles supported by the driver.
level
b / bit_rate
maxrate / rc_max_rate
bufsize / rc_buffer_size
rc_init_occupancy / rc_initial_buffer_occupancy
compression_level
Speed / quality tradeoff: higher values are faster / worse quality.
q / global_quality
Size / quality tradeoff: higher values are smaller / worse quality.
qmin
qmax
i_qfactor / i_quant_factor
i_qoffset / i_quant_offset
b_qfactor / b_quant_factor
b_qoffset / b_quant_offset
slices
All encoders support the following options:
low_power
Some drivers/platforms offer a second encoder for some codecs intended to use
less power than the default encoder; setting this option will attempt to use
that encoder.  Note that it may support a reduced feature set, so some other
options may not be available in this mode.
idr_interval
Set the number of normal intra frames between full-refresh (IDR) frames in
open-GOP mode.  The intra frames are still IRAPs, but will not include global
headers and may have non-decodable leading pictures.
b_depth
Set the B-frame reference depth.  When set to one (the default), all B-frames
will refer only to P- or I-frames.  When set to greater values multiple layers
of B-frames will be present, frames in each layer only referring to frames in
higher layers.
async_depth
Maximum processing parallelism. Increase this to improve single channel
performance. This option doesn’t work if driver doesn’t implement vaSyncBuffer
function. Please make sure there are enough hw_frames allocated if a large
number of async_depth is used.
max_frame_size
Set the allowed max size in bytes for each frame. If the frame size exceeds
the limitation, encoder will adjust the QP value to control the frame size.
Invalid in CQP rate control mode.
rc_mode
Set the rate control mode to use.  A given driver may only support a subset of
modes.
Possible modes:
auto
Choose the mode automatically based on driver support and the other options.
This is the default.
CQP
Constant-quality.
CBR
Constant-bitrate.
VBR
Variable-bitrate.
ICQ
Intelligent constant-quality.
QVBR
Quality-defined variable-bitrate.
AVBR
Average variable bitrate.
blbrc
Enable block level rate control, which assigns different bitrate block by block.
Invalid for CQP mode.
Each encoder also has its own specific options:
av1_vaapi
profile sets the value of seq_profile.
tier sets the value of seq_tier.
level sets the value of seq_level_idx.
tiles
Set the number of tiles to encode the input video with, as columns x rows.
(default is auto, which means use minimal tile column/row number).
tile_groups
Set tile groups number. All the tiles will be distributed as evenly as possible to
each tile group. (default is 1).
h264_vaapi
profile sets the value of profile_idc and the constraint_set*_flags.
level sets the value of level_idc.
coder
Set entropy encoder (default is cabac).  Possible values:
‘ac’
‘cabac’
Use CABAC.
‘vlc’
‘cavlc’
Use CAVLC.
aud
Include access unit delimiters in the stream (not included by default).
sei
Set SEI message types to include.
Some combination of the following values:
‘identifier’
Include a user_data_unregistered message containing information about
the encoder.
‘timing’
Include picture timing parameters (buffering_period and
pic_timing messages).
‘recovery_point’
Include recovery points where appropriate (recovery_point messages).
hevc_vaapi
profile and level set the values of
general_profile_idc and general_level_idc respectively.
aud
Include access unit delimiters in the stream (not included by default).
tier
Set general_tier_flag.  This may affect the level chosen for the stream
if it is not explicitly specified.
sei
Set SEI message types to include.
Some combination of the following values:
‘hdr’
Include HDR metadata if the input frames have it
(mastering_display_colour_volume and content_light_level
messages).
tiles
Set the number of tiles to encode the input video with, as columns x rows.
Larger numbers allow greater parallelism in both encoding and decoding, but
may decrease coding efficiency.
mjpeg_vaapi
Only baseline DCT encoding is supported.  The encoder always uses the standard
quantisation and huffman tables - global_quality scales the standard
quantisation table (range 1-100).
For YUV, 4:2:0, 4:2:2 and 4:4:4 subsampling modes are supported.  RGB is also
supported, and will create an RGB JPEG.
jfif
Include JFIF header in each frame (not included by default).
huffman
Include standard huffman tables (on by default).  Turning this off will save
a few hundred bytes in each output frame, but may lose compatibility with some
JPEG decoders which don’t fully handle MJPEG.
mpeg2_vaapi
profile and level set the value of profile_and_level_indication.
vp8_vaapi
B-frames are not supported.
global_quality sets the q_idx used for non-key frames (range 0-127).
loop_filter_level
loop_filter_sharpness
Manually set the loop filter parameters.
vp9_vaapi
global_quality sets the q_idx used for P-frames (range 0-255).
loop_filter_level
loop_filter_sharpness
Manually set the loop filter parameters.
B-frames are supported, but the output stream is always in encode order rather than display
order.  If B-frames are enabled, it may be necessary to use the vp9_raw_reorder
bitstream filter to modify the output stream to display frames in the correct order.
Only normal frames are produced - the vp9_superframe bitstream filter may be
required to produce a stream usable with all decoders.
16.29 vbn
Vizrt Binary Image encoder.
This format is used by the broadcast vendor Vizrt for quick texture streaming.
Advanced features of the format such as LZW compression of texture data or
generation of mipmaps are not supported.
16.29.1 Options
format string
Sets the texture compression used by the VBN file. Can be dxt1,
dxt5 or raw. Default is dxt5.
16.30 vc2
SMPTE VC-2 (previously BBC Dirac Pro). This codec was primarily aimed at
professional broadcasting but since it supports yuv420, yuv422 and yuv444 at
8 (limited range or full range), 10 or 12 bits, this makes it suitable for
other tasks which require low overhead and low compression (like screen
recording).
16.30.1 Options
b
Sets target video bitrate. Usually that’s around 1:6 of the uncompressed
video bitrate (e.g. for 1920x1080 50fps yuv422p10 that’s around 400Mbps). Higher
values (close to the uncompressed bitrate) turn on lossless compression mode.
field_order
Enables field coding when set (e.g. to tt - top field first) for interlaced
inputs. Should increase compression with interlaced content as it splits the
fields and encodes each separately.
wavelet_depth
Sets the total amount of wavelet transforms to apply, between 1 and 5 (default).
Lower values reduce compression and quality. Less capable decoders may not be
able to handle values of wavelet_depth over 3.
wavelet_type
Sets the transform type. Currently only 5_3 (LeGall) and 9_7
(Deslauriers-Dubuc)
are implemented, with 9_7 being the one with better compression and thus
is the default.
slice_width
slice_height
Sets the slice size for each slice. Larger values result in better compression.
For compatibility with other more limited decoders use slice_width of
32 and slice_height of 8.
tolerance
Sets the undershoot tolerance of the rate control system in percent. This is
to prevent an expensive search from being run.
qm
Sets the quantization matrix preset to use by default or when wavelet_depth
is set to 5
- default
Uses the default quantization matrix from the specifications, extended with
values for the fifth level. This provides a good balance between keeping detail
and omitting artifacts.
- flat
Use a completely zeroed out quantization matrix. This increases PSNR but might
reduce perception. Use in bogus benchmarks.
- color
Reduces detail but attempts to preserve color at extremely low bitrates.
17 Subtitles Encoders
17.1 dvdsub
This codec encodes the bitmap subtitle format that is used in DVDs.
Typically they are stored in VOBSUB file pairs (*.idx + *.sub),
and they can also be used in Matroska files.
17.1.1 Options
palette
Specify the global palette used by the bitmaps.
The format for this option is a string containing 16 24-bits hexadecimal
numbers (without 0x prefix) separated by commas, for example 0d00ee,
ee450d, 101010, eaeaea, 0ce60b, ec14ed, ebff0b, 0d617a, 7b7b7b, d1d1d1,
7b2a0e, 0d950c, 0f007b, cf0dec, cfa80c, 7c127b.
even_rows_fix
When set to 1, enable a work-around that makes the number of pixel rows
even in all subtitles.  This fixes a problem with some players that
cut off the bottom row if the number is odd.  The work-around just adds
a fully transparent row if needed.  The overhead is low, typically
one byte per subtitle on average.
By default, this work-around is disabled.
18 Bitstream Filters
When you configure your FFmpeg build, all the supported bitstream
filters are enabled by default. You can list all available ones using
the configure option --list-bsfs.
You can disable all the bitstream filters using the configure option
--disable-bsfs, and selectively enable any bitstream filter using
the option --enable-bsf=BSF, or you can disable a particular
bitstream filter using the option --disable-bsf=BSF.
The option -bsfs of the ff* tools will display the list of
all the supported bitstream filters included in your build.
The ff* tools have a -bsf option applied per stream, taking a
comma-separated list of filters, whose parameters follow the filter
name after a ’=’.
ffmpeg -i INPUT -c:v copy -bsf:v filter1[=opt1=str1:opt2=str2][,filter2] OUTPUT
Below is a description of the currently available bitstream filters,
with their parameters, if any.
18.1 aac_adtstoasc
Convert MPEG-2/4 AAC ADTS to an MPEG-4 Audio Specific Configuration
bitstream.
This filter creates an MPEG-4 AudioSpecificConfig from an MPEG-2/4
ADTS header and removes the ADTS header.
This filter is required for example when copying an AAC stream from a
raw ADTS AAC or an MPEG-TS container to MP4A-LATM, to an FLV file, or
to MOV/MP4 files and related formats such as 3GP or M4A. Please note
that it is auto-inserted for MP4A-LATM and MOV/MP4 and related formats.
18.2 av1_metadata
Modify metadata embedded in an AV1 stream.
td
Insert or remove temporal delimiter OBUs in all temporal units of the
stream.
‘insert’
Insert a TD at the beginning of every TU which does not already have one.
‘remove’
Remove the TD from the beginning of every TU which has one.
color_primaries
transfer_characteristics
matrix_coefficients
Set the color description fields in the stream (see AV1 section 6.4.2).
color_range
Set the color range in the stream (see AV1 section 6.4.2; note that
this cannot be set for streams using BT.709 primaries, sRGB transfer
characteristic and identity (RGB) matrix coefficients).
‘tv’
Limited range.
‘pc’
Full range.
chroma_sample_position
Set the chroma sample location in the stream (see AV1 section 6.4.2).
This can only be set for 4:2:0 streams.
‘vertical’
Left position (matching the default in MPEG-2 and H.264).
‘colocated’
Top-left position.
tick_rate
Set the tick rate (time_scale / num_units_in_display_tick) in
the timing info in the sequence header.
num_ticks_per_picture
Set the number of ticks in each picture, to indicate that the stream
has a fixed framerate.  Ignored if tick_rate is not also set.
delete_padding
Deletes Padding OBUs.
18.3 chomp
Remove zero padding at the end of a packet.
18.4 dca_core
Extract the core from a DCA/DTS stream, dropping extensions such as
DTS-HD.
18.5 dovi_rpu
Manipulate Dolby Vision metadata in a HEVC/AV1 bitstream, optionally enabling
metadata compression.
strip
If enabled, strip all Dolby Vision metadata (configuration record + RPU data
blocks) from the stream.
compression
Which compression level to enable.
‘none’
No metadata compression.
‘limited’
Limited metadata compression scheme. Should be compatible with most devices.
This is the default.
‘extended’
Extended metadata compression. Devices are not required to support this. Note
that this level currently behaves the same as ‘limited’ in libavcodec.
18.6 dump_extra
Add extradata to the beginning of the filtered packets except when
said packets already exactly begin with the extradata that is intended
to be added.
freq
The additional argument specifies which packets should be filtered.
It accepts the values:
‘k’
‘keyframe’
add extradata to all key packets
‘e’
‘all’
add extradata to all packets
If not specified it is assumed ‘k’.
For example the following ffmpeg command forces a global
header (thus disabling individual packet headers) in the H.264 packets
generated by the libx264 encoder, but corrects them by adding
the header stored in extradata to the key packets:
ffmpeg -i INPUT -map 0 -flags:v +global_header -c:v libx264 -bsf:v dump_extra out.ts
18.7 dv_error_marker
Blocks in DV which are marked as damaged are replaced by blocks of the specified color.
color
The color to replace damaged blocks by
sta
A 16 bit mask which specifies which of the 16 possible error status values are
to be replaced by colored blocks. 0xFFFE is the default which replaces all non 0
error status values.
‘ok’
No error, no concealment
‘err’
Error, No concealment
‘res’
Reserved
‘notok’
Error or concealment
‘notres’
Not reserved
‘Aa, Ba, Ca, Ab, Bb, Cb, A, B, C, a, b, erri, erru’
The specific error status code
see page 44-46 or section 5.5 of
http://web.archive.org/web/20060927044735/http://www.smpte.org/smpte_store/standards/pdf/s314m.pdf
18.8 eac3_core
Extract the core from a E-AC-3 stream, dropping extra channels.
18.9 extract_extradata
Extract the in-band extradata.
Certain codecs allow the long-term headers (e.g. MPEG-2 sequence headers,
or H.264/HEVC (VPS/)SPS/PPS) to be transmitted either "in-band" (i.e. as a part
of the bitstream containing the coded frames) or "out of band" (e.g. on the
container level). This latter form is called "extradata" in FFmpeg terminology.
This bitstream filter detects the in-band headers and makes them available as
extradata.
remove
When this option is enabled, the long-term headers are removed from the
bitstream after extraction.
18.10 filter_units
Remove units with types in or not in a given set from the stream.
pass_types
List of unit types or ranges of unit types to pass through while removing
all others.  This is specified as a ’|’-separated list of unit type values
or ranges of values with ’-’.
remove_types
Identical to pass_types, except the units in the given set
removed and all others passed through.
The types used by pass_types and remove_types correspond to NAL unit types
(nal_unit_type) in H.264, HEVC and H.266 (see Table 7-1 in the H.264
and HEVC specifications or Table 5 in the H.266 specification), to
marker values for JPEG (without 0xFF prefix) and to start codes without
start code prefix (i.e. the byte following the 0x000001) for MPEG-2.
For VP8 and VP9, every unit has type zero.
Extradata is unchanged by this transformation, but note that if the stream
contains inline parameter sets then the output may be unusable if they are
removed.
For example, to remove all non-VCL NAL units from an H.264 stream:
ffmpeg -i INPUT -c:v copy -bsf:v 'filter_units=pass_types=1-5' OUTPUT
To remove all AUDs, SEI and filler from an H.265 stream:
ffmpeg -i INPUT -c:v copy -bsf:v 'filter_units=remove_types=35|38-40' OUTPUT
To remove all user data from a MPEG-2 stream, including Closed Captions:
ffmpeg -i INPUT -c:v copy -bsf:v 'filter_units=remove_types=178' OUTPUT
To remove all SEI from a H264 stream, including Closed Captions:
ffmpeg -i INPUT -c:v copy -bsf:v 'filter_units=remove_types=6' OUTPUT
To remove all prefix and suffix SEI from a HEVC stream, including Closed Captions and dynamic HDR:
ffmpeg -i INPUT -c:v copy -bsf:v 'filter_units=remove_types=39|40' OUTPUT
18.11 hapqa_extract
Extract Rgb or Alpha part of an HAPQA file, without recompression, in order to create an HAPQ or an HAPAlphaOnly file.
texture
Specifies the texture to keep.
color
alpha
Convert HAPQA to HAPQ
ffmpeg -i hapqa_inputfile.mov -c copy -bsf:v hapqa_extract=texture=color -tag:v HapY -metadata:s:v:0 encoder="HAPQ" hapq_file.mov
Convert HAPQA to HAPAlphaOnly
ffmpeg -i hapqa_inputfile.mov -c copy -bsf:v hapqa_extract=texture=alpha -tag:v HapA -metadata:s:v:0 encoder="HAPAlpha Only" hapalphaonly_file.mov
18.12 h264_metadata
Modify metadata embedded in an H.264 stream.
aud
Insert or remove AUD NAL units in all access units of the stream.
‘pass’
‘insert’
‘remove’
Default is pass.
sample_aspect_ratio
Set the sample aspect ratio of the stream in the VUI parameters.
See H.264 table E-1.
overscan_appropriate_flag
Set whether the stream is suitable for display using overscan
or not (see H.264 section E.2.1).
video_format
video_full_range_flag
Set the video format in the stream (see H.264 section E.2.1 and
table E-2).
colour_primaries
transfer_characteristics
matrix_coefficients
Set the colour description in the stream (see H.264 section E.2.1
and tables E-3, E-4 and E-5).
chroma_sample_loc_type
Set the chroma sample location in the stream (see H.264 section
E.2.1 and figure E-1).
tick_rate
Set the tick rate (time_scale / num_units_in_tick) in the VUI
parameters.  This is the smallest time unit representable in the
stream, and in many cases represents the field rate of the stream
(double the frame rate).
fixed_frame_rate_flag
Set whether the stream has fixed framerate - typically this indicates
that the framerate is exactly half the tick rate, but the exact
meaning is dependent on interlacing and the picture structure (see
H.264 section E.2.1 and table E-6).
zero_new_constraint_set_flags
Zero constraint_set4_flag and constraint_set5_flag in the SPS. These
bits were reserved in a previous version of the H.264 spec, and thus
some hardware decoders require these to be zero. The result of zeroing
this is still a valid bitstream.
crop_left
crop_right
crop_top
crop_bottom
Set the frame cropping offsets in the SPS.  These values will replace
the current ones if the stream is already cropped.
These fields are set in pixels.  Note that some sizes may not be
representable if the chroma is subsampled or the stream is interlaced
(see H.264 section 7.4.2.1.1).
sei_user_data
Insert a string as SEI unregistered user data.  The argument must
be of the form UUID+string, where the UUID is as hex digits
possibly separated by hyphens, and the string can be anything.
For example, ‘086f3693-b7b3-4f2c-9653-21492feee5b8+hello’ will
insert the string “hello” associated with the given UUID.
delete_filler
Deletes both filler NAL units and filler SEI messages.
display_orientation
Insert, extract or remove Display orientation SEI messages.
See H.264 section D.1.27 and D.2.27 for syntax and semantics.
‘pass’
‘insert’
‘remove’
‘extract’
Default is pass.
Insert mode works in conjunction with rotate and flip options.
Any pre-existing Display orientation messages will be removed in insert or remove mode.
Extract mode attaches the display matrix to the packet as side data.
rotate
Set rotation in display orientation SEI (anticlockwise angle in degrees).
Range is -360 to +360. Default is NaN.
flip
Set flip in display orientation SEI.
‘horizontal’
‘vertical’
Default is unset.
level
Set the level in the SPS.  Refer to H.264 section A.3 and tables A-1
to A-5.
The argument must be the name of a level (for example, ‘4.2’), a
level_idc value (for example, ‘42’), or the special name ‘auto’
indicating that the filter should attempt to guess the level from the
input stream properties.
18.13 h264_mp4toannexb
Convert an H.264 bitstream from length prefixed mode to start code
prefixed mode (as defined in the Annex B of the ITU-T H.264
specification).
This is required by some streaming formats, typically the MPEG-2
transport stream format (muxer mpegts).
For example to remux an MP4 file containing an H.264 stream to mpegts
format with ffmpeg, you can use the command:
ffmpeg -i INPUT.mp4 -codec copy -bsf:v h264_mp4toannexb OUTPUT.ts
Please note that this filter is auto-inserted for MPEG-TS (muxer
mpegts) and raw H.264 (muxer h264) output formats.
18.14 h264_redundant_pps
This applies a specific fixup to some Blu-ray BDMV H264 streams
which contain redundant PPSs. The PPSs modify irrelevant parameters
of the stream, confusing other transformations which require
the correct extradata.
The encoder used on these impacted streams adds extra PPSs throughout
the stream, varying the initial QP and whether weighted prediction
was enabled. This causes issues after copying the stream into
a global header container, as the starting PPS is not suitable
for the rest of the stream. One side effect, for example,
is seeking will return garbled output until a new PPS appears.
This BSF removes the extra PPSs and rewrites the slice headers
such that the stream uses a single leading PPS in the global header,
which resolves the issue.
18.15 hevc_metadata
Modify metadata embedded in an HEVC stream.
aud
Insert or remove AUD NAL units in all access units of the stream.
‘insert’
‘remove’
sample_aspect_ratio
Set the sample aspect ratio in the stream in the VUI parameters.
video_format
video_full_range_flag
Set the video format in the stream (see H.265 section E.3.1 and
table E.2).
colour_primaries
transfer_characteristics
matrix_coefficients
Set the colour description in the stream (see H.265 section E.3.1
and tables E.3, E.4 and E.5).
chroma_sample_loc_type
Set the chroma sample location in the stream (see H.265 section
E.3.1 and figure E.1).
tick_rate
Set the tick rate in the VPS and VUI parameters (time_scale /
num_units_in_tick). Combined with num_ticks_poc_diff_one, this can
set a constant framerate in the stream.  Note that it is likely to be
overridden by container parameters when the stream is in a container.
num_ticks_poc_diff_one
Set poc_proportional_to_timing_flag in VPS and VUI and use this value
to set num_ticks_poc_diff_one_minus1 (see H.265 sections 7.4.3.1 and
E.3.1).  Ignored if tick_rate is not also set.
crop_left
crop_right
crop_top
crop_bottom
Set the conformance window cropping offsets in the SPS.  These values
will replace the current ones if the stream is already cropped.
These fields are set in pixels.  Note that some sizes may not be
representable if the chroma is subsampled (H.265 section 7.4.3.2.1).
width
height
Set width and height after crop.
level
Set the level in the VPS and SPS.  See H.265 section A.4 and tables
A.6 and A.7.
The argument must be the name of a level (for example, ‘5.1’), a
general_level_idc value (for example, ‘153’ for level 5.1),
or the special name ‘auto’ indicating that the filter should
attempt to guess the level from the input stream properties.
18.16 hevc_mp4toannexb
Convert an HEVC/H.265 bitstream from length prefixed mode to start code
prefixed mode (as defined in the Annex B of the ITU-T H.265
specification).
This is required by some streaming formats, typically the MPEG-2
transport stream format (muxer mpegts).
For example to remux an MP4 file containing an HEVC stream to mpegts
format with ffmpeg, you can use the command:
ffmpeg -i INPUT.mp4 -codec copy -bsf:v hevc_mp4toannexb OUTPUT.ts
Please note that this filter is auto-inserted for MPEG-TS (muxer
mpegts) and raw HEVC/H.265 (muxer h265 or
hevc) output formats.
18.17 imxdump
Modifies the bitstream to fit in MOV and to be usable by the Final Cut
Pro decoder. This filter only applies to the mpeg2video codec, and is
likely not needed for Final Cut Pro 7 and newer with the appropriate
-tag:v.
For example, to remux 30 MB/sec NTSC IMX to MOV:
ffmpeg -i input.mxf -c copy -bsf:v imxdump -tag:v mx3n output.mov
18.18 mjpeg2jpeg
Convert MJPEG/AVI1 packets to full JPEG/JFIF packets.
MJPEG is a video codec wherein each video frame is essentially a
JPEG image. The individual frames can be extracted without loss,
e.g. by
ffmpeg -i ../some_mjpeg.avi -c:v copy frames_%d.jpg
Unfortunately, these chunks are incomplete JPEG images, because
they lack the DHT segment required for decoding. Quoting from
http://www.digitalpreservation.gov/formats/fdd/fdd000063.shtml:
Avery Lee, writing in the rec.video.desktop newsgroup in 2001,
commented that "MJPEG, or at least the MJPEG in AVIs having the
MJPG fourcc, is restricted JPEG with a fixed – and *omitted* –
Huffman table. The JPEG must be YCbCr colorspace, it must be 4:2:2,
and it must use basic Huffman encoding, not arithmetic or
progressive. . . . You can indeed extract the MJPEG frames and
decode them with a regular JPEG decoder, but you have to prepend
the DHT segment to them, or else the decoder won’t have any idea
how to decompress the data. The exact table necessary is given in
the OpenDML spec."
This bitstream filter patches the header of frames extracted from an MJPEG
stream (carrying the AVI1 header ID and lacking a DHT segment) to
produce fully qualified JPEG images.
ffmpeg -i mjpeg-movie.avi -c:v copy -bsf:v mjpeg2jpeg frame_%d.jpg
exiftran -i -9 frame*.jpg
ffmpeg -i frame_%d.jpg -c:v copy rotated.avi
18.19 mjpegadump
Add an MJPEG A header to the bitstream, to enable decoding by
Quicktime.
18.20 mov2textsub
Extract a representable text file from MOV subtitles, stripping the
metadata header from each subtitle packet.
See also the text2movsub filter.
18.21 mpeg2_metadata
Modify metadata embedded in an MPEG-2 stream.
display_aspect_ratio
Set the display aspect ratio in the stream.
The following fixed values are supported:
4/3
16/9
221/100
Any other value will result in square pixels being signalled instead
(see H.262 section 6.3.3 and table 6-3).
frame_rate
Set the frame rate in the stream.  This is constructed from a table
of known values combined with a small multiplier and divisor - if
the supplied value is not exactly representable, the nearest
representable value will be used instead (see H.262 section 6.3.3
and table 6-4).
video_format
Set the video format in the stream (see H.262 section 6.3.6 and
table 6-6).
colour_primaries
transfer_characteristics
matrix_coefficients
Set the colour description in the stream (see H.262 section 6.3.6
and tables 6-7, 6-8 and 6-9).
18.22 mpeg4_unpack_bframes
Unpack DivX-style packed B-frames.
DivX-style packed B-frames are not valid MPEG-4 and were only a
workaround for the broken Video for Windows subsystem.
They use more space, can cause minor AV sync issues, require more
CPU power to decode (unless the player has some decoded picture queue
to compensate the 2,0,2,0 frame per packet style) and cause
trouble if copied into a standard container like mp4 or mpeg-ps/ts,
because MPEG-4 decoders may not be able to decode them, since they are
not valid MPEG-4.
For example to fix an AVI file containing an MPEG-4 stream with
DivX-style packed B-frames using ffmpeg, you can use the command:
ffmpeg -i INPUT.avi -codec copy -bsf:v mpeg4_unpack_bframes OUTPUT.avi
18.23 noise
Damages the contents of packets or simply drops them without damaging the
container. Can be used for fuzzing or testing error resilience/concealment.
Parameters:
amount
Accepts an expression whose evaluation per-packet determines how often bytes in that
packet will be modified. A value below 0 will result in a variable frequency.
Default is 0 which results in no modification. However, if neither amount nor drop is specified,
amount will be set to -1. See below for accepted variables.
drop
Accepts an expression evaluated per-packet whose value determines whether that packet is dropped.
Evaluation to a positive value results in the packet being dropped. Evaluation to a negative
value results in a variable chance of it being dropped, roughly inverse in proportion to the magnitude
of the value. Default is 0 which results in no drops. See below for accepted variables.
dropamount
Accepts a non-negative integer, which assigns a variable chance of it being dropped, roughly inverse
in proportion to the value. Default is 0 which results in no drops. This option is kept for backwards
compatibility and is equivalent to setting drop to a negative value with the same magnitude
i.e. dropamount=4 is the same as drop=-4. Ignored if drop is also specified.
Both amount and drop accept expressions containing the following variables:
‘n’
The index of the packet, starting from zero.
‘tb’
The timebase for packet timestamps.
‘pts’
Packet presentation timestamp.
‘dts’
Packet decoding timestamp.
‘nopts’
Constant representing AV_NOPTS_VALUE.
‘startpts’
First non-AV_NOPTS_VALUE PTS seen in the stream.
‘startdts’
First non-AV_NOPTS_VALUE DTS seen in the stream.
‘duration’
‘d’
Packet duration, in timebase units.
‘pos’
Packet position in input; may be -1 when unknown or not set.
‘size’
Packet size, in bytes.
‘key’
Whether packet is marked as a keyframe.
‘state’
A pseudo random integer, primarily derived from the content of packet payload.
18.23.1 Examples
Apply modification to every byte but don’t drop any packets.
ffmpeg -i INPUT -c copy -bsf noise=1 output.mkv
Drop every video packet not marked as a keyframe after timestamp 30s but do not
modify any of the remaining packets.
ffmpeg -i INPUT -c copy -bsf:v noise=drop='gt(t\,30)*not(key)' output.mkv
Drop one second of audio every 10 seconds and add some random noise to the rest.
ffmpeg -i INPUT -c copy -bsf:a noise=amount=-1:drop='between(mod(t\,10)\,9\,10)' output.mkv
18.24 null
This bitstream filter passes the packets through unchanged.
18.25 pcm_rechunk
Repacketize PCM audio to a fixed number of samples per packet or a fixed packet
rate per second. This is similar to the (ffmpeg-filters)asetnsamples audio
filter but works on audio packets instead of audio frames.
nb_out_samples, n
Set the number of samples per each output audio packet. The number is intended
as the number of samples per each channel. Default value is 1024.
pad, p
If set to 1, the filter will pad the last audio packet with silence, so that it
will contain the same number of samples (or roughly the same number of samples,
see frame_rate) as the previous ones. Default value is 1.
frame_rate, r
This option makes the filter output a fixed number of packets per second instead
of a fixed number of samples per packet. If the audio sample rate is not
divisible by the frame rate then the number of samples will not be constant but
will vary slightly so that each packet will start as close to the frame
boundary as possible. Using this option has precedence over nb_out_samples.
You can generate the well known 1602-1601-1602-1601-1602 pattern of 48kHz audio
for NTSC frame rate using the frame_rate option.
ffmpeg -f lavfi -i sine=r=48000:d=1 -c pcm_s16le -bsf pcm_rechunk=r=30000/1001 -f framecrc -
18.26 pgs_frame_merge
Merge a sequence of PGS Subtitle segments ending with an "end of display set"
segment into a single packet.
This is required by some containers that support PGS subtitles
(muxer matroska).
18.27 prores_metadata
Modify color property metadata embedded in prores stream.
color_primaries
Set the color primaries.
Available values are:
‘auto’
Keep the same color primaries property (default).
‘unknown’
‘bt709’
‘bt470bg’
BT601 625
‘smpte170m’
BT601 525
‘bt2020’
‘smpte431’
DCI P3
‘smpte432’
P3 D65
transfer_characteristics
Set the color transfer.
Available values are:
‘auto’
Keep the same transfer characteristics property (default).
‘unknown’
‘bt709’
BT 601, BT 709, BT 2020
‘smpte2084’
SMPTE ST 2084
‘arib-std-b67’
ARIB STD-B67
matrix_coefficients
Set the matrix coefficient.
Available values are:
‘auto’
Keep the same colorspace property (default).
‘unknown’
‘bt709’
‘smpte170m’
BT 601
‘bt2020nc’
Set Rec709 colorspace for each frame of the file
ffmpeg -i INPUT -c copy -bsf:v prores_metadata=color_primaries=bt709:color_trc=bt709:colorspace=bt709 output.mov
Set Hybrid Log-Gamma parameters for each frame of the file
ffmpeg -i INPUT -c copy -bsf:v prores_metadata=color_primaries=bt2020:color_trc=arib-std-b67:colorspace=bt2020nc output.mov
18.28 remove_extra
Remove extradata from packets.
It accepts the following parameter:
freq
Set which frame types to remove extradata from.
‘k’
Remove extradata from non-keyframes only.
‘keyframe’
Remove extradata from keyframes only.
‘e, all’
Remove extradata from all frames.
18.29 setts
Set PTS and DTS in packets.
It accepts the following parameters:
ts
pts
dts
Set expressions for PTS, DTS or both.
duration
Set expression for duration.
time_base
Set output time base.
The expressions are evaluated through the eval API and can contain the following
constants:
N
The count of the input packet. Starting from 0.
TS
The demux timestamp in input in case of ts or dts option or presentation
timestamp in case of pts option.
POS
The original position in the file of the packet, or undefined if undefined
for the current packet
DTS
The demux timestamp in input.
PTS
The presentation timestamp in input.
DURATION
The duration in input.
STARTDTS
The DTS of the first packet.
STARTPTS
The PTS of the first packet.
PREV_INDTS
The previous input DTS.
PREV_INPTS
The previous input PTS.
PREV_INDURATION
The previous input duration.
PREV_OUTDTS
The previous output DTS.
PREV_OUTPTS
The previous output PTS.
PREV_OUTDURATION
The previous output duration.
NEXT_DTS
The next input DTS.
NEXT_PTS
The next input PTS.
NEXT_DURATION
The next input duration.
TB
The timebase of stream packet belongs.
TB_OUT
The output timebase.
SR
The sample rate of stream packet belongs.
NOPTS
The AV_NOPTS_VALUE constant.
For example, to set PTS equal to DTS (not recommended if B-frames are involved):
ffmpeg -i INPUT -c:a copy -bsf:a setts=pts=DTS out.mkv
18.30 showinfo
Log basic packet information. Mainly useful for testing, debugging,
and development.
18.31 text2movsub
Convert text subtitles to MOV subtitles (as used by the mov_text
codec) with metadata headers.
See also the mov2textsub filter.
18.32 trace_headers
Log trace output containing all syntax elements in the coded stream
headers (everything above the level of individual coded blocks).
This can be useful for debugging low-level stream issues.
Supports AV1, H.264, H.265, (M)JPEG, MPEG-2 and VP9, but depending
on the build only a subset of these may be available.
18.33 truehd_core
Extract the core from a TrueHD stream, dropping ATMOS data.
18.34 vp9_metadata
Modify metadata embedded in a VP9 stream.
color_space
Set the color space value in the frame header.  Note that any frame
set to RGB will be implicitly set to PC range and that RGB is
incompatible with profiles 0 and 2.
‘unknown’
‘bt601’
‘bt709’
‘smpte170’
‘smpte240’
‘bt2020’
‘rgb’
color_range
Set the color range value in the frame header.  Note that any value
imposed by the color space will take precedence over this value.
‘tv’
‘pc’
18.35 vp9_superframe
Merge VP9 invisible (alt-ref) frames back into VP9 superframes. This
fixes merging of split/segmented VP9 streams where the alt-ref frame
was split from its visible counterpart.
18.36 vp9_superframe_split
Split VP9 superframes into single frames.
18.37 vp9_raw_reorder
Given a VP9 stream with correct timestamps but possibly out of order,
insert additional show-existing-frame packets to correct the ordering.