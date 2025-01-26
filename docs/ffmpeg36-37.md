36 Audio Filters
36.1 aap
36.2 acompressor
36.2.1 Commands
36.3 acontrast
36.4 acopy
36.5 acrossfade
36.5.1 Examples
36.6 acrossover
36.6.1 Examples
36.7 acrusher
36.7.1 Commands
36.8 acue
36.9 adeclick
36.10 adeclip
36.11 adecorrelate
36.12 adelay
36.12.1 Examples
36.13 adenorm
36.13.1 Commands
36.14 aderivative, aintegral
36.15 adrc
36.15.1 Commands
36.15.2 Examples
36.16 adynamicequalizer
36.16.1 Commands
36.17 adynamicsmooth
36.17.1 Commands
36.18 aecho
36.18.1 Examples
36.19 aemphasis
36.19.1 Commands
36.20 aeval
36.20.1 Examples
36.21 aexciter
36.21.1 Commands
36.22 afade
36.22.1 Commands
36.22.2 Examples
36.23 afftdn
36.23.1 Commands
36.23.2 Examples
36.24 afftfilt
36.24.1 Examples
36.25 afir
36.25.1 Examples
36.26 aformat
36.27 afreqshift
36.27.1 Commands
36.28 afwtdn
36.28.1 Commands
36.29 agate
36.29.1 Commands
36.30 aiir
36.30.1 Examples
36.31 alimiter
36.32 allpass
36.32.1 Commands
36.33 aloop
36.34 amerge
36.34.1 Examples
36.35 amix
36.35.1 Examples
36.35.2 Commands
36.36 amultiply
36.37 anequalizer
36.37.1 Examples
36.37.2 Commands
36.38 anlmdn
36.38.1 Commands
36.39 anlmf, anlms
36.39.1 Examples
36.39.2 Commands
36.40 anull
36.41 apad
36.41.1 Examples
36.42 aphaser
36.43 aphaseshift
36.43.1 Commands
36.44 apsnr
36.45 apsyclip
36.45.1 Commands
36.46 apulsator
36.47 aresample
36.47.1 Examples
36.48 areverse
36.48.1 Examples
36.49 arls
36.50 arnndn
36.50.1 Commands
36.51 asdr
36.52 asetnsamples
36.53 asetrate
36.54 ashowinfo
36.55 asisdr
36.56 asoftclip
36.56.1 Commands
36.57 aspectralstats
36.58 asr
36.59 astats
36.60 asubboost
36.60.1 Commands
36.61 asubcut
36.61.1 Commands
36.62 asupercut
36.62.1 Commands
36.63 asuperpass
36.63.1 Commands
36.64 asuperstop
36.64.1 Commands
36.65 atempo
36.65.1 Examples
36.65.2 Commands
36.66 atilt
36.66.1 Commands
36.67 atrim
36.68 axcorrelate
36.68.1 Examples
36.69 bandpass
36.69.1 Commands
36.70 bandreject
36.70.1 Commands
36.71 bass, lowshelf
36.71.1 Commands
36.72 biquad
36.72.1 Commands
36.73 bs2b
36.74 channelmap
36.74.1 Examples
36.75 channelsplit
36.75.1 Examples
36.76 chorus
36.76.1 Examples
36.77 compand
36.77.1 Examples
36.78 compensationdelay
36.78.1 Commands
36.79 crossfeed
36.79.1 Commands
36.80 crystalizer
36.80.1 Commands
36.81 dcshift
36.82 deesser
36.83 dialoguenhance
36.83.1 Commands
36.84 drmeter
36.85 dynaudnorm
36.85.1 Commands
36.86 earwax
36.87 equalizer
36.87.1 Examples
36.87.2 Commands
36.88 extrastereo
36.88.1 Commands
36.89 firequalizer
36.89.1 Examples
36.90 flanger
36.91 haas
36.92 hdcd
36.93 headphone
36.93.1 Examples
36.94 highpass
36.94.1 Commands
36.95 join
36.96 ladspa
36.96.1 Examples
36.96.2 Commands
36.97 loudnorm
36.98 lowpass
36.98.1 Examples
36.98.2 Commands
36.99 lv2
36.99.1 Examples
36.99.2 Commands
36.100 mcompand
36.101 pan
36.101.1 Mixing examples
36.101.2 Remapping examples
36.102 replaygain
36.103 resample
36.104 rubberband
36.104.1 Commands
36.105 sidechaincompress
36.105.1 Commands
36.105.2 Examples
36.106 sidechaingate
36.106.1 Commands
36.107 silencedetect
36.107.1 Examples
36.108 silenceremove
36.108.1 Examples
36.108.2 Commands
36.109 sofalizer
36.109.1 Examples
36.110 speechnorm
36.110.1 Commands
36.110.2 Examples
36.111 stereotools
36.111.1 Commands
36.111.2 Examples
36.112 stereowiden
36.112.1 Commands
36.113 superequalizer
36.114 surround
36.115 tiltshelf
36.115.1 Commands
36.116 treble, highshelf
36.116.1 Commands
36.117 tremolo
36.118 vibrato
36.119 virtualbass
36.120 volume
36.120.1 Commands
36.120.2 Examples
36.121 volumedetect
36.121.1 Examples
37 Audio Sources
37.1 abuffer
37.1.1 Examples
37.2 aevalsrc
37.2.1 Examples
37.3 afdelaysrc
37.4 afireqsrc
37.5 afirsrc
37.6 anullsrc
37.6.1 Examples
37.7 flite
37.7.1 Examples
37.8 anoisesrc
37.8.1 Examples
37.9 hilbert
37.10 sinc
37.11 sine
37.11.1 Examples


36 Audio Filters
When you configure your FFmpeg build, you can disable any of the
existing filters using --disable-filters.
The configure output will show the audio filters included in your
build.
Below is a description of the currently available audio filters.
36.1 aap
Apply Affine Projection algorithm to the first audio stream using the second audio stream.
This adaptive filter is used to estimate unknown audio based on multiple input audio samples.
Affine projection algorithm can make trade-offs between computation complexity with convergence speed.
A description of the accepted options follows.
order
Set the filter order.
projection
Set the projection order.
mu
Set the filter mu.
delta
Set the coefficient to initialize internal covariance matrix.
out_mode
Set the filter output samples. It accepts the following values:
i
Pass the 1st input.
d
Pass the 2nd input.
o
Pass difference between desired, 2nd input and error signal estimate.
n
Pass difference between input, 1st input and error signal estimate.
e
Pass error signal estimated samples.
Default value is o.
precision
Set which precision to use when processing samples.
auto
Auto pick internal sample format depending on other filters.
float
Always use single-floating point precision sample format.
double
Always use double-floating point precision sample format.
36.2 acompressor
A compressor is mainly used to reduce the dynamic range of a signal.
Especially modern music is mostly compressed at a high ratio to
improve the overall loudness. It’s done to get the highest attention
of a listener, "fatten" the sound and bring more "power" to the track.
If a signal is compressed too much it may sound dull or "dead"
afterwards or it may start to "pump" (which could be a powerful effect
but can also destroy a track completely).
The right compression is the key to reach a professional sound and is
the high art of mixing and mastering. Because of its complex settings
it may take a long time to get the right feeling for this kind of effect.
Compression is done by detecting the volume above a chosen level
threshold and dividing it by the factor set with ratio.
So if you set the threshold to -12dB and your signal reaches -6dB a ratio
of 2:1 will result in a signal at -9dB. Because an exact manipulation of
the signal would cause distortion of the waveform the reduction can be
levelled over the time. This is done by setting "Attack" and "Release".
attack determines how long the signal has to rise above the threshold
before any reduction will occur and release sets the time the signal
has to fall below the threshold to reduce the reduction again. Shorter signals
than the chosen attack time will be left untouched.
The overall reduction of the signal can be made up afterwards with the
makeup setting. So compressing the peaks of a signal about 6dB and
raising the makeup to this level results in a signal twice as loud than the
source. To gain a softer entry in the compression the knee flattens the
hard edge at the threshold in the range of the chosen decibels.
The filter accepts the following options:
level_in
Set input gain. Default is 1. Range is between 0.015625 and 64.
mode
Set mode of compressor operation. Can be upward or downward.
Default is downward.
threshold
If a signal of stream rises above this level it will affect the gain
reduction.
By default it is 0.125. Range is between 0.00097563 and 1.
ratio
Set a ratio by which the signal is reduced. 1:2 means that if the level
rose 4dB above the threshold, it will be only 2dB above after the reduction.
Default is 2. Range is between 1 and 20.
attack
Amount of milliseconds the signal has to rise above the threshold before gain
reduction starts. Default is 20. Range is between 0.01 and 2000.
release
Amount of milliseconds the signal has to fall below the threshold before
reduction is decreased again. Default is 250. Range is between 0.01 and 9000.
makeup
Set the amount by how much signal will be amplified after processing.
Default is 1. Range is from 1 to 64.
knee
Curve the sharp knee around the threshold to enter gain reduction more softly.
Default is 2.82843. Range is between 1 and 8.
link
Choose if the average level between all channels of input stream
or the louder(maximum) channel of input stream affects the
reduction. Default is average.
detection
Should the exact signal be taken in case of peak or an RMS one in case
of rms. Default is rms which is mostly smoother.
mix
How much to use compressed signal in output. Default is 1.
Range is between 0 and 1.
36.2.1 Commands
This filter supports the all above options as commands.
36.3 acontrast
Simple audio dynamic range compression/expansion filter.
The filter accepts the following options:
contrast
Set contrast. Default is 33. Allowed range is between 0 and 100.
36.4 acopy
Copy the input audio source unchanged to the output. This is mainly useful for
testing purposes.
36.5 acrossfade
Apply cross fade from one input audio stream to another input audio stream.
The cross fade is applied for specified duration near the end of first stream.
The filter accepts the following options:
nb_samples, ns
Specify the number of samples for which the cross fade effect has to last.
At the end of the cross fade effect the first input audio will be completely
silent. Default is 44100.
duration, d
Specify the duration of the cross fade effect. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
By default the duration is determined by nb_samples.
If set this option is used instead of nb_samples.
overlap, o
Should first stream end overlap with second stream start. Default is enabled.
curve1
Set curve for cross fade transition for first stream.
curve2
Set curve for cross fade transition for second stream.
For description of available curve types see afade filter description.
36.5.1 Examples
Cross fade from one input to another:
ffmpeg -i first.flac -i second.flac -filter_complex acrossfade=d=10:c1=exp:c2=exp output.flac
Cross fade from one input to another but without overlapping:
ffmpeg -i first.flac -i second.flac -filter_complex acrossfade=d=10:o=0:c1=exp:c2=exp output.flac
36.6 acrossover
Split audio stream into several bands.
This filter splits audio stream into two or more frequency ranges.
Summing all streams back will give flat output.
The filter accepts the following options:
split
Set split frequencies. Those must be positive and increasing.
order
Set filter order for each band split. This controls filter roll-off or steepness
of filter transfer function.
Available values are:
‘2nd’
12 dB per octave.
‘4th’
24 dB per octave.
‘6th’
36 dB per octave.
‘8th’
48 dB per octave.
‘10th’
60 dB per octave.
‘12th’
72 dB per octave.
‘14th’
84 dB per octave.
‘16th’
96 dB per octave.
‘18th’
108 dB per octave.
‘20th’
120 dB per octave.
Default is 4th.
level
Set input gain level. Allowed range is from 0 to 1. Default value is 1.
gains
Set output gain for each band. Default value is 1 for all bands.
precision
Set which precision to use when processing samples.
auto
Auto pick internal sample format depending on other filters.
float
Always use single-floating point precision sample format.
double
Always use double-floating point precision sample format.
Default value is auto.
36.6.1 Examples
Split input audio stream into two bands (low and high) with split frequency of 1500 Hz,
each band will be in separate stream:
ffmpeg -i in.flac -filter_complex 'acrossover=split=1500[LOW][HIGH]' -map '[LOW]' low.wav -map '[HIGH]' high.wav
Same as above, but with higher filter order:
ffmpeg -i in.flac -filter_complex 'acrossover=split=1500:order=8th[LOW][HIGH]' -map '[LOW]' low.wav -map '[HIGH]' high.wav
Same as above, but also with additional middle band (frequencies between 1500 and 8000):
ffmpeg -i in.flac -filter_complex 'acrossover=split=1500 8000:order=8th[LOW][MID][HIGH]' -map '[LOW]' low.wav -map '[MID]' mid.wav -map '[HIGH]' high.wav
36.7 acrusher
Reduce audio bit resolution.
This filter is bit crusher with enhanced functionality. A bit crusher
is used to audibly reduce number of bits an audio signal is sampled
with. This doesn’t change the bit depth at all, it just produces the
effect. Material reduced in bit depth sounds more harsh and "digital".
This filter is able to even round to continuous values instead of discrete
bit depths.
Additionally it has a D/C offset which results in different crushing of
the lower and the upper half of the signal.
An Anti-Aliasing setting is able to produce "softer" crushing sounds.
Another feature of this filter is the logarithmic mode.
This setting switches from linear distances between bits to logarithmic ones.
The result is a much more "natural" sounding crusher which doesn’t gate low
signals for example. The human ear has a logarithmic perception,
so this kind of crushing is much more pleasant.
Logarithmic crushing is also able to get anti-aliased.
The filter accepts the following options:
level_in
Set level in.
level_out
Set level out.
bits
Set bit reduction.
mix
Set mixing amount.
mode
Can be linear: lin or logarithmic: log.
dc
Set DC.
aa
Set anti-aliasing.
samples
Set sample reduction.
lfo
Enable LFO. By default disabled.
lforange
Set LFO range.
lforate
Set LFO rate.
36.7.1 Commands
This filter supports the all above options as commands.
36.8 acue
Delay audio filtering until a given wallclock timestamp. See the cue
filter.
36.9 adeclick
Remove impulsive noise from input audio.
Samples detected as impulsive noise are replaced by interpolated samples using
autoregressive modelling.
window, w
Set window size, in milliseconds. Allowed range is from 10 to
100. Default value is 55 milliseconds.
This sets size of window which will be processed at once.
overlap, o
Set window overlap, in percentage of window size. Allowed range is from
50 to 95. Default value is 75 percent.
Setting this to a very high value increases impulsive noise removal but makes
whole process much slower.
arorder, a
Set autoregression order, in percentage of window size. Allowed range is from
0 to 25. Default value is 2 percent. This option also
controls quality of interpolated samples using neighbour good samples.
threshold, t
Set threshold value. Allowed range is from 1 to 100.
Default value is 2.
This controls the strength of impulsive noise which is going to be removed.
The lower value, the more samples will be detected as impulsive noise.
burst, b
Set burst fusion, in percentage of window size. Allowed range is 0 to
10. Default value is 2.
If any two samples detected as noise are spaced less than this value then any
sample between those two samples will be also detected as noise.
method, m
Set overlap method.
It accepts the following values:
add, a
Select overlap-add method. Even not interpolated samples are slightly
changed with this method.
save, s
Select overlap-save method. Not interpolated samples remain unchanged.
Default value is a.
36.10 adeclip
Remove clipped samples from input audio.
Samples detected as clipped are replaced by interpolated samples using
autoregressive modelling.
window, w
Set window size, in milliseconds. Allowed range is from 10 to 100.
Default value is 55 milliseconds.
This sets size of window which will be processed at once.
overlap, o
Set window overlap, in percentage of window size. Allowed range is from 50
to 95. Default value is 75 percent.
arorder, a
Set autoregression order, in percentage of window size. Allowed range is from
0 to 25. Default value is 8 percent. This option also controls
quality of interpolated samples using neighbour good samples.
threshold, t
Set threshold value. Allowed range is from 1 to 100.
Default value is 10. Higher values make clip detection less aggressive.
hsize, n
Set size of histogram used to detect clips. Allowed range is from 100 to 9999.
Default value is 1000. Higher values make clip detection less aggressive.
method, m
Set overlap method.
It accepts the following values:
add, a
Select overlap-add method. Even not interpolated samples are slightly changed
with this method.
save, s
Select overlap-save method. Not interpolated samples remain unchanged.
Default value is a.
36.11 adecorrelate
Apply decorrelation to input audio stream.
The filter accepts the following options:
stages
Set decorrelation stages of filtering. Allowed
range is from 1 to 16. Default value is 6.
seed
Set random seed used for setting delay in samples across channels.
36.12 adelay
Delay one or more audio channels.
Samples in delayed channel are filled with silence.
The filter accepts the following option:
delays
Set list of delays in milliseconds for each channel separated by ’|’.
Unused delays will be silently ignored. If number of given delays is
smaller than number of channels all remaining channels will not be delayed.
If you want to delay exact number of samples, append ’S’ to number.
If you want instead to delay in seconds, append ’s’ to number.
all
Use last set delay for all remaining channels. By default is disabled.
This option if enabled changes how option delays is interpreted.
36.12.1 Examples
Delay first channel by 1.5 seconds, the third channel by 0.5 seconds and leave
the second channel (and any other channels that may be present) unchanged.
adelay=1500|0|500
Delay second channel by 500 samples, the third channel by 700 samples and leave
the first channel (and any other channels that may be present) unchanged.
adelay=0|500S|700S
Delay all channels by same number of samples:
adelay=delays=64S:all=1
36.13 adenorm
Remedy denormals in audio by adding extremely low-level noise.
This filter shall be placed before any filter that can produce denormals.
A description of the accepted parameters follows.
level
Set level of added noise in dB. Default is -351.
Allowed range is from -451 to -90.
type
Set type of added noise.
dc
Add DC signal.
ac
Add AC signal.
square
Add square signal.
pulse
Add pulse signal.
Default is dc.
36.13.1 Commands
This filter supports the all above options as commands.
36.14 aderivative, aintegral
Compute derivative/integral of audio stream.
Applying both filters one after another produces original audio.
36.15 adrc
Apply spectral dynamic range controller filter to input audio stream.
A description of the accepted options follows.
transfer
Set the transfer expression.
The expression can contain the following constants:
ch
current channel number
sn
current sample number
nb_channels
number of channels
t
timestamp expressed in seconds
sr
sample rate
p
current frequency power value, in dB
f
current frequency in Hz
Default value is p.
attack
Set the attack in milliseconds. Default is 50 milliseconds.
Allowed range is from 1 to 1000 milliseconds.
release
Set the release in milliseconds. Default is 100 milliseconds.
Allowed range is from 5 to 2000 milliseconds.
channels
Set which channels to filter, by default all channels in audio stream are filtered.
36.15.1 Commands
This filter supports the all above options as commands.
36.15.2 Examples
Apply spectral compression to all frequencies with threshold of -50 dB and 1:6 ratio:
adrc=transfer='if(gt(p,-50),-50+(p-(-50))/6,p)':attack=50:release=100
Similar to above but with 1:2 ratio and filtering only front center channel:
adrc=transfer='if(gt(p,-50),-50+(p-(-50))/2,p)':attack=50:release=100:channels=FC
Apply spectral noise gate to all frequencies with threshold of -85 dB and with short attack time and short release time:
adrc=transfer='if(lte(p,-85),p-800,p)':attack=1:release=5
Apply spectral expansion to all frequencies with threshold of -10 dB and 1:2 ratio:
adrc=transfer='if(lt(p,-10),-10+(p-(-10))*2,p)':attack=50:release=100
Apply limiter to max -60 dB to all frequencies, with attack of 2 ms and release of 10 ms:
adrc=transfer='min(p,-60)':attack=2:release=10
36.16 adynamicequalizer
Apply dynamic equalization to input audio stream.
A description of the accepted options follows.
threshold
Set the detection threshold used to trigger equalization.
Threshold detection is using detection filter.
Default value is 0. Allowed range is from 0 to 100.
dfrequency
Set the detection frequency in Hz used for detection filter used to trigger equalization.
Default value is 1000 Hz. Allowed range is between 2 and 1000000 Hz.
dqfactor
Set the detection resonance factor for detection filter used to trigger equalization.
Default value is 1. Allowed range is from 0.001 to 1000.
tfrequency
Set the target frequency of equalization filter.
Default value is 1000 Hz. Allowed range is between 2 and 1000000 Hz.
tqfactor
Set the target resonance factor for target equalization filter.
Default value is 1. Allowed range is from 0.001 to 1000.
attack
Set the amount of milliseconds the signal from detection has to rise above
the detection threshold before equalization starts.
Default is 20. Allowed range is between 1 and 2000.
release
Set the amount of milliseconds the signal from detection has to fall below the
detection threshold before equalization ends.
Default is 200. Allowed range is between 1 and 2000.
ratio
Set the ratio by which the equalization gain is raised.
Default is 1. Allowed range is between 0 and 30.
makeup
Set the makeup offset by which the equalization gain is raised.
Default is 0. Allowed range is between 0 and 100.
range
Set the max allowed cut/boost amount. Default is 50.
Allowed range is from 1 to 200.
mode
Set the mode of filter operation, can be one of the following:
‘listen’
Output only isolated detection signal.
‘cutbelow’
Cut frequencies below detection threshold.
‘cutabove’
Cut frequencies above detection threshold.
‘boostbelow’
Boost frequencies below detection threshold.
‘boostabove’
Boost frequencies above detection threshold.
Default mode is ‘cutbelow’.
dftype
Set the type of detection filter, can be one of the following:
‘bandpass’
‘lowpass’
‘highpass’
‘peak’
Default type is ‘bandpass’.
tftype
Set the type of target filter, can be one of the following:
‘bell’
‘lowshelf’
‘highshelf’
Default type is ‘bell’.
auto
Automatically gather threshold from detection filter. By default
is ‘disabled’.
This option is useful to detect threshold in certain time frame of
input audio stream, in such case option value is changed at runtime.
Available values are:
‘disabled’
Disable using automatically gathered threshold value.
‘off’
Stop picking threshold value.
‘on’
Start picking threshold value.
‘adaptive’
Adaptively pick threshold value, by calculating sliding window entropy.
precision
Set which precision to use when processing samples.
auto
Auto pick internal sample format depending on other filters.
float
Always use single-floating point precision sample format.
double
Always use double-floating point precision sample format.
36.16.1 Commands
This filter supports the all above options as commands.
36.17 adynamicsmooth
Apply dynamic smoothing to input audio stream.
A description of the accepted options follows.
sensitivity
Set an amount of sensitivity to frequency fluctations. Default is 2.
Allowed range is from 0 to 1e+06.
basefreq
Set a base frequency for smoothing. Default value is 22050.
Allowed range is from 2 to 1e+06.
36.17.1 Commands
This filter supports the all above options as commands.
36.18 aecho
Apply echoing to the input audio.
Echoes are reflected sound and can occur naturally amongst mountains
(and sometimes large buildings) when talking or shouting; digital echo
effects emulate this behaviour and are often used to help fill out the
sound of a single instrument or vocal. The time difference between the
original signal and the reflection is the delay, and the
loudness of the reflected signal is the decay.
Multiple echoes can have different delays and decays.
A description of the accepted parameters follows.
in_gain
Set input gain of reflected signal. Default is 0.6.
out_gain
Set output gain of reflected signal. Default is 0.3.
delays
Set list of time intervals in milliseconds between original signal and reflections
separated by ’|’. Allowed range for each delay is (0 - 90000.0].
Default is 1000.
decays
Set list of loudness of reflected signals separated by ’|’.
Allowed range for each decay is (0 - 1.0].
Default is 0.5.
36.18.1 Examples
Make it sound as if there are twice as many instruments as are actually playing:
aecho=0.8:0.88:60:0.4
If delay is very short, then it sounds like a (metallic) robot playing music:
aecho=0.8:0.88:6:0.4
A longer delay will sound like an open air concert in the mountains:
aecho=0.8:0.9:1000:0.3
Same as above but with one more mountain:
aecho=0.8:0.9:1000|1800:0.3|0.25
36.19 aemphasis
Audio emphasis filter creates or restores material directly taken from LPs or
emphased CDs with different filter curves. E.g. to store music on vinyl the
signal has to be altered by a filter first to even out the disadvantages of
this recording medium.
Once the material is played back the inverse filter has to be applied to
restore the distortion of the frequency response.
The filter accepts the following options:
level_in
Set input gain.
level_out
Set output gain.
mode
Set filter mode. For restoring material use reproduction mode, otherwise
use production mode. Default is reproduction mode.
type
Set filter type. Selects medium. Can be one of the following:
col
select Columbia.
emi
select EMI.
bsi
select BSI (78RPM).
riaa
select RIAA.
cd
select Compact Disc (CD).
50fm
select 50µs (FM).
75fm
select 75µs (FM).
50kf
select 50µs (FM-KF).
75kf
select 75µs (FM-KF).
36.19.1 Commands
This filter supports the all above options as commands.
36.20 aeval
Modify an audio signal according to the specified expressions.
This filter accepts one or more expressions (one for each channel),
which are evaluated and used to modify a corresponding audio signal.
It accepts the following parameters:
exprs
Set the ’|’-separated expressions list for each separate channel. If
the number of input channels is greater than the number of
expressions, the last specified expression is used for the remaining
output channels.
channel_layout, c
Set output channel layout. If not specified, the channel layout is
specified by the number of expressions. If set to ‘same’, it will
use by default the same input channel layout.
Each expression in exprs can contain the following constants and functions:
ch
channel number of the current expression
n
number of the evaluated sample, starting from 0
s
sample rate
t
time of the evaluated sample expressed in seconds
nb_in_channels
nb_out_channels
input and output number of channels
val(CH)
the value of input channel with number CH
Note: this filter is slow. For faster processing you should use a
dedicated filter.
36.20.1 Examples
Half volume:
aeval=val(ch)/2:c=same
Invert phase of the second channel:
aeval=val(0)|-val(1)
36.21 aexciter
An exciter is used to produce high sound that is not present in the
original signal. This is done by creating harmonic distortions of the
signal which are restricted in range and added to the original signal.
An Exciter raises the upper end of an audio signal without simply raising
the higher frequencies like an equalizer would do to create a more
"crisp" or "brilliant" sound.
The filter accepts the following options:
level_in
Set input level prior processing of signal.
Allowed range is from 0 to 64.
Default value is 1.
level_out
Set output level after processing of signal.
Allowed range is from 0 to 64.
Default value is 1.
amount
Set the amount of harmonics added to original signal.
Allowed range is from 0 to 64.
Default value is 1.
drive
Set the amount of newly created harmonics.
Allowed range is from 0.1 to 10.
Default value is 8.5.
blend
Set the octave of newly created harmonics.
Allowed range is from -10 to 10.
Default value is 0.
freq
Set the lower frequency limit of producing harmonics in Hz.
Allowed range is from 2000 to 12000 Hz.
Default is 7500 Hz.
ceil
Set the upper frequency limit of producing harmonics.
Allowed range is from 9999 to 20000 Hz.
If value is lower than 10000 Hz no limit is applied.
listen
Mute the original signal and output only added harmonics.
By default is disabled.
36.21.1 Commands
This filter supports the all above options as commands.
36.22 afade
Apply fade-in/out effect to input audio.
A description of the accepted parameters follows.
type, t
Specify the effect type, can be either in for fade-in, or
out for a fade-out effect. Default is in.
start_sample, ss
Specify the number of the start sample for starting to apply the fade
effect. Default is 0.
nb_samples, ns
Specify the number of samples for which the fade effect has to last. At
the end of the fade-in effect the output audio will have the same
volume as the input audio, at the end of the fade-out transition
the output audio will be silence. Default is 44100.
start_time, st
Specify the start time of the fade effect. Default is 0.
The value must be specified as a time duration; see
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
If set this option is used instead of start_sample.
duration, d
Specify the duration of the fade effect. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
At the end of the fade-in effect the output audio will have the same
volume as the input audio, at the end of the fade-out transition
the output audio will be silence.
By default the duration is determined by nb_samples.
If set this option is used instead of nb_samples.
curve
Set curve for fade transition.
It accepts the following values:
tri
select triangular, linear slope (default)
qsin
select quarter of sine wave
hsin
select half of sine wave
esin
select exponential sine wave
log
select logarithmic
ipar
select inverted parabola
qua
select quadratic
cub
select cubic
squ
select square root
cbr
select cubic root
par
select parabola
exp
select exponential
iqsin
select inverted quarter of sine wave
ihsin
select inverted half of sine wave
dese
select double-exponential seat
desi
select double-exponential sigmoid
losi
select logistic sigmoid
sinc
select sine cardinal function
isinc
select inverted sine cardinal function
quat
select quartic
quatr
select quartic root
qsin2
select squared quarter of sine wave
hsin2
select squared half of sine wave
nofade
no fade applied
silence
Set the initial gain for fade-in or final gain for fade-out.
Default value is 0.0.
unity
Set the initial gain for fade-out or final gain for fade-in.
Default value is 1.0.
36.22.1 Commands
This filter supports the all above options as commands.
36.22.2 Examples
Fade in first 15 seconds of audio:
afade=t=in:ss=0:d=15
Fade out last 25 seconds of a 900 seconds audio:
afade=t=out:st=875:d=25
36.23 afftdn
Denoise audio samples with FFT.
A description of the accepted parameters follows.
noise_reduction, nr
Set the noise reduction in dB, allowed range is 0.01 to 97.
Default value is 12 dB.
noise_floor, nf
Set the noise floor in dB, allowed range is -80 to -20.
Default value is -50 dB.
noise_type, nt
Set the noise type.
It accepts the following values:
white, w
Select white noise.
vinyl, v
Select vinyl noise.
shellac, s
Select shellac noise.
custom, c
Select custom noise, defined in bn option.
Default value is white noise.
band_noise, bn
Set custom band noise profile for every one of 15 bands.
Bands are separated by ’ ’ or ’|’.
residual_floor, rf
Set the residual floor in dB, allowed range is -80 to -20.
Default value is -38 dB.
track_noise, tn
Enable noise floor tracking. By default is disabled.
With this enabled, noise floor is automatically adjusted.
track_residual, tr
Enable residual tracking. By default is disabled.
output_mode, om
Set the output mode.
It accepts the following values:
input, i
Pass input unchanged.
output, o
Pass noise filtered out.
noise, n
Pass only noise.
Default value is output.
adaptivity, ad
Set the adaptivity factor, used how fast to adapt gains adjustments per
each frequency bin. Value 0 enables instant adaptation, while higher values
react much slower.
Allowed range is from 0 to 1. Default value is 0.5.
floor_offset, fo
Set the noise floor offset factor. This option is used to adjust offset applied to measured
noise floor. It is only effective when noise floor tracking is enabled.
Allowed range is from -2.0 to 2.0. Default value is 1.0.
noise_link, nl
Set the noise link used for multichannel audio.
It accepts the following values:
none
Use unchanged channel’s noise floor.
min
Use measured min noise floor of all channels.
max
Use measured max noise floor of all channels.
average
Use measured average noise floor of all channels.
Default value is min.
band_multiplier, bm
Set the band multiplier factor, used how much to spread bands across frequency bins.
Allowed range is from 0.2 to 5. Default value is 1.25.
sample_noise, sn
Toggle capturing and measurement of noise profile from input audio.
It accepts the following values:
start, begin
Start sample noise capture.
stop, end
Stop sample noise capture and measure new noise band profile.
Default value is none.
gain_smooth, gs
Set gain smooth spatial radius, used to smooth gains applied to each frequency bin.
Useful to reduce random music noise artefacts.
Higher values increases smoothing of gains.
Allowed range is from 0 to 50.
Default value is 0.
36.23.1 Commands
This filter supports the some above mentioned options as commands.
36.23.2 Examples
Reduce white noise by 10dB, and use previously measured noise floor of -40dB:
afftdn=nr=10:nf=-40
Reduce white noise by 10dB, also set initial noise floor to -80dB and enable automatic
tracking of noise floor so noise floor will gradually change during processing:
afftdn=nr=10:nf=-80:tn=1
Reduce noise by 20dB, using noise floor of -40dB and using commands to take noise profile
of first 0.4 seconds of input audio:
asendcmd=0.0 afftdn sn start,asendcmd=0.4 afftdn sn stop,afftdn=nr=20:nf=-40
36.24 afftfilt
Apply arbitrary expressions to samples in frequency domain.
real
Set frequency domain real expression for each separate channel separated
by ’|’. Default is "re".
If the number of input channels is greater than the number of
expressions, the last specified expression is used for the remaining
output channels.
imag
Set frequency domain imaginary expression for each separate channel
separated by ’|’. Default is "im".
Each expression in real and imag can contain the following
constants and functions:
sr
sample rate
b
current frequency bin number
nb
number of available bins
ch
channel number of the current expression
chs
number of channels
pts
current frame pts
re
current real part of frequency bin of current channel
im
current imaginary part of frequency bin of current channel
real(b, ch)
Return the value of real part of frequency bin at location (bin,channel)
imag(b, ch)
Return the value of imaginary part of frequency bin at location (bin,channel)
win_size
Set window size. Allowed range is from 16 to 131072.
Default is 4096
win_func
Set window function.
It accepts the following values:
‘rect’
‘bartlett’
‘hann, hanning’
‘hamming’
‘blackman’
‘welch’
‘flattop’
‘bharris’
‘bnuttall’
‘bhann’
‘sine’
‘nuttall’
‘lanczos’
‘gauss’
‘tukey’
‘dolph’
‘cauchy’
‘parzen’
‘poisson’
‘bohman’
‘kaiser’
Default is hann.
overlap
Set window overlap. If set to 1, the recommended overlap for selected
window function will be picked. Default is 0.75.
36.24.1 Examples
Leave almost only low frequencies in audio:
afftfilt="'real=re * (1-clip((b/nb)*b,0,1))':imag='im * (1-clip((b/nb)*b,0,1))'"
Apply robotize effect:
afftfilt="real='hypot(re,im)*sin(0)':imag='hypot(re,im)*cos(0)':win_size=512:overlap=0.75"
Apply whisper effect:
afftfilt="real='hypot(re,im)*cos((random(0)*2-1)*2*3.14)':imag='hypot(re,im)*sin((random(1)*2-1)*2*3.14)':win_size=128:overlap=0.8"
Apply phase shift:
afftfilt="real=re*cos(1)-im*sin(1):imag=re*sin(1)+im*cos(1)"
36.25 afir
Apply an arbitrary Finite Impulse Response filter.
This filter is designed for applying long FIR filters,
up to 60 seconds long.
It can be used as component for digital crossover filters,
room equalization, cross talk cancellation, wavefield synthesis,
auralization, ambiophonics, ambisonics and spatialization.
This filter uses the streams higher than first one as FIR coefficients.
If the non-first stream holds a single channel, it will be used
for all input channels in the first stream, otherwise
the number of channels in the non-first stream must be same as
the number of channels in the first stream.
It accepts the following parameters:
dry
Set dry gain. This sets input gain.
wet
Set wet gain. This sets final output gain.
length
Set Impulse Response filter length. Default is 1, which means whole IR is processed.
gtype
This option is deprecated, and does nothing.
irnorm
Set norm to be applied to IR coefficients before filtering.
Allowed range is from -1 to 2.
IR coefficients are normalized with calculated vector norm set by this option.
For negative values, no norm is calculated, and IR coefficients are not modified at all.
Default is 1.
irlink
For multichannel IR if this option is set to true, all IR channels will be
normalized with maximal measured gain of all IR channels coefficients as set by irnorm option.
When disabled, all IR coefficients in each IR channel will be normalized independently.
Default is true.
irgain
Set gain to be applied to IR coefficients before filtering.
Allowed range is 0 to 1. This gain is applied after any gain applied with irnorm option.
irfmt
Set format of IR stream. Can be mono or input.
Default is input.
maxir
Set max allowed Impulse Response filter duration in seconds. Default is 30 seconds.
Allowed range is 0.1 to 60 seconds.
response
This option is deprecated, and does nothing.
channel
This option is deprecated, and does nothing.
size
This option is deprecated, and does nothing.
rate
This option is deprecated, and does nothing.
minp
Set minimal partition size used for convolution. Default is 8192.
Allowed range is from 1 to 65536.
Lower values decreases latency at cost of higher CPU usage.
maxp
Set maximal partition size used for convolution. Default is 8192.
Allowed range is from 8 to 65536.
Lower values may increase CPU usage.
nbirs
Set number of input impulse responses streams which will be switchable at runtime.
Allowed range is from 1 to 32. Default is 1.
ir
Set IR stream which will be used for convolution, starting from 0, should always be
lower than supplied value by nbirs option. Default is 0.
This option can be changed at runtime via commands.
precision
Set which precision to use when processing samples.
auto
Auto pick internal sample format depending on other filters.
float
Always use single-floating point precision sample format.
double
Always use double-floating point precision sample format.
Default value is auto.
irload
Set when to load IR stream. Can be init or access.
First one load and prepares all IRs on initialization, second one
once on first access of specific IR.
Default is init.
36.25.1 Examples
Apply reverb to stream using mono IR file as second input, complete command using ffmpeg:
ffmpeg -i input.wav -i middle_tunnel_1way_mono.wav -lavfi afir output.wav
Apply true stereo processing given input stereo stream, and two stereo impulse responses for left and right channel,
the impulse response files are files with names l_ir.wav and r_ir.wav, and setting irnorm option value:
"pan=4C|c0=FL|c1=FL|c2=FR|c3=FR[a];amovie=l_ir.wav[LIR];amovie=r_ir.wav[RIR];[LIR][RIR]amerge[ir];[a][ir]afir=irfmt=input:irnorm=1.2,pan=stereo|FL<c0+c2|FR<c1+c3"
Similar to above example, but with irgain explicitly set to estimated value and with irnorm disabled:
"pan=4C|c0=FL|c1=FL|c2=FR|c3=FR[a];amovie=l_ir.wav[LIR];amovie=r_ir.wav[RIR];[LIR][RIR]amerge[ir];[a][ir]afir=irfmt=input:irgain=-5dB:irnom=-1,pan=stereo|FL<c0+c2|FR<c1+c3"
36.26 aformat
Set output format constraints for the input audio. The framework will
negotiate the most appropriate format to minimize conversions.
It accepts the following parameters:
sample_fmts, f
A ’|’-separated list of requested sample formats.
sample_rates, r
A ’|’-separated list of requested sample rates.
channel_layouts, cl
A ’|’-separated list of requested channel layouts.
See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual
for the required syntax.
If a parameter is omitted, all values are allowed.
Force the output to either unsigned 8-bit or signed 16-bit stereo
aformat=sample_fmts=u8|s16:channel_layouts=stereo
36.27 afreqshift
Apply frequency shift to input audio samples.
The filter accepts the following options:
shift
Specify frequency shift. Allowed range is -INT_MAX to INT_MAX.
Default value is 0.0.
level
Set output gain applied to final output. Allowed range is from 0.0 to 1.0.
Default value is 1.0.
order
Set filter order used for filtering. Allowed range is from 1 to 16.
Default value is 8.
36.27.1 Commands
This filter supports the all above options as commands.
36.28 afwtdn
Reduce broadband noise from input samples using Wavelets.
A description of the accepted options follows.
sigma
Set the noise sigma, allowed range is from 0 to 1.
Default value is 0.
This option controls strength of denoising applied to input samples.
Most useful way to set this option is via decibels, eg. -45dB.
levels
Set the number of wavelet levels of decomposition.
Allowed range is from 1 to 12.
Default value is 10.
Setting this too low make denoising performance very poor.
wavet
Set wavelet type for decomposition of input frame.
They are sorted by number of coefficients, from lowest to highest.
More coefficients means worse filtering speed, but overall better quality.
Available wavelets are:
‘sym2’
‘sym4’
‘rbior68’
‘deb10’
‘sym10’
‘coif5’
‘bl3’
percent
Set percent of full denoising. Allowed range is from 0 to 100 percent.
Default value is 85 percent or partial denoising.
profile
If enabled, first input frame will be used as noise profile.
If first frame samples contain non-noise performance will be very poor.
adaptive
If enabled, input frames are analyzed for presence of noise.
If noise is detected with high possibility then input frame profile will be
used for processing following frames, until new noise frame is detected.
samples
Set size of single frame in number of samples. Allowed range is from 512 to
65536. Default frame size is 8192 samples.
softness
Set softness applied inside thresholding function. Allowed range is from 0 to
10. Default softness is 1.
36.28.1 Commands
This filter supports the all above options as commands.
36.29 agate
A gate is mainly used to reduce lower parts of a signal. This kind of signal
processing reduces disturbing noise between useful signals.
Gating is done by detecting the volume below a chosen level threshold
and dividing it by the factor set with ratio. The bottom of the noise
floor is set via range. Because an exact manipulation of the signal
would cause distortion of the waveform the reduction can be levelled over
time. This is done by setting attack and release.
attack determines how long the signal has to fall below the threshold
before any reduction will occur and release sets the time the signal
has to rise above the threshold to reduce the reduction again.
Shorter signals than the chosen attack time will be left untouched.
level_in
Set input level before filtering.
Default is 1. Allowed range is from 0.015625 to 64.
mode
Set the mode of operation. Can be upward or downward.
Default is downward. If set to upward mode, higher parts of signal
will be amplified, expanding dynamic range in upward direction.
Otherwise, in case of downward lower parts of signal will be reduced.
range
Set the level of gain reduction when the signal is below the threshold.
Default is 0.06125. Allowed range is from 0 to 1.
Setting this to 0 disables reduction and then filter behaves like expander.
threshold
If a signal rises above this level the gain reduction is released.
Default is 0.125. Allowed range is from 0 to 1.
ratio
Set a ratio by which the signal is reduced.
Default is 2. Allowed range is from 1 to 9000.
attack
Amount of milliseconds the signal has to rise above the threshold before gain
reduction stops.
Default is 20 milliseconds. Allowed range is from 0.01 to 9000.
release
Amount of milliseconds the signal has to fall below the threshold before the
reduction is increased again. Default is 250 milliseconds.
Allowed range is from 0.01 to 9000.
makeup
Set amount of amplification of signal after processing.
Default is 1. Allowed range is from 1 to 64.
knee
Curve the sharp knee around the threshold to enter gain reduction more softly.
Default is 2.828427125. Allowed range is from 1 to 8.
detection
Choose if exact signal should be taken for detection or an RMS like one.
Default is rms. Can be peak or rms.
link
Choose if the average level between all channels or the louder channel affects
the reduction.
Default is average. Can be average or maximum.
36.29.1 Commands
This filter supports the all above options as commands.
36.30 aiir
Apply an arbitrary Infinite Impulse Response filter.
It accepts the following parameters:
zeros, z
Set B/numerator/zeros/reflection coefficients.
poles, p
Set A/denominator/poles/ladder coefficients.
gains, k
Set channels gains.
dry_gain
Set input gain.
wet_gain
Set output gain.
format, f
Set coefficients format.
‘ll’
lattice-ladder function
‘sf’
analog transfer function
‘tf’
digital transfer function
‘zp’
Z-plane zeros/poles, cartesian (default)
‘pr’
Z-plane zeros/poles, polar radians
‘pd’
Z-plane zeros/poles, polar degrees
‘sp’
S-plane zeros/poles
process, r
Set type of processing.
‘d’
direct processing
‘s’
serial processing
‘p’
parallel processing
precision, e
Set filtering precision.
‘dbl’
double-precision floating-point (default)
‘flt’
single-precision floating-point
‘i32’
32-bit integers
‘i16’
16-bit integers
normalize, n
Normalize filter coefficients, by default is enabled.
Enabling it will normalize magnitude response at DC to 0dB.
mix
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
response
Show IR frequency response, magnitude(magenta), phase(green) and group delay(yellow) in additional video stream.
By default it is disabled.
channel
Set for which IR channel to display frequency response. By default is first channel
displayed. This option is used only when response is enabled.
size
Set video stream size. This option is used only when response is enabled.
Coefficients in tf and sf format are separated by spaces and are in ascending
order.
Coefficients in zp format are separated by spaces and order of coefficients
doesn’t matter. Coefficients in zp format are complex numbers with i
imaginary unit.
Different coefficients and gains can be provided for every channel, in such case
use ’|’ to separate coefficients or gains. Last provided coefficients will be
used for all remaining channels.
36.30.1 Examples
Apply 2 pole elliptic notch at around 5000Hz for 48000 Hz sample rate:
aiir=k=1:z=7.957584807809675810E-1 -2.575128568908332300 3.674839853930788710 -2.57512875289799137 7.957586296317130880E-1:p=1 -2.86950072432325953 3.63022088054647218 -2.28075678147272232 6.361362326477423500E-1:f=tf:r=d
Same as above but in zp format:
aiir=k=0.79575848078096756:z=0.80918701+0.58773007i 0.80918701-0.58773007i 0.80884700+0.58784055i 0.80884700-0.58784055i:p=0.63892345+0.59951235i 0.63892345-0.59951235i 0.79582691+0.44198673i 0.79582691-0.44198673i:f=zp:r=s
Apply 3-rd order analog normalized Butterworth low-pass filter, using analog transfer function format:
aiir=z=1.3057 0 0 0:p=1.3057 2.3892 2.1860 1:f=sf:r=d
36.31 alimiter
The limiter prevents an input signal from rising over a desired threshold.
This limiter uses lookahead technology to prevent your signal from distorting.
It means that there is a small delay after the signal is processed. Keep in mind
that the delay it produces is the attack time you set.
The filter accepts the following options:
level_in
Set input gain. Default is 1.
level_out
Set output gain. Default is 1.
limit
Don’t let signals above this level pass the limiter. Default is 1.
attack
The limiter will reach its attenuation level in this amount of time in
milliseconds. Default is 5 milliseconds.
release
Come back from limiting to attenuation 1.0 in this amount of milliseconds.
Default is 50 milliseconds.
asc
When gain reduction is always needed ASC takes care of releasing to an
average reduction level rather than reaching a reduction of 0 in the release
time.
asc_level
Select how much the release time is affected by ASC, 0 means nearly no changes
in release time while 1 produces higher release times.
level
Auto level output signal. Default is enabled.
This normalizes audio back to 0dB if enabled.
latency
Compensate the delay introduced by using the lookahead buffer set with attack
parameter. Also flush the valid audio data in the lookahead buffer when the
stream hits EOF.
Depending on picked setting it is recommended to upsample input 2x or 4x times
with aresample before applying this filter.
36.32 allpass
Apply a two-pole all-pass filter with central frequency (in Hz)
frequency, and filter-width width.
An all-pass filter changes the audio’s frequency to phase relationship
without changing its frequency to amplitude relationship.
The filter accepts the following options:
frequency, f
Set frequency in Hz.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Specify the band-width of a filter in width_type units.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
order, o
Set the filter order, can be 1 or 2. Default is 2.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
36.32.1 Commands
This filter supports the following commands:
frequency, f
Change allpass frequency.
Syntax for the command is : "frequency"
width_type, t
Change allpass width_type.
Syntax for the command is : "width_type"
width, w
Change allpass width.
Syntax for the command is : "width"
mix, m
Change allpass mix.
Syntax for the command is : "mix"
36.33 aloop
Loop audio samples.
The filter accepts the following options:
loop
Set the number of loops. Setting this value to -1 will result in infinite loops.
Default is 0.
size
Set maximal number of samples. Default is 0.
start
Set first sample of loop. Default is 0.
time
Set the time of loop start in seconds.
Only used if option named start is set to -1.
36.34 amerge
Merge two or more audio streams into a single multi-channel stream.
The filter accepts the following options:
inputs
Set the number of inputs. Default is 2.
If the channel layouts of the inputs are disjoint, and therefore compatible,
the channel layout of the output will be set accordingly and the channels
will be reordered as necessary. If the channel layouts of the inputs are not
disjoint, the output will have all the channels of the first input then all
the channels of the second input, in that order, and the channel layout of
the output will be the default value corresponding to the total number of
channels.
For example, if the first input is in 2.1 (FL+FR+LF) and the second input
is FC+BL+BR, then the output will be in 5.1, with the channels in the
following order: a1, a2, b1, a3, b2, b3 (a1 is the first channel of the
first input, b1 is the first channel of the second input).
On the other hand, if both input are in stereo, the output channels will be
in the default order: a1, a2, b1, b2, and the channel layout will be
arbitrarily set to 4.0, which may or may not be the expected value.
All inputs must have the same sample rate, and format.
If inputs do not have the same duration, the output will stop with the
shortest.
36.34.1 Examples
Merge two mono files into a stereo stream:
amovie=left.wav [l] ; amovie=right.mp3 [r] ; [l] [r] amerge
Multiple merges assuming 1 video stream and 6 audio streams in input.mkv:
ffmpeg -i input.mkv -filter_complex "[0:1][0:2][0:3][0:4][0:5][0:6] amerge=inputs=6" -c:a pcm_s16le output.mkv
36.35 amix
Mixes multiple audio inputs into a single output.
Note that this filter only supports float samples (the amerge
and pan audio filters support many formats). If the amix
input has integer samples then aresample will be automatically
inserted to perform the conversion to float samples.
It accepts the following parameters:
inputs
The number of inputs. If unspecified, it defaults to 2.
duration
How to determine the end-of-stream.
longest
The duration of the longest input. (default)
shortest
The duration of the shortest input.
first
The duration of the first input.
dropout_transition
The transition time, in seconds, for volume renormalization when an input
stream ends. The default value is 2 seconds.
weights
Specify weight of each input audio stream as a sequence of numbers separated
by a space. If fewer weights are specified compared to number of inputs, the
last weight is assigned to the remaining inputs.
Default weight for each input is 1.
normalize
Always scale inputs instead of only doing summation of samples.
Beware of heavy clipping if inputs are not normalized prior or after filtering
by this filter if this option is disabled. By default is enabled.
36.35.1 Examples
This will mix 3 input audio streams to a single output with the same duration as the
first input and a dropout transition time of 3 seconds:
ffmpeg -i INPUT1 -i INPUT2 -i INPUT3 -filter_complex amix=inputs=3:duration=first:dropout_transition=3 OUTPUT
This will mix one vocal and one music input audio stream to a single output with the same duration as the
longest input. The music will have quarter the weight as the vocals, and the inputs are not normalized:
ffmpeg -i VOCALS -i MUSIC -filter_complex amix=inputs=2:duration=longest:dropout_transition=0:weights="1 0.25":normalize=0 OUTPUT
36.35.2 Commands
This filter supports the following commands:
weights
normalize
Syntax is same as option with same name.
36.36 amultiply
Multiply first audio stream with second audio stream and store result
in output audio stream. Multiplication is done by multiplying each
sample from first stream with sample at same position from second stream.
With this element-wise multiplication one can create amplitude fades and
amplitude modulations.
36.37 anequalizer
High-order parametric multiband equalizer for each channel.
It accepts the following parameters:
params
This option string is in format:
"cchn f=cf w=w g=g t=f | ..."
Each equalizer band is separated by ’|’.
chn
Set channel number to which equalization will be applied.
If input doesn’t have that channel the entry is ignored.
f
Set central frequency for band.
If input doesn’t have that frequency the entry is ignored.
w
Set band width in Hertz.
g
Set band gain in dB.
t
Set filter type for band, optional, can be:
‘0’
Butterworth, this is default.
‘1’
Chebyshev type 1.
‘2’
Chebyshev type 2.
curves
With this option activated frequency response of anequalizer is displayed
in video stream.
size
Set video stream size. Only useful if curves option is activated.
mgain
Set max gain that will be displayed. Only useful if curves option is activated.
Setting this to a reasonable value makes it possible to display gain which is derived from
neighbour bands which are too close to each other and thus produce higher gain
when both are activated.
fscale
Set frequency scale used to draw frequency response in video output.
Can be linear or logarithmic. Default is logarithmic.
colors
Set color for each channel curve which is going to be displayed in video stream.
This is list of color names separated by space or by ’|’.
Unrecognised or missing colors will be replaced by white color.
36.37.1 Examples
Lower gain by 10 of central frequency 200Hz and width 100 Hz
for first 2 channels using Chebyshev type 1 filter:
anequalizer=c0 f=200 w=100 g=-10 t=1|c1 f=200 w=100 g=-10 t=1
36.37.2 Commands
This filter supports the following commands:
change
Alter existing filter parameters.
Syntax for the commands is : "fN|f=freq|w=width|g=gain"
fN is existing filter number, starting from 0, if no such filter is available
error is returned.
freq set new frequency parameter.
width set new width parameter in Hertz.
gain set new gain parameter in dB.
Full filter invocation with asendcmd may look like this:
asendcmd=c=’4.0 anequalizer change 0|f=200|w=50|g=1’,anequalizer=...
36.38 anlmdn
Reduce broadband noise in audio samples using Non-Local Means algorithm.
Each sample is adjusted by looking for other samples with similar contexts. This
context similarity is defined by comparing their surrounding patches of size
p. Patches are searched in an area of r around the sample.
The filter accepts the following options:
strength, s
Set denoising strength. Allowed range is from 0.00001 to 10000. Default value is 0.00001.
patch, p
Set patch radius duration. Allowed range is from 1 to 100 milliseconds.
Default value is 2 milliseconds.
research, r
Set research radius duration. Allowed range is from 2 to 300 milliseconds.
Default value is 6 milliseconds.
output, o
Set the output mode.
It accepts the following values:
i
Pass input unchanged.
o
Pass noise filtered out.
n
Pass only noise.
Default value is o.
smooth, m
Set smooth factor. Default value is 11. Allowed range is from 1 to 1000.
36.38.1 Commands
This filter supports the all above options as commands.
36.39 anlmf, anlms
Apply Normalized Least-Mean-(Squares|Fourth) algorithm to the first audio stream using the second audio stream.
This adaptive filter is used to mimic a desired filter by finding the filter coefficients that
relate to producing the least mean square of the error signal (difference between the desired,
2nd input audio stream and the actual signal, the 1st input audio stream).
A description of the accepted options follows.
order
Set filter order.
mu
Set filter mu.
eps
Set the filter eps.
leakage
Set the filter leakage.
out_mode
It accepts the following values:
i
Pass the 1st input.
d
Pass the 2nd input.
o
Pass difference between desired, 2nd input and error signal estimate.
n
Pass difference between input, 1st input and error signal estimate.
e
Pass error signal estimated samples.
Default value is o.
precision
Set which precision to use when processing samples.
auto
Auto pick internal sample format depending on other filters.
float
Always use single-floating point precision sample format.
double
Always use double-floating point precision sample format.
36.39.1 Examples
One of many usages of this filter is noise reduction, input audio is filtered
with same samples that are delayed by fixed amount, one such example for stereo audio is:
asplit[a][b],[a]adelay=32S|32S[a],[b][a]anlms=order=128:leakage=0.0005:mu=.5:out_mode=o
36.39.2 Commands
This filter supports the same commands as options, excluding option order.
36.40 anull
Pass the audio source unchanged to the output.
36.41 apad
Pad the end of an audio stream with silence.
This can be used together with ffmpeg -shortest to
extend audio streams to the same length as the video stream.
A description of the accepted options follows.
packet_size
Set silence packet size. Default value is 4096.
pad_len
Set the number of samples of silence to add to the end. After the
value is reached, the stream is terminated. This option is mutually
exclusive with whole_len.
whole_len
Set the minimum total number of samples in the output audio stream. If
the value is longer than the input audio length, silence is added to
the end, until the value is reached. This option is mutually exclusive
with pad_len.
pad_dur
Specify the duration of samples of silence to add. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax. Used only if set to non-negative value.
whole_dur
Specify the minimum total duration in the output audio stream. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax. Used only if set to non-negative value. If the value is longer than
the input audio length, silence is added to the end, until the value is reached.
This option is mutually exclusive with pad_dur
If neither the pad_len nor the whole_len nor pad_dur
nor whole_dur option is set, the filter will add silence to the end of
the input stream indefinitely.
Note that for ffmpeg 4.4 and earlier a zero pad_dur or
whole_dur also caused the filter to add silence indefinitely.
36.41.1 Examples
Add 1024 samples of silence to the end of the input:
apad=pad_len=1024
Make sure the audio output will contain at least 10000 samples, pad
the input with silence if required:
apad=whole_len=10000
Use ffmpeg to pad the audio input with silence, so that the
video stream will always result the shortest and will be converted
until the end in the output file when using the shortest
option:
ffmpeg -i VIDEO -i AUDIO -filter_complex "[1:0]apad" -shortest OUTPUT
36.42 aphaser
Add a phasing effect to the input audio.
A phaser filter creates series of peaks and troughs in the frequency spectrum.
The position of the peaks and troughs are modulated so that they vary over time, creating a sweeping effect.
A description of the accepted parameters follows.
in_gain
Set input gain. Default is 0.4.
out_gain
Set output gain. Default is 0.74
delay
Set delay in milliseconds. Default is 3.0.
decay
Set decay. Default is 0.4.
speed
Set modulation speed in Hz. Default is 0.5.
type
Set modulation type. Default is triangular.
It accepts the following values:
‘triangular, t’
‘sinusoidal, s’
36.43 aphaseshift
Apply phase shift to input audio samples.
The filter accepts the following options:
shift
Specify phase shift. Allowed range is from -1.0 to 1.0.
Default value is 0.0.
level
Set output gain applied to final output. Allowed range is from 0.0 to 1.0.
Default value is 1.0.
order
Set filter order used for filtering. Allowed range is from 1 to 16.
Default value is 8.
36.43.1 Commands
This filter supports the all above options as commands.
36.44 apsnr
Measure Audio Peak Signal-to-Noise Ratio.
This filter takes two audio streams for input, and outputs first
audio stream.
Results are in dB per channel at end of either input.
36.45 apsyclip
Apply Psychoacoustic clipper to input audio stream.
The filter accepts the following options:
level_in
Set input gain. By default it is 1. Range is [0.015625 - 64].
level_out
Set output gain. By default it is 1. Range is [0.015625 - 64].
clip
Set the clipping start value. Default value is 0dBFS or 1.
diff
Output only difference samples, useful to hear introduced distortions.
By default is disabled.
adaptive
Set strength of adaptive distortion applied. Default value is 0.5.
Allowed range is from 0 to 1.
iterations
Set number of iterations of psychoacoustic clipper.
Allowed range is from 1 to 20. Default value is 10.
level
Auto level output signal. Default is disabled.
This normalizes audio back to 0dBFS if enabled.
36.45.1 Commands
This filter supports the all above options as commands.
36.46 apulsator
Audio pulsator is something between an autopanner and a tremolo.
But it can produce funny stereo effects as well. Pulsator changes the volume
of the left and right channel based on a LFO (low frequency oscillator) with
different waveforms and shifted phases.
This filter have the ability to define an offset between left and right
channel. An offset of 0 means that both LFO shapes match each other.
The left and right channel are altered equally - a conventional tremolo.
An offset of 50% means that the shape of the right channel is exactly shifted
in phase (or moved backwards about half of the frequency) - pulsator acts as
an autopanner. At 1 both curves match again. Every setting in between moves the
phase shift gapless between all stages and produces some "bypassing" sounds with
sine and triangle waveforms. The more you set the offset near 1 (starting from
the 0.5) the faster the signal passes from the left to the right speaker.
The filter accepts the following options:
level_in
Set input gain. By default it is 1. Range is [0.015625 - 64].
level_out
Set output gain. By default it is 1. Range is [0.015625 - 64].
mode
Set waveform shape the LFO will use. Can be one of: sine, triangle, square,
sawup or sawdown. Default is sine.
amount
Set modulation. Define how much of original signal is affected by the LFO.
offset_l
Set left channel offset. Default is 0. Allowed range is [0 - 1].
offset_r
Set right channel offset. Default is 0.5. Allowed range is [0 - 1].
width
Set pulse width. Default is 1. Allowed range is [0 - 2].
timing
Set possible timing mode. Can be one of: bpm, ms or hz. Default is hz.
bpm
Set bpm. Default is 120. Allowed range is [30 - 300]. Only used if timing
is set to bpm.
ms
Set ms. Default is 500. Allowed range is [10 - 2000]. Only used if timing
is set to ms.
hz
Set frequency in Hz. Default is 2. Allowed range is [0.01 - 100]. Only used
if timing is set to hz.
36.47 aresample
Resample the input audio to the specified parameters, using the
libswresample library. If none are specified then the filter will
automatically convert between its input and output.
This filter is also able to stretch/squeeze the audio data to make it match
the timestamps or to inject silence / cut out audio to make it match the
timestamps, do a combination of both or do neither.
The filter accepts the syntax
[sample_rate:]resampler_options, where sample_rate
expresses a sample rate and resampler_options is a list of
key=value pairs, separated by ":". See the
(ffmpeg-resampler)"Resampler Options" section in the
ffmpeg-resampler(1) manual
for the complete list of supported options.
36.47.1 Examples
Resample the input audio to 44100Hz:
aresample=44100
Stretch/squeeze samples to the given timestamps, with a maximum of 1000
samples per second compensation:
aresample=async=1000
36.48 areverse
Reverse an audio clip.
Warning: This filter requires memory to buffer the entire clip, so trimming
is suggested.
36.48.1 Examples
Take the first 5 seconds of a clip, and reverse it.
atrim=end=5,areverse
36.49 arls
Apply Recursive Least Squares algorithm to the first audio stream using the second audio stream.
This adaptive filter is used to mimic a desired filter by recursively finding the filter coefficients that
relate to producing the minimal weighted linear least squares cost function of the error signal (difference
between the desired, 2nd input audio stream and the actual signal, the 1st input audio stream).
A description of the accepted options follows.
order
Set the filter order.
lambda
Set the forgetting factor.
delta
Set the coefficient to initialize internal covariance matrix.
out_mode
Set the filter output samples. It accepts the following values:
i
Pass the 1st input.
d
Pass the 2nd input.
o
Pass difference between desired, 2nd input and error signal estimate.
n
Pass difference between input, 1st input and error signal estimate.
e
Pass error signal estimated samples.
Default value is o.
precision
Set which precision to use when processing samples.
auto
Auto pick internal sample format depending on other filters.
float
Always use single-floating point precision sample format.
double
Always use double-floating point precision sample format.
36.50 arnndn
Reduce noise from speech using Recurrent Neural Networks.
This filter accepts the following options:
model, m
Set train model file to load. This option is always required.
mix
Set how much to mix filtered samples into final output.
Allowed range is from -1 to 1. Default value is 1.
Negative values are special, they set how much to keep filtered noise
in the final filter output. Set this option to -1 to hear actual
noise removed from input signal.
36.50.1 Commands
This filter supports the all above options as commands.
36.51 asdr
Measure Audio Signal-to-Distortion Ratio.
This filter takes two audio streams for input, and outputs first
audio stream.
Results are in dB per channel at end of either input.
36.52 asetnsamples
Set the number of samples per each output audio frame.
The last output packet may contain a different number of samples, as
the filter will flush all the remaining samples when the input audio
signals its end.
The filter accepts the following options:
nb_out_samples, n
Set the number of frames per each output audio frame. The number is
intended as the number of samples per each channel.
Default value is 1024.
pad, p
If set to 1, the filter will pad the last audio frame with zeroes, so
that the last frame will contain the same number of samples as the
previous ones. Default value is 1.
For example, to set the number of per-frame samples to 1234 and
disable padding for the last frame, use:
asetnsamples=n=1234:p=0
36.53 asetrate
Set the sample rate without altering the PCM data.
This will result in a change of speed and pitch.
The filter accepts the following options:
sample_rate, r
Set the output sample rate. Default is 44100 Hz.
36.54 ashowinfo
Show a line containing various information for each input audio frame.
The input audio is not modified.
The shown line contains a sequence of key/value pairs of the form
key:value.
The following values are shown in the output:
n
The (sequential) number of the input frame, starting from 0.
pts
The presentation timestamp of the input frame, in time base units; the time base
depends on the filter input pad, and is usually 1/sample_rate.
pts_time
The presentation timestamp of the input frame in seconds.
fmt
The sample format.
chlayout
The channel layout.
rate
The sample rate for the audio frame.
nb_samples
The number of samples (per channel) in the frame.
checksum
The Adler-32 checksum (printed in hexadecimal) of the audio data. For planar
audio, the data is treated as if all the planes were concatenated.
plane_checksums
A list of Adler-32 checksums for each data plane.
36.55 asisdr
Measure Audio Scaled-Invariant Signal-to-Distortion Ratio.
This filter takes two audio streams for input, and outputs first
audio stream.
Results are in dB per channel at end of either input.
36.56 asoftclip
Apply audio soft clipping.
Soft clipping is a type of distortion effect where the amplitude of a signal is saturated
along a smooth curve, rather than the abrupt shape of hard-clipping.
This filter accepts the following options:
type
Set type of soft-clipping.
It accepts the following values:
hard
tanh
atan
cubic
exp
alg
quintic
sin
erf
threshold
Set threshold from where to start clipping. Default value is 0dB or 1.
output
Set gain applied to output. Default value is 0dB or 1.
param
Set additional parameter which controls sigmoid function.
oversample
Set oversampling factor.
36.56.1 Commands
This filter supports the all above options as commands.
36.57 aspectralstats
Display frequency domain statistical information about the audio channels.
Statistics are calculated and stored as metadata for each audio channel and for each audio frame.
It accepts the following option:
win_size
Set the window length in samples. Default value is 2048.
Allowed range is from 32 to 65536.
win_func
Set window function.
It accepts the following values:
‘rect’
‘bartlett’
‘hann, hanning’
‘hamming’
‘blackman’
‘welch’
‘flattop’
‘bharris’
‘bnuttall’
‘bhann’
‘sine’
‘nuttall’
‘lanczos’
‘gauss’
‘tukey’
‘dolph’
‘cauchy’
‘parzen’
‘poisson’
‘bohman’
‘kaiser’
Default is hann.
overlap
Set window overlap. Allowed range is from 0
to 1. Default value is 0.5.
measure
Select the parameters which are measured. The metadata keys can
be used as flags, default is all which measures everything.
none disables all measurement.
A list of each metadata key follows:
mean
variance
centroid
spread
skewness
kurtosis
entropy
flatness
crest
flux
slope
decrease
rolloff
36.58 asr
Automatic Speech Recognition
This filter uses PocketSphinx for speech recognition. To enable
compilation of this filter, you need to configure FFmpeg with
--enable-pocketsphinx.
It accepts the following options:
rate
Set sampling rate of input audio. Defaults is 16000.
This need to match speech models, otherwise one will get poor results.
hmm
Set dictionary containing acoustic model files.
dict
Set pronunciation dictionary.
lm
Set language model file.
lmctl
Set language model set.
lmname
Set which language model to use.
logfn
Set output for log messages.
The filter exports recognized speech as the frame metadata lavfi.asr.text.
36.59 astats
Display time domain statistical information about the audio channels.
Statistics are calculated and displayed for each audio channel and,
where applicable, an overall figure is also given.
It accepts the following option:
length
Short window length in seconds, used for peak and trough RMS measurement.
Default is 0.05 (50 milliseconds). Allowed range is [0 - 10].
metadata
Set metadata injection. All the metadata keys are prefixed with lavfi.astats.X,
where X is channel number starting from 1 or string Overall. Default is
disabled.
Available keys for each channel are:
Bit_depth
Crest_factor
DC_offset
Dynamic_range
Entropy
Flat_factor
Max_difference
Max_level
Mean_difference
Min_difference
Min_level
Noise_floor
Noise_floor_count
Number_of_Infs
Number_of_NaNs
Number_of_denormals
Peak_count
Abs_Peak_count
Peak_level
RMS_difference
RMS_peak
RMS_trough
Zero_crossings
Zero_crossings_rate
and for Overall:
Bit_depth
DC_offset
Entropy
Flat_factor
Max_difference
Max_level
Mean_difference
Min_difference
Min_level
Noise_floor
Noise_floor_count
Number_of_Infs
Number_of_NaNs
Number_of_denormals
Number_of_samples
Peak_count
Abs_Peak_count
Peak_level
RMS_difference
RMS_level
RMS_peak
RMS_trough
For example, a full key looks like lavfi.astats.1.DC_offset or
lavfi.astats.Overall.Peak_count.
Read below for the description of the keys.
reset
Set the number of frames over which cumulative stats are calculated before
being reset. Default is disabled.
measure_perchannel
Select the parameters which are measured per channel. The metadata keys can
be used as flags, default is all which measures everything.
none disables all per channel measurement.
measure_overall
Select the parameters which are measured overall. The metadata keys can
be used as flags, default is all which measures everything.
none disables all overall measurement.
A description of the measure keys follow:
none
no measures
all
all measures
Bit_depth
overall bit depth of audio, i.e. number of bits used for each sample
Crest_factor
standard ratio of peak to RMS level (note: not in dB)
DC_offset
mean amplitude displacement from zero
Dynamic_range
measured dynamic range of audio in dB
Entropy
entropy measured across whole audio, entropy of value near 1.0 is typically measured for white noise
Flat_factor
flatness (i.e. consecutive samples with the same value) of the signal at its peak levels
(i.e. either Min_level or Max_level)
Max_difference
maximal difference between two consecutive samples
Max_level
maximal sample level
Mean_difference
mean difference between two consecutive samples, i.e. the average of each difference between two consecutive samples
Min_difference
minimal difference between two consecutive samples
Min_level
minimal sample level
Noise_floor
minimum local peak measured in dBFS over a short window
Noise_floor_count
number of occasions (not the number of samples) that the signal attained
Noise floor
Number_of_Infs
number of samples with an infinite value
Number_of_NaNs
number of samples with a NaN (not a number) value
Number_of_denormals
number of samples with a subnormal value
Number_of_samples
number of samples
Peak_count
number of occasions (not the number of samples) that the signal attained either
Min_level or Max_level
Abs_Peak_count
number of occasions that the absolute samples taken from the signal attained
max absolute value of Min_level and Max_level
Peak_level
standard peak level measured in dBFS
RMS_difference
Root Mean Square difference between two consecutive samples
RMS_level
standard RMS level measured in dBFS
RMS_peak
RMS_trough
peak and trough values for RMS level measured over a short window,
measured in dBFS.
Zero crossings
number of points where the waveform crosses the zero level axis
Zero crossings rate
rate of Zero crossings and number of audio samples
36.60 asubboost
Boost subwoofer frequencies.
The filter accepts the following options:
dry
Set dry gain, how much of original signal is kept. Allowed range is from 0 to 1.
Default value is 1.0.
wet
Set wet gain, how much of filtered signal is kept. Allowed range is from 0 to 1.
Default value is 1.0.
boost
Set max boost factor. Allowed range is from 1 to 12. Default value is 2.
decay
Set delay line decay gain value. Allowed range is from 0 to 1.
Default value is 0.0.
feedback
Set delay line feedback gain value. Allowed range is from 0 to 1.
Default value is 0.9.
cutoff
Set cutoff frequency in Hertz. Allowed range is 50 to 900.
Default value is 100.
slope
Set slope amount for cutoff frequency. Allowed range is 0.0001 to 1.
Default value is 0.5.
delay
Set delay. Allowed range is from 1 to 100.
Default value is 20.
channels
Set the channels to process. Default value is all available.
36.60.1 Commands
This filter supports the all above options as commands.
36.61 asubcut
Cut subwoofer frequencies.
This filter allows to set custom, steeper
roll off than highpass filter, and thus is able to more attenuate
frequency content in stop-band.
The filter accepts the following options:
cutoff
Set cutoff frequency in Hertz. Allowed range is 2 to 200.
Default value is 20.
order
Set filter order. Available values are from 3 to 20.
Default value is 10.
level
Set input gain level. Allowed range is from 0 to 1. Default value is 1.
36.61.1 Commands
This filter supports the all above options as commands.
36.62 asupercut
Cut super frequencies.
The filter accepts the following options:
cutoff
Set cutoff frequency in Hertz. Allowed range is 20000 to 192000.
Default value is 20000.
order
Set filter order. Available values are from 3 to 20.
Default value is 10.
level
Set input gain level. Allowed range is from 0 to 1. Default value is 1.
36.62.1 Commands
This filter supports the all above options as commands.
36.63 asuperpass
Apply high order Butterworth band-pass filter.
The filter accepts the following options:
centerf
Set center frequency in Hertz. Allowed range is 2 to 999999.
Default value is 1000.
order
Set filter order. Available values are from 4 to 20.
Default value is 4.
qfactor
Set Q-factor. Allowed range is from 0.01 to 100. Default value is 1.
level
Set input gain level. Allowed range is from 0 to 2. Default value is 1.
36.63.1 Commands
This filter supports the all above options as commands.
36.64 asuperstop
Apply high order Butterworth band-stop filter.
The filter accepts the following options:
centerf
Set center frequency in Hertz. Allowed range is 2 to 999999.
Default value is 1000.
order
Set filter order. Available values are from 4 to 20.
Default value is 4.
qfactor
Set Q-factor. Allowed range is from 0.01 to 100. Default value is 1.
level
Set input gain level. Allowed range is from 0 to 2. Default value is 1.
36.64.1 Commands
This filter supports the all above options as commands.
36.65 atempo
Adjust audio tempo.
The filter accepts exactly one parameter, the audio tempo. If not
specified then the filter will assume nominal 1.0 tempo. Tempo must
be in the [0.5, 100.0] range.
Note that tempo greater than 2 will skip some samples rather than
blend them in.  If for any reason this is a concern it is always
possible to daisy-chain several instances of atempo to achieve the
desired product tempo.
36.65.1 Examples
Slow down audio to 80% tempo:
atempo=0.8
To speed up audio to 300% tempo:
atempo=3
To speed up audio to 300% tempo by daisy-chaining two atempo instances:
atempo=sqrt(3),atempo=sqrt(3)
36.65.2 Commands
This filter supports the following commands:
tempo
Change filter tempo scale factor.
Syntax for the command is : "tempo"
36.66 atilt
Apply spectral tilt filter to audio stream.
This filter apply any spectral roll-off slope over any specified frequency band.
The filter accepts the following options:
freq
Set central frequency of tilt in Hz. Default is 10000 Hz.
slope
Set slope direction of tilt. Default is 0. Allowed range is from -1 to 1.
width
Set width of tilt. Default is 1000. Allowed range is from 100 to 10000.
order
Set order of tilt filter.
level
Set input volume level. Allowed range is from 0 to 4.
Default is 1.
36.66.1 Commands
This filter supports the all above options as commands.
36.67 atrim
Trim the input so that the output contains one continuous subpart of the input.
It accepts the following parameters:
start
Timestamp (in seconds) of the start of the section to keep. I.e. the audio
sample with the timestamp start will be the first sample in the output.
end
Specify time of the first audio sample that will be dropped, i.e. the
audio sample immediately preceding the one with the timestamp end will be
the last sample in the output.
start_pts
Same as start, except this option sets the start timestamp in samples
instead of seconds.
end_pts
Same as end, except this option sets the end timestamp in samples instead
of seconds.
duration
The maximum duration of the output in seconds.
start_sample
The number of the first sample that should be output.
end_sample
The number of the first sample that should be dropped.
start, end, and duration are expressed as time
duration specifications; see
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual.
Note that the first two sets of the start/end options and the duration
option look at the frame timestamp, while the _sample options simply count the
samples that pass through the filter. So start/end_pts and start/end_sample will
give different results when the timestamps are wrong, inexact or do not start at
zero. Also note that this filter does not modify the timestamps. If you wish
to have the output timestamps start at zero, insert the asetpts filter after the
atrim filter.
If multiple start or end options are set, this filter tries to be greedy and
keep all samples that match at least one of the specified constraints. To keep
only the part that matches all the constraints at once, chain multiple atrim
filters.
The defaults are such that all the input is kept. So it is possible to set e.g.
just the end values to keep everything before the specified time.
Examples:
Drop everything except the second minute of input:
ffmpeg -i INPUT -af atrim=60:120
Keep only the first 1000 samples:
ffmpeg -i INPUT -af atrim=end_sample=1000
36.68 axcorrelate
Calculate normalized windowed cross-correlation between two input audio streams.
Resulted samples are always between -1 and 1 inclusive.
If result is 1 it means two input samples are highly correlated in that selected segment.
Result 0 means they are not correlated at all.
If result is -1 it means two input samples are out of phase, which means they cancel each
other.
The filter accepts the following options:
size
Set size of segment over which cross-correlation is calculated.
Default is 256. Allowed range is from 2 to 131072.
algo
Set algorithm for cross-correlation. Can be slow or fast or best.
Default is best. Fast algorithm assumes mean values over any given segment
are always zero and thus need much less calculations to make.
This is generally not true, but is valid for typical audio streams.
36.68.1 Examples
Calculate correlation between channels in stereo audio stream:
ffmpeg -i stereo.wav -af channelsplit,axcorrelate=size=1024:algo=fast correlation.wav
36.69 bandpass
Apply a two-pole Butterworth band-pass filter with central
frequency frequency, and (3dB-point) band-width width.
The csg option selects a constant skirt gain (peak gain = Q)
instead of the default: constant 0dB peak gain.
The filter roll off at 6dB per octave (20dB per decade).
The filter accepts the following options:
frequency, f
Set the filter’s central frequency. Default is 3000.
csg
Constant skirt gain if set to 1. Defaults to 0.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Specify the band-width of a filter in width_type units.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.69.1 Commands
This filter supports the following commands:
frequency, f
Change bandpass frequency.
Syntax for the command is : "frequency"
width_type, t
Change bandpass width_type.
Syntax for the command is : "width_type"
width, w
Change bandpass width.
Syntax for the command is : "width"
mix, m
Change bandpass mix.
Syntax for the command is : "mix"
36.70 bandreject
Apply a two-pole Butterworth band-reject filter with central
frequency frequency, and (3dB-point) band-width width.
The filter roll off at 6dB per octave (20dB per decade).
The filter accepts the following options:
frequency, f
Set the filter’s central frequency. Default is 3000.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Specify the band-width of a filter in width_type units.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.70.1 Commands
This filter supports the following commands:
frequency, f
Change bandreject frequency.
Syntax for the command is : "frequency"
width_type, t
Change bandreject width_type.
Syntax for the command is : "width_type"
width, w
Change bandreject width.
Syntax for the command is : "width"
mix, m
Change bandreject mix.
Syntax for the command is : "mix"
36.71 bass, lowshelf
Boost or cut the bass (lower) frequencies of the audio using a two-pole
shelving filter with a response similar to that of a standard
hi-fi’s tone-controls. This is also known as shelving equalisation (EQ).
The filter accepts the following options:
gain, g
Give the gain at 0 Hz. Its useful range is about -20
(for a large cut) to +20 (for a large boost).
Beware of clipping when using a positive gain.
frequency, f
Set the filter’s central frequency and so can be used
to extend or reduce the frequency range to be boosted or cut.
The default value is 100 Hz.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Determine how steep is the filter’s shelf transition.
poles, p
Set number of poles. Default is 2.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.71.1 Commands
This filter supports the following commands:
frequency, f
Change bass frequency.
Syntax for the command is : "frequency"
width_type, t
Change bass width_type.
Syntax for the command is : "width_type"
width, w
Change bass width.
Syntax for the command is : "width"
gain, g
Change bass gain.
Syntax for the command is : "gain"
mix, m
Change bass mix.
Syntax for the command is : "mix"
36.72 biquad
Apply a biquad IIR filter with the given coefficients.
Where b0, b1, b2 and a0, a1, a2
are the numerator and denominator coefficients respectively.
and channels, c specify which channels to filter, by default all
available are filtered.
36.72.1 Commands
This filter supports the following commands:
a0
a1
a2
b0
b1
b2
Change biquad parameter.
Syntax for the command is : "value"
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.73 bs2b
Bauer stereo to binaural transformation, which improves headphone listening of
stereo audio records.
To enable compilation of this filter you need to configure FFmpeg with
--enable-libbs2b.
It accepts the following parameters:
profile
Pre-defined crossfeed level.
default
Default level (fcut=700, feed=50).
cmoy
Chu Moy circuit (fcut=700, feed=60).
jmeier
Jan Meier circuit (fcut=650, feed=95).
fcut
Cut frequency (in Hz).
feed
Feed level (in Hz).
36.74 channelmap
Remap input channels to new locations.
It accepts the following parameters:
map
Map channels from input to output. The argument is a ’|’-separated list of
mappings, each in the in_channel-out_channel or
in_channel form. in_channel can be either the name of the
input channel (e.g. FL for front left) or its index in the input channel
layout. out_channel is the name of the output channel or its index in the
output channel layout. If out_channel is not given then it is implicitly
an index, starting with zero and increasing by one for each mapping. Mixing
different types of mappings is not allowed and will result in a parse error.
channel_layout
The channel layout of the output stream. If not specified, then filter will
guess it based on the out_channel names or the number of mappings.
Guessed layouts will not necessarily contain channels in the order of the
mappings.
If no mapping is present, the filter will implicitly map input channels to
output channels, preserving indices.
36.74.1 Examples
For example, assuming a 5.1+downmix input MOV file,
ffmpeg -i in.mov -filter 'channelmap=map=DL-FL|DR-FR' out.wav
will create an output WAV file tagged as stereo from the downmix channels of
the input.
To fix a 5.1 WAV improperly encoded in AAC’s native channel order
ffmpeg -i in.wav -filter 'channelmap=1|2|0|5|3|4:5.1' out.wav
36.75 channelsplit
Split each channel from an input audio stream into a separate output stream.
It accepts the following parameters:
channel_layout
The channel layout of the input stream. The default is "stereo".
channels
A channel layout describing the channels to be extracted as separate output streams
or "all" to extract each input channel as a separate stream. The default is "all".
Choosing channels not present in channel layout in the input will result in an error.
36.75.1 Examples
For example, assuming a stereo input MP3 file,
ffmpeg -i in.mp3 -filter_complex channelsplit out.mkv
will create an output Matroska file with two audio streams, one containing only
the left channel and the other the right channel.
Split a 5.1 WAV file into per-channel files:
ffmpeg -i in.wav -filter_complex
'channelsplit=channel_layout=5.1[FL][FR][FC][LFE][SL][SR]'
-map '[FL]' front_left.wav -map '[FR]' front_right.wav -map '[FC]'
front_center.wav -map '[LFE]' lfe.wav -map '[SL]' side_left.wav -map '[SR]'
side_right.wav
Extract only LFE from a 5.1 WAV file:
ffmpeg -i in.wav -filter_complex 'channelsplit=channel_layout=5.1:channels=LFE[LFE]'
-map '[LFE]' lfe.wav
36.76 chorus
Add a chorus effect to the audio.
Can make a single vocal sound like a chorus, but can also be applied to instrumentation.
Chorus resembles an echo effect with a short delay, but whereas with echo the delay is
constant, with chorus, it is varied using using sinusoidal or triangular modulation.
The modulation depth defines the range the modulated delay is played before or after
the delay. Hence the delayed sound will sound slower or faster, that is the delayed
sound tuned around the original one, like in a chorus where some vocals are slightly
off key.
It accepts the following parameters:
in_gain
Set input gain. Default is 0.4.
out_gain
Set output gain. Default is 0.4.
delays
Set delays. A typical delay is around 40ms to 60ms.
decays
Set decays.
speeds
Set speeds.
depths
Set depths.
36.76.1 Examples
A single delay:
chorus=0.7:0.9:55:0.4:0.25:2
Two delays:
chorus=0.6:0.9:50|60:0.4|0.32:0.25|0.4:2|1.3
Fuller sounding chorus with three delays:
chorus=0.5:0.9:50|60|40:0.4|0.32|0.3:0.25|0.4|0.3:2|2.3|1.3
36.77 compand
Compress or expand the audio’s dynamic range.
It accepts the following parameters:
attacks
decays
A list of times in seconds for each channel over which the instantaneous level
of the input signal is averaged to determine its volume. attacks refers to
increase of volume and decays refers to decrease of volume. For most
situations, the attack time (response to the audio getting louder) should be
shorter than the decay time, because the human ear is more sensitive to sudden
loud audio than sudden soft audio. A typical value for attack is 0.3 seconds and
a typical value for decay is 0.8 seconds.
If specified number of attacks & decays is lower than number of channels, the last
set attack/decay will be used for all remaining channels.
points
A list of points for the transfer function, specified in dB relative to the
maximum possible signal amplitude. Each key points list must be defined using
the following syntax: x0/y0|x1/y1|x2/y2|.... or
x0/y0 x1/y1 x2/y2 ....
The input values must be in strictly increasing order but the transfer function
does not have to be monotonically rising. The point 0/0 is assumed but
may be overridden (by 0/out-dBn). Typical values for the transfer
function are -70/-70|-60/-20|1/0.
soft-knee
Set the curve radius in dB for all joints. It defaults to 0.01.
gain
Set the additional gain in dB to be applied at all points on the transfer
function. This allows for easy adjustment of the overall gain.
It defaults to 0.
volume
Set an initial volume, in dB, to be assumed for each channel when filtering
starts. This permits the user to supply a nominal level initially, so that, for
example, a very large gain is not applied to initial signal levels before the
companding has begun to operate. A typical value for audio which is initially
quiet is -90 dB. It defaults to 0.
delay
Set a delay, in seconds. The input audio is analyzed immediately, but audio is
delayed before being fed to the volume adjuster. Specifying a delay
approximately equal to the attack/decay times allows the filter to effectively
operate in predictive rather than reactive mode. It defaults to 0.
36.77.1 Examples
Make music with both quiet and loud passages suitable for listening to in a
noisy environment:
compand=.3|.3:1|1:-90/-60|-60/-40|-40/-30|-20/-20:6:0:-90:0.2
Another example for audio with whisper and explosion parts:
compand=0|0:1|1:-90/-900|-70/-70|-30/-9|0/-3:6:0:0:0
A noise gate for when the noise is at a lower level than the signal:
compand=.1|.1:.2|.2:-900/-900|-50.1/-900|-50/-50:.01:0:-90:.1
Here is another noise gate, this time for when the noise is at a higher level
than the signal (making it, in some ways, similar to squelch):
compand=.1|.1:.1|.1:-45.1/-45.1|-45/-900|0/-900:.01:45:-90:.1
2:1 compression starting at -6dB:
compand=points=-80/-80|-6/-6|0/-3.8|20/3.5
2:1 compression starting at -9dB:
compand=points=-80/-80|-9/-9|0/-5.3|20/2.9
2:1 compression starting at -12dB:
compand=points=-80/-80|-12/-12|0/-6.8|20/1.9
2:1 compression starting at -18dB:
compand=points=-80/-80|-18/-18|0/-9.8|20/0.7
3:1 compression starting at -15dB:
compand=points=-80/-80|-15/-15|0/-10.8|20/-5.2
Compressor/Gate:
compand=points=-80/-105|-62/-80|-15.4/-15.4|0/-12|20/-7.6
Expander:
compand=attacks=0:points=-80/-169|-54/-80|-49.5/-64.6|-41.1/-41.1|-25.8/-15|-10.8/-4.5|0/0|20/8.3
Hard limiter at -6dB:
compand=attacks=0:points=-80/-80|-6/-6|20/-6
Hard limiter at -12dB:
compand=attacks=0:points=-80/-80|-12/-12|20/-12
Hard noise gate at -35 dB:
compand=attacks=0:points=-80/-115|-35.1/-80|-35/-35|20/20
Soft limiter:
compand=attacks=0:points=-80/-80|-12.4/-12.4|-6/-8|0/-6.8|20/-2.8
36.78 compensationdelay
Compensation Delay Line is a metric based delay to compensate differing
positions of microphones or speakers.
For example, you have recorded guitar with two microphones placed in
different locations. Because the front of sound wave has fixed speed in
normal conditions, the phasing of microphones can vary and depends on
their location and interposition. The best sound mix can be achieved when
these microphones are in phase (synchronized). Note that a distance of
~30 cm between microphones makes one microphone capture the signal in
antiphase to the other microphone. That makes the final mix sound moody.
This filter helps to solve phasing problems by adding different delays
to each microphone track and make them synchronized.
The best result can be reached when you take one track as base and
synchronize other tracks one by one with it.
Remember that synchronization/delay tolerance depends on sample rate, too.
Higher sample rates will give more tolerance.
The filter accepts the following parameters:
mm
Set millimeters distance. This is compensation distance for fine tuning.
Default is 0.
cm
Set cm distance. This is compensation distance for tightening distance setup.
Default is 0.
m
Set meters distance. This is compensation distance for hard distance setup.
Default is 0.
dry
Set dry amount. Amount of unprocessed (dry) signal.
Default is 0.
wet
Set wet amount. Amount of processed (wet) signal.
Default is 1.
temp
Set temperature in degrees Celsius. This is the temperature of the environment.
Default is 20.
36.78.1 Commands
This filter supports the all above options as commands.
36.79 crossfeed
Apply headphone crossfeed filter.
Crossfeed is the process of blending the left and right channels of stereo
audio recording.
It is mainly used to reduce extreme stereo separation of low frequencies.
The intent is to produce more speaker like sound to the listener.
The filter accepts the following options:
strength
Set strength of crossfeed. Default is 0.2. Allowed range is from 0 to 1.
This sets gain of low shelf filter for side part of stereo image.
Default is -6dB. Max allowed is -30db when strength is set to 1.
range
Set soundstage wideness. Default is 0.5. Allowed range is from 0 to 1.
This sets cut off frequency of low shelf filter. Default is cut off near
1550 Hz. With range set to 1 cut off frequency is set to 2100 Hz.
slope
Set curve slope of low shelf filter. Default is 0.5.
Allowed range is from 0.01 to 1.
level_in
Set input gain. Default is 0.9.
level_out
Set output gain. Default is 1.
block_size
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.79.1 Commands
This filter supports the all above options as commands.
36.80 crystalizer
Simple algorithm for audio noise sharpening.
This filter linearly increases differences between each audio sample.
The filter accepts the following options:
i
Sets the intensity of effect (default: 2.0). Must be in range between -10.0 to 0
(unchanged sound) to 10.0 (maximum effect).
To inverse filtering use negative value.
c
Enable clipping. By default is enabled.
36.80.1 Commands
This filter supports the all above options as commands.
36.81 dcshift
Apply a DC shift to the audio.
This can be useful to remove a DC offset (caused perhaps by a hardware problem
in the recording chain) from the audio. The effect of a DC offset is reduced
headroom and hence volume. The astats filter can be used to determine if
a signal has a DC offset.
shift
Set the DC shift, allowed range is [-1, 1]. It indicates the amount to shift
the audio.
limitergain
Optional. It should have a value much less than 1 (e.g. 0.05 or 0.02) and is
used to prevent clipping.
36.82 deesser
Apply de-essing to the audio samples.
i
Set intensity for triggering de-essing. Allowed range is from 0 to 1.
Default is 0.
m
Set amount of ducking on treble part of sound. Allowed range is from 0 to 1.
Default is 0.5.
f
How much of original frequency content to keep when de-essing. Allowed range is from 0 to 1.
Default is 0.5.
s
Set the output mode.
It accepts the following values:
i
Pass input unchanged.
o
Pass ess filtered out.
e
Pass only ess.
Default value is o.
36.83 dialoguenhance
Enhance dialogue in stereo audio.
This filter accepts stereo input and produce surround (3.0) channels output.
The newly produced front center channel have enhanced speech dialogue originally
available in both stereo channels.
This filter outputs front left and front right channels same as available in stereo input.
The filter accepts the following options:
original
Set the original center factor to keep in front center channel output.
Allowed range is from 0 to 1. Default value is 1.
enhance
Set the dialogue enhance factor to put in front center channel output.
Allowed range is from 0 to 3. Default value is 1.
voice
Set the voice detection factor.
Allowed range is from 2 to 32. Default value is 2.
36.83.1 Commands
This filter supports the all above options as commands.
36.84 drmeter
Measure audio dynamic range.
DR values of 14 and higher is found in very dynamic material. DR of 8 to 13
is found in transition material. And anything less that 8 have very poor dynamics
and is very compressed.
The filter accepts the following options:
length
Set window length in seconds used to split audio into segments of equal length.
Default is 3 seconds.
36.85 dynaudnorm
Dynamic Audio Normalizer.
This filter applies a certain amount of gain to the input audio in order
to bring its peak magnitude to a target level (e.g. 0 dBFS). However, in
contrast to more "simple" normalization algorithms, the Dynamic Audio
Normalizer *dynamically* re-adjusts the gain factor to the input audio.
This allows for applying extra gain to the "quiet" sections of the audio
while avoiding distortions or clipping the "loud" sections. In other words:
The Dynamic Audio Normalizer will "even out" the volume of quiet and loud
sections, in the sense that the volume of each section is brought to the
same target level. Note, however, that the Dynamic Audio Normalizer achieves
this goal *without* applying "dynamic range compressing". It will retain 100%
of the dynamic range *within* each section of the audio file.
framelen, f
Set the frame length in milliseconds. In range from 10 to 8000 milliseconds.
Default is 500 milliseconds.
The Dynamic Audio Normalizer processes the input audio in small chunks,
referred to as frames. This is required, because a peak magnitude has no
meaning for just a single sample value. Instead, we need to determine the
peak magnitude for a contiguous sequence of sample values. While a "standard"
normalizer would simply use the peak magnitude of the complete file, the
Dynamic Audio Normalizer determines the peak magnitude individually for each
frame. The length of a frame is specified in milliseconds. By default, the
Dynamic Audio Normalizer uses a frame length of 500 milliseconds, which has
been found to give good results with most files.
Note that the exact frame length, in number of samples, will be determined
automatically, based on the sampling rate of the individual input audio file.
gausssize, g
Set the Gaussian filter window size. In range from 3 to 301, must be odd
number. Default is 31.
Probably the most important parameter of the Dynamic Audio Normalizer is the
window size of the Gaussian smoothing filter. The filter’s window size
is specified in frames, centered around the current frame. For the sake of
simplicity, this must be an odd number. Consequently, the default value of 31
takes into account the current frame, as well as the 15 preceding frames and
the 15 subsequent frames. Using a larger window results in a stronger
smoothing effect and thus in less gain variation, i.e. slower gain
adaptation. Conversely, using a smaller window results in a weaker smoothing
effect and thus in more gain variation, i.e. faster gain adaptation.
In other words, the more you increase this value, the more the Dynamic Audio
Normalizer will behave like a "traditional" normalization filter. On the
contrary, the more you decrease this value, the more the Dynamic Audio
Normalizer will behave like a dynamic range compressor.
peak, p
Set the target peak value. This specifies the highest permissible magnitude
level for the normalized audio input. This filter will try to approach the
target peak magnitude as closely as possible, but at the same time it also
makes sure that the normalized signal will never exceed the peak magnitude.
A frame’s maximum local gain factor is imposed directly by the target peak
magnitude. The default value is 0.95 and thus leaves a headroom of 5%*.
It is not recommended to go above this value.
maxgain, m
Set the maximum gain factor. In range from 1.0 to 100.0. Default is 10.0.
The Dynamic Audio Normalizer determines the maximum possible (local) gain
factor for each input frame, i.e. the maximum gain factor that does not
result in clipping or distortion. The maximum gain factor is determined by
the frame’s highest magnitude sample. However, the Dynamic Audio Normalizer
additionally bounds the frame’s maximum gain factor by a predetermined
(global) maximum gain factor. This is done in order to avoid excessive gain
factors in "silent" or almost silent frames. By default, the maximum gain
factor is 10.0, For most inputs the default value should be sufficient and
it usually is not recommended to increase this value. Though, for input
with an extremely low overall volume level, it may be necessary to allow even
higher gain factors. Note, however, that the Dynamic Audio Normalizer does
not simply apply a "hard" threshold (i.e. cut off values above the threshold).
Instead, a "sigmoid" threshold function will be applied. This way, the
gain factors will smoothly approach the threshold value, but never exceed that
value.
targetrms, r
Set the target RMS. In range from 0.0 to 1.0. Default is 0.0 - disabled.
By default, the Dynamic Audio Normalizer performs "peak" normalization.
This means that the maximum local gain factor for each frame is defined
(only) by the frame’s highest magnitude sample. This way, the samples can
be amplified as much as possible without exceeding the maximum signal
level, i.e. without clipping. Optionally, however, the Dynamic Audio
Normalizer can also take into account the frame’s root mean square,
abbreviated RMS. In electrical engineering, the RMS is commonly used to
determine the power of a time-varying signal. It is therefore considered
that the RMS is a better approximation of the "perceived loudness" than
just looking at the signal’s peak magnitude. Consequently, by adjusting all
frames to a constant RMS value, a uniform "perceived loudness" can be
established. If a target RMS value has been specified, a frame’s local gain
factor is defined as the factor that would result in exactly that RMS value.
Note, however, that the maximum local gain factor is still restricted by the
frame’s highest magnitude sample, in order to prevent clipping.
coupling, n
Enable channels coupling. By default is enabled.
By default, the Dynamic Audio Normalizer will amplify all channels by the same
amount. This means the same gain factor will be applied to all channels, i.e.
the maximum possible gain factor is determined by the "loudest" channel.
However, in some recordings, it may happen that the volume of the different
channels is uneven, e.g. one channel may be "quieter" than the other one(s).
In this case, this option can be used to disable the channel coupling. This way,
the gain factor will be determined independently for each channel, depending
only on the individual channel’s highest magnitude sample. This allows for
harmonizing the volume of the different channels.
correctdc, c
Enable DC bias correction. By default is disabled.
An audio signal (in the time domain) is a sequence of sample values.
In the Dynamic Audio Normalizer these sample values are represented in the
-1.0 to 1.0 range, regardless of the original input format. Normally, the
audio signal, or "waveform", should be centered around the zero point.
That means if we calculate the mean value of all samples in a file, or in a
single frame, then the result should be 0.0 or at least very close to that
value. If, however, there is a significant deviation of the mean value from
0.0, in either positive or negative direction, this is referred to as a
DC bias or DC offset. Since a DC bias is clearly undesirable, the Dynamic
Audio Normalizer provides optional DC bias correction.
With DC bias correction enabled, the Dynamic Audio Normalizer will determine
the mean value, or "DC correction" offset, of each input frame and subtract
that value from all of the frame’s sample values which ensures those samples
are centered around 0.0 again. Also, in order to avoid "gaps" at the frame
boundaries, the DC correction offset values will be interpolated smoothly
between neighbouring frames.
altboundary, b
Enable alternative boundary mode. By default is disabled.
The Dynamic Audio Normalizer takes into account a certain neighbourhood
around each frame. This includes the preceding frames as well as the
subsequent frames. However, for the "boundary" frames, located at the very
beginning and at the very end of the audio file, not all neighbouring
frames are available. In particular, for the first few frames in the audio
file, the preceding frames are not known. And, similarly, for the last few
frames in the audio file, the subsequent frames are not known. Thus, the
question arises which gain factors should be assumed for the missing frames
in the "boundary" region. The Dynamic Audio Normalizer implements two modes
to deal with this situation. The default boundary mode assumes a gain factor
of exactly 1.0 for the missing frames, resulting in a smooth "fade in" and
"fade out" at the beginning and at the end of the input, respectively.
compress, s
Set the compress factor. In range from 0.0 to 30.0. Default is 0.0.
By default, the Dynamic Audio Normalizer does not apply "traditional"
compression. This means that signal peaks will not be pruned and thus the
full dynamic range will be retained within each local neighbourhood. However,
in some cases it may be desirable to combine the Dynamic Audio Normalizer’s
normalization algorithm with a more "traditional" compression.
For this purpose, the Dynamic Audio Normalizer provides an optional compression
(thresholding) function. If (and only if) the compression feature is enabled,
all input frames will be processed by a soft knee thresholding function prior
to the actual normalization process. Put simply, the thresholding function is
going to prune all samples whose magnitude exceeds a certain threshold value.
However, the Dynamic Audio Normalizer does not simply apply a fixed threshold
value. Instead, the threshold value will be adjusted for each individual
frame.
In general, smaller parameters result in stronger compression, and vice versa.
Values below 3.0 are not recommended, because audible distortion may appear.
threshold, t
Set the target threshold value. This specifies the lowest permissible
magnitude level for the audio input which will be normalized.
If input frame volume is above this value frame will be normalized.
Otherwise frame may not be normalized at all. The default value is set
to 0, which means all input frames will be normalized.
This option is mostly useful if digital noise is not wanted to be amplified.
channels, h
Specify which channels to filter, by default all available channels are filtered.
overlap, o
Specify overlap for frames. If set to 0 (default) no frame overlapping is done.
Using >0 and <1 values will make less conservative gain adjustments, like
when framelen option is set to smaller value, if framelen option value is
compensated for non-zero overlap then gain adjustments will be smoother across time
compared to zero overlap case.
curve, v
Specify the peak mapping curve expression which is going to be used when calculating
gain applied to frames. The max output frame gain will still be limited by other
options mentioned previously for this filter.
The expression can contain the following constants:
ch
current channel number
sn
current sample number
nb_channels
number of channels
t
timestamp expressed in seconds
sr
sample rate
p
current frame peak value
36.85.1 Commands
This filter supports the all above options as commands.
36.86 earwax
Make audio easier to listen to on headphones.
This filter adds ‘cues’ to 44.1kHz stereo (i.e. audio CD format) audio
so that when listened to on headphones the stereo image is moved from
inside your head (standard for headphones) to outside and in front of
the listener (standard for speakers).
Ported from SoX.
36.87 equalizer
Apply a two-pole peaking equalisation (EQ) filter. With this
filter, the signal-level at and around a selected frequency can
be increased or decreased, whilst (unlike bandpass and bandreject
filters) that at all other frequencies is unchanged.
In order to produce complex equalisation curves, this filter can
be given several times, each with a different central frequency.
The filter accepts the following options:
frequency, f
Set the filter’s central frequency in Hz.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Specify the band-width of a filter in width_type units.
gain, g
Set the required gain or attenuation in dB.
Beware of clipping when using a positive gain.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.87.1 Examples
Attenuate 10 dB at 1000 Hz, with a bandwidth of 200 Hz:
equalizer=f=1000:t=h:width=200:g=-10
Apply 2 dB gain at 1000 Hz with Q 1 and attenuate 5 dB at 100 Hz with Q 2:
equalizer=f=1000:t=q:w=1:g=2,equalizer=f=100:t=q:w=2:g=-5
36.87.2 Commands
This filter supports the following commands:
frequency, f
Change equalizer frequency.
Syntax for the command is : "frequency"
width_type, t
Change equalizer width_type.
Syntax for the command is : "width_type"
width, w
Change equalizer width.
Syntax for the command is : "width"
gain, g
Change equalizer gain.
Syntax for the command is : "gain"
mix, m
Change equalizer mix.
Syntax for the command is : "mix"
36.88 extrastereo
Linearly increases the difference between left and right channels which
adds some sort of "live" effect to playback.
The filter accepts the following options:
m
Sets the difference coefficient (default: 2.5). 0.0 means mono sound
(average of both channels), with 1.0 sound will be unchanged, with
-1.0 left and right channels will be swapped.
c
Enable clipping. By default is enabled.
36.88.1 Commands
This filter supports the all above options as commands.
36.89 firequalizer
Apply FIR Equalization using arbitrary frequency response.
The filter accepts the following option:
gain
Set gain curve equation (in dB). The expression can contain variables:
f
the evaluated frequency
sr
sample rate
ch
channel number, set to 0 when multichannels evaluation is disabled
chid
channel id, see libavutil/channel_layout.h, set to the first channel id when
multichannels evaluation is disabled
chs
number of channels
chlayout
channel_layout, see libavutil/channel_layout.h
and functions:
gain_interpolate(f)
interpolate gain on frequency f based on gain_entry
cubic_interpolate(f)
same as gain_interpolate, but smoother
This option is also available as command. Default is gain_interpolate(f).
gain_entry
Set gain entry for gain_interpolate function. The expression can
contain functions:
entry(f, g)
store gain entry at frequency f with value g
This option is also available as command.
delay
Set filter delay in seconds. Higher value means more accurate.
Default is 0.01.
accuracy
Set filter accuracy in Hz. Lower value means more accurate.
Default is 5.
wfunc
Set window function. Acceptable values are:
rectangular
rectangular window, useful when gain curve is already smooth
hann
hann window (default)
hamming
hamming window
blackman
blackman window
nuttall3
3-terms continuous 1st derivative nuttall window
mnuttall3
minimum 3-terms discontinuous nuttall window
nuttall
4-terms continuous 1st derivative nuttall window
bnuttall
minimum 4-terms discontinuous nuttall (blackman-nuttall) window
bharris
blackman-harris window
tukey
tukey window
fixed
If enabled, use fixed number of audio samples. This improves speed when
filtering with large delay. Default is disabled.
multi
Enable multichannels evaluation on gain. Default is disabled.
zero_phase
Enable zero phase mode by subtracting timestamp to compensate delay.
Default is disabled.
scale
Set scale used by gain. Acceptable values are:
linlin
linear frequency, linear gain
linlog
linear frequency, logarithmic (in dB) gain (default)
loglin
logarithmic (in octave scale where 20 Hz is 0) frequency, linear gain
loglog
logarithmic frequency, logarithmic gain
dumpfile
Set file for dumping, suitable for gnuplot.
dumpscale
Set scale for dumpfile. Acceptable values are same with scale option.
Default is linlog.
fft2
Enable 2-channel convolution using complex FFT. This improves speed significantly.
Default is disabled.
min_phase
Enable minimum phase impulse response. Default is disabled.
36.89.1 Examples
lowpass at 1000 Hz:
firequalizer=gain='if(lt(f,1000), 0, -INF)'
lowpass at 1000 Hz with gain_entry:
firequalizer=gain_entry='entry(1000,0); entry(1001, -INF)'
custom equalization:
firequalizer=gain_entry='entry(100,0); entry(400, -4); entry(1000, -6); entry(2000, 0)'
higher delay with zero phase to compensate delay:
firequalizer=delay=0.1:fixed=on:zero_phase=on
lowpass on left channel, highpass on right channel:
firequalizer=gain='if(eq(chid,1), gain_interpolate(f), if(eq(chid,2), gain_interpolate(1e6+f), 0))'
:gain_entry='entry(1000, 0); entry(1001,-INF); entry(1e6+1000,0)':multi=on
36.90 flanger
Apply a flanging effect to the audio.
The filter accepts the following options:
delay
Set base delay in milliseconds. Range from 0 to 30. Default value is 0.
depth
Set added sweep delay in milliseconds. Range from 0 to 10. Default value is 2.
regen
Set percentage regeneration (delayed signal feedback). Range from -95 to 95.
Default value is 0.
width
Set percentage of delayed signal mixed with original. Range from 0 to 100.
Default value is 71.
speed
Set sweeps per second (Hz). Range from 0.1 to 10. Default value is 0.5.
shape
Set swept wave shape, can be triangular or sinusoidal.
Default value is sinusoidal.
phase
Set swept wave percentage-shift for multi channel. Range from 0 to 100.
Default value is 25.
interp
Set delay-line interpolation, linear or quadratic.
Default is linear.
36.91 haas
Apply Haas effect to audio.
Note that this makes most sense to apply on mono signals.
With this filter applied to mono signals it give some directionality and
stretches its stereo image.
The filter accepts the following options:
level_in
Set input level. By default is 1, or 0dB
level_out
Set output level. By default is 1, or 0dB.
side_gain
Set gain applied to side part of signal. By default is 1.
middle_source
Set kind of middle source. Can be one of the following:
‘left’
Pick left channel.
‘right’
Pick right channel.
‘mid’
Pick middle part signal of stereo image.
‘side’
Pick side part signal of stereo image.
middle_phase
Change middle phase. By default is disabled.
left_delay
Set left channel delay. By default is 2.05 milliseconds.
left_balance
Set left channel balance. By default is -1.
left_gain
Set left channel gain. By default is 1.
left_phase
Change left phase. By default is disabled.
right_delay
Set right channel delay. By defaults is 2.12 milliseconds.
right_balance
Set right channel balance. By default is 1.
right_gain
Set right channel gain. By default is 1.
right_phase
Change right phase. By default is enabled.
36.92 hdcd
Decodes High Definition Compatible Digital (HDCD) data. A 16-bit PCM stream with
embedded HDCD codes is expanded into a 20-bit PCM stream.
The filter supports the Peak Extend and Low-level Gain Adjustment features
of HDCD, and detects the Transient Filter flag.
ffmpeg -i HDCD16.flac -af hdcd OUT24.flac
When using the filter with wav, note the default encoding for wav is 16-bit,
so the resulting 20-bit stream will be truncated back to 16-bit. Use something
like -acodec pcm_s24le after the filter to get 24-bit PCM output.
ffmpeg -i HDCD16.wav -af hdcd OUT16.wav
ffmpeg -i HDCD16.wav -af hdcd -c:a pcm_s24le OUT24.wav
The filter accepts the following options:
disable_autoconvert
Disable any automatic format conversion or resampling in the filter graph.
process_stereo
Process the stereo channels together. If target_gain does not match between
channels, consider it invalid and use the last valid target_gain.
cdt_ms
Set the code detect timer period in ms.
force_pe
Always extend peaks above -3dBFS even if PE isn’t signaled.
analyze_mode
Replace audio with a solid tone and adjust the amplitude to signal some
specific aspect of the decoding process. The output file can be loaded in
an audio editor alongside the original to aid analysis.
analyze_mode=pe:force_pe=true can be used to see all samples above the PE level.
Modes are:
‘0, off’
Disabled
‘1, lle’
Gain adjustment level at each sample
‘2, pe’
Samples where peak extend occurs
‘3, cdt’
Samples where the code detect timer is active
‘4, tgm’
Samples where the target gain does not match between channels
36.93 headphone
Apply head-related transfer functions (HRTFs) to create virtual
loudspeakers around the user for binaural listening via headphones.
The HRIRs are provided via additional streams, for each channel
one stereo input stream is needed.
The filter accepts the following options:
map
Set mapping of input streams for convolution.
The argument is a ’|’-separated list of channel names in order as they
are given as additional stream inputs for filter.
This also specify number of input streams. Number of input streams
must be not less than number of channels in first stream plus one.
gain
Set gain applied to audio. Value is in dB. Default is 0.
type
Set processing type. Can be time or freq. time is
processing audio in time domain which is slow.
freq is processing audio in frequency domain which is fast.
Default is freq.
lfe
Set custom gain for LFE channels. Value is in dB. Default is 0.
size
Set size of frame in number of samples which will be processed at once.
Default value is 1024. Allowed range is from 1024 to 96000.
hrir
Set format of hrir stream.
Default value is stereo. Alternative value is multich.
If value is set to stereo, number of additional streams should
be greater or equal to number of input channels in first input stream.
Also each additional stream should have stereo number of channels.
If value is set to multich, number of additional streams should
be exactly one. Also number of input channels of additional stream
should be equal or greater than twice number of channels of first input
stream.
36.93.1 Examples
Full example using wav files as coefficients with amovie filters for 7.1 downmix,
each amovie filter use stereo file with IR coefficients as input.
The files give coefficients for each position of virtual loudspeaker:
ffmpeg -i input.wav
-filter_complex "amovie=azi_270_ele_0_DFC.wav[sr];amovie=azi_90_ele_0_DFC.wav[sl];amovie=azi_225_ele_0_DFC.wav[br];amovie=azi_135_ele_0_DFC.wav[bl];amovie=azi_0_ele_0_DFC.wav,asplit[fc][lfe];amovie=azi_35_ele_0_DFC.wav[fl];amovie=azi_325_ele_0_DFC.wav[fr];[0:a][fl][fr][fc][lfe][bl][br][sl][sr]headphone=FL|FR|FC|LFE|BL|BR|SL|SR"
output.wav
Full example using wav files as coefficients with amovie filters for 7.1 downmix,
but now in multich hrir format.
ffmpeg -i input.wav -filter_complex "amovie=minp.wav[hrirs];[0:a][hrirs]headphone=map=FL|FR|FC|LFE|BL|BR|SL|SR:hrir=multich"
output.wav
36.94 highpass
Apply a high-pass filter with 3dB point frequency.
The filter can be either single-pole, or double-pole (the default).
The filter roll off at 6dB per pole per octave (20dB per pole per decade).
The filter accepts the following options:
frequency, f
Set frequency in Hz. Default is 3000.
poles, p
Set number of poles. Default is 2.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Specify the band-width of a filter in width_type units.
Applies only to double-pole filter.
The default is 0.707q and gives a Butterworth response.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.94.1 Commands
This filter supports the following commands:
frequency, f
Change highpass frequency.
Syntax for the command is : "frequency"
width_type, t
Change highpass width_type.
Syntax for the command is : "width_type"
width, w
Change highpass width.
Syntax for the command is : "width"
mix, m
Change highpass mix.
Syntax for the command is : "mix"
36.95 join
Join multiple input streams into one multi-channel stream.
It accepts the following parameters:
inputs
The number of input streams. It defaults to 2.
channel_layout
The desired output channel layout. It defaults to stereo.
map
Map channels from inputs to output. The argument is a ’|’-separated list of
mappings, each in the input_idx.in_channel-out_channel
form. input_idx is the 0-based index of the input stream. in_channel
can be either the name of the input channel (e.g. FL for front left) or its
index in the specified input stream. out_channel is the name of the output
channel.
The filter will attempt to guess the mappings when they are not specified
explicitly. It does so by first trying to find an unused matching input channel
and if that fails it picks the first unused input channel.
Join 3 inputs (with properly set channel layouts):
ffmpeg -i INPUT1 -i INPUT2 -i INPUT3 -filter_complex join=inputs=3 OUTPUT
Build a 5.1 output from 6 single-channel streams:
ffmpeg -i fl -i fr -i fc -i sl -i sr -i lfe -filter_complex
'join=inputs=6:channel_layout=5.1:map=0.0-FL|1.0-FR|2.0-FC|3.0-SL|4.0-SR|5.0-LFE'
out
36.96 ladspa
Load a LADSPA (Linux Audio Developer’s Simple Plugin API) plugin.
To enable compilation of this filter you need to configure FFmpeg with
--enable-ladspa.
file, f
Specifies the name of LADSPA plugin library to load. If the environment
variable LADSPA_PATH is defined, the LADSPA plugin is searched in
each one of the directories specified by the colon separated list in
LADSPA_PATH, otherwise in the standard LADSPA paths, which are in
this order: HOME/.ladspa/lib/, /usr/local/lib/ladspa/,
/usr/lib/ladspa/.
plugin, p
Specifies the plugin within the library. Some libraries contain only
one plugin, but others contain many of them. If this is not set filter
will list all available plugins within the specified library.
controls, c
Set the ’|’ separated list of controls which are zero or more floating point
values that determine the behavior of the loaded plugin (for example delay,
threshold or gain).
Controls need to be defined using the following syntax:
c0=value0|c1=value1|c2=value2|..., where
valuei is the value set on the i-th control.
Alternatively they can be also defined using the following syntax:
value0|value1|value2|..., where
valuei is the value set on the i-th control.
If controls is set to help, all available controls and
their valid ranges are printed.
sample_rate, s
Specify the sample rate, default to 44100. Only used if plugin have
zero inputs.
nb_samples, n
Set the number of samples per channel per each output frame, default
is 1024. Only used if plugin have zero inputs.
duration, d
Set the minimum duration of the sourced audio. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
Note that the resulting duration may be greater than the specified duration,
as the generated audio is always cut at the end of a complete frame.
If not specified, or the expressed duration is negative, the audio is
supposed to be generated forever.
Only used if plugin have zero inputs.
latency, l
Enable latency compensation, by default is disabled.
Only used if plugin have inputs.
36.96.1 Examples
List all available plugins within amp (LADSPA example plugin) library:
ladspa=file=amp
List all available controls and their valid ranges for vcf_notch
plugin from VCF library:
ladspa=f=vcf:p=vcf_notch:c=help
Simulate low quality audio equipment using Computer Music Toolkit (CMT)
plugin library:
ladspa=file=cmt:plugin=lofi:controls=c0=22|c1=12|c2=12
Add reverberation to the audio using TAP-plugins
(Tom’s Audio Processing plugins):
ladspa=file=tap_reverb:tap_reverb
Generate white noise, with 0.2 amplitude:
ladspa=file=cmt:noise_source_white:c=c0=.2
Generate 20 bpm clicks using plugin C* Click - Metronome from the
C* Audio Plugin Suite (CAPS) library:
ladspa=file=caps:Click:c=c1=20'
Apply C* Eq10X2 - Stereo 10-band equaliser effect:
ladspa=caps:Eq10X2:c=c0=-48|c9=-24|c3=12|c4=2
Increase volume by 20dB using fast lookahead limiter from Steve Harris
SWH Plugins collection:
ladspa=fast_lookahead_limiter_1913:fastLookaheadLimiter:20|0|2
Attenuate low frequencies using Multiband EQ from Steve Harris
SWH Plugins collection:
ladspa=mbeq_1197:mbeq:-24|-24|-24|0|0|0|0|0|0|0|0|0|0|0|0
Reduce stereo image using Narrower from the C* Audio Plugin Suite
(CAPS) library:
ladspa=caps:Narrower
Another white noise, now using C* Audio Plugin Suite (CAPS) library:
ladspa=caps:White:.2
Some fractal noise, using C* Audio Plugin Suite (CAPS) library:
ladspa=caps:Fractal:c=c1=1
Dynamic volume normalization using VLevel plugin:
ladspa=vlevel-ladspa:vlevel_mono
36.96.2 Commands
This filter supports the following commands:
cN
Modify the N-th control value.
If the specified value is not valid, it is ignored and prior one is kept.
36.97 loudnorm
EBU R128 loudness normalization. Includes both dynamic and linear normalization modes.
Support for both single pass (livestreams, files) and double pass (files) modes.
This algorithm can target IL, LRA, and maximum true peak. In dynamic mode, to accurately
detect true peaks, the audio stream will be upsampled to 192 kHz.
Use the -ar option or aresample filter to explicitly set an output sample rate.
The filter accepts the following options:
I, i
Set integrated loudness target.
Range is -70.0 - -5.0. Default value is -24.0.
LRA, lra
Set loudness range target.
Range is 1.0 - 50.0. Default value is 7.0.
TP, tp
Set maximum true peak.
Range is -9.0 - +0.0. Default value is -2.0.
measured_I, measured_i
Measured IL of input file.
Range is -99.0 - +0.0.
measured_LRA, measured_lra
Measured LRA of input file.
Range is  0.0 - 99.0.
measured_TP, measured_tp
Measured true peak of input file.
Range is  -99.0 - +99.0.
measured_thresh
Measured threshold of input file.
Range is -99.0 - +0.0.
offset
Set offset gain. Gain is applied before the true-peak limiter.
Range is  -99.0 - +99.0. Default is +0.0.
linear
Normalize by linearly scaling the source audio.
measured_I, measured_LRA, measured_TP,
and measured_thresh must all be specified. Target LRA shouldn’t
be lower than source LRA and the change in integrated loudness shouldn’t
result in a true peak which exceeds the target TP. If any of these
conditions aren’t met, normalization mode will revert to dynamic.
Options are true or false. Default is true.
dual_mono
Treat mono input files as "dual-mono". If a mono file is intended for playback
on a stereo system, its EBU R128 measurement will be perceptually incorrect.
If set to true, this option will compensate for this effect.
Multi-channel input files are not affected by this option.
Options are true or false. Default is false.
print_format
Set print format for stats. Options are summary, json, or none.
Default value is none.
36.98 lowpass
Apply a low-pass filter with 3dB point frequency.
The filter can be either single-pole or double-pole (the default).
The filter roll off at 6dB per pole per octave (20dB per pole per decade).
The filter accepts the following options:
frequency, f
Set frequency in Hz. Default is 500.
poles, p
Set number of poles. Default is 2.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Specify the band-width of a filter in width_type units.
Applies only to double-pole filter.
The default is 0.707q and gives a Butterworth response.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.98.1 Examples
Lowpass only LFE channel, it LFE is not present it does nothing:
lowpass=c=LFE
36.98.2 Commands
This filter supports the following commands:
frequency, f
Change lowpass frequency.
Syntax for the command is : "frequency"
width_type, t
Change lowpass width_type.
Syntax for the command is : "width_type"
width, w
Change lowpass width.
Syntax for the command is : "width"
mix, m
Change lowpass mix.
Syntax for the command is : "mix"
36.99 lv2
Load a LV2 (LADSPA Version 2) plugin.
To enable compilation of this filter you need to configure FFmpeg with
--enable-lv2.
plugin, p
Specifies the plugin URI. You may need to escape ’:’.
controls, c
Set the ’|’ separated list of controls which are zero or more floating point
values that determine the behavior of the loaded plugin (for example delay,
threshold or gain).
If controls is set to help, all available controls and
their valid ranges are printed.
sample_rate, s
Specify the sample rate, default to 44100. Only used if plugin have
zero inputs.
nb_samples, n
Set the number of samples per channel per each output frame, default
is 1024. Only used if plugin have zero inputs.
duration, d
Set the minimum duration of the sourced audio. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
Note that the resulting duration may be greater than the specified duration,
as the generated audio is always cut at the end of a complete frame.
If not specified, or the expressed duration is negative, the audio is
supposed to be generated forever.
Only used if plugin have zero inputs.
36.99.1 Examples
Apply bass enhancer plugin from Calf:
lv2=p=http\\\\://calf.sourceforge.net/plugins/BassEnhancer:c=amount=2
Apply vinyl plugin from Calf:
lv2=p=http\\\\://calf.sourceforge.net/plugins/Vinyl:c=drone=0.2|aging=0.5
Apply bit crusher plugin from ArtyFX:
lv2=p=http\\\\://www.openavproductions.com/artyfx#bitta:c=crush=0.3
36.99.2 Commands
This filter supports all options that are exported by plugin as commands.
36.100 mcompand
Multiband Compress or expand the audio’s dynamic range.
The input audio is divided into bands using 4th order Linkwitz-Riley IIRs.
This is akin to the crossover of a loudspeaker, and results in flat frequency
response when absent compander action.
It accepts the following parameters:
args
This option syntax is:
attack,decay,[attack,decay..] soft-knee points crossover_frequency [delay [initial_volume [gain]]] | attack,decay ...
For explanation of each item refer to compand filter documentation.
36.101 pan
Mix channels with specific gain levels. The filter accepts the output
channel layout followed by a set of channels definitions.
This filter is also designed to efficiently remap the channels of an audio
stream.
The filter accepts parameters of the form:
"l|outdef|outdef|..."
l
output channel layout or number of channels
outdef
output channel specification, of the form:
"out_name=[gain*]in_name[(+-)[gain*]in_name...]"
out_name
output channel to define, either a channel name (FL, FR, etc.) or a channel
number (c0, c1, etc.)
gain
multiplicative coefficient for the channel, 1 leaving the volume unchanged
in_name
input channel to use, see out_name for details; it is not possible to mix
named and numbered input channels
If the ‘=’ in a channel specification is replaced by ‘<’, then the gains for
that specification will be renormalized so that the total is 1, thus
avoiding clipping noise.
36.101.1 Mixing examples
For example, if you want to down-mix from stereo to mono, but with a bigger
factor for the left channel:
pan=1c|c0=0.9*c0+0.1*c1
A customized down-mix to stereo that works automatically for 3-, 4-, 5- and
7-channels surround:
pan=stereo| FL < FL + 0.5*FC + 0.6*BL + 0.6*SL | FR < FR + 0.5*FC + 0.6*BR + 0.6*SR
Note that ffmpeg integrates a default down-mix (and up-mix) system
that should be preferred (see "-ac" option) unless you have very specific
needs.
36.101.2 Remapping examples
The channel remapping will be effective if, and only if:
gain coefficients are zeroes or ones,
only one input per channel output,
If all these conditions are satisfied, the filter will notify the user ("Pure
channel mapping detected"), and use an optimized and lossless method to do the
remapping.
For example, if you have a 5.1 source and want a stereo audio stream by
dropping the extra channels:
pan="stereo| c0=FL | c1=FR"
Given the same source, you can also switch front left and front right channels
and keep the input channel layout:
pan="5.1| c0=c1 | c1=c0 | c2=c2 | c3=c3 | c4=c4 | c5=c5"
If the input is a stereo audio stream, you can mute the front left channel (and
still keep the stereo channel layout) with:
pan="stereo|c1=c1"
Still with a stereo audio stream input, you can copy the right channel in both
front left and right:
pan="stereo| c0=FR | c1=FR"
36.102 replaygain
ReplayGain scanner filter. This filter takes an audio stream as an input and
outputs it unchanged.
At end of filtering it displays track_gain and track_peak.
The filter accepts the following exported read-only options:
track_gain
Exported track gain in dB at end of stream.
track_peak
Exported track peak at end of stream.
36.103 resample
Convert the audio sample format, sample rate and channel layout. It is
not meant to be used directly.
36.104 rubberband
Apply time-stretching and pitch-shifting with librubberband.
To enable compilation of this filter, you need to configure FFmpeg with
--enable-librubberband.
The filter accepts the following options:
tempo
Set tempo scale factor.
pitch
Set pitch scale factor.
transients
Set transients detector.
Possible values are:
crisp
mixed
smooth
detector
Set detector.
Possible values are:
compound
percussive
soft
phase
Set phase.
Possible values are:
laminar
independent
window
Set processing window size.
Possible values are:
standard
short
long
smoothing
Set smoothing.
Possible values are:
off
on
formant
Enable formant preservation when shift pitching.
Possible values are:
shifted
preserved
pitchq
Set pitch quality.
Possible values are:
quality
speed
consistency
channels
Set channels.
Possible values are:
apart
together
36.104.1 Commands
This filter supports the following commands:
tempo
Change filter tempo scale factor.
Syntax for the command is : "tempo"
pitch
Change filter pitch scale factor.
Syntax for the command is : "pitch"
36.105 sidechaincompress
This filter acts like normal compressor but has the ability to compress
detected signal using second input signal.
It needs two input streams and returns one output stream.
First input stream will be processed depending on second stream signal.
The filtered signal then can be filtered with other filters in later stages of
processing. See pan and amerge filter.
The filter accepts the following options:
level_in
Set input gain. Default is 1. Range is between 0.015625 and 64.
mode
Set mode of compressor operation. Can be upward or downward.
Default is downward.
threshold
If a signal of second stream raises above this level it will affect the gain
reduction of first stream.
By default is 0.125. Range is between 0.00097563 and 1.
ratio
Set a ratio about which the signal is reduced. 1:2 means that if the level
raised 4dB above the threshold, it will be only 2dB above after the reduction.
Default is 2. Range is between 1 and 20.
attack
Amount of milliseconds the signal has to rise above the threshold before gain
reduction starts. Default is 20. Range is between 0.01 and 2000.
release
Amount of milliseconds the signal has to fall below the threshold before
reduction is decreased again. Default is 250. Range is between 0.01 and 9000.
makeup
Set the amount by how much signal will be amplified after processing.
Default is 1. Range is from 1 to 64.
knee
Curve the sharp knee around the threshold to enter gain reduction more softly.
Default is 2.82843. Range is between 1 and 8.
link
Choose if the average level between all channels of side-chain stream
or the louder(maximum) channel of side-chain stream affects the
reduction. Default is average.
detection
Should the exact signal be taken in case of peak or an RMS one in case
of rms. Default is rms which is mainly smoother.
level_sc
Set sidechain gain. Default is 1. Range is between 0.015625 and 64.
mix
How much to use compressed signal in output. Default is 1.
Range is between 0 and 1.
36.105.1 Commands
This filter supports the all above options as commands.
36.105.2 Examples
Full ffmpeg example taking 2 audio inputs, 1st input to be compressed
depending on the signal of 2nd input and later compressed signal to be
merged with 2nd input:
ffmpeg -i main.flac -i sidechain.flac -filter_complex "[1:a]asplit=2[sc][mix];[0:a][sc]sidechaincompress[compr];[compr][mix]amerge"
36.106 sidechaingate
A sidechain gate acts like a normal (wideband) gate but has the ability to
filter the detected signal before sending it to the gain reduction stage.
Normally a gate uses the full range signal to detect a level above the
threshold.
For example: If you cut all lower frequencies from your sidechain signal
the gate will decrease the volume of your track only if not enough highs
appear. With this technique you are able to reduce the resonation of a
natural drum or remove "rumbling" of muted strokes from a heavily distorted
guitar.
It needs two input streams and returns one output stream.
First input stream will be processed depending on second stream signal.
The filter accepts the following options:
level_in
Set input level before filtering.
Default is 1. Allowed range is from 0.015625 to 64.
mode
Set the mode of operation. Can be upward or downward.
Default is downward. If set to upward mode, higher parts of signal
will be amplified, expanding dynamic range in upward direction.
Otherwise, in case of downward lower parts of signal will be reduced.
range
Set the level of gain reduction when the signal is below the threshold.
Default is 0.06125. Allowed range is from 0 to 1.
Setting this to 0 disables reduction and then filter behaves like expander.
threshold
If a signal rises above this level the gain reduction is released.
Default is 0.125. Allowed range is from 0 to 1.
ratio
Set a ratio about which the signal is reduced.
Default is 2. Allowed range is from 1 to 9000.
attack
Amount of milliseconds the signal has to rise above the threshold before gain
reduction stops.
Default is 20 milliseconds. Allowed range is from 0.01 to 9000.
release
Amount of milliseconds the signal has to fall below the threshold before the
reduction is increased again. Default is 250 milliseconds.
Allowed range is from 0.01 to 9000.
makeup
Set amount of amplification of signal after processing.
Default is 1. Allowed range is from 1 to 64.
knee
Curve the sharp knee around the threshold to enter gain reduction more softly.
Default is 2.828427125. Allowed range is from 1 to 8.
detection
Choose if exact signal should be taken for detection or an RMS like one.
Default is rms. Can be peak or rms.
link
Choose if the average level between all channels or the louder channel affects
the reduction.
Default is average. Can be average or maximum.
level_sc
Set sidechain gain. Default is 1. Range is from 0.015625 to 64.
36.106.1 Commands
This filter supports the all above options as commands.
36.107 silencedetect
Detect silence in an audio stream.
This filter logs a message when it detects that the input audio volume is less
or equal to a noise tolerance value for a duration greater or equal to the
minimum detected noise duration.
The printed times and duration are expressed in seconds. The
lavfi.silence_start or lavfi.silence_start.X metadata key
is set on the first frame whose timestamp equals or exceeds the detection
duration and it contains the timestamp of the first frame of the silence.
The lavfi.silence_duration or lavfi.silence_duration.X
and lavfi.silence_end or lavfi.silence_end.X metadata
keys are set on the first frame after the silence. If mono is
enabled, and each channel is evaluated separately, the .X
suffixed keys are used, and X corresponds to the channel number.
The filter accepts the following options:
noise, n
Set noise tolerance. Can be specified in dB (in case "dB" is appended to the
specified value) or amplitude ratio. Default is -60dB, or 0.001.
duration, d
Set silence duration until notification (default is 2 seconds). See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
mono, m
Process each channel separately, instead of combined. By default is disabled.
36.107.1 Examples
Detect 5 seconds of silence with -50dB noise tolerance:
silencedetect=n=-50dB:d=5
Complete example with ffmpeg to detect silence with 0.0001 noise
tolerance in silence.mp3:
ffmpeg -i silence.mp3 -af silencedetect=noise=0.0001 -f null -
36.108 silenceremove
Remove silence from the beginning, middle or end of the audio.
The filter accepts the following options:
start_periods
This value is used to indicate if audio should be trimmed at beginning of
the audio. A value of zero indicates no silence should be trimmed from the
beginning. When specifying a non-zero value, it trims audio up until it
finds non-silence. Normally, when trimming silence from beginning of audio
the start_periods will be 1 but it can be increased to higher
values to trim all audio up to specific count of non-silence periods.
Default value is 0.
start_duration
Specify the amount of time that non-silence must be detected before it stops
trimming audio. By increasing the duration, bursts of noises can be treated
as silence and trimmed off. Default value is 0.
start_threshold
This indicates what sample value should be treated as silence. For digital
audio, a value of 0 may be fine but for audio recorded from analog,
you may wish to increase the value to account for background noise.
Can be specified in dB (in case "dB" is appended to the specified value)
or amplitude ratio. Default value is 0.
start_silence
Specify max duration of silence at beginning that will be kept after
trimming. Default is 0, which is equal to trimming all samples detected
as silence.
start_mode
Specify mode of detection of silence end at start of multi-channel audio.
Can be any or all. Default is any.
With any, any sample from any channel that is detected as non-silence
will trigger end of silence trimming at start of audio stream.
With all, only if every sample from every channel is detected as non-silence
will trigger end of silence trimming at start of audio stream, limited usage.
stop_periods
Set the count for trimming silence from the end of audio. When specifying a
positive value, it trims audio after it finds specified silence period.
To remove silence from the middle of a file, specify a stop_periods
that is negative. This value is then treated as a positive value and is
used to indicate the effect should restart processing as specified by
stop_periods, making it suitable for removing periods of silence
in the middle of the audio.
Default value is 0.
stop_duration
Specify a duration of silence that must exist before audio is not copied any
more. By specifying a higher duration, silence that is wanted can be left in
the audio.
Default value is 0.
stop_threshold
This is the same as start_threshold but for trimming silence from
the end of audio.
Can be specified in dB (in case "dB" is appended to the specified value)
or amplitude ratio. Default value is 0.
stop_silence
Specify max duration of silence at end that will be kept after
trimming. Default is 0, which is equal to trimming all samples detected
as silence.
stop_mode
Specify mode of detection of silence start after start of multi-channel audio.
Can be any or all. Default is all.
With any, any sample from any channel that is detected as silence
will trigger start of silence trimming after start of audio stream, limited usage.
With all, only if every sample from every channel is detected as silence
will trigger start of silence trimming after start of audio stream.
detection
Set how is silence detected.
avg
Mean of absolute values of samples in moving window.
rms
Root squared mean of absolute values of samples in moving window.
peak
Maximum of absolute values of samples in moving window.
median
Median of absolute values of samples in moving window.
ptp
Absolute of max peak to min peak difference of samples in moving window.
dev
Standard deviation of values of samples in moving window.
Default value is rms.
window
Set duration in number of seconds used to calculate size of window in number
of samples for detecting silence. Using 0 will effectively disable
any windowing and use only single sample per channel for silence detection.
In that case it may be needed to also set start_silence and/or
stop_silence to nonzero values with also start_duration and/or
stop_duration to nonzero values.
Default value is 0.02. Allowed range is from 0 to 10.
timestamp
Set processing mode of every audio frame output timestamp.
write
Full timestamps rewrite, keep only the start time for the first output frame.
copy
Non-dropped frames are left with same timestamp as input audio frame.
Defaults value is write.
36.108.1 Examples
The following example shows how this filter can be used to start a recording
that does not contain the delay at the start which usually occurs between
pressing the record button and the start of the performance:
silenceremove=start_periods=1:start_duration=5:start_threshold=0.02
Trim all silence encountered from beginning to end where there is more than 1
second of silence in audio:
silenceremove=stop_periods=-1:stop_duration=1:stop_threshold=-90dB
Trim all digital silence samples, using peak detection, from beginning to end
where there is more than 0 samples of digital silence in audio and digital
silence is detected in all channels at same positions in stream:
silenceremove=window=0:detection=peak:stop_mode=all:start_mode=all:stop_periods=-1:stop_threshold=0
Trim every 2nd encountered silence period from beginning to end where there is
more than 1 second of silence per silence period in audio:
silenceremove=stop_periods=-2:stop_duration=1:stop_threshold=-90dB
Similar as above, but keep maximum of 0.5 seconds of silence from each trimmed period:
silenceremove=stop_periods=-2:stop_duration=1:stop_threshold=-90dB:stop_silence=0.5
Similar as above, but keep maximum of 1.5 seconds of silence from start of audio:
silenceremove=stop_periods=-2:stop_duration=1:stop_threshold=-90dB:stop_silence=0.5:start_periods=1:start_duration=1:start_silence=1.5:stop_threshold=-90dB
36.108.2 Commands
This filter supports some above options as commands.
36.109 sofalizer
SOFAlizer uses head-related transfer functions (HRTFs) to create virtual
loudspeakers around the user for binaural listening via headphones (audio
formats up to 9 channels supported).
The HRTFs are stored in SOFA files (see http://www.sofacoustics.org/ for a database).
SOFAlizer is developed at the Acoustics Research Institute (ARI) of the
Austrian Academy of Sciences.
To enable compilation of this filter you need to configure FFmpeg with
--enable-libmysofa.
The filter accepts the following options:
sofa
Set the SOFA file used for rendering.
gain
Set gain applied to audio. Value is in dB. Default is 0.
rotation
Set rotation of virtual loudspeakers in deg. Default is 0.
elevation
Set elevation of virtual speakers in deg. Default is 0.
radius
Set distance in meters between loudspeakers and the listener with near-field
HRTFs. Default is 1.
type
Set processing type. Can be time or freq. time is
processing audio in time domain which is slow.
freq is processing audio in frequency domain which is fast.
Default is freq.
speakers
Set custom positions of virtual loudspeakers. Syntax for this option is:
<CH> <AZIM> <ELEV>[|<CH> <AZIM> <ELEV>|...].
Each virtual loudspeaker is described with short channel name following with
azimuth and elevation in degrees.
Each virtual loudspeaker description is separated by ’|’.
For example to override front left and front right channel positions use:
’speakers=FL 45 15|FR 345 15’.
Descriptions with unrecognised channel names are ignored.
lfegain
Set custom gain for LFE channels. Value is in dB. Default is 0.
framesize
Set custom frame size in number of samples. Default is 1024.
Allowed range is from 1024 to 96000. Only used if option ‘type’
is set to freq.
normalize
Should all IRs be normalized upon importing SOFA file.
By default is enabled.
interpolate
Should nearest IRs be interpolated with neighbor IRs if exact position
does not match. By default is disabled.
minphase
Minphase all IRs upon loading of SOFA file. By default is disabled.
anglestep
Set neighbor search angle step. Only used if option interpolate is enabled.
radstep
Set neighbor search radius step. Only used if option interpolate is enabled.
36.109.1 Examples
Using ClubFritz6 sofa file:
sofalizer=sofa=/path/to/ClubFritz6.sofa:type=freq:radius=1
Using ClubFritz12 sofa file and bigger radius with small rotation:
sofalizer=sofa=/path/to/ClubFritz12.sofa:type=freq:radius=2:rotation=5
Similar as above but with custom speaker positions for front left, front right, back left and back right
and also with custom gain:
"sofalizer=sofa=/path/to/ClubFritz6.sofa:type=freq:radius=2:speakers=FL 45|FR 315|BL 135|BR 225:gain=28"
36.110 speechnorm
Speech Normalizer.
This filter expands or compresses each half-cycle of audio samples
(local set of samples all above or all below zero and between two nearest zero crossings) depending
on threshold value, so audio reaches target peak value under conditions controlled by below options.
The filter accepts the following options:
peak, p
Set the expansion target peak value. This specifies the highest allowed absolute amplitude
level for the normalized audio input. Default value is 0.95. Allowed range is from 0.0 to 1.0.
expansion, e
Set the maximum expansion factor. Allowed range is from 1.0 to 50.0. Default value is 2.0.
This option controls maximum local half-cycle of samples expansion. The maximum expansion
would be such that local peak value reaches target peak value but never to surpass it and that
ratio between new and previous peak value does not surpass this option value.
compression, c
Set the maximum compression factor. Allowed range is from 1.0 to 50.0. Default value is 2.0.
This option controls maximum local half-cycle of samples compression. This option is used
only if threshold option is set to value greater than 0.0, then in such cases
when local peak is lower or same as value set by threshold all samples belonging to
that peak’s half-cycle will be compressed by current compression factor.
threshold, t
Set the threshold value. Default value is 0.0. Allowed range is from 0.0 to 1.0.
This option specifies which half-cycles of samples will be compressed and which will be expanded.
Any half-cycle samples with their local peak value below or same as this option value will be
compressed by current compression factor, otherwise, if greater than threshold value they will be
expanded with expansion factor so that it could reach peak target value but never surpass it.
raise, r
Set the expansion raising amount per each half-cycle of samples. Default value is 0.001.
Allowed range is from 0.0 to 1.0. This controls how fast expansion factor is raised per
each new half-cycle until it reaches expansion value.
Setting this options too high may lead to distortions.
fall, f
Set the compression raising amount per each half-cycle of samples. Default value is 0.001.
Allowed range is from 0.0 to 1.0. This controls how fast compression factor is raised per
each new half-cycle until it reaches compression value.
channels, h
Specify which channels to filter, by default all available channels are filtered.
invert, i
Enable inverted filtering, by default is disabled. This inverts interpretation of threshold
option. When enabled any half-cycle of samples with their local peak value below or same as
threshold option will be expanded otherwise it will be compressed.
link, l
Link channels when calculating gain applied to each filtered channel sample, by default is disabled.
When disabled each filtered channel gain calculation is independent, otherwise when this option
is enabled the minimum of all possible gains for each filtered channel is used.
rms, m
Set the expansion target RMS value. This specifies the highest allowed RMS level for the normalized
audio input. Default value is 0.0, thus disabled. Allowed range is from 0.0 to 1.0.
36.110.1 Commands
This filter supports the all above options as commands.
36.110.2 Examples
Weak and slow amplification:
speechnorm=e=3:r=0.00001:l=1
Moderate and slow amplification:
speechnorm=e=6.25:r=0.00001:l=1
Strong and fast amplification:
speechnorm=e=12.5:r=0.0001:l=1
Very strong and fast amplification:
speechnorm=e=25:r=0.0001:l=1
Extreme and fast amplification:
speechnorm=e=50:r=0.0001:l=1
36.111 stereotools
This filter has some handy utilities to manage stereo signals, for converting
M/S stereo recordings to L/R signal while having control over the parameters
or spreading the stereo image of master track.
The filter accepts the following options:
level_in
Set input level before filtering for both channels. Defaults is 1.
Allowed range is from 0.015625 to 64.
level_out
Set output level after filtering for both channels. Defaults is 1.
Allowed range is from 0.015625 to 64.
balance_in
Set input balance between both channels. Default is 0.
Allowed range is from -1 to 1.
balance_out
Set output balance between both channels. Default is 0.
Allowed range is from -1 to 1.
softclip
Enable softclipping. Results in analog distortion instead of harsh digital 0dB
clipping. Disabled by default.
mutel
Mute the left channel. Disabled by default.
muter
Mute the right channel. Disabled by default.
phasel
Change the phase of the left channel. Disabled by default.
phaser
Change the phase of the right channel. Disabled by default.
mode
Set stereo mode. Available values are:
‘lr>lr’
Left/Right to Left/Right, this is default.
‘lr>ms’
Left/Right to Mid/Side.
‘ms>lr’
Mid/Side to Left/Right.
‘lr>ll’
Left/Right to Left/Left.
‘lr>rr’
Left/Right to Right/Right.
‘lr>l+r’
Left/Right to Left + Right.
‘lr>rl’
Left/Right to Right/Left.
‘ms>ll’
Mid/Side to Left/Left.
‘ms>rr’
Mid/Side to Right/Right.
‘ms>rl’
Mid/Side to Right/Left.
‘lr>l-r’
Left/Right to Left - Right.
slev
Set level of side signal. Default is 1.
Allowed range is from 0.015625 to 64.
sbal
Set balance of side signal. Default is 0.
Allowed range is from -1 to 1.
mlev
Set level of the middle signal. Default is 1.
Allowed range is from 0.015625 to 64.
mpan
Set middle signal pan. Default is 0. Allowed range is from -1 to 1.
base
Set stereo base between mono and inversed channels. Default is 0.
Allowed range is from -1 to 1.
delay
Set delay in milliseconds how much to delay left from right channel and
vice versa. Default is 0. Allowed range is from -20 to 20.
sclevel
Set S/C level. Default is 1. Allowed range is from 1 to 100.
phase
Set the stereo phase in degrees. Default is 0. Allowed range is from 0 to 360.
bmode_in, bmode_out
Set balance mode for balance_in/balance_out option.
Can be one of the following:
‘balance’
Classic balance mode. Attenuate one channel at time.
Gain is raised up to 1.
‘amplitude’
Similar as classic mode above but gain is raised up to 2.
‘power’
Equal power distribution, from -6dB to +6dB range.
36.111.1 Commands
This filter supports the all above options as commands.
36.111.2 Examples
Apply karaoke like effect:
stereotools=mlev=0.015625
Convert M/S signal to L/R:
"stereotools=mode=ms>lr"
36.112 stereowiden
This filter enhance the stereo effect by suppressing signal common to both
channels and by delaying the signal of left into right and vice versa,
thereby widening the stereo effect.
The filter accepts the following options:
delay
Time in milliseconds of the delay of left signal into right and vice versa.
Default is 20 milliseconds.
feedback
Amount of gain in delayed signal into right and vice versa. Gives a delay
effect of left signal in right output and vice versa which gives widening
effect. Default is 0.3.
crossfeed
Cross feed of left into right with inverted phase. This helps in suppressing
the mono. If the value is 1 it will cancel all the signal common to both
channels. Default is 0.3.
drymix
Set level of input signal of original channel. Default is 0.8.
36.112.1 Commands
This filter supports the all above options except delay as commands.
36.113 superequalizer
Apply 18 band equalizer.
The filter accepts the following options:
1b
Set 65Hz band gain.
2b
Set 92Hz band gain.
3b
Set 131Hz band gain.
4b
Set 185Hz band gain.
5b
Set 262Hz band gain.
6b
Set 370Hz band gain.
7b
Set 523Hz band gain.
8b
Set 740Hz band gain.
9b
Set 1047Hz band gain.
10b
Set 1480Hz band gain.
11b
Set 2093Hz band gain.
12b
Set 2960Hz band gain.
13b
Set 4186Hz band gain.
14b
Set 5920Hz band gain.
15b
Set 8372Hz band gain.
16b
Set 11840Hz band gain.
17b
Set 16744Hz band gain.
18b
Set 20000Hz band gain.
36.114 surround
Apply audio surround upmix filter.
This filter allows to produce multichannel output from audio stream.
The filter accepts the following options:
chl_out
Set output channel layout. By default, this is 5.1.
See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual
for the required syntax.
chl_in
Set input channel layout. By default, this is stereo.
See (ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1) manual
for the required syntax.
level_in
Set input volume level. By default, this is 1.
level_out
Set output volume level. By default, this is 1.
lfe
Enable LFE channel output if output channel layout has it. By default, this is enabled.
lfe_low
Set LFE low cut off frequency. By default, this is 128 Hz.
lfe_high
Set LFE high cut off frequency. By default, this is 256 Hz.
lfe_mode
Set LFE mode, can be add or sub. Default is add.
In add mode, LFE channel is created from input audio and added to output.
In sub mode, LFE channel is created from input audio and added to output but
also all non-LFE output channels are subtracted with output LFE channel.
smooth
Set temporal smoothness strength, used to gradually change factors when transforming
stereo sound in time. Allowed range is from 0.0 to 1.0.
Useful to improve output quality with focus option values greater than 0.0.
Default is 0.0. Only values inside this range and without edges are effective.
angle
Set angle of stereo surround transform, Allowed range is from 0 to 360.
Default is 90.
focus
Set focus of stereo surround transform, Allowed range is from -1 to 1.
Default is 0.
fc_in
Set front center input volume. By default, this is 1.
fc_out
Set front center output volume. By default, this is 1.
fl_in
Set front left input volume. By default, this is 1.
fl_out
Set front left output volume. By default, this is 1.
fr_in
Set front right input volume. By default, this is 1.
fr_out
Set front right output volume. By default, this is 1.
sl_in
Set side left input volume. By default, this is 1.
sl_out
Set side left output volume. By default, this is 1.
sr_in
Set side right input volume. By default, this is 1.
sr_out
Set side right output volume. By default, this is 1.
bl_in
Set back left input volume. By default, this is 1.
bl_out
Set back left output volume. By default, this is 1.
br_in
Set back right input volume. By default, this is 1.
br_out
Set back right output volume. By default, this is 1.
bc_in
Set back center input volume. By default, this is 1.
bc_out
Set back center output volume. By default, this is 1.
lfe_in
Set LFE input volume. By default, this is 1.
lfe_out
Set LFE output volume. By default, this is 1.
allx
Set spread usage of stereo image across X axis for all channels.
Allowed range is from -1 to 15.
By default this value is negative -1, and thus unused.
ally
Set spread usage of stereo image across Y axis for all channels.
Allowed range is from -1 to 15.
By default this value is negative -1, and thus unused.
fcx, flx, frx, blx, brx, slx, srx, bcx
Set spread usage of stereo image across X axis for each channel.
Allowed range is from 0.06 to 15.
By default this value is 0.5.
fcy, fly, fry, bly, bry, sly, sry, bcy
Set spread usage of stereo image across Y axis for each channel.
Allowed range is from 0.06 to 15.
By default this value is 0.5.
win_size
Set window size. Allowed range is from 1024 to 65536. Default size is 4096.
win_func
Set window function.
It accepts the following values:
‘rect’
‘bartlett’
‘hann, hanning’
‘hamming’
‘blackman’
‘welch’
‘flattop’
‘bharris’
‘bnuttall’
‘bhann’
‘sine’
‘nuttall’
‘lanczos’
‘gauss’
‘tukey’
‘dolph’
‘cauchy’
‘parzen’
‘poisson’
‘bohman’
‘kaiser’
Default is hann.
overlap
Set window overlap. If set to 1, the recommended overlap for selected
window function will be picked. Default is 0.5.
36.115 tiltshelf
Boost or cut the lower frequencies and cut or boost higher frequencies
of the audio using a two-pole shelving filter with a response similar to
that of a standard hi-fi’s tone-controls.
This is also known as shelving equalisation (EQ).
The filter accepts the following options:
gain, g
Give the gain at 0 Hz. Its useful range is about -20
(for a large cut) to +20 (for a large boost).
Beware of clipping when using a positive gain.
frequency, f
Set the filter’s central frequency and so can be used
to extend or reduce the frequency range to be boosted or cut.
The default value is 3000 Hz.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Determine how steep is the filter’s shelf transition.
poles, p
Set number of poles. Default is 2.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.115.1 Commands
This filter supports some options as commands.
36.116 treble, highshelf
Boost or cut treble (upper) frequencies of the audio using a two-pole
shelving filter with a response similar to that of a standard
hi-fi’s tone-controls. This is also known as shelving equalisation (EQ).
The filter accepts the following options:
gain, g
Give the gain at whichever is the lower of ~22 kHz and the
Nyquist frequency. Its useful range is about -20 (for a large cut)
to +20 (for a large boost). Beware of clipping when using a positive gain.
frequency, f
Set the filter’s central frequency and so can be used
to extend or reduce the frequency range to be boosted or cut.
The default value is 3000 Hz.
width_type, t
Set method to specify band-width of filter.
h
Hz
q
Q-Factor
o
octave
s
slope
k
kHz
width, w
Determine how steep is the filter’s shelf transition.
poles, p
Set number of poles. Default is 2.
mix, m
How much to use filtered signal in output. Default is 1.
Range is between 0 and 1.
channels, c
Specify which channels to filter, by default all available are filtered.
normalize, n
Normalize biquad coefficients, by default is disabled.
Enabling it will normalize magnitude response at DC to 0dB.
transform, a
Set transform type of IIR filter.
di
dii
tdi
tdii
latt
svf
zdf
precision, r
Set precision of filtering.
auto
Pick automatic sample format depending on surround filters.
s16
Always use signed 16-bit.
s32
Always use signed 32-bit.
f32
Always use float 32-bit.
f64
Always use float 64-bit.
block_size, b
Set block size used for reverse IIR processing. If this value is set to high enough
value (higher than impulse response length truncated when reaches near zero values) filtering
will become linear phase otherwise if not big enough it will just produce nasty artifacts.
Note that filter delay will be exactly this many samples when set to non-zero value.
36.116.1 Commands
This filter supports the following commands:
frequency, f
Change treble frequency.
Syntax for the command is : "frequency"
width_type, t
Change treble width_type.
Syntax for the command is : "width_type"
width, w
Change treble width.
Syntax for the command is : "width"
gain, g
Change treble gain.
Syntax for the command is : "gain"
mix, m
Change treble mix.
Syntax for the command is : "mix"
36.117 tremolo
Sinusoidal amplitude modulation.
The filter accepts the following options:
f
Modulation frequency in Hertz. Modulation frequencies in the subharmonic range
(20 Hz or lower) will result in a tremolo effect.
This filter may also be used as a ring modulator by specifying
a modulation frequency higher than 20 Hz.
Range is 0.1 - 20000.0. Default value is 5.0 Hz.
d
Depth of modulation as a percentage. Range is 0.0 - 1.0.
Default value is 0.5.
36.118 vibrato
Sinusoidal phase modulation.
The filter accepts the following options:
f
Modulation frequency in Hertz.
Range is 0.1 - 20000.0. Default value is 5.0 Hz.
d
Depth of modulation as a percentage. Range is 0.0 - 1.0.
Default value is 0.5.
36.119 virtualbass
Apply audio Virtual Bass filter.
This filter accepts stereo input and produce stereo with LFE (2.1) channels output.
The newly produced LFE channel have enhanced virtual bass originally obtained from both stereo channels.
This filter outputs front left and front right channels unchanged as available in stereo input.
The filter accepts the following options:
cutoff
Set the virtual bass cutoff frequency. Default value is 250 Hz.
Allowed range is from 100 to 500 Hz.
strength
Set the virtual bass strength. Allowed range is from 0.5 to 3.
Default value is 3.
36.120 volume
Adjust the input audio volume.
It accepts the following parameters:
volume
Set audio volume expression.
Output values are clipped to the maximum value.
The output audio volume is given by the relation:
output_volume = volume * input_volume
The default value for volume is "1.0".
precision
This parameter represents the mathematical precision.
It determines which input sample formats will be allowed, which affects the
precision of the volume scaling.
fixed
8-bit fixed-point; this limits input sample format to U8, S16, and S32.
float
32-bit floating-point; this limits input sample format to FLT. (default)
double
64-bit floating-point; this limits input sample format to DBL.
replaygain
Choose the behaviour on encountering ReplayGain side data in input frames.
drop
Remove ReplayGain side data, ignoring its contents (the default).
ignore
Ignore ReplayGain side data, but leave it in the frame.
track
Prefer the track gain, if present.
album
Prefer the album gain, if present.
replaygain_preamp
Pre-amplification gain in dB to apply to the selected replaygain gain.
Default value for replaygain_preamp is 0.0.
replaygain_noclip
Prevent clipping by limiting the gain applied.
Default value for replaygain_noclip is 1.
eval
Set when the volume expression is evaluated.
It accepts the following values:
‘once’
only evaluate expression once during the filter initialization, or
when the ‘volume’ command is sent
‘frame’
evaluate expression for each incoming frame
Default value is ‘once’.
The volume expression can contain the following parameters.
n
frame number (starting at zero)
nb_channels
number of channels
nb_consumed_samples
number of samples consumed by the filter
nb_samples
number of samples in the current frame
pos
original frame position in the file; deprecated, do not use
pts
frame PTS
sample_rate
sample rate
startpts
PTS at start of stream
startt
time at start of stream
t
frame time
tb
timestamp timebase
volume
last set volume value
Note that when eval is set to ‘once’ only the
sample_rate and tb variables are available, all other
variables will evaluate to NAN.
36.120.1 Commands
This filter supports the following commands:
volume
Modify the volume expression.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
36.120.2 Examples
Halve the input audio volume:
volume=volume=0.5
volume=volume=1/2
volume=volume=-6.0206dB
In all the above example the named key for volume can be
omitted, for example like in:
volume=0.5
Increase input audio power by 6 decibels using fixed-point precision:
volume=volume=6dB:precision=fixed
Fade volume after time 10 with an annihilation period of 5 seconds:
volume='if(lt(t,10),1,max(1-(t-10)/5,0))':eval=frame
36.121 volumedetect
Detect the volume of the input video.
The filter has no parameters. It supports only 16-bit signed integer samples,
so the input will be converted when needed. Statistics about the volume will
be printed in the log when the input stream end is reached.
In particular it will show the mean volume (root mean square), maximum
volume (on a per-sample basis), and the beginning of a histogram of the
registered volume values (from the maximum value to a cumulated 1/1000 of
the samples).
All volumes are in decibels relative to the maximum PCM value.
36.121.1 Examples
Here is an excerpt of the output:
[Parsed_volumedetect_0  0xa23120] mean_volume: -27 dB
[Parsed_volumedetect_0  0xa23120] max_volume: -4 dB
[Parsed_volumedetect_0  0xa23120] histogram_4db: 6
[Parsed_volumedetect_0  0xa23120] histogram_5db: 62
[Parsed_volumedetect_0  0xa23120] histogram_6db: 286
[Parsed_volumedetect_0  0xa23120] histogram_7db: 1042
[Parsed_volumedetect_0  0xa23120] histogram_8db: 2551
[Parsed_volumedetect_0  0xa23120] histogram_9db: 4609
[Parsed_volumedetect_0  0xa23120] histogram_10db: 8409
It means that:
The mean square energy is approximately -27 dB, or 10^-2.7.
The largest sample is at -4 dB, or more precisely between -4 dB and -5 dB.
There are 6 samples at -4 dB, 62 at -5 dB, 286 at -6 dB, etc.
In other words, raising the volume by +4 dB does not cause any clipping,
raising it by +5 dB causes clipping for 6 samples, etc.
37 Audio Sources
Below is a description of the currently available audio sources.
37.1 abuffer
Buffer audio frames, and make them available to the filter chain.
This source is mainly intended for a programmatic use, in particular
through the interface defined in libavfilter/buffersrc.h.
It accepts the following parameters:
time_base
The timebase which will be used for timestamps of submitted frames. It must be
either a floating-point number or in numerator/denominator form.
sample_rate
The sample rate of the incoming audio buffers.
sample_fmt
The sample format of the incoming audio buffers.
Either a sample format name or its corresponding integer representation from
the enum AVSampleFormat in libavutil/samplefmt.h
channel_layout
The channel layout of the incoming audio buffers.
Either a channel layout name from channel_layout_map in
libavutil/channel_layout.c or its corresponding integer representation
from the AV_CH_LAYOUT_* macros in libavutil/channel_layout.h
channels
The number of channels of the incoming audio buffers.
If both channels and channel_layout are specified, then they
must be consistent.
37.1.1 Examples
abuffer=sample_rate=44100:sample_fmt=s16p:channel_layout=stereo
will instruct the source to accept planar 16bit signed stereo at 44100Hz.
Since the sample format with name "s16p" corresponds to the number
6 and the "stereo" channel layout corresponds to the value 0x3, this is
equivalent to:
abuffer=sample_rate=44100:sample_fmt=6:channel_layout=0x3
37.2 aevalsrc
Generate an audio signal specified by an expression.
This source accepts in input one or more expressions (one for each
channel), which are evaluated and used to generate a corresponding
audio signal.
This source accepts the following options:
exprs
Set the ’|’-separated expressions list for each separate channel. In case the
channel_layout option is not specified, the selected channel layout
depends on the number of provided expressions. Otherwise the last
specified expression is applied to the remaining output channels.
channel_layout, c
Set the channel layout. The number of channels in the specified layout
must be equal to the number of specified expressions.
duration, d
Set the minimum duration of the sourced audio. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
Note that the resulting duration may be greater than the specified
duration, as the generated audio is always cut at the end of a
complete frame.
If not specified, or the expressed duration is negative, the audio is
supposed to be generated forever.
nb_samples, n
Set the number of samples per channel per each output frame,
default to 1024.
sample_rate, s
Specify the sample rate, default to 44100.
Each expression in exprs can contain the following constants:
n
number of the evaluated sample, starting from 0
t
time of the evaluated sample expressed in seconds, starting from 0
s
sample rate
37.2.1 Examples
Generate silence:
aevalsrc=0
Generate a sin signal with frequency of 440 Hz, set sample rate to
8000 Hz:
aevalsrc="sin(440*2*PI*t):s=8000"
Generate a two channels signal, specify the channel layout (Front
Center + Back Center) explicitly:
aevalsrc="sin(420*2*PI*t)|cos(430*2*PI*t):c=FC|BC"
Generate white noise:
aevalsrc="-2+random(0)"
Generate an amplitude modulated signal:
aevalsrc="sin(10*2*PI*t)*sin(880*2*PI*t)"
Generate 2.5 Hz binaural beats on a 360 Hz carrier:
aevalsrc="0.1*sin(2*PI*(360-2.5/2)*t) | 0.1*sin(2*PI*(360+2.5/2)*t)"
37.3 afdelaysrc
Generate a fractional delay FIR coefficients.
The resulting stream can be used with afir filter for filtering the audio signal.
The filter accepts the following options:
delay, d
Set the fractional delay. Default is 0.
sample_rate, r
Set the sample rate, default is 44100.
nb_samples, n
Set the number of samples per each frame. Default is 1024.
taps, t
Set the number of filter coefficients in output audio stream.
Default value is 0.
channel_layout, c
Specifies the channel layout, and can be a string representing a channel layout.
The default value of channel_layout is "stereo".
37.4 afireqsrc
Generate a FIR equalizer coefficients.
The resulting stream can be used with afir filter for filtering the audio signal.
The filter accepts the following options:
preset, p
Set equalizer preset.
Default preset is flat.
Available presets are:
‘custom’
‘flat’
‘acoustic’
‘bass’
‘beats’
‘classic’
‘clear’
‘deep bass’
‘dubstep’
‘electronic’
‘hard-style’
‘hip-hop’
‘jazz’
‘metal’
‘movie’
‘pop’
‘r&b’
‘rock’
‘vocal booster’
gains, g
Set custom gains for each band. Only used if the preset option is set to custom.
Gains are separated by white spaces and each gain is set in dBFS.
Default is 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.
bands, b
Set the custom bands from where custon equalizer gains are set.
This must be in strictly increasing order. Only used if the preset option is set to custom.
Bands are separated by white spaces and each band represent frequency in Hz.
Default is 25 40 63 100 160 250 400 630 1000 1600 2500 4000 6300 10000 16000 24000.
taps, t
Set number of filter coefficients in output audio stream.
Default value is 4096.
sample_rate, r
Set sample rate of output audio stream, default is 44100.
nb_samples, n
Set number of samples per each frame in output audio stream. Default is 1024.
interp, i
Set interpolation method for FIR equalizer coefficients. Can be linear or cubic.
phase, h
Set phase type of FIR filter. Can be linear or min: minimum-phase.
Default is minimum-phase filter.
37.5 afirsrc
Generate a FIR coefficients using frequency sampling method.
The resulting stream can be used with afir filter for filtering the audio signal.
The filter accepts the following options:
taps, t
Set number of filter coefficients in output audio stream.
Default value is 1025.
frequency, f
Set frequency points from where magnitude and phase are set.
This must be in non decreasing order, and first element must be 0, while last element
must be 1. Elements are separated by white spaces.
magnitude, m
Set magnitude value for every frequency point set by frequency.
Number of values must be same as number of frequency points.
Values are separated by white spaces.
phase, p
Set phase value for every frequency point set by frequency.
Number of values must be same as number of frequency points.
Values are separated by white spaces.
sample_rate, r
Set sample rate, default is 44100.
nb_samples, n
Set number of samples per each frame. Default is 1024.
win_func, w
Set window function. Default is blackman.
37.6 anullsrc
The null audio source, return unprocessed audio frames. It is mainly useful
as a template and to be employed in analysis / debugging tools, or as
the source for filters which ignore the input data (for example the sox
synth filter).
This source accepts the following options:
channel_layout, cl
Specifies the channel layout, and can be either an integer or a string
representing a channel layout. The default value of channel_layout
is "stereo".
Check the channel_layout_map definition in
libavutil/channel_layout.c for the mapping between strings and
channel layout values.
sample_rate, r
Specifies the sample rate, and defaults to 44100.
nb_samples, n
Set the number of samples per requested frames.
duration, d
Set the duration of the sourced audio. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
If not specified, or the expressed duration is negative, the audio is
supposed to be generated forever.
37.6.1 Examples
Set the sample rate to 48000 Hz and the channel layout to AV_CH_LAYOUT_MONO.
anullsrc=r=48000:cl=4
Do the same operation with a more obvious syntax:
anullsrc=r=48000:cl=mono
All the parameters need to be explicitly defined.
37.7 flite
Synthesize a voice utterance using the libflite library.
To enable compilation of this filter you need to configure FFmpeg with
--enable-libflite.
Note that versions of the flite library prior to 2.0 are not thread-safe.
The filter accepts the following options:
list_voices
If set to 1, list the names of the available voices and exit
immediately. Default value is 0.
nb_samples, n
Set the maximum number of samples per frame. Default value is 512.
textfile
Set the filename containing the text to speak.
text
Set the text to speak.
voice, v
Set the voice to use for the speech synthesis. Default value is
kal. See also the list_voices option.
37.7.1 Examples
Read from file speech.txt, and synthesize the text using the
standard flite voice:
flite=textfile=speech.txt
Read the specified text selecting the slt voice:
flite=text='So fare thee well, poor devil of a Sub-Sub, whose commentator I am':voice=slt
Input text to ffmpeg:
ffmpeg -f lavfi -i flite=text='So fare thee well, poor devil of a Sub-Sub, whose commentator I am':voice=slt
Make ffplay speak the specified text, using flite and
the lavfi device:
ffplay -f lavfi flite=text='No more be grieved for which that thou hast done.'
For more information about libflite, check:
http://www.festvox.org/flite/
37.8 anoisesrc
Generate a noise audio signal.
The filter accepts the following options:
sample_rate, r
Specify the sample rate. Default value is 48000 Hz.
amplitude, a
Specify the amplitude (0.0 - 1.0) of the generated audio stream. Default value
is 1.0.
duration, d
Specify the duration of the generated audio stream. Not specifying this option
results in noise with an infinite length.
color, colour, c
Specify the color of noise. Available noise colors are white, pink, brown,
blue, violet and velvet. Default color is white.
seed, s
Specify a value used to seed the PRNG.
nb_samples, n
Set the number of samples per each output frame, default is 1024.
density
Set the density (0.0 - 1.0) for the velvet noise generator, default is 0.05.
37.8.1 Examples
Generate 60 seconds of pink noise, with a 44.1 kHz sampling rate and an amplitude of 0.5:
anoisesrc=d=60:c=pink:r=44100:a=0.5
37.9 hilbert
Generate odd-tap Hilbert transform FIR coefficients.
The resulting stream can be used with afir filter for phase-shifting
the signal by 90 degrees.
This is used in many matrix coding schemes and for analytic signal generation.
The process is often written as a multiplication by i (or j), the imaginary unit.
The filter accepts the following options:
sample_rate, s
Set sample rate, default is 44100.
taps, t
Set length of FIR filter, default is 22051.
nb_samples, n
Set number of samples per each frame.
win_func, w
Set window function to be used when generating FIR coefficients.
37.10 sinc
Generate a sinc kaiser-windowed low-pass, high-pass, band-pass, or band-reject FIR coefficients.
The resulting stream can be used with afir filter for filtering the audio signal.
The filter accepts the following options:
sample_rate, r
Set sample rate, default is 44100.
nb_samples, n
Set number of samples per each frame. Default is 1024.
hp
Set high-pass frequency. Default is 0.
lp
Set low-pass frequency. Default is 0.
If high-pass frequency is lower than low-pass frequency and low-pass frequency
is higher than 0 then filter will create band-pass filter coefficients,
otherwise band-reject filter coefficients.
phase
Set filter phase response. Default is 50. Allowed range is from 0 to 100.
beta
Set Kaiser window beta.
att
Set stop-band attenuation. Default is 120dB, allowed range is from 40 to 180 dB.
round
Enable rounding, by default is disabled.
hptaps
Set number of taps for high-pass filter.
lptaps
Set number of taps for low-pass filter.
37.11 sine
Generate an audio signal made of a sine wave with amplitude 1/8.
The audio signal is bit-exact.
The filter accepts the following options:
frequency, f
Set the carrier frequency. Default is 440 Hz.
beep_factor, b
Enable a periodic beep every second with frequency beep_factor times
the carrier frequency. Default is 0, meaning the beep is disabled.
sample_rate, r
Specify the sample rate, default is 44100.
duration, d
Specify the duration of the generated audio stream.
samples_per_frame
Set the number of samples per output frame.
The expression can contain the following constants:
n
The (sequential) number of the output audio frame, starting from 0.
pts
The PTS (Presentation TimeStamp) of the output audio frame,
expressed in TB units.
t
The PTS of the output audio frame, expressed in seconds.
TB
The timebase of the output audio frames.
Default is 1024.
37.11.1 Examples
Generate a simple 440 Hz sine wave:
sine
Generate a 220 Hz sine wave with a 880 Hz beep each second, for 5 seconds:
sine=220:4:d=5
sine=f=220:b=4:d=5
sine=frequency=220:beep_factor=4:duration=5
Generate a 1 kHz sine wave following 1602,1601,1602,1601,1602 NTSC
pattern:
sine=1000:samples_per_frame='st(0,mod(n,5)); 1602-not(not(eq(ld(0),1)+eq(ld(0),3)))'
38 Audio Sinks
Below is a description of the currently available audio sinks.
38.1 abuffersink
Buffer audio frames, and make them available to the end of filter chain.
This sink is mainly intended for programmatic use, in particular
through the interface defined in libavfilter/buffersink.h
or the options system.
It accepts a pointer to an AVABufferSinkContext structure, which
defines the incoming buffers’ formats, to be passed as the opaque
parameter to avfilter_init_filter for initialization.
38.2 anullsink
Null audio sink; do absolutely nothing with the input audio. It is
mainly useful as a template and for use in analysis / debugging
tools.
39 Video Filters
When you configure your FFmpeg build, you can disable any of the
existing filters using --disable-filters.
The configure output will show the video filters included in your
build.
Below is a description of the currently available video filters.
39.1 addroi
Mark a region of interest in a video frame.
The frame data is passed through unchanged, but metadata is attached
to the frame indicating regions of interest which can affect the
behaviour of later encoding.  Multiple regions can be marked by
applying the filter multiple times.
x
Region distance in pixels from the left edge of the frame.
y
Region distance in pixels from the top edge of the frame.
w
Region width in pixels.
h
Region height in pixels.
The parameters x, y, w and h are expressions,
and may contain the following variables:
iw
Width of the input frame.
ih
Height of the input frame.
qoffset
Quantisation offset to apply within the region.
This must be a real value in the range -1 to +1.  A value of zero
indicates no quality change.  A negative value asks for better quality
(less quantisation), while a positive value asks for worse quality
(greater quantisation).
The range is calibrated so that the extreme values indicate the
largest possible offset - if the rest of the frame is encoded with the
worst possible quality, an offset of -1 indicates that this region
should be encoded with the best possible quality anyway.  Intermediate
values are then interpolated in some codec-dependent way.
For example, in 10-bit H.264 the quantisation parameter varies between
-12 and 51.  A typical qoffset value of -1/10 therefore indicates that
this region should be encoded with a QP around one-tenth of the full
range better than the rest of the frame.  So, if most of the frame
were to be encoded with a QP of around 30, this region would get a QP
of around 24 (an offset of approximately -1/10 * (51 - -12) = -6.3).
An extreme value of -1 would indicate that this region should be
encoded with the best possible quality regardless of the treatment of
the rest of the frame - that is, should be encoded at a QP of -12.
clear
If set to true, remove any existing regions of interest marked on the
frame before adding the new one.
39.1.1 Examples
Mark the centre quarter of the frame as interesting.
addroi=iw/4:ih/4:iw/2:ih/2:-1/10
Mark the 100-pixel-wide region on the left edge of the frame as very
uninteresting (to be encoded at much lower quality than the rest of
the frame).
addroi=0:0:100:ih:+1/5
39.2 alphaextract
Extract the alpha component from the input as a grayscale video. This
is especially useful with the alphamerge filter.
39.3 alphamerge
Add or replace the alpha component of the primary input with the
grayscale value of a second input. This is intended for use with
alphaextract to allow the transmission or storage of frame
sequences that have alpha in a format that doesn’t support an alpha
channel.
For example, to reconstruct full frames from a normal YUV-encoded video
and a separate video created with alphaextract, you might use:
movie=in_alpha.mkv [alpha]; [in][alpha] alphamerge [out]
39.4 amplify
Amplify differences between current pixel and pixels of adjacent frames in
same pixel location.
This filter accepts the following options:
radius
Set frame radius. Default is 2. Allowed range is from 1 to 63.
For example radius of 3 will instruct filter to calculate average of 7 frames.
factor
Set factor to amplify difference. Default is 2. Allowed range is from 0 to 65535.
threshold
Set threshold for difference amplification. Any difference greater or equal to
this value will not alter source pixel. Default is 10.
Allowed range is from 0 to 65535.
tolerance
Set tolerance for difference amplification. Any difference lower to
this value will not alter source pixel. Default is 0.
Allowed range is from 0 to 65535.
low
Set lower limit for changing source pixel. Default is 65535. Allowed range is from 0 to 65535.
This option controls maximum possible value that will decrease source pixel value.
high
Set high limit for changing source pixel. Default is 65535. Allowed range is from 0 to 65535.
This option controls maximum possible value that will increase source pixel value.
planes
Set which planes to filter. Default is all. Allowed range is from 0 to 15.
39.4.1 Commands
This filter supports the following commands that corresponds to option of same name:
factor
threshold
tolerance
low
high
planes
39.5 ass
Same as the subtitles filter, except that it doesn’t require libavcodec
and libavformat to work. On the other hand, it is limited to ASS (Advanced
Substation Alpha) subtitles files.
This filter accepts the following option in addition to the common options from
the subtitles filter:
shaping
Set the shaping engine
Available values are:
‘auto’
The default libass shaping engine, which is the best available.
‘simple’
Fast, font-agnostic shaper that can do only substitutions
‘complex’
Slower shaper using OpenType for substitutions and positioning
The default is auto.
39.6 atadenoise
Apply an Adaptive Temporal Averaging Denoiser to the video input.
The filter accepts the following options:
0a
Set threshold A for 1st plane. Default is 0.02.
Valid range is 0 to 0.3.
0b
Set threshold B for 1st plane. Default is 0.04.
Valid range is 0 to 5.
1a
Set threshold A for 2nd plane. Default is 0.02.
Valid range is 0 to 0.3.
1b
Set threshold B for 2nd plane. Default is 0.04.
Valid range is 0 to 5.
2a
Set threshold A for 3rd plane. Default is 0.02.
Valid range is 0 to 0.3.
2b
Set threshold B for 3rd plane. Default is 0.04.
Valid range is 0 to 5.
Threshold A is designed to react on abrupt changes in the input signal and
threshold B is designed to react on continuous changes in the input signal.
s
Set number of frames filter will use for averaging. Default is 9. Must be odd
number in range [5, 129].
p
Set what planes of frame filter will use for averaging. Default is all.
a
Set what variant of algorithm filter will use for averaging. Default is p parallel.
Alternatively can be set to s serial.
Parallel can be faster then serial, while other way around is never true.
Parallel will abort early on first change being greater then thresholds, while serial
will continue processing other side of frames if they are equal or below thresholds.
0s
1s
2s
Set sigma for 1st plane, 2nd plane or 3rd plane. Default is 32767.
Valid range is from 0 to 32767.
This options controls weight for each pixel in radius defined by size.
Default value means every pixel have same weight.
Setting this option to 0 effectively disables filtering.
39.6.1 Commands
This filter supports same commands as options except option s.
The command accepts the same syntax of the corresponding option.
39.7 avgblur
Apply average blur filter.
The filter accepts the following options:
sizeX
Set horizontal radius size.
planes
Set which planes to filter. By default all planes are filtered.
sizeY
Set vertical radius size, if zero it will be same as sizeX.
Default is 0.
39.7.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.8 backgroundkey
Turns a static background into transparency.
The filter accepts the following option:
threshold
Threshold for scene change detection.
similarity
Similarity percentage with the background.
blend
Set the blend amount for pixels that are not similar.
39.8.1 Commands
This filter supports the all above options as commands.
39.9 bbox
Compute the bounding box for the non-black pixels in the input frame
luma plane.
This filter computes the bounding box containing all the pixels with a
luma value greater than the minimum allowed value.
The parameters describing the bounding box are printed on the filter
log.
The filter accepts the following option:
min_val
Set the minimal luma value. Default is 16.
39.9.1 Commands
This filter supports the all above options as commands.
39.10 bilateral
Apply bilateral filter, spatial smoothing while preserving edges.
The filter accepts the following options:
sigmaS
Set sigma of gaussian function to calculate spatial weight.
Allowed range is 0 to 512. Default is 0.1.
sigmaR
Set sigma of gaussian function to calculate range weight.
Allowed range is 0 to 1. Default is 0.1.
planes
Set planes to filter. Default is first only.
39.10.1 Commands
This filter supports the all above options as commands.
39.11 bilateral_cuda
CUDA accelerated bilateral filter, an edge preserving filter.
This filter is mathematically accurate thanks to the use of GPU acceleration.
For best output quality, use one to one chroma subsampling, i.e. yuv444p format.
The filter accepts the following options:
sigmaS
Set sigma of gaussian function to calculate spatial weight, also called sigma space.
Allowed range is 0.1 to 512. Default is 0.1.
sigmaR
Set sigma of gaussian function to calculate color range weight, also called sigma color.
Allowed range is 0.1 to 512. Default is 0.1.
window_size
Set window size of the bilateral function to determine the number of neighbours to loop on.
If the number entered is even, one will be added automatically.
Allowed range is 1 to 255. Default is 1.
39.11.1 Examples
Apply the bilateral filter on a video.
./ffmpeg -v verbose \
-hwaccel cuda -hwaccel_output_format cuda -i input.mp4  \
-init_hw_device cuda \
-filter_complex \
" \
[0:v]scale_cuda=format=yuv444p[scaled_video];
[scaled_video]bilateral_cuda=window_size=9:sigmaS=3.0:sigmaR=50.0" \
-an -sn -c:v h264_nvenc -cq 20 out.mp4
39.12 bitplanenoise
Show and measure bit plane noise.
The filter accepts the following options:
bitplane
Set which plane to analyze. Default is 1.
filter
Filter out noisy pixels from bitplane set above.
Default is disabled.
39.13 blackdetect
Detect video intervals that are (almost) completely black. Can be
useful to detect chapter transitions, commercials, or invalid
recordings.
The filter outputs its detection analysis to both the log as well as
frame metadata. If a black segment of at least the specified minimum
duration is found, a line with the start and end timestamps as well
as duration is printed to the log with level info. In addition,
a log line with level debug is printed per frame showing the
black amount detected for that frame.
The filter also attaches metadata to the first frame of a black
segment with key lavfi.black_start and to the first frame
after the black segment ends with key lavfi.black_end. The
value is the frame’s timestamp. This metadata is added regardless
of the minimum duration specified.
The filter accepts the following options:
black_min_duration, d
Set the minimum detected black duration expressed in seconds. It must
be a non-negative floating point number.
Default value is 2.0.
picture_black_ratio_th, pic_th
Set the threshold for considering a picture "black".
Express the minimum value for the ratio:
nb_black_pixels / nb_pixels
for which a picture is considered black.
Default value is 0.98.
pixel_black_th, pix_th
Set the threshold for considering a pixel "black".
The threshold expresses the maximum pixel luma value for which a
pixel is considered "black". The provided value is scaled according to
the following equation:
absolute_threshold = luma_minimum_value + pixel_black_th * luma_range_size
luma_range_size and luma_minimum_value depend on
the input video format, the range is [0-255] for YUV full-range
formats and [16-235] for YUV non full-range formats.
Default value is 0.10.
The following example sets the maximum pixel threshold to the minimum
value, and detects only black intervals of 2 or more seconds:
blackdetect=d=2:pix_th=0.00
39.14 blackframe
Detect frames that are (almost) completely black. Can be useful to
detect chapter transitions or commercials. Output lines consist of
the frame number of the detected frame, the percentage of blackness,
the position in the file if known or -1 and the timestamp in seconds.
In order to display the output lines, you need to set the loglevel at
least to the AV_LOG_INFO value.
This filter exports frame metadata lavfi.blackframe.pblack.
The value represents the percentage of pixels in the picture that
are below the threshold value.
It accepts the following parameters:
amount
The percentage of the pixels that have to be below the threshold; it defaults to
98.
threshold, thresh
The threshold below which a pixel value is considered black; it defaults to
32.
39.15 blend
Blend two video frames into each other.
The blend filter takes two input streams and outputs one
stream, the first input is the "top" layer and second input is
"bottom" layer.  By default, the output terminates when the longest input terminates.
The tblend (time blend) filter takes two consecutive frames
from one single stream, and outputs the result obtained by blending
the new frame on top of the old frame.
A description of the accepted options follows.
c0_mode
c1_mode
c2_mode
c3_mode
all_mode
Set blend mode for specific pixel component or all pixel components in case
of all_mode. Default value is normal.
Available values for component modes are:
‘addition’
‘and’
‘average’
‘bleach’
‘burn’
‘darken’
‘difference’
‘divide’
‘dodge’
‘exclusion’
‘extremity’
‘freeze’
‘geometric’
‘glow’
‘grainextract’
‘grainmerge’
‘hardlight’
‘hardmix’
‘hardoverlay’
‘harmonic’
‘heat’
‘interpolate’
‘lighten’
‘linearlight’
‘multiply’
‘multiply128’
‘negation’
‘normal’
‘or’
‘overlay’
‘phoenix’
‘pinlight’
‘reflect’
‘screen’
‘softdifference’
‘softlight’
‘stain’
‘subtract’
‘vividlight’
‘xor’
c0_opacity
c1_opacity
c2_opacity
c3_opacity
all_opacity
Set blend opacity for specific pixel component or all pixel components in case
of all_opacity. Only used in combination with pixel component blend modes.
c0_expr
c1_expr
c2_expr
c3_expr
all_expr
Set blend expression for specific pixel component or all pixel components in case
of all_expr. Note that related mode options will be ignored if those are set.
The expressions can use the following variables:
N
The sequential number of the filtered frame, starting from 0.
X
Y
the coordinates of the current sample
W
H
the width and height of currently filtered plane
SW
SH
Width and height scale for the plane being filtered. It is the
ratio between the dimensions of the current plane to the luma plane,
e.g. for a yuv420p frame, the values are 1,1 for
the luma plane and 0.5,0.5 for the chroma planes.
T
Time of the current frame, expressed in seconds.
TOP, A
Value of pixel component at current location for first video frame (top layer).
BOTTOM, B
Value of pixel component at current location for second video frame (bottom layer).
The blend filter also supports the framesync options.
39.15.1 Examples
Apply transition from bottom layer to top layer in first 10 seconds:
blend=all_expr='A*(if(gte(T,10),1,T/10))+B*(1-(if(gte(T,10),1,T/10)))'
Apply linear horizontal transition from top layer to bottom layer:
blend=all_expr='A*(X/W)+B*(1-X/W)'
Apply 1x1 checkerboard effect:
blend=all_expr='if(eq(mod(X,2),mod(Y,2)),A,B)'
Apply uncover left effect:
blend=all_expr='if(gte(N*SW+X,W),A,B)'
Apply uncover down effect:
blend=all_expr='if(gte(Y-N*SH,0),A,B)'
Apply uncover up-left effect:
blend=all_expr='if(gte(T*SH*40+Y,H)*gte((T*40*SW+X)*W/H,W),A,B)'
Split diagonally video and shows top and bottom layer on each side:
blend=all_expr='if(gt(X,Y*(W/H)),A,B)'
Display differences between the current and the previous frame:
tblend=all_mode=grainextract
39.15.2 Commands
This filter supports same commands as options.
39.16 blockdetect
Determines blockiness of frames without altering the input frames.
Based on Remco Muijs and Ihor Kirenko: "A no-reference blocking artifact measure for adaptive video processing." 2005 13th European signal processing conference.
The filter accepts the following options:
period_min
period_max
Set minimum and maximum values for determining pixel grids (periods).
Default values are [3,24].
planes
Set planes to filter. Default is first only.
39.16.1 Examples
Determine blockiness for the first plane and search for periods within [8,32]:
blockdetect=period_min=8:period_max=32:planes=1
39.17 blurdetect
Determines blurriness of frames without altering the input frames.
Based on Marziliano, Pina, et al. "A no-reference perceptual blur metric."
Allows for a block-based abbreviation.
The filter accepts the following options:
low
high
Set low and high threshold values used by the Canny thresholding
algorithm.
The high threshold selects the "strong" edge pixels, which are then
connected through 8-connectivity with the "weak" edge pixels selected
by the low threshold.
low and high threshold values must be chosen in the range
[0,1], and low should be lesser or equal to high.
Default value for low is 20/255, and default value for high
is 50/255.
radius
Define the radius to search around an edge pixel for local maxima.
block_pct
Determine blurriness only for the most significant blocks, given in percentage.
block_width
Determine blurriness for blocks of width block_width. If set to any value smaller 1, no blocks are used and the whole image is processed as one no matter of block_height.
block_height
Determine blurriness for blocks of height block_height. If set to any value smaller 1, no blocks are used and the whole image is processed as one no matter of block_width.
planes
Set planes to filter. Default is first only.
39.17.1 Examples
Determine blur for 80% of most significant 32x32 blocks:
blurdetect=block_width=32:block_height=32:block_pct=80
39.18 bm3d
Denoise frames using Block-Matching 3D algorithm.
The filter accepts the following options.
sigma
Set denoising strength. Default value is 1.
Allowed range is from 0 to 999.9.
The denoising algorithm is very sensitive to sigma, so adjust it
according to the source.
block
Set local patch size. This sets dimensions in 2D.
bstep
Set sliding step for processing blocks. Default value is 4.
Allowed range is from 1 to 64.
Smaller values allows processing more reference blocks and is slower.
group
Set maximal number of similar blocks for 3rd dimension. Default value is 1.
When set to 1, no block matching is done. Larger values allows more blocks
in single group.
Allowed range is from 1 to 256.
range
Set radius for search block matching. Default is 9.
Allowed range is from 1 to INT32_MAX.
mstep
Set step between two search locations for block matching. Default is 1.
Allowed range is from 1 to 64. Smaller is slower.
thmse
Set threshold of mean square error for block matching. Valid range is 0 to
INT32_MAX.
hdthr
Set thresholding parameter for hard thresholding in 3D transformed domain.
Larger values results in stronger hard-thresholding filtering in frequency
domain.
estim
Set filtering estimation mode. Can be basic or final.
Default is basic.
ref
If enabled, filter will use 2nd stream for block matching.
Default is disabled for basic value of estim option,
and always enabled if value of estim is final.
planes
Set planes to filter. Default is all available except alpha.
39.18.1 Examples
Basic filtering with bm3d:
bm3d=sigma=3:block=4:bstep=2:group=1:estim=basic
Same as above, but filtering only luma:
bm3d=sigma=3:block=4:bstep=2:group=1:estim=basic:planes=1
Same as above, but with both estimation modes:
split[a][b],[a]bm3d=sigma=3:block=4:bstep=2:group=1:estim=basic[a],[b][a]bm3d=sigma=3:block=4:bstep=2:group=16:estim=final:ref=1
Same as above, but prefilter with nlmeans filter instead:
split[a][b],[a]nlmeans=s=3:r=7:p=3[a],[b][a]bm3d=sigma=3:block=4:bstep=2:group=16:estim=final:ref=1
39.19 boxblur
Apply a boxblur algorithm to the input video.
It accepts the following parameters:
luma_radius, lr
luma_power, lp
chroma_radius, cr
chroma_power, cp
alpha_radius, ar
alpha_power, ap
A description of the accepted options follows.
luma_radius, lr
chroma_radius, cr
alpha_radius, ar
Set an expression for the box radius in pixels used for blurring the
corresponding input plane.
The radius value must be a non-negative number, and must not be
greater than the value of the expression min(w,h)/2 for the
luma and alpha planes, and of min(cw,ch)/2 for the chroma
planes.
Default value for luma_radius is "2". If not specified,
chroma_radius and alpha_radius default to the
corresponding value set for luma_radius.
The expressions can contain the following constants:
w
h
The input width and height in pixels.
cw
ch
The input chroma image width and height in pixels.
hsub
vsub
The horizontal and vertical chroma subsample values. For example, for the
pixel format "yuv422p", hsub is 2 and vsub is 1.
luma_power, lp
chroma_power, cp
alpha_power, ap
Specify how many times the boxblur filter is applied to the
corresponding plane.
Default value for luma_power is 2. If not specified,
chroma_power and alpha_power default to the
corresponding value set for luma_power.
A value of 0 will disable the effect.
39.19.1 Examples
Apply a boxblur filter with the luma, chroma, and alpha radii
set to 2:
boxblur=luma_radius=2:luma_power=1
boxblur=2:1
Set the luma radius to 2, and alpha and chroma radius to 0:
boxblur=2:1:cr=0:ar=0
Set the luma and chroma radii to a fraction of the video dimension:
boxblur=luma_radius=min(h\,w)/10:luma_power=1:chroma_radius=min(cw\,ch)/10:chroma_power=1
39.20 bwdif
Deinterlace the input video ("bwdif" stands for "Bob Weaver
Deinterlacing Filter").
Motion adaptive deinterlacing based on yadif with the use of w3fdif and cubic
interpolation algorithms.
It accepts the following parameters:
mode
The interlacing mode to adopt. It accepts one of the following values:
0, send_frame
Output one frame for each frame.
1, send_field
Output one frame for each field.
The default value is send_field.
parity
The picture field parity assumed for the input interlaced video. It accepts one
of the following values:
0, tff
Assume the top field is first.
1, bff
Assume the bottom field is first.
-1, auto
Enable automatic detection of field parity.
The default value is auto.
If the interlacing is unknown or the decoder does not export this information,
top field first will be assumed.
deint
Specify which frames to deinterlace. Accepts one of the following
values:
0, all
Deinterlace all frames.
1, interlaced
Only deinterlace frames marked as interlaced.
The default value is all.
39.21 bwdif_cuda
Deinterlace the input video using the bwdif algorithm, but implemented
in CUDA so that it can work as part of a GPU accelerated pipeline with nvdec
and/or nvenc.
It accepts the following parameters:
mode
The interlacing mode to adopt. It accepts one of the following values:
0, send_frame
Output one frame for each frame.
1, send_field
Output one frame for each field.
The default value is send_field.
parity
The picture field parity assumed for the input interlaced video. It accepts one
of the following values:
0, tff
Assume the top field is first.
1, bff
Assume the bottom field is first.
-1, auto
Enable automatic detection of field parity.
The default value is auto.
If the interlacing is unknown or the decoder does not export this information,
top field first will be assumed.
deint
Specify which frames to deinterlace. Accepts one of the following
values:
0, all
Deinterlace all frames.
1, interlaced
Only deinterlace frames marked as interlaced.
The default value is all.
39.22 ccrepack
Repack CEA-708 closed captioning side data
This filter fixes various issues seen with commerical encoders
related to upstream malformed CEA-708 payloads, specifically
incorrect number of tuples (wrong cc_count for the target FPS),
and incorrect ordering of tuples (i.e. the CEA-608 tuples are not at
the first entries in the payload).
39.23 cas
Apply Contrast Adaptive Sharpen filter to video stream.
The filter accepts the following options:
strength
Set the sharpening strength. Default value is 0.
planes
Set planes to filter. Default value is to filter all
planes except alpha plane.
39.23.1 Commands
This filter supports same commands as options.
39.24 chromahold
Remove all color information for all colors except for certain one.
The filter accepts the following options:
color
The color which will not be replaced with neutral chroma.
similarity
Similarity percentage with the above color.
0.01 matches only the exact key color, while 1.0 matches everything.
blend
Blend percentage.
0.0 makes pixels either fully gray, or not gray at all.
Higher values result in more preserved color.
yuv
Signals that the color passed is already in YUV instead of RGB.
Literal colors like "green" or "red" don’t make sense with this enabled anymore.
This can be used to pass exact YUV values as hexadecimal numbers.
39.24.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.25 chromakey
YUV colorspace color/chroma keying.
The filter accepts the following options:
color
The color which will be replaced with transparency.
similarity
Similarity percentage with the key color.
0.01 matches only the exact key color, while 1.0 matches everything.
blend
Blend percentage.
0.0 makes pixels either fully transparent, or not transparent at all.
Higher values result in semi-transparent pixels, with a higher transparency
the more similar the pixels color is to the key color.
yuv
Signals that the color passed is already in YUV instead of RGB.
Literal colors like "green" or "red" don’t make sense with this enabled anymore.
This can be used to pass exact YUV values as hexadecimal numbers.
39.25.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.25.2 Examples
Make every green pixel in the input image transparent:
ffmpeg -i input.png -vf chromakey=green out.png
Overlay a greenscreen-video on top of a static black background.
ffmpeg -f lavfi -i color=c=black:s=1280x720 -i video.mp4 -shortest -filter_complex "[1:v]chromakey=0x70de77:0.1:0.2[ckout];[0:v][ckout]overlay[out]" -map "[out]" output.mkv
39.26 chromakey_cuda
CUDA accelerated YUV colorspace color/chroma keying.
This filter works like normal chromakey filter but operates on CUDA frames.
for more details and parameters see chromakey.
39.26.1 Examples
Make all the green pixels in the input video transparent and use it as an overlay for another video:
./ffmpeg \
-hwaccel cuda -hwaccel_output_format cuda -i input_green.mp4  \
-hwaccel cuda -hwaccel_output_format cuda -i base_video.mp4 \
-init_hw_device cuda \
-filter_complex \
" \
[0:v]chromakey_cuda=0x25302D:0.1:0.12:1[overlay_video]; \
[1:v]scale_cuda=format=yuv420p[base]; \
[base][overlay_video]overlay_cuda" \
-an -sn -c:v h264_nvenc -cq 20 output.mp4
Process two software sources, explicitly uploading the frames:
./ffmpeg -init_hw_device cuda=cuda -filter_hw_device cuda \
-f lavfi -i color=size=800x600:color=white,format=yuv420p \
-f lavfi -i yuvtestsrc=size=200x200,format=yuv420p \
-filter_complex \
" \
[0]hwupload[under]; \
[1]hwupload,chromakey_cuda=green:0.1:0.12[over]; \
[under][over]overlay_cuda" \
-c:v hevc_nvenc -cq 18 -preset slow output.mp4
39.27 chromanr
Reduce chrominance noise.
The filter accepts the following options:
thres
Set threshold for averaging chrominance values.
Sum of absolute difference of Y, U and V pixel components of current
pixel and neighbour pixels lower than this threshold will be used in
averaging. Luma component is left unchanged and is copied to output.
Default value is 30. Allowed range is from 1 to 200.
sizew
Set horizontal radius of rectangle used for averaging.
Allowed range is from 1 to 100. Default value is 5.
sizeh
Set vertical radius of rectangle used for averaging.
Allowed range is from 1 to 100. Default value is 5.
stepw
Set horizontal step when averaging. Default value is 1.
Allowed range is from 1 to 50.
Mostly useful to speed-up filtering.
steph
Set vertical step when averaging. Default value is 1.
Allowed range is from 1 to 50.
Mostly useful to speed-up filtering.
threy
Set Y threshold for averaging chrominance values.
Set finer control for max allowed difference between Y components
of current pixel and neigbour pixels.
Default value is 200. Allowed range is from 1 to 200.
threu
Set U threshold for averaging chrominance values.
Set finer control for max allowed difference between U components
of current pixel and neigbour pixels.
Default value is 200. Allowed range is from 1 to 200.
threv
Set V threshold for averaging chrominance values.
Set finer control for max allowed difference between V components
of current pixel and neigbour pixels.
Default value is 200. Allowed range is from 1 to 200.
distance
Set distance type used in calculations.
‘manhattan’
Absolute difference.
‘euclidean’
Difference squared.
Default distance type is manhattan.
39.27.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
39.28 chromashift
Shift chroma pixels horizontally and/or vertically.
The filter accepts the following options:
cbh
Set amount to shift chroma-blue horizontally.
cbv
Set amount to shift chroma-blue vertically.
crh
Set amount to shift chroma-red horizontally.
crv
Set amount to shift chroma-red vertically.
edge
Set edge mode, can be smear, default, or warp.
39.28.1 Commands
This filter supports the all above options as commands.
39.29 ciescope
Display CIE color diagram with pixels overlaid onto it.
The filter accepts the following options:
system
Set color system.
‘ntsc, 470m’
‘ebu, 470bg’
‘smpte’
‘240m’
‘apple’
‘widergb’
‘cie1931’
‘rec709, hdtv’
‘uhdtv, rec2020’
‘dcip3’
cie
Set CIE system.
‘xyy’
‘ucs’
‘luv’
gamuts
Set what gamuts to draw.
See system option for available values.
size, s
Set ciescope size, by default set to 512.
intensity, i
Set intensity used to map input pixel values to CIE diagram.
contrast
Set contrast used to draw tongue colors that are out of active color system gamut.
corrgamma
Correct gamma displayed on scope, by default enabled.
showwhite
Show white point on CIE diagram, by default disabled.
gamma
Set input gamma. Used only with XYZ input color space.
fill
Fill with CIE colors. By default is enabled.
39.30 codecview
Visualize information exported by some codecs.
Some codecs can export information through frames using side-data or other
means. For example, some MPEG based codecs export motion vectors through the
export_mvs flag in the codec flags2 option.
The filter accepts the following option:
block
Display block partition structure using the luma plane.
mv
Set motion vectors to visualize.
Available flags for mv are:
‘pf’
forward predicted MVs of P-frames
‘bf’
forward predicted MVs of B-frames
‘bb’
backward predicted MVs of B-frames
qp
Display quantization parameters using the chroma planes.
mv_type, mvt
Set motion vectors type to visualize. Includes MVs from all frames unless specified by frame_type option.
Available flags for mv_type are:
‘fp’
forward predicted MVs
‘bp’
backward predicted MVs
frame_type, ft
Set frame type to visualize motion vectors of.
Available flags for frame_type are:
‘if’
intra-coded frames (I-frames)
‘pf’
predicted frames (P-frames)
‘bf’
bi-directionally predicted frames (B-frames)
39.30.1 Examples
Visualize forward predicted MVs of all frames using ffplay:
ffplay -flags2 +export_mvs input.mp4 -vf codecview=mv_type=fp
Visualize multi-directionals MVs of P and B-Frames using ffplay:
ffplay -flags2 +export_mvs input.mp4 -vf codecview=mv=pf+bf+bb
39.31 colorbalance
Modify intensity of primary colors (red, green and blue) of input frames.
The filter allows an input frame to be adjusted in the shadows, midtones or highlights
regions for the red-cyan, green-magenta or blue-yellow balance.
A positive adjustment value shifts the balance towards the primary color, a negative
value towards the complementary color.
The filter accepts the following options:
rs
gs
bs
Adjust red, green and blue shadows (darkest pixels).
rm
gm
bm
Adjust red, green and blue midtones (medium pixels).
rh
gh
bh
Adjust red, green and blue highlights (brightest pixels).
Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
pl
Preserve lightness when changing color balance. Default is disabled.
39.31.1 Examples
Add red color cast to shadows:
colorbalance=rs=.3
39.31.2 Commands
This filter supports the all above options as commands.
39.32 colorcontrast
Adjust color contrast between RGB components.
The filter accepts the following options:
rc
Set the red-cyan contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
gm
Set the green-magenta contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
by
Set the blue-yellow contrast. Defaults is 0.0. Allowed range is from -1.0 to 1.0.
rcw
gmw
byw
Set the weight of each rc, gm, by option value. Default value is 0.0.
Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
pl
Set the amount of preserving lightness. Default value is 0.0. Allowed range is from 0.0 to 1.0.
39.32.1 Commands
This filter supports the all above options as commands.
39.33 colorcorrect
Adjust color white balance selectively for blacks and whites.
This filter operates in YUV colorspace.
The filter accepts the following options:
rl
Set the red shadow spot. Allowed range is from -1.0 to 1.0.
Default value is 0.
bl
Set the blue shadow spot. Allowed range is from -1.0 to 1.0.
Default value is 0.
rh
Set the red highlight spot. Allowed range is from -1.0 to 1.0.
Default value is 0.
bh
Set the blue highlight spot. Allowed range is from -1.0 to 1.0.
Default value is 0.
saturation
Set the amount of saturation. Allowed range is from -3.0 to 3.0.
Default value is 1.
analyze
If set to anything other than manual it will analyze every frame and use derived
parameters for filtering output frame.
Possible values are:
‘manual’
‘average’
‘minmax’
‘median’
Default value is manual.
39.33.1 Commands
This filter supports the all above options as commands.
39.34 colorchannelmixer
Adjust video input frames by re-mixing color channels.
This filter modifies a color channel by adding the values associated to
the other channels of the same pixels. For example if the value to
modify is red, the output value will be:
red=red*rr + blue*rb + green*rg + alpha*ra
The filter accepts the following options:
rr
rg
rb
ra
Adjust contribution of input red, green, blue and alpha channels for output red channel.
Default is 1 for rr, and 0 for rg, rb and ra.
gr
gg
gb
ga
Adjust contribution of input red, green, blue and alpha channels for output green channel.
Default is 1 for gg, and 0 for gr, gb and ga.
br
bg
bb
ba
Adjust contribution of input red, green, blue and alpha channels for output blue channel.
Default is 1 for bb, and 0 for br, bg and ba.
ar
ag
ab
aa
Adjust contribution of input red, green, blue and alpha channels for output alpha channel.
Default is 1 for aa, and 0 for ar, ag and ab.
Allowed ranges for options are [-2.0, 2.0].
pc
Set preserve color mode. The accepted values are:
‘none’
Disable color preserving, this is default.
‘lum’
Preserve luminance.
‘max’
Preserve max value of RGB triplet.
‘avg’
Preserve average value of RGB triplet.
‘sum’
Preserve sum value of RGB triplet.
‘nrm’
Preserve normalized value of RGB triplet.
‘pwr’
Preserve power value of RGB triplet.
pa
Set the preserve color amount when changing colors. Allowed range is from [0.0, 1.0].
Default is 0.0, thus disabled.
39.34.1 Examples
Convert source to grayscale:
colorchannelmixer=.3:.4:.3:0:.3:.4:.3:0:.3:.4:.3
Simulate sepia tones:
colorchannelmixer=.393:.769:.189:0:.349:.686:.168:0:.272:.534:.131
39.34.2 Commands
This filter supports the all above options as commands.
39.35 colorize
Overlay a solid color on the video stream.
The filter accepts the following options:
hue
Set the color hue. Allowed range is from 0 to 360.
Default value is 0.
saturation
Set the color saturation. Allowed range is from 0 to 1.
Default value is 0.5.
lightness
Set the color lightness. Allowed range is from 0 to 1.
Default value is 0.5.
mix
Set the mix of source lightness. By default is set to 1.0.
Allowed range is from 0.0 to 1.0.
39.35.1 Commands
This filter supports the all above options as commands.
39.36 colorkey
RGB colorspace color keying.
This filter operates on 8-bit RGB format frames by setting the alpha component of each pixel
which falls within the similarity radius of the key color to 0. The alpha value for pixels outside
the similarity radius depends on the value of the blend option.
The filter accepts the following options:
color
Set the color for which alpha will be set to 0 (full transparency).
See (ffmpeg-utils)"Color" section in the ffmpeg-utils manual.
Default is black.
similarity
Set the radius from the key color within which other colors also have full transparency.
The computed distance is related to the unit fractional distance in 3D space between the RGB values
of the key color and the pixel’s color. Range is 0.01 to 1.0. 0.01 matches within a very small radius
around the exact key color, while 1.0 matches everything.
Default is 0.01.
blend
Set how the alpha value for pixels that fall outside the similarity radius is computed.
0.0 makes pixels either fully transparent or fully opaque.
Higher values result in semi-transparent pixels, with greater transparency
the more similar the pixel color is to the key color.
Range is 0.0 to 1.0. Default is 0.0.
39.36.1 Examples
Make every green pixel in the input image transparent:
ffmpeg -i input.png -vf colorkey=green out.png
Overlay a greenscreen-video on top of a static background image.
ffmpeg -i background.png -i video.mp4 -filter_complex "[1:v]colorkey=0x3BBD1E:0.3:0.2[ckout];[0:v][ckout]overlay[out]" -map "[out]" output.flv
39.36.2 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.37 colorhold
Remove all color information for all RGB colors except for certain one.
The filter accepts the following options:
color
The color which will not be replaced with neutral gray.
similarity
Similarity percentage with the above color.
0.01 matches only the exact key color, while 1.0 matches everything.
blend
Blend percentage. 0.0 makes pixels fully gray.
Higher values result in more preserved color.
39.37.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.38 colorlevels
Adjust video input frames using levels.
The filter accepts the following options:
rimin
gimin
bimin
aimin
Adjust red, green, blue and alpha input black point.
Allowed ranges for options are [-1.0, 1.0]. Defaults are 0.
rimax
gimax
bimax
aimax
Adjust red, green, blue and alpha input white point.
Allowed ranges for options are [-1.0, 1.0]. Defaults are 1.
Input levels are used to lighten highlights (bright tones), darken shadows
(dark tones), change the balance of bright and dark tones.
romin
gomin
bomin
aomin
Adjust red, green, blue and alpha output black point.
Allowed ranges for options are [0, 1.0]. Defaults are 0.
romax
gomax
bomax
aomax
Adjust red, green, blue and alpha output white point.
Allowed ranges for options are [0, 1.0]. Defaults are 1.
Output levels allows manual selection of a constrained output level range.
preserve
Set preserve color mode. The accepted values are:
‘none’
Disable color preserving, this is default.
‘lum’
Preserve luminance.
‘max’
Preserve max value of RGB triplet.
‘avg’
Preserve average value of RGB triplet.
‘sum’
Preserve sum value of RGB triplet.
‘nrm’
Preserve normalized value of RGB triplet.
‘pwr’
Preserve power value of RGB triplet.
39.38.1 Examples
Make video output darker:
colorlevels=rimin=0.058:gimin=0.058:bimin=0.058
Increase contrast:
colorlevels=rimin=0.039:gimin=0.039:bimin=0.039:rimax=0.96:gimax=0.96:bimax=0.96
Make video output lighter:
colorlevels=rimax=0.902:gimax=0.902:bimax=0.902
Increase brightness:
colorlevels=romin=0.5:gomin=0.5:bomin=0.5
39.38.2 Commands
This filter supports the all above options as commands.
39.39 colormap
Apply custom color maps to video stream.
This filter needs three input video streams.
First stream is video stream that is going to be filtered out.
Second and third video stream specify color patches for source
color to target color mapping.
The filter accepts the following options:
patch_size
Set the source and target video stream patch size in pixels.
nb_patches
Set the max number of used patches from source and target video stream.
Default value is number of patches available in additional video streams.
Max allowed number of patches is 64.
type
Set the adjustments used for target colors. Can be relative or absolute.
Defaults is absolute.
kernel
Set the kernel used to measure color differences between mapped colors.
The accepted values are:
‘euclidean’
‘weuclidean’
Default is euclidean.
39.40 colormatrix
Convert color matrix.
The filter accepts the following options:
src
dst
Specify the source and destination color matrix. Both values must be
specified.
The accepted values are:
‘bt709’
BT.709
‘fcc’
FCC
‘bt601’
BT.601
‘bt470’
BT.470
‘bt470bg’
BT.470BG
‘smpte170m’
SMPTE-170M
‘smpte240m’
SMPTE-240M
‘bt2020’
BT.2020
For example to convert from BT.601 to SMPTE-240M, use the command:
colormatrix=bt601:smpte240m
39.41 colorspace
Convert colorspace, transfer characteristics or color primaries.
Input video needs to have an even size.
The filter accepts the following options:
all
Specify all color properties at once.
The accepted values are:
‘bt470m’
BT.470M
‘bt470bg’
BT.470BG
‘bt601-6-525’
BT.601-6 525
‘bt601-6-625’
BT.601-6 625
‘bt709’
BT.709
‘smpte170m’
SMPTE-170M
‘smpte240m’
SMPTE-240M
‘bt2020’
BT.2020
space
Specify output colorspace.
The accepted values are:
‘bt709’
BT.709
‘fcc’
FCC
‘bt470bg’
BT.470BG or BT.601-6 625
‘smpte170m’
SMPTE-170M or BT.601-6 525
‘smpte240m’
SMPTE-240M
‘ycgco’
YCgCo
‘bt2020ncl’
BT.2020 with non-constant luminance
trc
Specify output transfer characteristics.
The accepted values are:
‘bt709’
BT.709
‘bt470m’
BT.470M
‘bt470bg’
BT.470BG
‘gamma22’
Constant gamma of 2.2
‘gamma28’
Constant gamma of 2.8
‘smpte170m’
SMPTE-170M, BT.601-6 625 or BT.601-6 525
‘smpte240m’
SMPTE-240M
‘srgb’
SRGB
‘iec61966-2-1’
iec61966-2-1
‘iec61966-2-4’
iec61966-2-4
‘xvycc’
xvycc
‘bt2020-10’
BT.2020 for 10-bits content
‘bt2020-12’
BT.2020 for 12-bits content
primaries
Specify output color primaries.
The accepted values are:
‘bt709’
BT.709
‘bt470m’
BT.470M
‘bt470bg’
BT.470BG or BT.601-6 625
‘smpte170m’
SMPTE-170M or BT.601-6 525
‘smpte240m’
SMPTE-240M
‘film’
film
‘smpte431’
SMPTE-431
‘smpte432’
SMPTE-432
‘bt2020’
BT.2020
‘jedec-p22’
JEDEC P22 phosphors
range
Specify output color range.
The accepted values are:
‘tv’
TV (restricted) range
‘mpeg’
MPEG (restricted) range
‘pc’
PC (full) range
‘jpeg’
JPEG (full) range
format
Specify output color format.
The accepted values are:
‘yuv420p’
YUV 4:2:0 planar 8-bits
‘yuv420p10’
YUV 4:2:0 planar 10-bits
‘yuv420p12’
YUV 4:2:0 planar 12-bits
‘yuv422p’
YUV 4:2:2 planar 8-bits
‘yuv422p10’
YUV 4:2:2 planar 10-bits
‘yuv422p12’
YUV 4:2:2 planar 12-bits
‘yuv444p’
YUV 4:4:4 planar 8-bits
‘yuv444p10’
YUV 4:4:4 planar 10-bits
‘yuv444p12’
YUV 4:4:4 planar 12-bits
fast
Do a fast conversion, which skips gamma/primary correction. This will take
significantly less CPU, but will be mathematically incorrect. To get output
compatible with that produced by the colormatrix filter, use fast=1.
dither
Specify dithering mode.
The accepted values are:
‘none’
No dithering
‘fsb’
Floyd-Steinberg dithering
wpadapt
Whitepoint adaptation mode.
The accepted values are:
‘bradford’
Bradford whitepoint adaptation
‘vonkries’
von Kries whitepoint adaptation
‘identity’
identity whitepoint adaptation (i.e. no whitepoint adaptation)
iall
Override all input properties at once. Same accepted values as all.
ispace
Override input colorspace. Same accepted values as space.
iprimaries
Override input color primaries. Same accepted values as primaries.
itrc
Override input transfer characteristics. Same accepted values as trc.
irange
Override input color range. Same accepted values as range.
The filter converts the transfer characteristics, color space and color
primaries to the specified user values. The output value, if not specified,
is set to a default value based on the "all" property. If that property is
also not specified, the filter will log an error. The output color range and
format default to the same value as the input color range and format. The
input transfer characteristics, color space, color primaries and color range
should be set on the input data. If any of these are missing, the filter will
log an error and no conversion will take place.
For example to convert the input to SMPTE-240M, use the command:
colorspace=smpte240m
39.42 colorspace_cuda
CUDA accelerated implementation of the colorspace filter.
It is by no means feature complete compared to the software colorspace filter,
and at the current time only supports color range conversion between jpeg/full
and mpeg/limited range.
The filter accepts the following options:
range
Specify output color range.
The accepted values are:
‘tv’
TV (restricted) range
‘mpeg’
MPEG (restricted) range
‘pc’
PC (full) range
‘jpeg’
JPEG (full) range
39.43 colortemperature
Adjust color temperature in video to simulate variations in ambient color temperature.
The filter accepts the following options:
temperature
Set the temperature in Kelvin. Allowed range is from 1000 to 40000.
Default value is 6500 K.
mix
Set mixing with filtered output. Allowed range is from 0 to 1.
Default value is 1.
pl
Set the amount of preserving lightness. Allowed range is from 0 to 1.
Default value is 0.
39.43.1 Commands
This filter supports same commands as options.
39.44 convolution
Apply convolution of 3x3, 5x5, 7x7 or horizontal/vertical up to 49 elements.
The filter accepts the following options:
0m
1m
2m
3m
Set matrix for each plane.
Matrix is sequence of 9, 25 or 49 signed integers in square mode,
and from 1 to 49 odd number of signed integers in row mode.
0rdiv
1rdiv
2rdiv
3rdiv
Set multiplier for calculated value for each plane.
If unset or 0, it will be 1/sum of all matrix elements.
0bias
1bias
2bias
3bias
Set bias for each plane. This value is added to the result of the multiplication.
Useful for making the overall image brighter or darker. Default is 0.0.
0mode
1mode
2mode
3mode
Set matrix mode for each plane. Can be square, row or column.
Default is square.
39.44.1 Commands
This filter supports the all above options as commands.
39.44.2 Examples
Apply sharpen:
convolution="0 -1 0 -1 5 -1 0 -1 0:0 -1 0 -1 5 -1 0 -1 0:0 -1 0 -1 5 -1 0 -1 0:0 -1 0 -1 5 -1 0 -1 0"
Apply blur:
convolution="1 1 1 1 1 1 1 1 1:1 1 1 1 1 1 1 1 1:1 1 1 1 1 1 1 1 1:1 1 1 1 1 1 1 1 1:1/9:1/9:1/9:1/9"
Apply edge enhance:
convolution="0 0 0 -1 1 0 0 0 0:0 0 0 -1 1 0 0 0 0:0 0 0 -1 1 0 0 0 0:0 0 0 -1 1 0 0 0 0:5:1:1:1:0:128:128:128"
Apply edge detect:
convolution="0 1 0 1 -4 1 0 1 0:0 1 0 1 -4 1 0 1 0:0 1 0 1 -4 1 0 1 0:0 1 0 1 -4 1 0 1 0:5:5:5:1:0:128:128:128"
Apply laplacian edge detector which includes diagonals:
convolution="1 1 1 1 -8 1 1 1 1:1 1 1 1 -8 1 1 1 1:1 1 1 1 -8 1 1 1 1:1 1 1 1 -8 1 1 1 1:5:5:5:1:0:128:128:0"
Apply emboss:
convolution="-2 -1 0 -1 1 1 0 1 2:-2 -1 0 -1 1 1 0 1 2:-2 -1 0 -1 1 1 0 1 2:-2 -1 0 -1 1 1 0 1 2"
39.45 convolve
Apply 2D convolution of video stream in frequency domain using second stream
as impulse.
The filter accepts the following options:
planes
Set which planes to process.
impulse
Set which impulse video frames will be processed, can be first
or all. Default is all.
The convolve filter also supports the framesync options.
39.46 copy
Copy the input video source unchanged to the output. This is mainly useful for
testing purposes.
39.47 coreimage
Video filtering on GPU using Apple’s CoreImage API on OSX.
Hardware acceleration is based on an OpenGL context. Usually, this means it is
processed by video hardware. However, software-based OpenGL implementations
exist which means there is no guarantee for hardware processing. It depends on
the respective OSX.
There are many filters and image generators provided by Apple that come with a
large variety of options. The filter has to be referenced by its name along
with its options.
The coreimage filter accepts the following options:
list_filters
List all available filters and generators along with all their respective
options as well as possible minimum and maximum values along with the default
values.
list_filters=true
filter
Specify all filters by their respective name and options.
Use list_filters to determine all valid filter names and options.
Numerical options are specified by a float value and are automatically clamped
to their respective value range.  Vector and color options have to be specified
by a list of space separated float values. Character escaping has to be done.
A special option name default is available to use default options for a
filter.
It is required to specify either default or at least one of the filter options.
All omitted options are used with their default values.
The syntax of the filter string is as follows:
filter=<NAME>@<OPTION>=<VALUE>[@<OPTION>=<VALUE>][@...][#<NAME>@<OPTION>=<VALUE>[@<OPTION>=<VALUE>][@...]][#...]
output_rect
Specify a rectangle where the output of the filter chain is copied into the
input image. It is given by a list of space separated float values:
output_rect=x\ y\ width\ height
If not given, the output rectangle equals the dimensions of the input image.
The output rectangle is automatically cropped at the borders of the input
image. Negative values are valid for each component.
output_rect=25\ 25\ 100\ 100
Several filters can be chained for successive processing without GPU-HOST
transfers allowing for fast processing of complex filter chains.
Currently, only filters with zero (generators) or exactly one (filters) input
image and one output image are supported. Also, transition filters are not yet
usable as intended.
Some filters generate output images with additional padding depending on the
respective filter kernel. The padding is automatically removed to ensure the
filter output has the same size as the input image.
For image generators, the size of the output image is determined by the
previous output image of the filter chain or the input image of the whole
filterchain, respectively. The generators do not use the pixel information of
this image to generate their output. However, the generated output is
blended onto this image, resulting in partial or complete coverage of the
output image.
The coreimagesrc video source can be used for generating input images
which are directly fed into the filter chain. By using it, providing input
images by another video source or an input video is not required.
39.47.1 Examples
List all filters available:
coreimage=list_filters=true
Use the CIBoxBlur filter with default options to blur an image:
coreimage=filter=CIBoxBlur@default
Use a filter chain with CISepiaTone at default values and CIVignetteEffect with
its center at 100x100 and a radius of 50 pixels:
coreimage=filter=CIBoxBlur@default#CIVignetteEffect@inputCenter=100\ 100@inputRadius=50
Use nullsrc and CIQRCodeGenerator to create a QR code for the FFmpeg homepage,
given as complete and escaped command-line for Apple’s standard bash shell:
ffmpeg -f lavfi -i nullsrc=s=100x100,coreimage=filter=CIQRCodeGenerator@inputMessage=https\\\\\://FFmpeg.org/@inputCorrectionLevel=H -frames:v 1 QRCode.png
39.48 corr
Obtain the correlation between two input videos.
This filter takes two input videos.
Both input videos must have the same resolution and pixel format for
this filter to work correctly. Also it assumes that both inputs
have the same number of frames, which are compared one by one.
The obtained per component, average, min and max correlation is printed through
the logging system.
The filter stores the calculated correlation of each frame in frame metadata.
This filter also supports the framesync options.
In the below example the input file main.mpg being processed is compared
with the reference file ref.mpg.
ffmpeg -i main.mpg -i ref.mpg -lavfi corr -f null -
39.49 cover_rect
Cover a rectangular object
It accepts the following options:
cover
Filepath of the optional cover image, needs to be in yuv420.
mode
Set covering mode.
It accepts the following values:
‘cover’
cover it by the supplied image
‘blur’
cover it by interpolating the surrounding pixels
Default value is blur.
39.49.1 Examples
Cover a rectangular object by the supplied image of a given video using ffmpeg:
ffmpeg -i file.ts -vf find_rect=newref.pgm,cover_rect=cover.jpg:mode=cover new.mkv
39.50 crop
Crop the input video to given dimensions.
It accepts the following parameters:
w, out_w
The width of the output video. It defaults to iw.
This expression is evaluated only once during the filter
configuration, or when the ‘w’ or ‘out_w’ command is sent.
h, out_h
The height of the output video. It defaults to ih.
This expression is evaluated only once during the filter
configuration, or when the ‘h’ or ‘out_h’ command is sent.
x
The horizontal position, in the input video, of the left edge of the output
video. It defaults to (in_w-out_w)/2.
This expression is evaluated per-frame.
y
The vertical position, in the input video, of the top edge of the output video.
It defaults to (in_h-out_h)/2.
This expression is evaluated per-frame.
keep_aspect
If set to 1 will force the output display aspect ratio
to be the same of the input, by changing the output sample aspect
ratio. It defaults to 0.
exact
Enable exact cropping. If enabled, subsampled videos will be cropped at exact
width/height/x/y as specified and will not be rounded to nearest smaller value.
It defaults to 0.
The out_w, out_h, x, y parameters are
expressions containing the following constants:
x
y
The computed values for x and y. They are evaluated for
each new frame.
in_w
in_h
The input width and height.
iw
ih
These are the same as in_w and in_h.
out_w
out_h
The output (cropped) width and height.
ow
oh
These are the same as out_w and out_h.
a
same as iw / ih
sar
input sample aspect ratio
dar
input display aspect ratio, it is the same as (iw / ih) * sar
hsub
vsub
horizontal and vertical chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
n
The number of the input frame, starting from 0.
pos
the position in the file of the input frame, NAN if unknown; deprecated,
do not use
t
The timestamp expressed in seconds. It’s NAN if the input timestamp is unknown.
The expression for out_w may depend on the value of out_h,
and the expression for out_h may depend on out_w, but they
cannot depend on x and y, as x and y are
evaluated after out_w and out_h.
The x and y parameters specify the expressions for the
position of the top-left corner of the output (non-cropped) area. They
are evaluated for each frame. If the evaluated value is not valid, it
is approximated to the nearest valid value.
The expression for x may depend on y, and the expression
for y may depend on x.
39.50.1 Examples
Crop area with size 100x100 at position (12,34).
crop=100:100:12:34
Using named options, the example above becomes:
crop=w=100:h=100:x=12:y=34
Crop the central input area with size 100x100:
crop=100:100
Crop the central input area with size 2/3 of the input video:
crop=2/3*in_w:2/3*in_h
Crop the input video central square:
crop=out_w=in_h
crop=in_h
Delimit the rectangle with the top-left corner placed at position
100:100 and the right-bottom corner corresponding to the right-bottom
corner of the input image.
crop=in_w-100:in_h-100:100:100
Crop 10 pixels from the left and right borders, and 20 pixels from
the top and bottom borders
crop=in_w-2*10:in_h-2*20
Keep only the bottom right quarter of the input image:
crop=in_w/2:in_h/2:in_w/2:in_h/2
Crop height for getting Greek harmony:
crop=in_w:1/PHI*in_w
Apply trembling effect:
crop=in_w/2:in_h/2:(in_w-out_w)/2+((in_w-out_w)/2)*sin(n/10):(in_h-out_h)/2 +((in_h-out_h)/2)*sin(n/7)
Apply erratic camera effect depending on timestamp:
crop=in_w/2:in_h/2:(in_w-out_w)/2+((in_w-out_w)/2)*sin(t*10):(in_h-out_h)/2 +((in_h-out_h)/2)*sin(t*13)
Set x depending on the value of y:
crop=in_w/2:in_h/2:y:10+10*sin(n/10)
39.50.2 Commands
This filter supports the following commands:
w, out_w
h, out_h
x
y
Set width/height of the output video and the horizontal/vertical position
in the input video.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.51 cropdetect
Auto-detect the crop size.
It calculates the necessary cropping parameters and prints the
recommended parameters via the logging system. The detected dimensions
correspond to the non-black or video area of the input video according to mode.
It accepts the following parameters:
mode
Depending on mode crop detection is based on either the mere black value of surrounding pixels or a combination of motion vectors and edge pixels.
‘black’
Detect black pixels surrounding the playing video. For fine control use option limit.
‘mvedges’
Detect the playing video by the motion vectors inside the video and scanning for edge pixels typically forming the border of a playing video.
limit
Set higher black value threshold, which can be optionally specified
from nothing (0) to everything (255 for 8-bit based formats). An intensity
value greater to the set value is considered non-black. It defaults to 24.
You can also specify a value between 0.0 and 1.0 which will be scaled depending
on the bitdepth of the pixel format.
round
The value which the width/height should be divisible by. It defaults to
16. The offset is automatically adjusted to center the video. Use 2 to
get only even dimensions (needed for 4:2:2 video). 16 is best when
encoding to most video codecs.
skip
Set the number of initial frames for which evaluation is skipped.
Default is 2. Range is 0 to INT_MAX.
reset_count, reset
Set the counter that determines after how many frames cropdetect will
reset the previously detected largest video area and start over to
detect the current optimal crop area. Default value is 0.
This can be useful when channel logos distort the video area. 0
indicates ’never reset’, and returns the largest area encountered during
playback.
mv_threshold
Set motion in pixel units as threshold for motion detection. It defaults to 8.
low
high
Set low and high threshold values used by the Canny thresholding
algorithm.
The high threshold selects the "strong" edge pixels, which are then
connected through 8-connectivity with the "weak" edge pixels selected
by the low threshold.
low and high threshold values must be chosen in the range
[0,1], and low should be lesser or equal to high.
Default value for low is 5/255, and default value for high
is 15/255.
39.51.1 Examples
Find video area surrounded by black borders:
ffmpeg -i file.mp4 -vf cropdetect,metadata=mode=print -f null -
Find an embedded video area, generate motion vectors beforehand:
ffmpeg -i file.mp4 -vf mestimate,cropdetect=mode=mvedges,metadata=mode=print -f null -
Find an embedded video area, use motion vectors from decoder:
ffmpeg -flags2 +export_mvs -i file.mp4 -vf cropdetect=mode=mvedges,metadata=mode=print -f null -
39.51.2 Commands
This filter supports the following commands:
limit
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current value.
39.52 cue
Delay video filtering until a given wallclock timestamp. The filter first
passes on preroll amount of frames, then it buffers at most
buffer amount of frames and waits for the cue. After reaching the cue
it forwards the buffered frames and also any subsequent frames coming in its
input.
The filter can be used synchronize the output of multiple ffmpeg processes for
realtime output devices like decklink. By putting the delay in the filtering
chain and pre-buffering frames the process can pass on data to output almost
immediately after the target wallclock timestamp is reached.
Perfect frame accuracy cannot be guaranteed, but the result is good enough for
some use cases.
cue
The cue timestamp expressed in a UNIX timestamp in microseconds. Default is 0.
preroll
The duration of content to pass on as preroll expressed in seconds. Default is 0.
buffer
The maximum duration of content to buffer before waiting for the cue expressed
in seconds. Default is 0.
39.53 curves
Apply color adjustments using curves.
This filter is similar to the Adobe Photoshop and GIMP curves tools. Each
component (red, green and blue) has its values defined by N key points
tied from each other using a smooth curve. The x-axis represents the pixel
values from the input frame, and the y-axis the new pixel values to be set for
the output frame.
By default, a component curve is defined by the two points (0;0) and
(1;1). This creates a straight line where each original pixel value is
"adjusted" to its own value, which means no change to the image.
The filter allows you to redefine these two points and add some more. A new
curve will be defined to pass smoothly through all these new coordinates. The
new defined points need to be strictly increasing over the x-axis, and their
x and y values must be in the [0;1] interval. The curve is
formed by using a natural or monotonic cubic spline interpolation, depending
on the interp option (default: natural). The natural
spline produces a smoother curve in general while the monotonic (pchip)
spline guarantees the transitions between the specified points to be
monotonic. If the computed curves happened to go outside the vector spaces,
the values will be clipped accordingly.
The filter accepts the following options:
preset
Select one of the available color presets. This option can be used in addition
to the r, g, b parameters; in this case, the later
options takes priority on the preset values.
Available presets are:
‘none’
‘color_negative’
‘cross_process’
‘darker’
‘increase_contrast’
‘lighter’
‘linear_contrast’
‘medium_contrast’
‘negative’
‘strong_contrast’
‘vintage’
Default is none.
master, m
Set the master key points. These points will define a second pass mapping. It
is sometimes called a "luminance" or "value" mapping. It can be used with
r, g, b or all since it acts like a
post-processing LUT.
red, r
Set the key points for the red component.
green, g
Set the key points for the green component.
blue, b
Set the key points for the blue component.
all
Set the key points for all components (not including master).
Can be used in addition to the other key points component
options. In this case, the unset component(s) will fallback on this
all setting.
psfile
Specify a Photoshop curves file (.acv) to import the settings from.
plot
Save Gnuplot script of the curves in specified file.
interp
Specify the kind of interpolation. Available algorithms are:
‘natural’
Natural cubic spline using a piece-wise cubic polynomial that is twice continuously differentiable.
‘pchip’
Monotonic cubic spline using a piecewise cubic Hermite interpolating polynomial (PCHIP).
To avoid some filtergraph syntax conflicts, each key points list need to be
defined using the following syntax: x0/y0 x1/y1 x2/y2 ....
39.53.1 Commands
This filter supports same commands as options.
39.53.2 Examples
Increase slightly the middle level of blue:
curves=blue='0/0 0.5/0.58 1/1'
Vintage effect:
curves=r='0/0.11 .42/.51 1/0.95':g='0/0 0.50/0.48 1/1':b='0/0.22 .49/.44 1/0.8'
Here we obtain the following coordinates for each components:
red
(0;0.11) (0.42;0.51) (1;0.95)
green
(0;0) (0.50;0.48) (1;1)
blue
(0;0.22) (0.49;0.44) (1;0.80)
The previous example can also be achieved with the associated built-in preset:
curves=preset=vintage
Or simply:
curves=vintage
Use a Photoshop preset and redefine the points of the green component:
curves=psfile='MyCurvesPresets/purple.acv':green='0/0 0.45/0.53 1/1'
Check out the curves of the cross_process profile using ffmpeg
and gnuplot:
ffmpeg -f lavfi -i color -vf curves=cross_process:plot=/tmp/curves.plt -frames:v 1 -f null -
gnuplot -p /tmp/curves.plt
39.54 datascope
Video data analysis filter.
This filter shows hexadecimal pixel values of part of video.
The filter accepts the following options:
size, s
Set output video size.
x
Set x offset from where to pick pixels.
y
Set y offset from where to pick pixels.
mode
Set scope mode, can be one of the following:
‘mono’
Draw hexadecimal pixel values with white color on black background.
‘color’
Draw hexadecimal pixel values with input video pixel color on black
background.
‘color2’
Draw hexadecimal pixel values on color background picked from input video,
the text color is picked in such way so its always visible.
axis
Draw rows and columns numbers on left and top of video.
opacity
Set background opacity.
format
Set display number format. Can be hex, or dec. Default is hex.
components
Set pixel components to display. By default all pixel components are displayed.
39.54.1 Commands
This filter supports same commands as options excluding size option.
39.55 dblur
Apply Directional blur filter.
The filter accepts the following options:
angle
Set angle of directional blur. Default is 45.
radius
Set radius of directional blur. Default is 5.
planes
Set which planes to filter. By default all planes are filtered.
39.55.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.56 dctdnoiz
Denoise frames using 2D DCT (frequency domain filtering).
This filter is not designed for real time.
The filter accepts the following options:
sigma, s
Set the noise sigma constant.
This sigma defines a hard threshold of 3 * sigma; every DCT
coefficient (absolute value) below this threshold with be dropped.
If you need a more advanced filtering, see expr.
Default is 0.
overlap
Set number overlapping pixels for each block. Since the filter can be slow, you
may want to reduce this value, at the cost of a less effective filter and the
risk of various artefacts.
If the overlapping value doesn’t permit processing the whole input width or
height, a warning will be displayed and according borders won’t be denoised.
Default value is blocksize-1, which is the best possible setting.
expr, e
Set the coefficient factor expression.
For each coefficient of a DCT block, this expression will be evaluated as a
multiplier value for the coefficient.
If this is option is set, the sigma option will be ignored.
The absolute value of the coefficient can be accessed through the c
variable.
n
Set the blocksize using the number of bits. 1<<n defines the
blocksize, which is the width and height of the processed blocks.
The default value is 3 (8x8) and can be raised to 4 for a
blocksize of 16x16. Note that changing this setting has huge consequences
on the speed processing. Also, a larger block size does not necessarily means a
better de-noising.
39.56.1 Examples
Apply a denoise with a sigma of 4.5:
dctdnoiz=4.5
The same operation can be achieved using the expression system:
dctdnoiz=e='gte(c, 4.5*3)'
Violent denoise using a block size of 16x16:
dctdnoiz=15:n=4
39.57 deband
Remove banding artifacts from input video.
It works by replacing banded pixels with average value of referenced pixels.
The filter accepts the following options:
1thr
2thr
3thr
4thr
Set banding detection threshold for each plane. Default is 0.02.
Valid range is 0.00003 to 0.5.
If difference between current pixel and reference pixel is less than threshold,
it will be considered as banded.
range, r
Banding detection range in pixels. Default is 16. If positive, random number
in range 0 to set value will be used. If negative, exact absolute value
will be used.
The range defines square of four pixels around current pixel.
direction, d
Set direction in radians from which four pixel will be compared. If positive,
random direction from 0 to set direction will be picked. If negative, exact of
absolute value will be picked. For example direction 0, -PI or -2*PI radians
will pick only pixels on same row and -PI/2 will pick only pixels on same
column.
blur, b
If enabled, current pixel is compared with average value of all four
surrounding pixels. The default is enabled. If disabled current pixel is
compared with all four surrounding pixels. The pixel is considered banded
if only all four differences with surrounding pixels are less than threshold.
coupling, c
If enabled, current pixel is changed if and only if all pixel components are banded,
e.g. banding detection threshold is triggered for all color components.
The default is disabled.
39.57.1 Commands
This filter supports the all above options as commands.
39.58 deblock
Remove blocking artifacts from input video.
The filter accepts the following options:
filter
Set filter type, can be weak or strong. Default is strong.
This controls what kind of deblocking is applied.
block
Set size of block, allowed range is from 4 to 512. Default is 8.
alpha
beta
gamma
delta
Set blocking detection thresholds. Allowed range is 0 to 1.
Defaults are: 0.098 for alpha and 0.05 for the rest.
Using higher threshold gives more deblocking strength.
Setting alpha controls threshold detection at exact edge of block.
Remaining options controls threshold detection near the edge. Each one for
below/above or left/right. Setting any of those to 0 disables
deblocking.
planes
Set planes to filter. Default is to filter all available planes.
39.58.1 Examples
Deblock using weak filter and block size of 4 pixels.
deblock=filter=weak:block=4
Deblock using strong filter, block size of 4 pixels and custom thresholds for
deblocking more edges.
deblock=filter=strong:block=4:alpha=0.12:beta=0.07:gamma=0.06:delta=0.05
Similar as above, but filter only first plane.
deblock=filter=strong:block=4:alpha=0.12:beta=0.07:gamma=0.06:delta=0.05:planes=1
Similar as above, but filter only second and third plane.
deblock=filter=strong:block=4:alpha=0.12:beta=0.07:gamma=0.06:delta=0.05:planes=6
39.58.2 Commands
This filter supports the all above options as commands.
39.59 decimate
Drop duplicated frames at regular intervals.
The filter accepts the following options:
cycle
Set the number of frames from which one will be dropped. Setting this to
N means one frame in every batch of N frames will be dropped.
Default is 5.
dupthresh
Set the threshold for duplicate detection. If the difference metric for a frame
is less than or equal to this value, then it is declared as duplicate. Default
is 1.1
scthresh
Set scene change threshold. Default is 15.
blockx
blocky
Set the size of the x and y-axis blocks used during metric calculations.
Larger blocks give better noise suppression, but also give worse detection of
small movements. Must be a power of two. Default is 32.
ppsrc
Mark main input as a pre-processed input and activate clean source input
stream. This allows the input to be pre-processed with various filters to help
the metrics calculation while keeping the frame selection lossless. When set to
1, the first stream is for the pre-processed input, and the second
stream is the clean source from where the kept frames are chosen. Default is
0.
chroma
Set whether or not chroma is considered in the metric calculations. Default is
1.
mixed
Set whether or not the input only partially contains content to be decimated.
Default is false.
If enabled video output stream will be in variable frame rate.
39.60 deconvolve
Apply 2D deconvolution of video stream in frequency domain using second stream
as impulse.
The filter accepts the following options:
planes
Set which planes to process.
impulse
Set which impulse video frames will be processed, can be first
or all. Default is all.
noise
Set noise when doing divisions. Default is 0.0000001. Useful when width
and height are not same and not power of 2 or if stream prior to convolving
had noise.
The deconvolve filter also supports the framesync options.
39.61 dedot
Reduce cross-luminance (dot-crawl) and cross-color (rainbows) from video.
It accepts the following options:
m
Set mode of operation. Can be combination of dotcrawl for cross-luminance reduction and/or
rainbows for cross-color reduction.
lt
Set spatial luma threshold. Lower values increases reduction of cross-luminance.
tl
Set tolerance for temporal luma. Higher values increases reduction of cross-luminance.
tc
Set tolerance for chroma temporal variation. Higher values increases reduction of cross-color.
ct
Set temporal chroma threshold. Lower values increases reduction of cross-color.
39.62 deflate
Apply deflate effect to the video.
This filter replaces the pixel by the local(3x3) average by taking into account
only values lower than the pixel.
It accepts the following options:
threshold0
threshold1
threshold2
threshold3
Limit the maximum change for each plane, default is 65535.
If 0, plane will remain unchanged.
39.62.1 Commands
This filter supports the all above options as commands.
39.63 deflicker
Remove temporal frame luminance variations.
It accepts the following options:
size, s
Set moving-average filter size in frames. Default is 5. Allowed range is 2 - 129.
mode, m
Set averaging mode to smooth temporal luminance variations.
Available values are:
‘am’
Arithmetic mean
‘gm’
Geometric mean
‘hm’
Harmonic mean
‘qm’
Quadratic mean
‘cm’
Cubic mean
‘pm’
Power mean
‘median’
Median
bypass
Do not actually modify frame. Useful when one only wants metadata.
39.64 dejudder
Remove judder produced by partially interlaced telecined content.
Judder can be introduced, for instance, by pullup filter. If the original
source was partially telecined content then the output of pullup,dejudder
will have a variable frame rate. May change the recorded frame rate of the
container. Aside from that change, this filter will not affect constant frame
rate video.
The option available in this filter is:
cycle
Specify the length of the window over which the judder repeats.
Accepts any integer greater than 1. Useful values are:
‘4’
If the original was telecined from 24 to 30 fps (Film to NTSC).
‘5’
If the original was telecined from 25 to 30 fps (PAL to NTSC).
‘20’
If a mixture of the two.
The default is ‘4’.
39.65 delogo
Suppress a TV station logo by a simple interpolation of the surrounding
pixels. Just set a rectangle covering the logo and watch it disappear
(and sometimes something even uglier appear - your mileage may vary).
It accepts the following parameters:
x
y
Specify the top left corner coordinates of the logo. They must be
specified.
w
h
Specify the width and height of the logo to clear. They must be
specified.
show
When set to 1, a green rectangle is drawn on the screen to simplify
finding the right x, y, w, and h parameters.
The default value is 0.
The rectangle is drawn on the outermost pixels which will be (partly)
replaced with interpolated values. The values of the next pixels
immediately outside this rectangle in each direction will be used to
compute the interpolated pixel values inside the rectangle.
39.65.1 Examples
Set a rectangle covering the area with top left corner coordinates 0,0
and size 100x77:
delogo=x=0:y=0:w=100:h=77
39.66 derain
Remove the rain in the input image/video by applying the derain methods based on
convolutional neural networks. Supported models:
Recurrent Squeeze-and-Excitation Context Aggregation Net (RESCAN).
See http://openaccess.thecvf.com/content_ECCV_2018/papers/Xia_Li_Recurrent_Squeeze-and-Excitation_Context_ECCV_2018_paper.pdf.
Training as well as model generation scripts are provided in
the repository at https://github.com/XueweiMeng/derain_filter.git.
The filter accepts the following options:
filter_type
Specify which filter to use. This option accepts the following values:
‘derain’
Derain filter. To conduct derain filter, you need to use a derain model.
‘dehaze’
Dehaze filter. To conduct dehaze filter, you need to use a dehaze model.
Default value is ‘derain’.
dnn_backend
Specify which DNN backend to use for model loading and execution. This option accepts
the following values:
‘tensorflow’
TensorFlow backend. To enable this backend you
need to install the TensorFlow for C library (see
https://www.tensorflow.org/install/lang_c) and configure FFmpeg with
--enable-libtensorflow
model
Set path to model file specifying network architecture and its parameters.
Note that different backends use different file formats. TensorFlow can load files for only its format.
To get full functionality (such as async execution), please use the dnn_processing filter.
39.67 deshake
Attempt to fix small changes in horizontal and/or vertical shift. This
filter helps remove camera shake from hand-holding a camera, bumping a
tripod, moving on a vehicle, etc.
The filter accepts the following options:
x
y
w
h
Specify a rectangular area where to limit the search for motion
vectors.
If desired the search for motion vectors can be limited to a
rectangular area of the frame defined by its top left corner, width
and height. These parameters have the same meaning as the drawbox
filter which can be used to visualise the position of the bounding
box.
This is useful when simultaneous movement of subjects within the frame
might be confused for camera motion by the motion vector search.
If any or all of x, y, w and h are set to -1
then the full frame is used. This allows later options to be set
without specifying the bounding box for the motion vector search.
Default - search the whole frame.
rx
ry
Specify the maximum extent of movement in x and y directions in the
range 0-64 pixels. Default 16.
edge
Specify how to generate pixels to fill blanks at the edge of the
frame. Available values are:
‘blank, 0’
Fill zeroes at blank locations
‘original, 1’
Original image at blank locations
‘clamp, 2’
Extruded edge value at blank locations
‘mirror, 3’
Mirrored edge at blank locations
Default value is ‘mirror’.
blocksize
Specify the blocksize to use for motion search. Range 4-128 pixels,
default 8.
contrast
Specify the contrast threshold for blocks. Only blocks with more than
the specified contrast (difference between darkest and lightest
pixels) will be considered. Range 1-255, default 125.
search
Specify the search strategy. Available values are:
‘exhaustive, 0’
Set exhaustive search
‘less, 1’
Set less exhaustive search.
Default value is ‘exhaustive’.
filename
If set then a detailed log of the motion search is written to the
specified file.
39.68 despill
Remove unwanted contamination of foreground colors, caused by reflected color of
greenscreen or bluescreen.
This filter accepts the following options:
type
Set what type of despill to use.
mix
Set how spillmap will be generated.
expand
Set how much to get rid of still remaining spill.
red
Controls amount of red in spill area.
green
Controls amount of green in spill area.
Should be -1 for greenscreen.
blue
Controls amount of blue in spill area.
Should be -1 for bluescreen.
brightness
Controls brightness of spill area, preserving colors.
alpha
Modify alpha from generated spillmap.
39.68.1 Commands
This filter supports the all above options as commands.
39.69 detelecine
Apply an exact inverse of the telecine operation. It requires a predefined
pattern specified using the pattern option which must be the same as that passed
to the telecine filter.
This filter accepts the following options:
first_field
‘top, t’
top field first
‘bottom, b’
bottom field first
The default value is top.
pattern
A string of numbers representing the pulldown pattern you wish to apply.
The default value is 23.
start_frame
A number representing position of the first frame with respect to the telecine
pattern. This is to be used if the stream is cut. The default value is 0.
39.70 dilation
Apply dilation effect to the video.
This filter replaces the pixel by the local(3x3) maximum.
It accepts the following options:
threshold0
threshold1
threshold2
threshold3
Limit the maximum change for each plane, default is 65535.
If 0, plane will remain unchanged.
coordinates
Flag which specifies the pixel to refer to. Default is 255 i.e. all eight
pixels are used.
Flags to local 3x3 coordinates maps like this:
1 2 3
4   5
6 7 8
39.70.1 Commands
This filter supports the all above options as commands.
39.71 displace
Displace pixels as indicated by second and third input stream.
It takes three input streams and outputs one stream, the first input is the
source, and second and third input are displacement maps.
The second input specifies how much to displace pixels along the
x-axis, while the third input specifies how much to displace pixels
along the y-axis.
If one of displacement map streams terminates, last frame from that
displacement map will be used.
Note that once generated, displacements maps can be reused over and over again.
A description of the accepted options follows.
edge
Set displace behavior for pixels that are out of range.
Available values are:
‘blank’
Missing pixels are replaced by black pixels.
‘smear’
Adjacent pixels will spread out to replace missing pixels.
‘wrap’
Out of range pixels are wrapped so they point to pixels of other side.
‘mirror’
Out of range pixels will be replaced with mirrored pixels.
Default is ‘smear’.
39.71.1 Examples
Add ripple effect to rgb input of video size hd720:
ffmpeg -i INPUT -f lavfi -i nullsrc=s=hd720,lutrgb=128:128:128 -f lavfi -i nullsrc=s=hd720,geq='r=128+30*sin(2*PI*X/400+T):g=128+30*sin(2*PI*X/400+T):b=128+30*sin(2*PI*X/400+T)' -lavfi '[0][1][2]displace' OUTPUT
Add wave effect to rgb input of video size hd720:
ffmpeg -i INPUT -f lavfi -i nullsrc=hd720,geq='r=128+80*(sin(sqrt((X-W/2)*(X-W/2)+(Y-H/2)*(Y-H/2))/220*2*PI+T)):g=128+80*(sin(sqrt((X-W/2)*(X-W/2)+(Y-H/2)*(Y-H/2))/220*2*PI+T)):b=128+80*(sin(sqrt((X-W/2)*(X-W/2)+(Y-H/2)*(Y-H/2))/220*2*PI+T))' -lavfi '[1]split[x][y],[0][x][y]displace' OUTPUT
39.72 dnn_classify
Do classification with deep neural networks based on bounding boxes.
The filter accepts the following options:
dnn_backend
Specify which DNN backend to use for model loading and execution. This option accepts
only openvino now, tensorflow backends will be added.
model
Set path to model file specifying network architecture and its parameters.
Note that different backends use different file formats.
input
Set the input name of the dnn network.
output
Set the output name of the dnn network.
confidence
Set the confidence threshold (default: 0.5).
labels
Set path to label file specifying the mapping between label id and name.
Each label name is written in one line, tailing spaces and empty lines are skipped.
The first line is the name of label id 0,
and the second line is the name of label id 1, etc.
The label id is considered as name if the label file is not provided.
backend_configs
Set the configs to be passed into backend
For tensorflow backend, you can set its configs with sess_config options,
please use tools/python/tf_sess_config.py to get the configs for your system.
39.73 dnn_detect
Do object detection with deep neural networks.
The filter accepts the following options:
dnn_backend
Specify which DNN backend to use for model loading and execution. This option accepts
only openvino now, tensorflow backends will be added.
model
Set path to model file specifying network architecture and its parameters.
Note that different backends use different file formats.
input
Set the input name of the dnn network.
output
Set the output name of the dnn network.
confidence
Set the confidence threshold (default: 0.5).
labels
Set path to label file specifying the mapping between label id and name.
Each label name is written in one line, tailing spaces and empty lines are skipped.
The first line is the name of label id 0 (usually it is ’background’),
and the second line is the name of label id 1, etc.
The label id is considered as name if the label file is not provided.
backend_configs
Set the configs to be passed into backend. To use async execution, set async (default: set).
Roll back to sync execution if the backend does not support async.
39.74 dnn_processing
Do image processing with deep neural networks. It works together with another filter
which converts the pixel format of the Frame to what the dnn network requires.
The filter accepts the following options:
dnn_backend
Specify which DNN backend to use for model loading and execution. This option accepts
the following values:
‘tensorflow’
TensorFlow backend. To enable this backend you
need to install the TensorFlow for C library (see
https://www.tensorflow.org/install/lang_c) and configure FFmpeg with
--enable-libtensorflow
‘openvino’
OpenVINO backend. To enable this backend you
need to build and install the OpenVINO for C library (see
https://github.com/openvinotoolkit/openvino/blob/master/build-instruction.md) and configure FFmpeg with
--enable-libopenvino (–extra-cflags=-I... –extra-ldflags=-L... might
be needed if the header files and libraries are not installed into system path)
‘torch’
Libtorch backend. To enable this backend you need to build and install Libtroch
for C++ library. Please download cxx11 ABI version (see
https://pytorch.org/get-started/locally)
and configure FFmpeg with --enable-libtorch
--extra-cflags=-I/libtorch_root/libtorch/include
--extra-cflags=-I/libtorch_root/libtorch/include/torch/csrc/api/include
--extra-ldflags=-L/libtorch_root/libtorch/lib/
model
Set path to model file specifying network architecture and its parameters.
Note that different backends use different file formats. TensorFlow, OpenVINO
and Libtorch backend can load files for only its format.
input
Set the input name of the dnn network.
output
Set the output name of the dnn network.
backend_configs
Set the configs to be passed into backend. To use async execution, set async (default: set).
Roll back to sync execution if the backend does not support async.
For tensorflow backend, you can set its configs with sess_config options,
please use tools/python/tf_sess_config.py to get the configs of TensorFlow backend for your system.
39.74.1 Examples
Remove rain in rgb24 frame with can.pb (see derain filter):
./ffmpeg -i rain.jpg -vf format=rgb24,dnn_processing=dnn_backend=tensorflow:model=can.pb:input=x:output=y derain.jpg
Handle the Y channel with srcnn.pb (see sr filter) for frame with yuv420p (planar YUV formats supported):
./ffmpeg -i 480p.jpg -vf format=yuv420p,scale=w=iw*2:h=ih*2,dnn_processing=dnn_backend=tensorflow:model=srcnn.pb:input=x:output=y -y srcnn.jpg
Handle the Y channel with espcn.pb (see sr filter), which changes frame size, for format yuv420p (planar YUV formats supported),
please use tools/python/tf_sess_config.py to get the configs of TensorFlow backend for your system.
./ffmpeg -i 480p.jpg -vf format=yuv420p,dnn_processing=dnn_backend=tensorflow:model=espcn.pb:input=x:output=y:backend_configs=sess_config=0x10022805320e09cdccccccccccec3f20012a01303801 -y tmp.espcn.jpg
39.75 drawbox
Draw a colored box on the input image.
It accepts the following parameters:
x
y
The expressions which specify the top left corner coordinates of the box. It defaults to 0.
width, w
height, h
The expressions which specify the width and height of the box; if 0 they are interpreted as
the input width and height. It defaults to 0.
color, c
Specify the color of the box to write. For the general syntax of this option,
check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special
value invert is used, the box edge color is the same as the
video with inverted luma.
thickness, t
The expression which sets the thickness of the box edge.
A value of fill will create a filled box. Default value is 3.
See below for the list of accepted constants.
replace
Applicable if the input has alpha. With value 1, the pixels of the painted box
will overwrite the video’s color and alpha pixels.
Default is 0, which composites the box onto the input, leaving the video’s alpha intact.
The parameters for x, y, w and h and t are expressions containing the
following constants:
dar
The input display aspect ratio, it is the same as (w / h) * sar.
hsub
vsub
horizontal and vertical chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
in_h, ih
in_w, iw
The input width and height.
sar
The input sample aspect ratio.
x
y
The x and y offset coordinates where the box is drawn.
w
h
The width and height of the drawn box.
box_source
Box source can be set as side_data_detection_bboxes if you want to use box data in
detection bboxes of side data.
If box_source is set, the x, y, width and height will be ignored and
still use box data in detection bboxes of side data. So please do not use this parameter if you were
not sure about the box source.
t
The thickness of the drawn box.
These constants allow the x, y, w, h and t expressions to refer to
each other, so you may for example specify y=x/dar or h=w/dar.
39.75.1 Examples
Draw a black box around the edge of the input image:
drawbox
Draw a box with color red and an opacity of 50%:
drawbox=10:20:200:60:[email protected]
The previous example can be specified as:
drawbox=x=10:y=20:w=200:h=60:[email protected]
Fill the box with pink color:
drawbox=x=10:y=10:w=100:h=100:[email protected]:t=fill
Draw a 2-pixel red 2.40:1 mask:
drawbox=x=-t:y=0.5*(ih-iw/2.4)-t:w=iw+t*2:h=iw/2.4+t*2:t=2:c=red
39.75.2 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.76 drawgraph
Draw a graph using input video metadata.
It accepts the following parameters:
m1
Set 1st frame metadata key from which metadata values will be used to draw a graph.
fg1
Set 1st foreground color expression.
m2
Set 2nd frame metadata key from which metadata values will be used to draw a graph.
fg2
Set 2nd foreground color expression.
m3
Set 3rd frame metadata key from which metadata values will be used to draw a graph.
fg3
Set 3rd foreground color expression.
m4
Set 4th frame metadata key from which metadata values will be used to draw a graph.
fg4
Set 4th foreground color expression.
min
Set minimal value of metadata value.
max
Set maximal value of metadata value.
bg
Set graph background color. Default is white.
mode
Set graph mode.
Available values for mode is:
‘bar’
‘dot’
‘line’
Default is line.
slide
Set slide mode.
Available values for slide is:
‘frame’
Draw new frame when right border is reached.
‘replace’
Replace old columns with new ones.
‘scroll’
Scroll from right to left.
‘rscroll’
Scroll from left to right.
‘picture’
Draw single picture.
Default is frame.
size
Set size of graph video. For the syntax of this option, check the
(ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.
The default value is 900x256.
rate, r
Set the output frame rate. Default value is 25.
The foreground color expressions can use the following variables:
MIN
Minimal value of metadata value.
MAX
Maximal value of metadata value.
VAL
Current metadata key value.
The color is defined as 0xAABBGGRR.
Example using metadata from signalstats filter:
signalstats,drawgraph=lavfi.signalstats.YAVG:min=0:max=255
Example using metadata from ebur128 filter:
ebur128=metadata=1,adrawgraph=lavfi.r128.M:min=-120:max=5
39.77 drawgrid
Draw a grid on the input image.
It accepts the following parameters:
x
y
The expressions which specify the coordinates of some point of grid intersection (meant to configure offset). Both default to 0.
width, w
height, h
The expressions which specify the width and height of the grid cell, if 0 they are interpreted as the
input width and height, respectively, minus thickness, so image gets
framed. Default to 0.
color, c
Specify the color of the grid. For the general syntax of this option,
check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual. If the special
value invert is used, the grid color is the same as the
video with inverted luma.
thickness, t
The expression which sets the thickness of the grid line. Default value is 1.
See below for the list of accepted constants.
replace
Applicable if the input has alpha. With 1 the pixels of the painted grid
will overwrite the video’s color and alpha pixels.
Default is 0, which composites the grid onto the input, leaving the video’s alpha intact.
The parameters for x, y, w and h and t are expressions containing the
following constants:
dar
The input display aspect ratio, it is the same as (w / h) * sar.
hsub
vsub
horizontal and vertical chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
in_h, ih
in_w, iw
The input grid cell width and height.
sar
The input sample aspect ratio.
x
y
The x and y coordinates of some point of grid intersection (meant to configure offset).
w
h
The width and height of the drawn cell.
t
The thickness of the drawn cell.
These constants allow the x, y, w, h and t expressions to refer to
each other, so you may for example specify y=x/dar or h=w/dar.
39.77.1 Examples
Draw a grid with cell 100x100 pixels, thickness 2 pixels, with color red and an opacity of 50%:
drawgrid=width=100:height=100:thickness=2:[email protected]
Draw a white 3x3 grid with an opacity of 50%:
drawgrid=w=iw/3:h=ih/3:t=2:[email protected]
39.77.2 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.78 drawtext
Draw a text string or text from a specified file on top of a video, using the
libfreetype library.
To enable compilation of this filter, you need to configure FFmpeg with
--enable-libfreetype and --enable-libharfbuzz.
To enable default font fallback and the font option you need to
configure FFmpeg with --enable-libfontconfig.
To enable the text_shaping option, you need to configure FFmpeg with
--enable-libfribidi.
39.78.1 Syntax
It accepts the following parameters:
box
Used to draw a box around text using the background color.
The value must be either 1 (enable) or 0 (disable).
The default value of box is 0.
boxborderw
Set the width of the border to be drawn around the box using boxcolor.
The value must be specified using one of the following formats:
boxborderw=10 set the width of all the borders to 10
boxborderw=10|20 set the width of the top and bottom borders to 10
and the width of the left and right borders to 20
boxborderw=10|20|30 set the width of the top border to 10, the width
of the bottom border to 30 and the width of the left and right borders to 20
boxborderw=10|20|30|40 set the borders width to 10 (top), 20 (right),
30 (bottom), 40 (left)
The default value of boxborderw is "0".
boxcolor
The color to be used for drawing box around text. For the syntax of this
option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual.
The default value of boxcolor is "white".
line_spacing
Set the line spacing in pixels. The default value of line_spacing is 0.
text_align
Set the vertical and horizontal alignment of the text with respect to the box boundaries.
The value is combination of flags, one for the vertical alignment (T=top,
M=middle, B=bottom) and one for the horizontal alignment (L=left, C=center, R=right).
Please note that tab characters are only supported with the left horizontal alignment.
y_align
Specify what the y value is referred to. Possible values are:
text the top of the highest glyph of the first text line is placed at y
baseline the baseline of the first text line is placed at y
font the baseline of the first text line is placed at y plus the
ascent (in pixels) defined in the font metrics
The default value of y_align is "text" for backward compatibility.
borderw
Set the width of the border to be drawn around the text using bordercolor.
The default value of borderw is 0.
bordercolor
Set the color to be used for drawing border around text. For the syntax of this
option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual.
The default value of bordercolor is "black".
expansion
Select how the text is expanded. Can be either none,
strftime (deprecated) or normal (default). See the
Text expansion section below for details.
basetime
Set a start time for the count. Value is in microseconds. Only applied
in the deprecated strftime expansion mode. To emulate in normal expansion
mode use the pts function, supplying the start time (in seconds)
as the second argument.
fix_bounds
If true, check and fix text coords to avoid clipping.
fontcolor
The color to be used for drawing fonts. For the syntax of this option, check
the (ffmpeg-utils)"Color" section in the ffmpeg-utils manual.
The default value of fontcolor is "black".
fontcolor_expr
String which is expanded the same way as text to obtain dynamic
fontcolor value. By default this option has empty value and is not
processed. When this option is set, it overrides fontcolor option.
font
The font family to be used for drawing text. By default Sans.
fontfile
The font file to be used for drawing text. The path must be included.
This parameter is mandatory if the fontconfig support is disabled.
alpha
Draw the text applying alpha blending. The value can
be a number between 0.0 and 1.0.
The expression accepts the same variables x, y as well.
The default value is 1.
Please see fontcolor_expr.
fontsize
The font size to be used for drawing text.
The default value of fontsize is 16.
text_shaping
If set to 1, attempt to shape the text (for example, reverse the order of
right-to-left text and join Arabic characters) before drawing it.
Otherwise, just draw the text exactly as given.
By default 1 (if supported).
ft_load_flags
The flags to be used for loading the fonts.
The flags map the corresponding flags supported by libfreetype, and are
a combination of the following values:
default
no_scale
no_hinting
render
no_bitmap
vertical_layout
force_autohint
crop_bitmap
pedantic
ignore_global_advance_width
no_recurse
ignore_transform
monochrome
linear_design
no_autohint
Default value is "default".
For more information consult the documentation for the FT_LOAD_*
libfreetype flags.
shadowcolor
The color to be used for drawing a shadow behind the drawn text. For the
syntax of this option, check the (ffmpeg-utils)"Color" section in the
ffmpeg-utils manual.
The default value of shadowcolor is "black".
boxw
Set the width of the box to be drawn around text.
The default value of boxw is computed automatically to match the text width
boxh
Set the height of the box to be drawn around text.
The default value of boxh is computed automatically to match the text height
shadowx
shadowy
The x and y offsets for the text shadow position with respect to the
position of the text. They can be either positive or negative
values. The default value for both is "0".
start_number
The starting frame number for the n/frame_num variable. The default value
is "0".
tabsize
The size in number of spaces to use for rendering the tab.
Default value is 4.
timecode
Set the initial timecode representation in "hh:mm:ss[:;.]ff"
format. It can be used with or without text parameter. timecode_rate
option must be specified.
timecode_rate, rate, r
Set the timecode frame rate (timecode only). Value will be rounded to nearest
integer. Minimum value is "1".
Drop-frame timecode is supported for frame rates 30 & 60.
tc24hmax
If set to 1, the output of the timecode option will wrap around at 24 hours.
Default is 0 (disabled).
text
The text string to be drawn. The text must be a sequence of UTF-8
encoded characters.
This parameter is mandatory if no file is specified with the parameter
textfile.
textfile
A text file containing text to be drawn. The text must be a sequence
of UTF-8 encoded characters.
This parameter is mandatory if no text string is specified with the
parameter text.
If both text and textfile are specified, an error is thrown.
text_source
Text source should be set as side_data_detection_bboxes if you want to use text data in
detection bboxes of side data.
If text source is set, text and textfile will be ignored and still use
text data in detection bboxes of side data. So please do not use this parameter
if you are not sure about the text source.
reload
The textfile will be reloaded at specified frame interval.
Be sure to update textfile atomically, or it may be read partially,
or even fail.
Range is 0 to INT_MAX. Default is 0.
x
y
The expressions which specify the offsets where text will be drawn
within the video frame. They are relative to the top/left border of the
output image.
The default value of x and y is "0".
See below for the list of accepted constants and functions.
The parameters for x and y are expressions containing the
following constants and functions:
dar
input display aspect ratio, it is the same as (w / h) * sar
hsub
vsub
horizontal and vertical chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
line_h, lh
the height of each text line
main_h, h, H
the input height
main_w, w, W
the input width
max_glyph_a, ascent
the maximum distance from the baseline to the highest/upper grid
coordinate used to place a glyph outline point, for all the rendered
glyphs.
It is a positive value, due to the grid’s orientation with the Y axis
upwards.
max_glyph_d, descent
the maximum distance from the baseline to the lowest grid coordinate
used to place a glyph outline point, for all the rendered glyphs.
This is a negative value, due to the grid’s orientation, with the Y axis
upwards.
max_glyph_h
maximum glyph height, that is the maximum height for all the glyphs
contained in the rendered text, it is equivalent to ascent -
descent.
max_glyph_w
maximum glyph width, that is the maximum width for all the glyphs
contained in the rendered text
font_a
the ascent size defined in the font metrics
font_d
the descent size defined in the font metrics
top_a
the maximum ascender of the glyphs of the first text line
bottom_d
the maximum descender of the glyphs of the last text line
n
the number of input frame, starting from 0
rand(min, max)
return a random number included between min and max
sar
The input sample aspect ratio.
t
timestamp expressed in seconds, NAN if the input timestamp is unknown
text_h, th
the height of the rendered text
text_w, tw
the width of the rendered text
x
y
the x and y offset coordinates where the text is drawn.
These parameters allow the x and y expressions to refer
to each other, so you can for example specify y=x/dar.
pict_type
A one character description of the current frame’s picture type.
pkt_pos
The current packet’s position in the input file or stream
(in bytes, from the start of the input). A value of -1 indicates
this info is not available.
duration
The current packet’s duration, in seconds.
pkt_size
The current packet’s size (in bytes).
39.78.2 Text expansion
If expansion is set to strftime, the filter recognizes
sequences accepted by the strftime C function in the provided
text and expands them accordingly. Check the documentation of
strftime. This feature is deprecated in favor of normal
expansion with the gmtime or localtime expansion
functions.
If expansion is set to none, the text is printed verbatim.
If expansion is set to normal (which is the default),
the following expansion mechanism is used.
The backslash character ‘\’, followed by any character, always expands to
the second character.
Sequences of the form %{...} are expanded. The text between the
braces is a function name, possibly followed by arguments separated by ’:’.
If the arguments contain special characters or delimiters (’:’ or ’}’),
they should be escaped.
Note that they probably must also be escaped as the value for the text
option in the filter argument string and as the filter argument in the
filtergraph description, and possibly also for the shell, that makes up to four
levels of escaping; using a text file with the textfile option avoids
these problems.
The following functions are available:
expr, e
The expression evaluation result.
It must take one argument specifying the expression to be evaluated,
which accepts the same constants and functions as the x and
y values. Note that not all constants should be used, for
example the text size is not known when evaluating the expression, so
the constants text_w and text_h will have an undefined
value.
expr_int_format, eif
Evaluate the expression’s value and output as formatted integer.
The first argument is the expression to be evaluated, just as for the expr function.
The second argument specifies the output format. Allowed values are ‘x’,
‘X’, ‘d’ and ‘u’. They are treated exactly as in the
printf function.
The third parameter is optional and sets the number of positions taken by the output.
It can be used to add padding with zeros from the left.
gmtime
The time at which the filter is running, expressed in UTC.
It can accept an argument: a strftime C function format string.
The format string is extended to support the variable %[1-6]N
which prints fractions of the second with optionally specified number of digits.
localtime
The time at which the filter is running, expressed in the local time zone.
It can accept an argument: a strftime C function format string.
The format string is extended to support the variable %[1-6]N
which prints fractions of the second with optionally specified number of digits.
metadata
Frame metadata. Takes one or two arguments.
The first argument is mandatory and specifies the metadata key.
The second argument is optional and specifies a default value, used when the
metadata key is not found or empty.
Available metadata can be identified by inspecting entries
starting with TAG included within each frame section
printed by running ffprobe -show_frames.
String metadata generated in filters leading to
the drawtext filter are also available.
n, frame_num
The frame number, starting from 0.
pict_type
A one character description of the current picture type.
pts
The timestamp of the current frame.
It can take up to three arguments.
The first argument is the format of the timestamp; it defaults to flt
for seconds as a decimal number with microsecond accuracy; hms stands
for a formatted [-]HH:MM:SS.mmm timestamp with millisecond accuracy.
gmtime stands for the timestamp of the frame formatted as UTC time;
localtime stands for the timestamp of the frame formatted as
local time zone time.
The second argument is an offset added to the timestamp.
If the format is set to hms, a third argument 24HH may be
supplied to present the hour part of the formatted timestamp in 24h format
(00-23).
If the format is set to localtime or gmtime, a third
argument may be supplied: a strftime C function format string.
By default, YYYY-MM-DD HH:MM:SS format will be used.
39.78.3 Commands
This filter supports altering parameters via commands:
reinit
Alter existing filter parameters.
Syntax for the argument is the same as for filter invocation, e.g.
fontsize=56:fontcolor=green:text='Hello World'
Full filter invocation with sendcmd would look like this:
sendcmd=c='56.0 drawtext reinit fontsize=56\:fontcolor=green\:text=Hello\\ World'
If the entire argument can’t be parsed or applied as valid values then the filter will
continue with its existing parameters.
The following options are also supported as commands:
x
y
alpha
fontsize
fontcolor
boxcolor
bordercolor
shadowcolor
box
boxw
boxh
boxborderw
line_spacing
text_align
shadowx
shadowy
borderw
39.78.4 Examples
Draw "Test Text" with font FreeSerif, using the default values for the
optional parameters.
drawtext="fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf: text='Test Text'"
Draw ’Test Text’ with font FreeSerif of size 24 at position x=100
and y=50 (counting from the top-left corner of the screen), text is
yellow with a red box around it. Both the text and the box have an
opacity of 20%.
drawtext="fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf: text='Test Text':\
x=100: y=50: fontsize=24: [email protected]: box=1: [email protected]"
Note that the double quotes are not necessary if spaces are not used
within the parameter list.
Show the text at the center of the video frame:
drawtext="fontsize=30:fontfile=FreeSerif.ttf:text='hello world':x=(w-text_w)/2:y=(h-text_h)/2"
Show the text at a random position, switching to a new position every 30 seconds:
drawtext="fontsize=30:fontfile=FreeSerif.ttf:text='hello world':x=if(eq(mod(t\,30)\,0)\,rand(0\,(w-text_w))\,x):y=if(eq(mod(t\,30)\,0)\,rand(0\,(h-text_h))\,y)"
Show a text line sliding from right to left in the last row of the video
frame. The file LONG_LINE is assumed to contain a single line
with no newlines.
drawtext="fontsize=15:fontfile=FreeSerif.ttf:text=LONG_LINE:y=h-line_h:x=-50*t"
Show the content of file CREDITS off the bottom of the frame and scroll up.
drawtext="fontsize=20:fontfile=FreeSerif.ttf:textfile=CREDITS:y=h-20*t"
Draw a single green letter "g", at the center of the input video.
The glyph baseline is placed at half screen height.
drawtext="fontsize=60:fontfile=FreeSerif.ttf:fontcolor=green:text=g:x=(w-max_glyph_w)/2:y=h/2-ascent"
Show text for 1 second every 3 seconds:
drawtext="fontfile=FreeSerif.ttf:fontcolor=white:x=100:y=x/dar:enable=lt(mod(t\,3)\,1):text='blink'"
Use fontconfig to set the font. Note that the colons need to be escaped.
drawtext='fontfile=Linux Libertine O-40\\:style=Semibold:text=FFmpeg'
Draw "Test Text" with font size dependent on height of the video.
drawtext="text='Test Text': fontsize=h/30: x=(w-text_w)/2: y=(h-text_h*2)"
Print the date of a real-time encoding (see documentation for the
strftime C function):
drawtext='fontfile=FreeSans.ttf:text=%{localtime\:%a %b %d %Y}'
Show text fading in and out (appearing/disappearing):
#!/bin/sh
DS=1.0 # display start
DE=10.0 # display end
FID=1.5 # fade in duration
FOD=5 # fade out duration
ffplay -f lavfi "color,drawtext=text=TEST:fontsize=50:fontfile=FreeSerif.ttf:fontcolor_expr=ff0000%{eif\\\\: clip(255*(1*between(t\\, $DS + $FID\\, $DE - $FOD) + ((t - $DS)/$FID)*between(t\\, $DS\\, $DS + $FID) + (-(t - $DE)/$FOD)*between(t\\, $DE - $FOD\\, $DE) )\\, 0\\, 255) \\\\: x\\\\: 2 }"
Horizontally align multiple separate texts. Note that max_glyph_a
and the fontsize value are included in the y offset.
drawtext=fontfile=FreeSans.ttf:text=DOG:fontsize=24:x=10:y=20+24-max_glyph_a,
drawtext=fontfile=FreeSans.ttf:text=cow:fontsize=24:x=80:y=20+24-max_glyph_a
Plot special lavf.image2dec.source_basename metadata onto each frame if
such metadata exists. Otherwise, plot the string "NA". Note that image2 demuxer
must have option -export_path_metadata 1 for the special metadata fields
to be available for filters.
drawtext="fontsize=20:fontcolor=white:fontfile=FreeSans.ttf:text='%{metadata\:lavf.image2dec.source_basename\:NA}':x=10:y=10"
For more information about libfreetype, check:
http://www.freetype.org/.
For more information about fontconfig, check:
http://freedesktop.org/software/fontconfig/fontconfig-user.html.
For more information about libfribidi, check:
http://fribidi.org/.
For more information about libharfbuzz, check:
https://github.com/harfbuzz/harfbuzz.
39.79 edgedetect
Detect and draw edges. The filter uses the Canny Edge Detection algorithm.
The filter accepts the following options:
low
high
Set low and high threshold values used by the Canny thresholding
algorithm.
The high threshold selects the "strong" edge pixels, which are then
connected through 8-connectivity with the "weak" edge pixels selected
by the low threshold.
low and high threshold values must be chosen in the range
[0,1], and low should be lesser or equal to high.
Default value for low is 20/255, and default value for high
is 50/255.
mode
Define the drawing mode.
‘wires’
Draw white/gray wires on black background.
‘colormix’
Mix the colors to create a paint/cartoon effect.
‘canny’
Apply Canny edge detector on all selected planes.
Default value is wires.
planes
Select planes for filtering. By default all available planes are filtered.
39.79.1 Examples
Standard edge detection with custom values for the hysteresis thresholding:
edgedetect=low=0.1:high=0.4
Painting effect without thresholding:
edgedetect=mode=colormix:high=0
39.80 elbg
Apply a posterize effect using the ELBG (Enhanced LBG) algorithm.
For each input image, the filter will compute the optimal mapping from
the input to the output given the codebook length, that is the number
of distinct output colors.
This filter accepts the following options.
codebook_length, l
Set codebook length. The value must be a positive integer, and
represents the number of distinct output colors. Default value is 256.
nb_steps, n
Set the maximum number of iterations to apply for computing the optimal
mapping. The higher the value the better the result and the higher the
computation time. Default value is 1.
seed, s
Set a random seed, must be an integer included between 0 and
UINT32_MAX. If not specified, or if explicitly set to -1, the filter
will try to use a good random seed on a best effort basis.
pal8
Set pal8 output pixel format. This option does not work with codebook
length greater than 256. Default is disabled.
use_alpha
Include alpha values in the quantization calculation. Allows creating
palettized output images (e.g. PNG8) with multiple alpha smooth blending.
39.81 entropy
Measure graylevel entropy in histogram of color channels of video frames.
It accepts the following parameters:
mode
Can be either normal or diff. Default is normal.
diff mode measures entropy of histogram delta values, absolute differences
between neighbour histogram values.
39.82 epx
Apply the EPX magnification filter which is designed for pixel art.
It accepts the following option:
n
Set the scaling dimension: 2 for 2xEPX, 3 for
3xEPX.
Default is 3.
39.83 eq
Set brightness, contrast, saturation and approximate gamma adjustment.
The filter accepts the following options:
contrast
Set the contrast expression. The value must be a float value in range
-1000.0 to 1000.0. The default value is "1".
brightness
Set the brightness expression. The value must be a float value in
range -1.0 to 1.0. The default value is "0".
saturation
Set the saturation expression. The value must be a float in
range 0.0 to 3.0. The default value is "1".
gamma
Set the gamma expression. The value must be a float in range
0.1 to 10.0.  The default value is "1".
gamma_r
Set the gamma expression for red. The value must be a float in
range 0.1 to 10.0. The default value is "1".
gamma_g
Set the gamma expression for green. The value must be a float in range
0.1 to 10.0. The default value is "1".
gamma_b
Set the gamma expression for blue. The value must be a float in range
0.1 to 10.0. The default value is "1".
gamma_weight
Set the gamma weight expression. It can be used to reduce the effect
of a high gamma value on bright image areas, e.g. keep them from
getting overamplified and just plain white. The value must be a float
in range 0.0 to 1.0. A value of 0.0 turns the
gamma correction all the way down while 1.0 leaves it at its
full strength. Default is "1".
eval
Set when the expressions for brightness, contrast, saturation and
gamma expressions are evaluated.
It accepts the following values:
‘init’
only evaluate expressions once during the filter initialization or
when a command is processed
‘frame’
evaluate expressions for each incoming frame
Default value is ‘init’.
The expressions accept the following parameters:
n
frame count of the input frame starting from 0
pos
byte position of the corresponding packet in the input file, NAN if
unspecified; deprecated, do not use
r
frame rate of the input video, NAN if the input frame rate is unknown
t
timestamp expressed in seconds, NAN if the input timestamp is unknown
39.83.1 Commands
The filter supports the following commands:
contrast
Set the contrast expression.
brightness
Set the brightness expression.
saturation
Set the saturation expression.
gamma
Set the gamma expression.
gamma_r
Set the gamma_r expression.
gamma_g
Set gamma_g expression.
gamma_b
Set gamma_b expression.
gamma_weight
Set gamma_weight expression.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.84 erosion
Apply erosion effect to the video.
This filter replaces the pixel by the local(3x3) minimum.
It accepts the following options:
threshold0
threshold1
threshold2
threshold3
Limit the maximum change for each plane, default is 65535.
If 0, plane will remain unchanged.
coordinates
Flag which specifies the pixel to refer to. Default is 255 i.e. all eight
pixels are used.
Flags to local 3x3 coordinates maps like this:
1 2 3
4   5
6 7 8
39.84.1 Commands
This filter supports the all above options as commands.
39.85 estdif
Deinterlace the input video ("estdif" stands for "Edge Slope
Tracing Deinterlacing Filter").
Spatial only filter that uses edge slope tracing algorithm
to interpolate missing lines.
It accepts the following parameters:
mode
The interlacing mode to adopt. It accepts one of the following values:
frame
Output one frame for each frame.
field
Output one frame for each field.
The default value is field.
parity
The picture field parity assumed for the input interlaced video. It accepts one
of the following values:
tff
Assume the top field is first.
bff
Assume the bottom field is first.
auto
Enable automatic detection of field parity.
The default value is auto.
If the interlacing is unknown or the decoder does not export this information,
top field first will be assumed.
deint
Specify which frames to deinterlace. Accepts one of the following
values:
all
Deinterlace all frames.
interlaced
Only deinterlace frames marked as interlaced.
The default value is all.
rslope
Specify the search radius for edge slope tracing. Default value is 1.
Allowed range is from 1 to 15.
redge
Specify the search radius for best edge matching. Default value is 2.
Allowed range is from 0 to 15.
ecost
Specify the edge cost for edge matching. Default value is 2.
Allowed range is from 0 to 50.
mcost
Specify the middle cost for edge matching. Default value is 1.
Allowed range is from 0 to 50.
dcost
Specify the distance cost for edge matching. Default value is 1.
Allowed range is from 0 to 50.
interp
Specify the interpolation used. Default is 4-point interpolation. It accepts one
of the following values:
2p
Two-point interpolation.
4p
Four-point interpolation.
6p
Six-point interpolation.
39.85.1 Commands
This filter supports same commands as options.
39.86 exposure
Adjust exposure of the video stream.
The filter accepts the following options:
exposure
Set the exposure correction in EV. Allowed range is from -3.0 to 3.0 EV
Default value is 0 EV.
black
Set the black level correction. Allowed range is from -1.0 to 1.0.
Default value is 0.
39.86.1 Commands
This filter supports same commands as options.
39.87 extractplanes
Extract color channel components from input video stream into
separate grayscale video streams.
The filter accepts the following option:
planes
Set plane(s) to extract.
Available values for planes are:
‘y’
‘u’
‘v’
‘a’
‘r’
‘g’
‘b’
Choosing planes not available in the input will result in an error.
That means you cannot select r, g, b planes
with y, u, v planes at same time.
39.87.1 Examples
Extract luma, u and v color channel component from input video frame
into 3 grayscale outputs:
ffmpeg -i video.avi -filter_complex 'extractplanes=y+u+v[y][u][v]' -map '[y]' y.avi -map '[u]' u.avi -map '[v]' v.avi
39.88 fade
Apply a fade-in/out effect to the input video.
It accepts the following parameters:
type, t
The effect type can be either "in" for a fade-in, or "out" for a fade-out
effect.
Default is in.
start_frame, s
Specify the number of the frame to start applying the fade
effect at. Default is 0.
nb_frames, n
The number of frames that the fade effect lasts. At the end of the
fade-in effect, the output video will have the same intensity as the input video.
At the end of the fade-out transition, the output video will be filled with the
selected color.
Default is 25.
alpha
If set to 1, fade only alpha channel, if one exists on the input.
Default value is 0.
start_time, st
Specify the timestamp (in seconds) of the frame to start to apply the fade
effect. If both start_frame and start_time are specified, the fade will start at
whichever comes last.  Default is 0.
duration, d
The number of seconds for which the fade effect has to last. At the end of the
fade-in effect the output video will have the same intensity as the input video,
at the end of the fade-out transition the output video will be filled with the
selected color.
If both duration and nb_frames are specified, duration is used. Default is 0
(nb_frames is used by default).
color, c
Specify the color of the fade. Default is "black".
39.88.1 Examples
Fade in the first 30 frames of video:
fade=in:0:30
The command above is equivalent to:
fade=t=in:s=0:n=30
Fade out the last 45 frames of a 200-frame video:
fade=out:155:45
fade=type=out:start_frame=155:nb_frames=45
Fade in the first 25 frames and fade out the last 25 frames of a 1000-frame video:
fade=in:0:25, fade=out:975:25
Make the first 5 frames yellow, then fade in from frame 5-24:
fade=in:5:20:color=yellow
Fade in alpha over first 25 frames of video:
fade=in:0:25:alpha=1
Make the first 5.5 seconds black, then fade in for 0.5 seconds:
fade=t=in:st=5.5:d=0.5
39.89 feedback
Apply feedback video filter.
This filter pass cropped input frames to 2nd output.
From there it can be filtered with other video filters.
After filter receives frame from 2nd input, that frame
is combined on top of original frame from 1st input and passed
to 1st output.
The typical usage is filter only part of frame.
The filter accepts the following options:
x
y
Set the top left crop position.
w
h
Set the crop size.
39.89.1 Examples
Blur only top left rectangular part of video frame size 100x100 with gblur filter.
[in][blurin]feedback=x=0:y=0:w=100:h=100[out][blurout];[blurout]gblur=8[blurin]
Draw black box on top left part of video frame of size 100x100 with drawbox filter.
[in][blurin]feedback=x=0:y=0:w=100:h=100[out][blurout];[blurout]drawbox=x=0:y=0:w=100:h=100:t=100[blurin]
Pixelize rectangular part of video frame of size 100x100 with pixelize filter.
[in][blurin]feedback=x=320:y=240:w=100:h=100[out][blurout];[blurout]pixelize[blurin]
39.90 fftdnoiz
Denoise frames using 3D FFT (frequency domain filtering).
The filter accepts the following options:
sigma
Set the noise sigma constant. This sets denoising strength.
Default value is 1. Allowed range is from 0 to 30.
Using very high sigma with low overlap may give blocking artifacts.
amount
Set amount of denoising. By default all detected noise is reduced.
Default value is 1. Allowed range is from 0 to 1.
block
Set size of block in pixels, Default is 32, can be 8 to 256.
overlap
Set block overlap. Default is 0.5. Allowed range is from 0.2 to 0.8.
method
Set denoising method. Default is wiener, can also be hard.
prev
Set number of previous frames to use for denoising. By default is set to 0.
next
Set number of next frames to to use for denoising. By default is set to 0.
planes
Set planes which will be filtered, by default are all available filtered
except alpha.
39.91 fftfilt
Apply arbitrary expressions to samples in frequency domain
dc_Y
Adjust the dc value (gain) of the luma plane of the image. The filter
accepts an integer value in range 0 to 1000. The default
value is set to 0.
dc_U
Adjust the dc value (gain) of the 1st chroma plane of the image. The
filter accepts an integer value in range 0 to 1000. The
default value is set to 0.
dc_V
Adjust the dc value (gain) of the 2nd chroma plane of the image. The
filter accepts an integer value in range 0 to 1000. The
default value is set to 0.
weight_Y
Set the frequency domain weight expression for the luma plane.
weight_U
Set the frequency domain weight expression for the 1st chroma plane.
weight_V
Set the frequency domain weight expression for the 2nd chroma plane.
eval
Set when the expressions are evaluated.
It accepts the following values:
‘init’
Only evaluate expressions once during the filter initialization.
‘frame’
Evaluate expressions for each incoming frame.
Default value is ‘init’.
The filter accepts the following variables:
X
Y
The coordinates of the current sample.
W
H
The width and height of the image.
N
The number of input frame, starting from 0.
WS
HS
The size of FFT array for horizontal and vertical processing.
39.91.1 Examples
High-pass:
fftfilt=dc_Y=128:weight_Y='squish(1-(Y+X)/100)'
Low-pass:
fftfilt=dc_Y=0:weight_Y='squish((Y+X)/100-1)'
Sharpen:
fftfilt=dc_Y=0:weight_Y='1+squish(1-(Y+X)/100)'
Blur:
fftfilt=dc_Y=0:weight_Y='exp(-4 * ((Y+X)/(W+H)))'
39.92 field
Extract a single field from an interlaced image using stride
arithmetic to avoid wasting CPU time. The output frames are marked as
non-interlaced.
The filter accepts the following options:
type
Specify whether to extract the top (if the value is 0 or
top) or the bottom field (if the value is 1 or
bottom).
39.93 fieldhint
Create new frames by copying the top and bottom fields from surrounding frames
supplied as numbers by the hint file.
hint
Set file containing hints: absolute/relative frame numbers.
There must be one line for each frame in a clip. Each line must contain two
numbers separated by the comma, optionally followed by - or +.
Numbers supplied on each line of file can not be out of [N-1,N+1] where N
is current frame number for absolute mode or out of [-1, 1] range
for relative mode. First number tells from which frame to pick up top
field and second number tells from which frame to pick up bottom field.
If optionally followed by + output frame will be marked as interlaced,
else if followed by - output frame will be marked as progressive, else
it will be marked same as input frame.
If optionally followed by t output frame will use only top field, or in
case of b it will use only bottom field.
If line starts with # or ; that line is skipped.
mode
Can be item absolute or relative or pattern. Default is absolute.
The pattern mode is same as relative mode, except at last entry of file if there
are more frames to process than hint file is seek back to start.
Example of first several lines of hint file for relative mode:
0,0 - # first frame
1,0 - # second frame, use third's frame top field and second's frame bottom field
1,0 - # third frame, use fourth's frame top field and third's frame bottom field
1,0 -
0,0 -
0,0 -
1,0 -
1,0 -
1,0 -
0,0 -
0,0 -
1,0 -
1,0 -
1,0 -
0,0 -
39.94 fieldmatch
Field matching filter for inverse telecine. It is meant to reconstruct the
progressive frames from a telecined stream. The filter does not drop duplicated
frames, so to achieve a complete inverse telecine fieldmatch needs to be
followed by a decimation filter such as decimate in the filtergraph.
The separation of the field matching and the decimation is notably motivated by
the possibility of inserting a de-interlacing filter fallback between the two.
If the source has mixed telecined and real interlaced content,
fieldmatch will not be able to match fields for the interlaced parts.
But these remaining combed frames will be marked as interlaced, and thus can be
de-interlaced by a later filter such as yadif before decimation.
In addition to the various configuration options, fieldmatch can take an
optional second stream, activated through the ppsrc option. If
enabled, the frames reconstruction will be based on the fields and frames from
this second stream. This allows the first input to be pre-processed in order to
help the various algorithms of the filter, while keeping the output lossless
(assuming the fields are matched properly). Typically, a field-aware denoiser,
or brightness/contrast adjustments can help.
Note that this filter uses the same algorithms as TIVTC/TFM (AviSynth project)
and VIVTC/VFM (VapourSynth project). The later is a light clone of TFM from
which fieldmatch is based on. While the semantic and usage are very
close, some behaviour and options names can differ.
The decimate filter currently only works for constant frame rate input.
If your input has mixed telecined (30fps) and progressive content with a lower
framerate like 24fps use the following filterchain to produce the necessary cfr
stream: dejudder,fps=30000/1001,fieldmatch,decimate.
The filter accepts the following options:
order
Specify the assumed field order of the input stream. Available values are:
‘auto’
Auto detect parity (use FFmpeg’s internal parity value).
‘bff’
Assume bottom field first.
‘tff’
Assume top field first.
Note that it is sometimes recommended not to trust the parity announced by the
stream.
Default value is auto.
mode
Set the matching mode or strategy to use. pc mode is the safest in the
sense that it won’t risk creating jerkiness due to duplicate frames when
possible, but if there are bad edits or blended fields it will end up
outputting combed frames when a good match might actually exist. On the other
hand, pcn_ub mode is the most risky in terms of creating jerkiness,
but will almost always find a good frame if there is one. The other values are
all somewhere in between pc and pcn_ub in terms of risking
jerkiness and creating duplicate frames versus finding good matches in sections
with bad edits, orphaned fields, blended fields, etc.
More details about p/c/n/u/b are available in p/c/n/u/b meaning section.
Available values are:
‘pc’
2-way matching (p/c)
‘pc_n’
2-way matching, and trying 3rd match if still combed (p/c + n)
‘pc_u’
2-way matching, and trying 3rd match (same order) if still combed (p/c + u)
‘pc_n_ub’
2-way matching, trying 3rd match if still combed, and trying 4th/5th matches if
still combed (p/c + n + u/b)
‘pcn’
3-way matching (p/c/n)
‘pcn_ub’
3-way matching, and trying 4th/5th matches if all 3 of the original matches are
detected as combed (p/c/n + u/b)
The parenthesis at the end indicate the matches that would be used for that
mode assuming order=tff (and field on auto or
top).
In terms of speed pc mode is by far the fastest and pcn_ub is
the slowest.
Default value is pc_n.
ppsrc
Mark the main input stream as a pre-processed input, and enable the secondary
input stream as the clean source to pick the fields from. See the filter
introduction for more details. It is similar to the clip2 feature from
VFM/TFM.
Default value is 0 (disabled).
field
Set the field to match from. It is recommended to set this to the same value as
order unless you experience matching failures with that setting. In
certain circumstances changing the field that is used to match from can have a
large impact on matching performance. Available values are:
‘auto’
Automatic (same value as order).
‘bottom’
Match from the bottom field.
‘top’
Match from the top field.
Default value is auto.
mchroma
Set whether or not chroma is included during the match comparisons. In most
cases it is recommended to leave this enabled. You should set this to 0
only if your clip has bad chroma problems such as heavy rainbowing or other
artifacts. Setting this to 0 could also be used to speed things up at
the cost of some accuracy.
Default value is 1.
y0
y1
These define an exclusion band which excludes the lines between y0 and
y1 from being included in the field matching decision. An exclusion
band can be used to ignore subtitles, a logo, or other things that may
interfere with the matching. y0 sets the starting scan line and
y1 sets the ending line; all lines in between y0 and
y1 (including y0 and y1) will be ignored. Setting
y0 and y1 to the same value will disable the feature.
y0 and y1 defaults to 0.
scthresh
Set the scene change detection threshold as a percentage of maximum change on
the luma plane. Good values are in the [8.0, 14.0] range. Scene change
detection is only relevant in case combmatch=sc.  The range for
scthresh is [0.0, 100.0].
Default value is 12.0.
combmatch
When combatch is not none, fieldmatch will take into
account the combed scores of matches when deciding what match to use as the
final match. Available values are:
‘none’
No final matching based on combed scores.
‘sc’
Combed scores are only used when a scene change is detected.
‘full’
Use combed scores all the time.
Default is sc.
combdbg
Force fieldmatch to calculate the combed metrics for certain matches and
print them. This setting is known as micout in TFM/VFM vocabulary.
Available values are:
‘none’
No forced calculation.
‘pcn’
Force p/c/n calculations.
‘pcnub’
Force p/c/n/u/b calculations.
Default value is none.
cthresh
This is the area combing threshold used for combed frame detection. This
essentially controls how "strong" or "visible" combing must be to be detected.
Larger values mean combing must be more visible and smaller values mean combing
can be less visible or strong and still be detected. Valid settings are from
-1 (every pixel will be detected as combed) to 255 (no pixel will
be detected as combed). This is basically a pixel difference value. A good
range is [8, 12].
Default value is 9.
chroma
Sets whether or not chroma is considered in the combed frame decision.  Only
disable this if your source has chroma problems (rainbowing, etc.) that are
causing problems for the combed frame detection with chroma enabled. Actually,
using chroma=0 is usually more reliable, except for the case
where there is chroma only combing in the source.
Default value is 0.
blockx
blocky
Respectively set the x-axis and y-axis size of the window used during combed
frame detection. This has to do with the size of the area in which
combpel pixels are required to be detected as combed for a frame to be
declared combed. See the combpel parameter description for more info.
Possible values are any number that is a power of 2 starting at 4 and going up
to 512.
Default value is 16.
combpel
The number of combed pixels inside any of the blocky by
blockx size blocks on the frame for the frame to be detected as
combed. While cthresh controls how "visible" the combing must be, this
setting controls "how much" combing there must be in any localized area (a
window defined by the blockx and blocky settings) on the
frame. Minimum value is 0 and maximum is blocky x blockx (at
which point no frames will ever be detected as combed). This setting is known
as MI in TFM/VFM vocabulary.
Default value is 80.
39.94.1 p/c/n/u/b meaning
39.94.1.1 p/c/n
We assume the following telecined stream:
Top fields:     1 2 2 3 4
Bottom fields:  1 2 3 4 4
The numbers correspond to the progressive frame the fields relate to. Here, the
first two frames are progressive, the 3rd and 4th are combed, and so on.
When fieldmatch is configured to run a matching from bottom
(field=bottom) this is how this input stream get transformed:
Input stream:
T     1 2 2 3 4
B     1 2 3 4 4   <-- matching reference
Matches:              c c n n c
Output stream:
T     1 2 3 4 4
B     1 2 3 4 4
As a result of the field matching, we can see that some frames get duplicated.
To perform a complete inverse telecine, you need to rely on a decimation filter
after this operation. See for instance the decimate filter.
The same operation now matching from top fields (field=top)
looks like this:
Input stream:
T     1 2 2 3 4   <-- matching reference
B     1 2 3 4 4
Matches:              c c p p c
Output stream:
T     1 2 2 3 4
B     1 2 2 3 4
In these examples, we can see what p, c and n mean;
basically, they refer to the frame and field of the opposite parity:
p matches the field of the opposite parity in the previous frame
c matches the field of the opposite parity in the current frame
n matches the field of the opposite parity in the next frame
39.94.1.2 u/b
The u and b matching are a bit special in the sense that they match
from the opposite parity flag. In the following examples, we assume that we are
currently matching the 2nd frame (Top:2, bottom:2). According to the match, a
’x’ is placed above and below each matched fields.
With bottom matching (field=bottom):
Match:           c         p           n          b          u
x       x               x        x          x
Top          1 2 2     1 2 2       1 2 2      1 2 2      1 2 2
Bottom       1 2 3     1 2 3       1 2 3      1 2 3      1 2 3
x         x           x        x              x
Output frames:
2          1          2          2          2
2          2          2          1          3
With top matching (field=top):
Match:           c         p           n          b          u
x         x           x        x              x
Top          1 2 2     1 2 2       1 2 2      1 2 2      1 2 2
Bottom       1 2 3     1 2 3       1 2 3      1 2 3      1 2 3
x       x               x        x          x
Output frames:
2          2          2          1          2
2          1          3          2          2
39.94.2 Examples
Simple IVTC of a top field first telecined stream:
fieldmatch=order=tff:combmatch=none, decimate
Advanced IVTC, with fallback on yadif for still combed frames:
fieldmatch=order=tff:combmatch=full, yadif=deint=interlaced, decimate
39.95 fieldorder
Transform the field order of the input video.
It accepts the following parameters:
order
The output field order. Valid values are tff for top field first or bff
for bottom field first.
The default value is ‘tff’.
The transformation is done by shifting the picture content up or down
by one line, and filling the remaining line with appropriate picture content.
This method is consistent with most broadcast field order converters.
If the input video is not flagged as being interlaced, or it is already
flagged as being of the required output field order, then this filter does
not alter the incoming video.
It is very useful when converting to or from PAL DV material,
which is bottom field first.
For example:
ffmpeg -i in.vob -vf "fieldorder=bff" out.dv
39.96 fillborders
Fill borders of the input video, without changing video stream dimensions.
Sometimes video can have garbage at the four edges and you may not want to
crop video input to keep size multiple of some number.
This filter accepts the following options:
left
Number of pixels to fill from left border.
right
Number of pixels to fill from right border.
top
Number of pixels to fill from top border.
bottom
Number of pixels to fill from bottom border.
mode
Set fill mode.
It accepts the following values:
‘smear’
fill pixels using outermost pixels
‘mirror’
fill pixels using mirroring (half sample symmetric)
‘fixed’
fill pixels with constant value
‘reflect’
fill pixels using reflecting (whole sample symmetric)
‘wrap’
fill pixels using wrapping
‘fade’
fade pixels to constant value
‘margins’
fill pixels at top and bottom with weighted averages pixels near borders
Default is smear.
color
Set color for pixels in fixed or fade mode. Default is black.
39.96.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.97 find_rect
Find a rectangular object in the input video.
The object to search for must be specified as a gray8 image specified with the
object option.
For each possible match, a score is computed. If the score reaches the specified
threshold, the object is considered found.
If the input video contains multiple instances of the object, the filter will
find only one of them.
When an object is found, the following metadata entries are set in the matching
frame:
lavfi.rect.w
width of object
lavfi.rect.h
height of object
lavfi.rect.x
x position of object
lavfi.rect.y
y position of object
lavfi.rect.score
match score of the found object
It accepts the following options:
object
Filepath of the object image, needs to be in gray8.
threshold
Detection threshold, expressed as a decimal number in the range 0-1.
A threshold value of 0.01 means only exact matches, a threshold of 0.99 means
almost everything matches.
Default value is 0.5.
mipmaps
Number of mipmaps, default is 3.
xmin, ymin, xmax, ymax
Specifies the rectangle in which to search.
discard
Discard frames where object is not detected. Default is disabled.
39.97.1 Examples
Cover a rectangular object by the supplied image of a given video using ffmpeg:
ffmpeg -i file.ts -vf find_rect=newref.pgm,cover_rect=cover.jpg:mode=cover new.mkv
Find the position of an object in each frame using ffprobe and write
it to a log file:
ffprobe -f lavfi movie=test.mp4,find_rect=object=object.pgm:threshold=0.3 \
-show_entries frame=pkt_pts_time:frame_tags=lavfi.rect.x,lavfi.rect.y \
-of csv -o find_rect.csv
39.98 floodfill
Flood area with values of same pixel components with another values.
It accepts the following options:
x
Set pixel x coordinate.
y
Set pixel y coordinate.
s0
Set source #0 component value.
s1
Set source #1 component value.
s2
Set source #2 component value.
s3
Set source #3 component value.
d0
Set destination #0 component value.
d1
Set destination #1 component value.
d2
Set destination #2 component value.
d3
Set destination #3 component value.
39.99 format
Convert the input video to one of the specified pixel formats.
Libavfilter will try to pick one that is suitable as input to
the next filter.
It accepts the following parameters:
pix_fmts
A ’|’-separated list of pixel format names, such as
"pix_fmts=yuv420p|monow|rgb24".
color_spaces
A ’|’-separated list of color space names, such as
"color_spaces=bt709|bt470bg|bt2020nc".
color_ranges
A ’|’-separated list of color range names, such as
"color_spaces=tv|pc".
39.99.1 Examples
Convert the input video to the yuv420p format
format=pix_fmts=yuv420p
Convert the input video to any of the formats in the list
format=pix_fmts=yuv420p|yuv444p|yuv410p
39.100 fps
Convert the video to specified constant frame rate by duplicating or dropping
frames as necessary.
It accepts the following parameters:
fps
The desired output frame rate. It accepts expressions containing the following
constants:
‘source_fps’
The input’s frame rate
‘ntsc’
NTSC frame rate of 30000/1001
‘pal’
PAL frame rate of 25.0
‘film’
Film frame rate of 24.0
‘ntsc_film’
NTSC-film frame rate of 24000/1001
The default is 25.
start_time
Assume the first PTS should be the given value, in seconds. This allows for
padding/trimming at the start of stream. By default, no assumption is made
about the first frame’s expected PTS, so no padding or trimming is done.
For example, this could be set to 0 to pad the beginning with duplicates of
the first frame if a video stream starts after the audio stream or to trim any
frames with a negative PTS.
round
Timestamp (PTS) rounding method.
Possible values are:
zero
round towards 0
inf
round away from 0
down
round towards -infinity
up
round towards +infinity
near
round to nearest
The default is near.
eof_action
Action performed when reading the last frame.
Possible values are:
round
Use same timestamp rounding method as used for other frames.
pass
Pass through last frame if input duration has not been reached yet.
The default is round.
Alternatively, the options can be specified as a flat string:
fps[:start_time[:round]].
See also the setpts filter.
39.100.1 Examples
A typical usage in order to set the fps to 25:
fps=fps=25
Sets the fps to 24, using abbreviation and rounding method to round to nearest:
fps=fps=film:round=near
39.101 framepack
Pack two different video streams into a stereoscopic video, setting proper
metadata on supported codecs. The two views should have the same size and
framerate and processing will stop when the shorter video ends. Please note
that you may conveniently adjust view properties with the scale and
fps filters.
It accepts the following parameters:
format
The desired packing format. Supported values are:
sbs
The views are next to each other (default).
tab
The views are on top of each other.
lines
The views are packed by line.
columns
The views are packed by column.
frameseq
The views are temporally interleaved.
Some examples:
# Convert left and right views into a frame-sequential video
ffmpeg -i LEFT -i RIGHT -filter_complex framepack=frameseq OUTPUT
# Convert views into a side-by-side video with the same output resolution as the input
ffmpeg -i LEFT -i RIGHT -filter_complex [0:v]scale=w=iw/2[left],[1:v]scale=w=iw/2[right],[left][right]framepack=sbs OUTPUT
39.102 framerate
Change the frame rate by interpolating new video output frames from the source
frames.
This filter is not designed to function correctly with interlaced media. If
you wish to change the frame rate of interlaced media then you are required
to deinterlace before this filter and re-interlace after this filter.
A description of the accepted options follows.
fps
Specify the output frames per second. This option can also be specified
as a value alone. The default is 50.
interp_start
Specify the start of a range where the output frame will be created as a
linear interpolation of two frames. The range is [0-255],
the default is 15.
interp_end
Specify the end of a range where the output frame will be created as a
linear interpolation of two frames. The range is [0-255],
the default is 240.
scene
Specify the level at which a scene change is detected as a value between
0 and 100 to indicate a new scene; a low value reflects a low
probability for the current frame to introduce a new scene, while a higher
value means the current frame is more likely to be one.
The default is 8.2.
flags
Specify flags influencing the filter process.
Available value for flags is:
scene_change_detect, scd
Enable scene change detection using the value of the option scene.
This flag is enabled by default.
39.103 framestep
Select one frame every N-th frame.
This filter accepts the following option:
step
Select frame after every step frames.
Allowed values are positive integers higher than 0. Default value is 1.
39.104 freezedetect
Detect frozen video.
This filter logs a message and sets frame metadata when it detects that the
input video has no significant change in content during a specified duration.
Video freeze detection calculates the mean average absolute difference of all
the components of video frames and compares it to a noise floor.
The printed times and duration are expressed in seconds. The
lavfi.freezedetect.freeze_start metadata key is set on the first frame
whose timestamp equals or exceeds the detection duration and it contains the
timestamp of the first frame of the freeze. The
lavfi.freezedetect.freeze_duration and
lavfi.freezedetect.freeze_end metadata keys are set on the first frame
after the freeze.
The filter accepts the following options:
noise, n
Set noise tolerance. Can be specified in dB (in case "dB" is appended to the
specified value) or as a difference ratio between 0 and 1. Default is -60dB, or
0.001.
duration, d
Set freeze duration until notification (default is 2 seconds).
39.105 freezeframes
Freeze video frames.
This filter freezes video frames using frame from 2nd input.
The filter accepts the following options:
first
Set number of first frame from which to start freeze.
last
Set number of last frame from which to end freeze.
replace
Set number of frame from 2nd input which will be used instead of replaced frames.
39.106 frei0r
Apply a frei0r effect to the input video.
To enable the compilation of this filter, you need to install the frei0r
header and configure FFmpeg with --enable-frei0r.
It accepts the following parameters:
filter_name
The name of the frei0r effect to load. If the environment variable
FREI0R_PATH is defined, the frei0r effect is searched for in each of the
directories specified by the colon-separated list in FREI0R_PATH.
Otherwise, the standard frei0r paths are searched, in this order:
HOME/.frei0r-1/lib/, /usr/local/lib/frei0r-1/,
/usr/lib/frei0r-1/.
filter_params
A ’|’-separated list of parameters to pass to the frei0r effect.
A frei0r effect parameter can be a boolean (its value is either
"y" or "n"), a double, a color (specified as
R/G/B, where R, G, and B are floating point
numbers between 0.0 and 1.0, inclusive) or a color description as specified in the
(ffmpeg-utils)"Color" section in the ffmpeg-utils manual,
a position (specified as X/Y, where
X and Y are floating point numbers) and/or a string.
The number and types of parameters depend on the loaded effect. If an
effect parameter is not specified, the default value is set.
39.106.1 Examples
Apply the distort0r effect, setting the first two double parameters:
frei0r=filter_name=distort0r:filter_params=0.5|0.01
Apply the colordistance effect, taking a color as the first parameter:
frei0r=colordistance:0.2/0.3/0.4
frei0r=colordistance:violet
frei0r=colordistance:0x112233
Apply the perspective effect, specifying the top left and top right image
positions:
frei0r=perspective:0.2/0.2|0.8/0.2
For more information, see
http://frei0r.dyne.org
39.106.2 Commands
This filter supports the filter_params option as commands.
39.107 fspp
Apply fast and simple postprocessing. It is a faster version of spp.
It splits (I)DCT into horizontal/vertical passes. Unlike the simple post-
processing filter, one of them is performed once per block, not per pixel.
This allows for much higher speed.
The filter accepts the following options:
quality
Set quality. This option defines the number of levels for averaging. It accepts
an integer in the range 4-5. Default value is 4.
qp
Force a constant quantization parameter. It accepts an integer in range 0-63.
If not set, the filter will use the QP from the video stream (if available).
strength
Set filter strength. It accepts an integer in range -15 to 32. Lower values mean
more details but also more artifacts, while higher values make the image smoother
but also blurrier. Default value is 0 − PSNR optimal.
use_bframe_qp
Enable the use of the QP from the B-Frames if set to 1. Using this
option may cause flicker since the B-Frames have often larger QP. Default is
0 (not enabled).
39.108 fsync
Synchronize video frames with an external mapping from a file.
For each input PTS given in the map file it either drops or creates as many
frames as necessary to recreate the sequence of output frames given in the
map file.
This filter is useful to recreate the output frames of a framerate conversion
by the fps filter, recorded into a map file using the ffmpeg option
-stats_mux_pre, and do further processing to the corresponding frames
e.g. quality comparison.
Each line of the map file must contain three items per input frame, the input
PTS (decimal), the output PTS (decimal) and the
output TIMEBASE (decimal/decimal), seperated by a space.
This file format corresponds to the output
of -stats_mux_pre_fmt="{ptsi} {pts} {tb}".
The filter assumes the map file is sorted by increasing input PTS.
The filter accepts the following options:
file, f
The filename of the map file to be used.
Example:
# Convert a video to 25 fps and record a MAP_FILE file with the default format of this filter
ffmpeg -i INPUT -vf fps=fps=25 -stats_mux_pre MAP_FILE -stats_mux_pre_fmt "{ptsi} {pts} {tb}" OUTPUT
# Sort MAP_FILE by increasing input PTS
sort -n MAP_FILE
# Use INPUT, OUTPUT and the MAP_FILE from above to compare the corresponding frames in INPUT and OUTPUT via SSIM
ffmpeg -i INPUT -i OUTPUT -filter_complex '[0:v]fsync=file=MAP_FILE[ref];[1:v][ref]ssim' -f null -
39.109 gblur
Apply Gaussian blur filter.
The filter accepts the following options:
sigma
Set horizontal sigma, standard deviation of Gaussian blur. Default is 0.5.
steps
Set number of steps for Gaussian approximation. Default is 1.
planes
Set which planes to filter. By default all planes are filtered.
sigmaV
Set vertical sigma, if negative it will be same as sigma.
Default is -1.
39.109.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.110 geq
Apply generic equation to each pixel.
The filter accepts the following options:
lum_expr, lum
Set the luma expression.
cb_expr, cb
Set the chrominance blue expression.
cr_expr, cr
Set the chrominance red expression.
alpha_expr, a
Set the alpha expression.
red_expr, r
Set the red expression.
green_expr, g
Set the green expression.
blue_expr, b
Set the blue expression.
The colorspace is selected according to the specified options. If one
of the lum_expr, cb_expr, or cr_expr
options is specified, the filter will automatically select a YCbCr
colorspace. If one of the red_expr, green_expr, or
blue_expr options is specified, it will select an RGB
colorspace.
If one of the chrominance expression is not defined, it falls back on the other
one. If no alpha expression is specified it will evaluate to opaque value.
If none of chrominance expressions are specified, they will evaluate
to the luma expression.
The expressions can use the following variables and functions:
N
The sequential number of the filtered frame, starting from 0.
X
Y
The coordinates of the current sample.
W
H
The width and height of the image.
SW
SH
Width and height scale depending on the currently filtered plane. It is the
ratio between the corresponding luma plane number of pixels and the current
plane ones. E.g. for YUV4:2:0 the values are 1,1 for the luma plane, and
0.5,0.5 for chroma planes.
T
Time of the current frame, expressed in seconds.
p(x, y)
Return the value of the pixel at location (x,y) of the current
plane.
lum(x, y)
Return the value of the pixel at location (x,y) of the luma
plane.
cb(x, y)
Return the value of the pixel at location (x,y) of the
blue-difference chroma plane. Return 0 if there is no such plane.
cr(x, y)
Return the value of the pixel at location (x,y) of the
red-difference chroma plane. Return 0 if there is no such plane.
r(x, y)
g(x, y)
b(x, y)
Return the value of the pixel at location (x,y) of the
red/green/blue component. Return 0 if there is no such component.
alpha(x, y)
Return the value of the pixel at location (x,y) of the alpha
plane. Return 0 if there is no such plane.
psum(x,y), lumsum(x, y), cbsum(x,y), crsum(x,y), rsum(x,y), gsum(x,y), bsum(x,y), alphasum(x,y)
Sum of sample values in the rectangle from (0,0) to (x,y), this allows obtaining
sums of samples within a rectangle. See the functions without the sum postfix.
interpolation
Set one of interpolation methods:
nearest, n
bilinear, b
Default is bilinear.
For functions, if x and y are outside the area, the value will be
automatically clipped to the closer edge.
Please note that this filter can use multiple threads in which case each slice
will have its own expression state. If you want to use only a single expression
state because your expressions depend on previous state then you should limit
the number of filter threads to 1.
39.110.1 Examples
Flip the image horizontally:
geq=p(W-X\,Y)
Generate a bidimensional sine wave, with angle PI/3 and a
wavelength of 100 pixels:
geq=128 + 100*sin(2*(PI/100)*(cos(PI/3)*(X-50*T) + sin(PI/3)*Y)):128:128
Generate a fancy enigmatic moving light:
nullsrc=s=256x256,geq=random(1)/hypot(X-cos(N*0.07)*W/2-W/2\,Y-sin(N*0.09)*H/2-H/2)^2*1000000*sin(N*0.02):128:128
Generate a quick emboss effect:
format=gray,geq=lum_expr='(p(X,Y)+(256-p(X-4,Y-4)))/2'
Modify RGB components depending on pixel position:
geq=r='X/W*r(X,Y)':g='(1-X/W)*g(X,Y)':b='(H-Y)/H*b(X,Y)'
Create a radial gradient that is the same size as the input (also see
the vignette filter):
geq=lum=255*gauss((X/W-0.5)*3)*gauss((Y/H-0.5)*3)/gauss(0)/gauss(0),format=gray
39.111 gradfun
Fix the banding artifacts that are sometimes introduced into nearly flat
regions by truncation to 8-bit color depth.
Interpolate the gradients that should go where the bands are, and
dither them.
It is designed for playback only.  Do not use it prior to
lossy compression, because compression tends to lose the dither and
bring back the bands.
It accepts the following parameters:
strength
The maximum amount by which the filter will change any one pixel. This is also
the threshold for detecting nearly flat regions. Acceptable values range from
.51 to 64; the default value is 1.2. Out-of-range values will be clipped to the
valid range.
radius
The neighborhood to fit the gradient to. A larger radius makes for smoother
gradients, but also prevents the filter from modifying the pixels near detailed
regions. Acceptable values are 8-32; the default value is 16. Out-of-range
values will be clipped to the valid range.
Alternatively, the options can be specified as a flat string:
strength[:radius]
39.111.1 Examples
Apply the filter with a 3.5 strength and radius of 8:
gradfun=3.5:8
Specify radius, omitting the strength (which will fall-back to the default
value):
gradfun=radius=8
39.112 graphmonitor
Show various filtergraph stats.
With this filter one can debug complete filtergraph.
Especially issues with links filling with queued frames.
The filter accepts the following options:
size, s
Set video output size. Default is hd720.
opacity, o
Set video opacity. Default is 0.9. Allowed range is from 0 to 1.
mode, m
Set output mode flags.
Available values for flags are:
‘full’
No any filtering. Default.
‘compact’
Show only filters with queued frames.
‘nozero’
Show only filters with non-zero stats.
‘noeof’
Show only filters with non-eof stat.
‘nodisabled’
Show only filters that are enabled in timeline.
flags, f
Set flags which enable which stats are shown in video.
Available values for flags are:
‘none’
All flags turned off.
‘all’
All flags turned on.
‘queue’
Display number of queued frames in each link.
‘frame_count_in’
Display number of frames taken from filter.
‘frame_count_out’
Display number of frames given out from filter.
‘frame_count_delta’
Display delta number of frames between above two values.
‘pts’
Display current filtered frame pts.
‘pts_delta’
Display pts delta between current and previous frame.
‘time’
Display current filtered frame time.
‘time_delta’
Display time delta between current and previous frame.
‘timebase’
Display time base for filter link.
‘format’
Display used format for filter link.
‘size’
Display video size or number of audio channels in case of audio used by filter link.
‘rate’
Display video frame rate or sample rate in case of audio used by filter link.
‘eof’
Display link output status.
‘sample_count_in’
Display number of samples taken from filter.
‘sample_count_out’
Display number of samples given out from filter.
‘sample_count_delta’
Display delta number of samples between above two values.
‘disabled’
Show the timeline filter status.
rate, r
Set upper limit for video rate of output stream, Default value is 25.
This guarantee that output video frame rate will not be higher than this value.
39.113 grayworld
A color constancy filter that applies color correction based on the grayworld assumption
See: https://www.researchgate.net/publication/275213614_A_New_Color_Correction_Method_for_Underwater_Imaging
The algorithm  uses linear light, so input
data should be linearized beforehand (and possibly correctly tagged).
ffmpeg -i INPUT -vf zscale=transfer=linear,grayworld,zscale=transfer=bt709,format=yuv420p OUTPUT
39.114 greyedge
A color constancy variation filter which estimates scene illumination via grey edge algorithm
and corrects the scene colors accordingly.
See: https://staff.science.uva.nl/th.gevers/pub/GeversTIP07.pdf
The filter accepts the following options:
difford
The order of differentiation to be applied on the scene. Must be chosen in the range
[0,2] and default value is 1.
minknorm
The Minkowski parameter to be used for calculating the Minkowski distance. Must
be chosen in the range [0,20] and default value is 1. Set to 0 for getting
max value instead of calculating Minkowski distance.
sigma
The standard deviation of Gaussian blur to be applied on the scene. Must be
chosen in the range [0,1024.0] and default value = 1. floor( sigma * break_off_sigma(3) )
can’t be equal to 0 if difford is greater than 0.
39.114.1 Examples
Grey Edge:
greyedge=difford=1:minknorm=5:sigma=2
Max Edge:
greyedge=difford=1:minknorm=0:sigma=2
39.115 guided
Apply guided filter for edge-preserving smoothing, dehazing and so on.
The filter accepts the following options:
radius
Set the box radius in pixels.
Allowed range is 1 to 20. Default is 3.
eps
Set regularization parameter (with square).
Allowed range is 0 to 1. Default is 0.01.
mode
Set filter mode. Can be basic or fast.
Default is basic.
sub
Set subsampling ratio for fast mode.
Range is 2 to 64. Default is 4.
No subsampling occurs in basic mode.
guidance
Set guidance mode. Can be off or on. Default is off.
If off, single input is required.
If on, two inputs of the same resolution and pixel format are required.
The second input serves as the guidance.
planes
Set planes to filter. Default is first only.
39.115.1 Commands
This filter supports the all above options as commands.
39.115.2 Examples
Edge-preserving smoothing with guided filter:
ffmpeg -i in.png -vf guided out.png
Dehazing, structure-transferring filtering, detail enhancement with guided filter.
For the generation of guidance image, refer to paper "Guided Image Filtering".
See: http://kaiminghe.com/publications/pami12guidedfilter.pdf.
ffmpeg -i in.png -i guidance.png -filter_complex guided=guidance=on out.png
39.116 haldclut
Apply a Hald CLUT to a video stream.
First input is the video stream to process, and second one is the Hald CLUT.
The Hald CLUT input can be a simple picture or a complete video stream.
The filter accepts the following options:
clut
Set which CLUT video frames will be processed from second input stream,
can be first or all. Default is all.
shortest
Force termination when the shortest input terminates. Default is 0.
repeatlast
Continue applying the last CLUT after the end of the stream. A value of
0 disable the filter after the last frame of the CLUT is reached.
Default is 1.
haldclut also has the same interpolation options as lut3d (both
filters share the same internals).
This filter also supports the framesync options.
More information about the Hald CLUT can be found on Eskil Steenberg’s website
(Hald CLUT author) at http://www.quelsolaar.com/technology/clut.html.
39.116.1 Commands
This filter supports the interp option as commands.
39.116.2 Workflow examples
39.116.2.1 Hald CLUT video stream
Generate an identity Hald CLUT stream altered with various effects:
ffmpeg -f lavfi -i haldclutsrc=8 -vf "hue=H=2*PI*t:s=sin(2*PI*t)+1, curves=cross_process" -t 10 -c:v ffv1 clut.nut
Note: make sure you use a lossless codec.
Then use it with haldclut to apply it on some random stream:
ffmpeg -f lavfi -i mandelbrot -i clut.nut -filter_complex '[0][1] haldclut' -t 20 mandelclut.mkv
The Hald CLUT will be applied to the 10 first seconds (duration of
clut.nut), then the latest picture of that CLUT stream will be applied
to the remaining frames of the mandelbrot stream.
39.116.2.2 Hald CLUT with preview
A Hald CLUT is supposed to be a squared image of Level*Level*Level by
Level*Level*Level pixels. For a given Hald CLUT, FFmpeg will select the
biggest possible square starting at the top left of the picture. The remaining
padding pixels (bottom or right) will be ignored. This area can be used to add
a preview of the Hald CLUT.
Typically, the following generated Hald CLUT will be supported by the
haldclut filter:
ffmpeg -f lavfi -i haldclutsrc=8 -vf "
pad=iw+320 [padded_clut];
smptebars=s=320x256, split [a][b];
[padded_clut][a] overlay=W-320:h, curves=color_negative [main];
[main][b] overlay=W-320" -frames:v 1 clut.png
It contains the original and a preview of the effect of the CLUT: SMPTE color
bars are displayed on the right-top, and below the same color bars processed by
the color changes.
Then, the effect of this Hald CLUT can be visualized with:
ffplay input.mkv -vf "movie=clut.png, [in] haldclut"
39.117 hflip
Flip the input video horizontally.
For example, to horizontally flip the input video with ffmpeg:
ffmpeg -i in.avi -vf "hflip" out.avi
39.118 histeq
This filter applies a global color histogram equalization on a
per-frame basis.
It can be used to correct video that has a compressed range of pixel
intensities.  The filter redistributes the pixel intensities to
equalize their distribution across the intensity range. It may be
viewed as an "automatically adjusting contrast filter". This filter is
useful only for correcting degraded or poorly captured source
video.
The filter accepts the following options:
strength
Determine the amount of equalization to be applied.  As the strength
is reduced, the distribution of pixel intensities more-and-more
approaches that of the input frame. The value must be a float number
in the range [0,1] and defaults to 0.200.
intensity
Set the maximum intensity that can generated and scale the output
values appropriately.  The strength should be set as desired and then
the intensity can be limited if needed to avoid washing-out. The value
must be a float number in the range [0,1] and defaults to 0.210.
antibanding
Set the antibanding level. If enabled the filter will randomly vary
the luminance of output pixels by a small amount to avoid banding of
the histogram. Possible values are none, weak or
strong. It defaults to none.
39.119 histogram
Compute and draw a color distribution histogram for the input video.
The computed histogram is a representation of the color component
distribution in an image.
Standard histogram displays the color components distribution in an image.
Displays color graph for each color component. Shows distribution of
the Y, U, V, A or R, G, B components, depending on input format, in the
current frame. Below each graph a color component scale meter is shown.
The filter accepts the following options:
level_height
Set height of level. Default value is 200.
Allowed range is [50, 2048].
scale_height
Set height of color scale. Default value is 12.
Allowed range is [0, 40].
display_mode
Set display mode.
It accepts the following values:
‘stack’
Per color component graphs are placed below each other.
‘parade’
Per color component graphs are placed side by side.
‘overlay’
Presents information identical to that in the parade, except
that the graphs representing color components are superimposed directly
over one another.
Default is stack.
levels_mode
Set mode. Can be either linear, or logarithmic.
Default is linear.
components
Set what color components to display.
Default is 7.
fgopacity
Set foreground opacity. Default is 0.7.
bgopacity
Set background opacity. Default is 0.5.
colors_mode
Set colors mode.
It accepts the following values:
‘whiteonblack’
‘blackonwhite’
‘whiteongray’
‘blackongray’
‘coloronblack’
‘coloronwhite’
‘colorongray’
‘blackoncolor’
‘whiteoncolor’
‘grayoncolor’
Default is whiteonblack.
39.119.1 Examples
Calculate and draw histogram:
ffplay -i input -vf histogram
39.120 hqdn3d
This is a high precision/quality 3d denoise filter. It aims to reduce
image noise, producing smooth images and making still images really
still. It should enhance compressibility.
It accepts the following optional parameters:
luma_spatial
A non-negative floating point number which specifies spatial luma strength.
It defaults to 4.0.
chroma_spatial
A non-negative floating point number which specifies spatial chroma strength.
It defaults to 3.0*luma_spatial/4.0.
luma_tmp
A floating point number which specifies luma temporal strength. It defaults to
6.0*luma_spatial/4.0.
chroma_tmp
A floating point number which specifies chroma temporal strength. It defaults to
luma_tmp*chroma_spatial/luma_spatial.
39.120.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.121 hwdownload
Download hardware frames to system memory.
The input must be in hardware frames, and the output a non-hardware format.
Not all formats will be supported on the output - it may be necessary to insert
an additional format filter immediately following in the graph to get
the output in a supported format.
39.122 hwmap
Map hardware frames to system memory or to another device.
This filter has several different modes of operation; which one is used depends
on the input and output formats:
Hardware frame input, normal frame output
Map the input frames to system memory and pass them to the output.  If the
original hardware frame is later required (for example, after overlaying
something else on part of it), the hwmap filter can be used again
in the next mode to retrieve it.
Normal frame input, hardware frame output
If the input is actually a software-mapped hardware frame, then unmap it -
that is, return the original hardware frame.
Otherwise, a device must be provided.  Create new hardware surfaces on that
device for the output, then map them back to the software format at the input
and give those frames to the preceding filter.  This will then act like the
hwupload filter, but may be able to avoid an additional copy when
the input is already in a compatible format.
Hardware frame input and output
A device must be supplied for the output, either directly or with the
derive_device option.  The input and output devices must be of
different types and compatible - the exact meaning of this is
system-dependent, but typically it means that they must refer to the same
underlying hardware context (for example, refer to the same graphics card).
If the input frames were originally created on the output device, then unmap
to retrieve the original frames.
Otherwise, map the frames to the output device - create new hardware frames
on the output corresponding to the frames on the input.
The following additional parameters are accepted:
mode
Set the frame mapping mode.  Some combination of:
read
The mapped frame should be readable.
write
The mapped frame should be writeable.
overwrite
The mapping will always overwrite the entire frame.
This may improve performance in some cases, as the original contents of the
frame need not be loaded.
direct
The mapping must not involve any copying.
Indirect mappings to copies of frames are created in some cases where either
direct mapping is not possible or it would have unexpected properties.
Setting this flag ensures that the mapping is direct and will fail if that is
not possible.
Defaults to read+write if not specified.
derive_device type
Rather than using the device supplied at initialisation, instead derive a new
device of type type from the device the input frames exist on.
reverse
In a hardware to hardware mapping, map in reverse - create frames in the sink
and map them back to the source.  This may be necessary in some cases where
a mapping in one direction is required but only the opposite direction is
supported by the devices being used.
This option is dangerous - it may break the preceding filter in undefined
ways if there are any additional constraints on that filter’s output.
Do not use it without fully understanding the implications of its use.
39.123 hwupload
Upload system memory frames to hardware surfaces.
The device to upload to must be supplied when the filter is initialised.  If
using ffmpeg, select the appropriate device with the -filter_hw_device
option or with the derive_device option.  The input and output devices
must be of different types and compatible - the exact meaning of this is
system-dependent, but typically it means that they must refer to the same
underlying hardware context (for example, refer to the same graphics card).
The following additional parameters are accepted:
derive_device type
Rather than using the device supplied at initialisation, instead derive a new
device of type type from the device the input frames exist on.
39.124 hwupload_cuda
Upload system memory frames to a CUDA device.
It accepts the following optional parameters:
device
The number of the CUDA device to use
39.125 hqx
Apply a high-quality magnification filter designed for pixel art. This filter
was originally created by Maxim Stepin.
It accepts the following option:
n
Set the scaling dimension: 2 for hq2x, 3 for
hq3x and 4 for hq4x.
Default is 3.
39.126 hstack
Stack input videos horizontally.
All streams must be of same pixel format and of same height.
Note that this filter is faster than using overlay and pad filter
to create same output.
The filter accepts the following option:
inputs
Set number of input streams. Default is 2.
shortest
If set to 1, force the output to terminate when the shortest input
terminates. Default value is 0.
39.127 hsvhold
Turns a certain HSV range into gray values.
This filter measures color difference between set HSV color in options
and ones measured in video stream. Depending on options, output
colors can be changed to be gray or not.
The filter accepts the following options:
hue
Set the hue value which will be used in color difference calculation.
Allowed range is from -360 to 360. Default value is 0.
sat
Set the saturation value which will be used in color difference calculation.
Allowed range is from -1 to 1. Default value is 0.
val
Set the value which will be used in color difference calculation.
Allowed range is from -1 to 1. Default value is 0.
similarity
Set similarity percentage with the key color.
Allowed range is from 0 to 1. Default value is 0.01.
0.00001 matches only the exact key color, while 1.0 matches everything.
blend
Blend percentage.
Allowed range is from 0 to 1. Default value is 0.
0.0 makes pixels either fully gray, or not gray at all.
Higher values result in more gray pixels, with a higher gray pixel
the more similar the pixels color is to the key color.
39.128 hsvkey
Turns a certain HSV range into transparency.
This filter measures color difference between set HSV color in options
and ones measured in video stream. Depending on options, output
colors can be changed to transparent by adding alpha channel.
The filter accepts the following options:
hue
Set the hue value which will be used in color difference calculation.
Allowed range is from -360 to 360. Default value is 0.
sat
Set the saturation value which will be used in color difference calculation.
Allowed range is from -1 to 1. Default value is 0.
val
Set the value which will be used in color difference calculation.
Allowed range is from -1 to 1. Default value is 0.
similarity
Set similarity percentage with the key color.
Allowed range is from 0 to 1. Default value is 0.01.
0.00001 matches only the exact key color, while 1.0 matches everything.
blend
Blend percentage.
Allowed range is from 0 to 1. Default value is 0.
0.0 makes pixels either fully transparent, or not transparent at all.
Higher values result in semi-transparent pixels, with a higher transparency
the more similar the pixels color is to the key color.
39.129 hue
Modify the hue and/or the saturation of the input.
It accepts the following parameters:
h
Specify the hue angle as a number of degrees. It accepts an expression,
and defaults to "0".
s
Specify the saturation in the [-10,10] range. It accepts an expression and
defaults to "1".
H
Specify the hue angle as a number of radians. It accepts an
expression, and defaults to "0".
b
Specify the brightness in the [-10,10] range. It accepts an expression and
defaults to "0".
h and H are mutually exclusive, and can’t be
specified at the same time.
The b, h, H and s option values are
expressions containing the following constants:
n
frame count of the input frame starting from 0
pts
presentation timestamp of the input frame expressed in time base units
r
frame rate of the input video, NAN if the input frame rate is unknown
t
timestamp expressed in seconds, NAN if the input timestamp is unknown
tb
time base of the input video
39.129.1 Examples
Set the hue to 90 degrees and the saturation to 1.0:
hue=h=90:s=1
Same command but expressing the hue in radians:
hue=H=PI/2:s=1
Rotate hue and make the saturation swing between 0
and 2 over a period of 1 second:
hue="H=2*PI*t: s=sin(2*PI*t)+1"
Apply a 3 seconds saturation fade-in effect starting at 0:
hue="s=min(t/3\,1)"
The general fade-in expression can be written as:
hue="s=min(0\, max((t-START)/DURATION\, 1))"
Apply a 3 seconds saturation fade-out effect starting at 5 seconds:
hue="s=max(0\, min(1\, (8-t)/3))"
The general fade-out expression can be written as:
hue="s=max(0\, min(1\, (START+DURATION-t)/DURATION))"
39.129.2 Commands
This filter supports the following commands:
b
s
h
H
Modify the hue and/or the saturation and/or brightness of the input video.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.130 huesaturation
Apply hue-saturation-intensity adjustments to input video stream.
This filter operates in RGB colorspace.
This filter accepts the following options:
hue
Set the hue shift in degrees to apply. Default is 0.
Allowed range is from -180 to 180.
saturation
Set the saturation shift. Default is 0.
Allowed range is from -1 to 1.
intensity
Set the intensity shift. Default is 0.
Allowed range is from -1 to 1.
colors
Set which primary and complementary colors are going to be adjusted.
This options is set by providing one or multiple values.
This can select multiple colors at once. By default all colors are selected.
‘r’
Adjust reds.
‘y’
Adjust yellows.
‘g’
Adjust greens.
‘c’
Adjust cyans.
‘b’
Adjust blues.
‘m’
Adjust magentas.
‘a’
Adjust all colors.
strength
Set strength of filtering. Allowed range is from 0 to 100.
Default value is 1.
rw, gw, bw
Set weight for each RGB component. Allowed range is from 0 to 1.
By default is set to 0.333, 0.334, 0.333.
Those options are used in saturation and lightess processing.
lightness
Set preserving lightness, by default is disabled.
Adjusting hues can change lightness from original RGB triplet,
with this option enabled lightness is kept at same value.
39.131 hysteresis
Grow first stream into second stream by connecting components.
This makes it possible to build more robust edge masks.
This filter accepts the following options:
planes
Set which planes will be processed as bitmap, unprocessed planes will be
copied from first stream.
By default value 0xf, all planes will be processed.
threshold
Set threshold which is used in filtering. If pixel component value is higher than
this value filter algorithm for connecting components is activated.
By default value is 0.
The hysteresis filter also supports the framesync options.
39.132 iccdetect
Detect the colorspace  from an embedded ICC profile (if present), and update
the frame’s tags accordingly.
This filter accepts the following options:
force
If true, the frame’s existing colorspace tags will always be overridden by
values detected from an ICC profile. Otherwise, they will only be assigned if
they contain unknown. Enabled by default.
39.133 iccgen
Generate ICC profiles and attach them to frames.
This filter accepts the following options:
color_primaries
color_trc
Configure the colorspace that the ICC profile will be generated for. The
default value of auto infers the value from the input frame’s metadata,
defaulting to BT.709/sRGB as appropriate.
See the setparams filter for a list of possible values, but note that
unknown are not valid values for this filter.
force
If true, an ICC profile will be generated even if it would overwrite an
already existing ICC profile. Disabled by default.
39.134 identity
Obtain the identity score between two input videos.
This filter takes two input videos.
Both input videos must have the same resolution and pixel format for
this filter to work correctly. Also it assumes that both inputs
have the same number of frames, which are compared one by one.
The obtained per component, average, min and max identity score is printed through
the logging system.
The filter stores the calculated identity scores of each frame in frame metadata.
This filter also supports the framesync options.
In the below example the input file main.mpg being processed is compared
with the reference file ref.mpg.
ffmpeg -i main.mpg -i ref.mpg -lavfi identity -f null -
39.135 idet
Detect video interlacing type.
This filter tries to detect if the input frames are interlaced, progressive,
top or bottom field first. It will also try to detect fields that are
repeated between adjacent frames (a sign of telecine).
Single frame detection considers only immediately adjacent frames when classifying each frame.
Multiple frame detection incorporates the classification history of previous frames.
The filter will log these metadata values:
single.current_frame
Detected type of current frame using single-frame detection. One of:
“tff” (top field first), “bff” (bottom field first),
“progressive”, or “undetermined”
single.tff
Cumulative number of frames detected as top field first using single-frame detection.
multiple.tff
Cumulative number of frames detected as top field first using multiple-frame detection.
single.bff
Cumulative number of frames detected as bottom field first using single-frame detection.
multiple.current_frame
Detected type of current frame using multiple-frame detection. One of:
“tff” (top field first), “bff” (bottom field first),
“progressive”, or “undetermined”
multiple.bff
Cumulative number of frames detected as bottom field first using multiple-frame detection.
single.progressive
Cumulative number of frames detected as progressive using single-frame detection.
multiple.progressive
Cumulative number of frames detected as progressive using multiple-frame detection.
single.undetermined
Cumulative number of frames that could not be classified using single-frame detection.
multiple.undetermined
Cumulative number of frames that could not be classified using multiple-frame detection.
repeated.current_frame
Which field in the current frame is repeated from the last. One of “neither”, “top”, or “bottom”.
repeated.neither
Cumulative number of frames with no repeated field.
repeated.top
Cumulative number of frames with the top field repeated from the previous frame’s top field.
repeated.bottom
Cumulative number of frames with the bottom field repeated from the previous frame’s bottom field.
The filter accepts the following options:
intl_thres
Set interlacing threshold.
prog_thres
Set progressive threshold.
rep_thres
Threshold for repeated field detection.
half_life
Number of frames after which a given frame’s contribution to the
statistics is halved (i.e., it contributes only 0.5 to its
classification). The default of 0 means that all frames seen are given
full weight of 1.0 forever.
analyze_interlaced_flag
When this is not 0 then idet will use the specified number of frames to determine
if the interlaced flag is accurate, it will not count undetermined frames.
If the flag is found to be accurate it will be used without any further
computations, if it is found to be inaccurate it will be cleared without any
further computations. This allows inserting the idet filter as a low computational
method to clean up the interlaced flag
39.135.1 Examples
Inspect the field order of the first 360 frames in a video, in verbose detail:
ffmpeg -i INPUT -filter:v idet,metadata=mode=print -frames:v 360 -an -f null -
The idet filter will add analysis metadata to each frame, which will then be
discarded. At the end, the filter will also print a final report with statistics.
39.136 il
Deinterleave or interleave fields.
This filter allows one to process interlaced images fields without
deinterlacing them. Deinterleaving splits the input frame into 2
fields (so called half pictures). Odd lines are moved to the top
half of the output image, even lines to the bottom half.
You can process (filter) them independently and then re-interleave them.
The filter accepts the following options:
luma_mode, l
chroma_mode, c
alpha_mode, a
Available values for luma_mode, chroma_mode and
alpha_mode are:
‘none’
Do nothing.
‘deinterleave, d’
Deinterleave fields, placing one above the other.
‘interleave, i’
Interleave fields. Reverse the effect of deinterleaving.
Default value is none.
luma_swap, ls
chroma_swap, cs
alpha_swap, as
Swap luma/chroma/alpha fields. Exchange even & odd lines. Default value is 0.
39.136.1 Commands
This filter supports the all above options as commands.
39.137 inflate
Apply inflate effect to the video.
This filter replaces the pixel by the local(3x3) average by taking into account
only values higher than the pixel.
It accepts the following options:
threshold0
threshold1
threshold2
threshold3
Limit the maximum change for each plane, default is 65535.
If 0, plane will remain unchanged.
39.137.1 Commands
This filter supports the all above options as commands.
39.138 interlace
Simple interlacing filter from progressive contents. This interleaves upper (or
lower) lines from odd frames with lower (or upper) lines from even frames,
halving the frame rate and preserving image height.
Original        Original             New Frame
Frame 'j'      Frame 'j+1'             (tff)
==========      ===========       ==================
Line 0  -------------------->    Frame 'j' Line 0
Line 1          Line 1  ---->   Frame 'j+1' Line 1
Line 2 --------------------->    Frame 'j' Line 2
Line 3          Line 3  ---->   Frame 'j+1' Line 3
...             ...                   ...
New Frame + 1 will be generated by Frame 'j+2' and Frame 'j+3' and so on
It accepts the following optional parameters:
scan
This determines whether the interlaced frame is taken from the even
(tff - default) or odd (bff) lines of the progressive frame.
lowpass
Vertical lowpass filter to avoid twitter interlacing and
reduce moire patterns.
‘0, off’
Disable vertical lowpass filter
‘1, linear’
Enable linear filter (default)
‘2, complex’
Enable complex filter. This will slightly less reduce twitter and moire
but better retain detail and subjective sharpness impression.
39.139 kerndeint
Deinterlace input video by applying Donald Graft’s adaptive kernel
deinterling. Work on interlaced parts of a video to produce
progressive frames.
The description of the accepted parameters follows.
thresh
Set the threshold which affects the filter’s tolerance when
determining if a pixel line must be processed. It must be an integer
in the range [0,255] and defaults to 10. A value of 0 will result in
applying the process on every pixels.
map
Paint pixels exceeding the threshold value to white if set to 1.
Default is 0.
order
Set the fields order. Swap fields if set to 1, leave fields alone if
0. Default is 0.
sharp
Enable additional sharpening if set to 1. Default is 0.
twoway
Enable twoway sharpening if set to 1. Default is 0.
39.139.1 Examples
Apply default values:
kerndeint=thresh=10:map=0:order=0:sharp=0:twoway=0
Enable additional sharpening:
kerndeint=sharp=1
Paint processed pixels in white:
kerndeint=map=1
39.140 kirsch
Apply kirsch operator to input video stream.
The filter accepts the following option:
planes
Set which planes will be processed, unprocessed planes will be copied.
By default value 0xf, all planes will be processed.
scale
Set value which will be multiplied with filtered result.
delta
Set value which will be added to filtered result.
39.140.1 Commands
This filter supports the all above options as commands.
39.141 lagfun
Slowly update darker pixels.
This filter makes short flashes of light appear longer.
This filter accepts the following options:
decay
Set factor for decaying. Default is .95. Allowed range is from 0 to 1.
planes
Set which planes to filter. Default is all. Allowed range is from 0 to 15.
39.141.1 Commands
This filter supports the all above options as commands.
39.142 lenscorrection
Correct radial lens distortion
This filter can be used to correct for radial distortion as can result from the use
of wide angle lenses, and thereby re-rectify the image. To find the right parameters
one can use tools available for example as part of opencv or simply trial-and-error.
To use opencv use the calibration sample (under samples/cpp) from the opencv sources
and extract the k1 and k2 coefficients from the resulting matrix.
Note that effectively the same filter is available in the open-source tools Krita and
Digikam from the KDE project.
In contrast to the vignette filter, which can also be used to compensate lens errors,
this filter corrects the distortion of the image, whereas vignette corrects the
brightness distribution, so you may want to use both filters together in certain
cases, though you will have to take care of ordering, i.e. whether vignetting should
be applied before or after lens correction.
39.142.1 Options
The filter accepts the following options:
cx
Relative x-coordinate of the focal point of the image, and thereby the center of the
distortion. This value has a range [0,1] and is expressed as fractions of the image
width. Default is 0.5.
cy
Relative y-coordinate of the focal point of the image, and thereby the center of the
distortion. This value has a range [0,1] and is expressed as fractions of the image
height. Default is 0.5.
k1
Coefficient of the quadratic correction term. This value has a range [-1,1]. 0 means
no correction. Default is 0.
k2
Coefficient of the double quadratic correction term. This value has a range [-1,1].
0 means no correction. Default is 0.
i
Set interpolation type. Can be nearest or bilinear.
Default is nearest.
fc
Specify the color of the unmapped pixels. For the syntax of this option,
check the (ffmpeg-utils)"Color" section in the ffmpeg-utils
manual. Default color is black@0.
The formula that generates the correction is:
r_src = r_tgt * (1 + k1 * (r_tgt / r_0)^2 + k2 * (r_tgt / r_0)^4)
where r_0 is halve of the image diagonal and r_src and r_tgt are the
distances from the focal point in the source and target images, respectively.
39.142.2 Commands
This filter supports the all above options as commands.
39.143 lensfun
Apply lens correction via the lensfun library (http://lensfun.sourceforge.net/).
The lensfun filter requires the camera make, camera model, and lens model
to apply the lens correction. The filter will load the lensfun database and
query it to find the corresponding camera and lens entries in the database. As
long as these entries can be found with the given options, the filter can
perform corrections on frames. Note that incomplete strings will result in the
filter choosing the best match with the given options, and the filter will
output the chosen camera and lens models (logged with level "info"). You must
provide the make, camera model, and lens model as they are required.
To obtain a list of available makes and models, leave out one or both of make and
model options. The filter will send the full list to the log with level INFO.
The first column is the make and the second column is the model.
To obtain a list of available lenses, set any values for make and model and leave out the
lens_model option. The filter will send the full list of lenses in the log with level
INFO. The ffmpeg tool will exit after the list is printed.
The filter accepts the following options:
make
The make of the camera (for example, "Canon"). This option is required.
model
The model of the camera (for example, "Canon EOS 100D"). This option is
required.
lens_model
The model of the lens (for example, "Canon EF-S 18-55mm f/3.5-5.6 IS STM"). This
option is required.
db_path
The full path to the lens database folder. If not set, the filter will attempt to
load the database from the install path when the library was built. Default is unset.
mode
The type of correction to apply. The following values are valid options:
‘vignetting’
Enables fixing lens vignetting.
‘geometry’
Enables fixing lens geometry. This is the default.
‘subpixel’
Enables fixing chromatic aberrations.
‘vig_geo’
Enables fixing lens vignetting and lens geometry.
‘vig_subpixel’
Enables fixing lens vignetting and chromatic aberrations.
‘distortion’
Enables fixing both lens geometry and chromatic aberrations.
‘all’
Enables all possible corrections.
focal_length
The focal length of the image/video (zoom; expected constant for video). For
example, a 18–55mm lens has focal length range of [18–55], so a value in that
range should be chosen when using that lens. Default 18.
aperture
The aperture of the image/video (expected constant for video). Note that
aperture is only used for vignetting correction. Default 3.5.
focus_distance
The focus distance of the image/video (expected constant for video). Note that
focus distance is only used for vignetting and only slightly affects the
vignetting correction process. If unknown, leave it at the default value (which
is 1000).
scale
The scale factor which is applied after transformation. After correction the
video is no longer necessarily rectangular. This parameter controls how much of
the resulting image is visible. The value 0 means that a value will be chosen
automatically such that there is little or no unmapped area in the output
image. 1.0 means that no additional scaling is done. Lower values may result
in more of the corrected image being visible, while higher values may avoid
unmapped areas in the output.
target_geometry
The target geometry of the output image/video. The following values are valid
options:
‘rectilinear (default)’
‘fisheye’
‘panoramic’
‘equirectangular’
‘fisheye_orthographic’
‘fisheye_stereographic’
‘fisheye_equisolid’
‘fisheye_thoby’
reverse
Apply the reverse of image correction (instead of correcting distortion, apply
it).
interpolation
The type of interpolation used when correcting distortion. The following values
are valid options:
‘nearest’
‘linear (default)’
‘lanczos’
39.143.1 Examples
Apply lens correction with make "Canon", camera model "Canon EOS 100D", and lens
model "Canon EF-S 18-55mm f/3.5-5.6 IS STM" with focal length of "18" and
aperture of "8.0".
ffmpeg -i input.mov -vf lensfun=make=Canon:model="Canon EOS 100D":lens_model="Canon EF-S 18-55mm f/3.5-5.6 IS STM":focal_length=18:aperture=8 -c:v h264 -b:v 8000k output.mov
Apply the same as before, but only for the first 5 seconds of video.
ffmpeg -i input.mov -vf lensfun=make=Canon:model="Canon EOS 100D":lens_model="Canon EF-S 18-55mm f/3.5-5.6 IS STM":focal_length=18:aperture=8:enable='lte(t\,5)' -c:v h264 -b:v 8000k output.mov
39.144 lcevc
Low Complexity Enhancement Video Codec filter based on liblcevc_dec
(https://github.com/v-novaltd/LCEVCdec).
39.145 libplacebo
Flexible GPU-accelerated processing filter based on libplacebo
(https://code.videolan.org/videolan/libplacebo).
39.145.1 Options
The options for this filter are divided into the following sections:
39.145.1.1 Output mode
These options control the overall output mode. By default, libplacebo will try
to preserve the source colorimetry and size as best as it can, but it will
apply any embedded film grain, dolby vision metadata or anamorphic SAR present
in source frames.
inputs
Set the number of inputs. This can be used, alongside the idx variable,
to allow placing/blending multiple inputs inside the output frame. This
effectively enables functionality similar to hstack, overlay, etc.
w
h
Set the output video dimension expression. Default values are iw and
ih.
Allows for the same expressions as the scale filter.
crop_x
crop_y
Set the input crop x/y expressions, default values are (iw-cw)/2 and
(ih-ch)/2.
crop_w
crop_h
Set the input crop width/height expressions, default values are iw and
ih.
pos_x
pos_y
Set the output placement x/y expressions, default values are (ow-pw)/2
and (oh-ph)/2.
pos_w
pos_h
Set the output placement width/height expressions, default values are ow
and oh.
fps
Set the output frame rate. This can be rational, e.g. 60000/1001. If
set to the special string none (the default), input timestamps will
instead be passed through to the output unmodified. Otherwise, the input video
frames will be interpolated as necessary to rescale the video to the specified
target framerate, in a manner as determined by the frame_mixer option.
format
Set the output format override. If unset (the default), frames will be output
in the same format as the respective input frames. Otherwise, format conversion
will be performed.
force_original_aspect_ratio
force_divisible_by
Work the same as the identical scale filter options.
normalize_sar
If enabled, output frames will always have a pixel aspect ratio of 1:1. This
will introduce additional padding/cropping as necessary. If disabled (the
default), any aspect ratio mismatches, including those from e.g. anamorphic
video sources, are forwarded to the output pixel aspect ratio.
pad_crop_ratio
Specifies a ratio (between 0.0 and 1.0) between padding and
cropping when the input aspect ratio does not match the output aspect ratio and
normalize_sar is in effect. The default of 0.0 always pads the
content with black borders, while a value of 1.0 always crops off parts
of the content. Intermediate values are possible, leading to a mix of the two
approaches.
fillcolor
Set the color used to fill the output area not covered by the output image, for
example as a result of normalize_sar. For the general syntax of this
option, check the (ffmpeg-utils)"Color" section in the ffmpeg-utils
manual. Defaults to black.
corner_rounding
Render frames with rounded corners. The value, given as a float ranging from
0.0 to 1.0, indicates the relative degree of rounding, from fully
square to fully circular. In other words, it gives the radius divided by half
the smaller side length. Defaults to 0.0.
extra_opts
Pass extra libplacebo internal configuration options. These can be specified
as a list of key=value pairs separated by ’:’. The following example
shows how to configure a custom filter kernel ("EWA LanczosSharp") and use it
to double the input image resolution:
-vf "libplacebo=w=iw*2:h=ih*2:extra_opts='upscaler=custom\:upscaler_preset=ewa_lanczos\:upscaler_blur=0.9812505644269356'"
colorspace
color_primaries
color_trc
range
Configure the colorspace that output frames will be delivered in. The default
value of auto outputs frames in the same format as the input frames,
leading to no change. For any other value, conversion will be performed.
See the setparams filter for a list of possible values.
apply_filmgrain
Apply film grain (e.g. AV1 or H.274) if present in source frames, and strip
it from the output. Enabled by default.
apply_dolbyvision
Apply Dolby Vision RPU metadata if present in source frames, and strip it from
the output. Enabled by default. Note that Dolby Vision will always output
BT.2020+PQ, overriding the usual input frame metadata. These will also be
picked as the values of auto for the respective frame output options.
In addition to the expression constants documented for the scale filter,
the crop_w, crop_h, crop_x, crop_y,
pos_w, pos_h, pos_x and pos_y options can
also contain the following constants:
in_idx, idx
The (0-based) numeric index of the currently active input stream.
crop_w, cw
crop_h, ch
The computed values of crop_w and crop_h.
pos_w, pw
pos_h, ph
The computed values of pos_w and pos_h.
in_t, t
The input frame timestamp, in seconds. NAN if input timestamp is unknown.
out_t, ot
The input frame timestamp, in seconds. NAN if input timestamp is unknown.
n
The input frame number, starting with 0.
39.145.1.2 Scaling
The options in this section control how libplacebo performs upscaling and (if
necessary) downscaling. Note that libplacebo will always internally operate on
4:4:4 content, so any sub-sampled chroma formats such as yuv420p will
necessarily be upsampled and downsampled as part of the rendering process. That
means scaling might be in effect even if the source and destination resolution
are the same.
upscaler
downscaler
Configure the filter kernel used for upscaling and downscaling. The respective
defaults are spline36 and mitchell. For a full list of possible
values, pass help to these options. The most important values are:
‘none’
Forces the use of built-in GPU texture sampling (typically bilinear). Extremely
fast but poor quality, especially when downscaling.
‘bilinear’
Bilinear interpolation. Can generally be done for free on GPUs, except when
doing so would lead to aliasing. Fast and low quality.
‘nearest’
Nearest-neighbour interpolation. Sharp but highly aliasing.
‘oversample’
Algorithm that looks visually similar to nearest-neighbour interpolation but
tries to preserve pixel aspect ratio. Good for pixel art, since it results in
minimal distortion of the artistic appearance.
‘lanczos’
Standard sinc-sinc interpolation kernel.
‘spline36’
Cubic spline approximation of lanczos. No difference in performance, but has
very slightly less ringing.
‘ewa_lanczos’
Elliptically weighted average version of lanczos, based on a jinc-sinc kernel.
This is also popularly referred to as just "Jinc scaling". Slow but very high
quality.
‘gaussian’
Gaussian kernel. Has certain ideal mathematical properties, but subjectively
very blurry.
‘mitchell’
Cubic BC spline with parameters recommended by Mitchell and Netravali. Very
little ringing.
frame_mixer
Controls the kernel used for mixing frames temporally. The default value is
none, which disables frame mixing. For a full list of possible values,
pass help to this option. The most important values are:
‘none’
Disables frame mixing, giving a result equivalent to "nearest neighbour"
semantics.
‘oversample’
Oversamples the input video to create a "Smooth Motion"-type effect: if an
output frame would exactly fall on the transition between two video frames, it
is blended according to the relative overlap. This is the recommended option
whenever preserving the original subjective appearance is desired.
‘mitchell_clamp’
Larger filter kernel that smoothly interpolates multiple frames in a manner
designed to eliminate ringing and other artefacts as much as possible. This is
the recommended option wherever maximum visual smoothness is desired.
‘linear’
Linear blend/fade between frames. Especially useful for constructing e.g.
slideshows.
lut_entries
Configures the size of scaler LUTs, ranging from 1 to 256. The
default of 0 will pick libplacebo’s internal default, typically
64.
antiringing
Enables anti-ringing (for non-EWA filters). The value (between 0.0 and
1.0) configures the strength of the anti-ringing algorithm. May increase
aliasing if set too high. Disabled by default.
sigmoid
Enable sigmoidal compression during upscaling. Reduces ringing slightly.
Enabled by default.
39.145.1.3 Debanding
Libplacebo comes with a built-in debanding filter that is good at counteracting
many common sources of banding and blocking. Turning this on is highly
recommended whenever quality is desired.
deband
Enable (fast) debanding algorithm. Disabled by default.
deband_iterations
Number of deband iterations of the debanding algorithm. Each iteration is
performed with progressively increased radius (and diminished threshold).
Recommended values are in the range 1 to 4. Defaults to 1.
deband_threshold
Debanding filter strength. Higher numbers lead to more aggressive debanding.
Defaults to 4.0.
deband_radius
Debanding filter radius. A higher radius is better for slow gradients, while
a lower radius is better for steep gradients. Defaults to 16.0.
deband_grain
Amount of extra output grain to add. Helps hide imperfections. Defaults to
6.0.
39.145.1.4 Color adjustment
A collection of subjective color controls. Not very rigorous, so the exact
effect will vary somewhat depending on the input primaries and colorspace.
brightness
Brightness boost, between -1.0 and 1.0. Defaults to 0.0.
contrast
Contrast gain, between 0.0 and 16.0. Defaults to 1.0.
saturation
Saturation gain, between 0.0 and 16.0. Defaults to 1.0.
hue
Hue shift in radians, between -3.14 and 3.14. Defaults to
0.0. This will rotate the UV subvector, defaulting to BT.709
coefficients for RGB inputs.
gamma
Gamma adjustment, between 0.0 and 16.0. Defaults to 1.0.
cones
Cone model to use for color blindness simulation. Accepts any combination of
l, m and s. Here are some examples:
‘m’
Deuteranomaly / deuteranopia (affecting 3%-4% of the population)
‘l’
Protanomaly / protanopia (affecting 1%-2% of the population)
‘l+m’
Monochromacy (very rare)
‘l+m+s’
Achromatopsy (complete loss of daytime vision, extremely rare)
cone-strength
Gain factor for the cones specified by cones, between 0.0 and
10.0. A value of 1.0 results in no change to color vision. A
value of 0.0 (the default) simulates complete loss of those cones. Values
above 1.0 result in exaggerating the differences between cones, which
may help compensate for reduced color vision.
39.145.1.5 Peak detection
To help deal with sources that only have static HDR10 metadata (or no tagging
whatsoever), libplacebo uses its own internal frame analysis compute shader to
analyze source frames and adapt the tone mapping function in realtime. If this
is too slow, or if exactly reproducible frame-perfect results are needed, it’s
recommended to turn this feature off.
peak_detect
Enable HDR peak detection. Ignores static MaxCLL/MaxFALL values in favor of
dynamic detection from the input. Note that the detected values do not get
written back to the output frames, they merely guide the internal tone mapping
process. Enabled by default.
smoothing_period
Peak detection smoothing period, between 0.0 and 1000.0. Higher
values result in peak detection becoming less responsive to changes in the
input. Defaults to 100.0.
minimum_peak
Lower bound on the detected peak (relative to SDR white), between 0.0
and 100.0. Defaults to 1.0.
scene_threshold_low
scene_threshold_high
Lower and upper thresholds for scene change detection. Expressed in a
logarithmic scale between 0.0 and 100.0. Default to 5.5
and 10.0, respectively. Setting either to a negative value disables
this functionality.
percentile
Which percentile of the frame brightness histogram to use as the source peak
for tone-mapping. Defaults to 99.995, a fairly conservative value.
Setting this to 100.0 disables frame histogram measurement and instead
uses the true peak brightness for tone-mapping.
39.145.1.6 Tone mapping
The options in this section control how libplacebo performs tone-mapping and
gamut-mapping when dealing with mismatches between wide-gamut or HDR content.
In general, libplacebo relies on accurate source tagging and mastering display
gamut information to produce the best results.
gamut_mode
How to handle out-of-gamut colors that can occur as a result of colorimetric
gamut mapping.
‘clip’
Do nothing, simply clip out-of-range colors to the RGB volume. Low quality but
extremely fast.
‘perceptual’
Perceptually soft-clip colors to the gamut volume. This is the default.
‘relative’
Relative colorimetric hard-clip. Similar to perceptual but without
the soft knee.
‘saturation’
Saturation mapping, maps primaries directly to primaries in RGB space.
Not recommended except for artificial computer graphics for which a bright,
saturated display is desired.
‘absolute’
Absolute colorimetric hard-clip. Performs no adjustment of the white point.
‘desaturate’
Hard-desaturates out-of-gamut colors towards white, while preserving the
luminance. Has a tendency to distort the visual appearance of bright objects.
‘darken’
Linearly reduces content brightness to preserves saturated details, followed by
clipping the remaining out-of-gamut colors.
‘warn’
Highlight out-of-gamut pixels (by inverting/marking them).
‘linear’
Linearly reduces chromaticity of the entire image to make it fit within the
target color volume. Be careful when using this on BT.2020 sources without
proper mastering metadata, as doing so will lead to excessive desaturation.
tonemapping
Tone-mapping algorithm to use. Available values are:
‘auto’
Automatic selection based on internal heuristics. This is the default.
‘clip’
Performs no tone-mapping, just clips out-of-range colors. Retains perfect color
accuracy for in-range colors but completely destroys out-of-range information.
Does not perform any black point adaptation. Not configurable.
‘st2094-40’
EETF from SMPTE ST 2094-40 Annex B, which applies the Bezier curves from HDR10+
dynamic metadata based on Bezier curves to perform tone-mapping. The OOTF used
is adjusted based on the ratio between the targeted and actual display peak
luminances.
‘st2094-10’
EETF from SMPTE ST 2094-10 Annex B.2, which takes into account the input signal
average luminance in addition to the maximum/minimum. The configurable contrast
parameter influences the slope of the linear output segment, defaulting to
1.0 for no increase/decrease in contrast. Note that this does not
currently include the subjective gain/offset/gamma controls defined in Annex
B.3.
‘bt.2390’
EETF from the ITU-R Report BT.2390, a hermite spline roll-off with linear
segment. The knee point offset is configurable. Note that this parameter
defaults to 1.0, rather than the value of 0.5 from the ITU-R
spec.
‘bt.2446a’
EETF from ITU-R Report BT.2446, method A. Designed for well-mastered HDR
sources. Can be used for both forward and inverse tone mapping. Not
configurable.
‘spline’
Simple spline consisting of two polynomials, joined by a single pivot point.
The parameter gives the pivot point (in PQ space), defaulting to 0.30.
Can be used for both forward and inverse tone mapping.
‘reinhard’
Simple non-linear, global tone mapping algorithm. The parameter specifies the
local contrast coefficient at the display peak. Essentially, a parameter of
0.5 implies that the reference white will be about half as bright as
when clipping. Defaults to 0.5, which results in the simplest
formulation of this function.
‘mobius’
Generalization of the reinhard tone mapping algorithm to support an additional
linear slope near black. The tone mapping parameter indicates the trade-off
between the linear section and the non-linear section. Essentially, for a given
parameter x, every color value below x will be mapped linearly,
while higher values get non-linearly tone-mapped. Values near 1.0 make
this curve behave like clip, while values near 0.0 make this
curve behave like reinhard. The default value is 0.3, which
provides a good balance between colorimetric accuracy and preserving
out-of-gamut details.
‘hable’
Piece-wise, filmic tone-mapping algorithm developed by John Hable for use in
Uncharted 2, inspired by a similar tone-mapping algorithm used by Kodak.
Popularized by its use in video games with HDR rendering. Preserves both dark
and bright details very well, but comes with the drawback of changing the
average brightness quite significantly. This is sort of similar to
reinhard with parameter 0.24.
‘gamma’
Fits a gamma (power) function to transfer between the source and target color
spaces, effectively resulting in a perceptual hard-knee joining two roughly
linear sections. This preserves details at all scales fairly accurately, but
can result in an image with a muted or dull appearance. The parameter is used
as the cutoff point, defaulting to 0.5.
‘linear’
Linearly stretches the input range to the output range, in PQ space. This will
preserve all details accurately, but results in a significantly different
average brightness. Can be used for inverse tone-mapping in addition to regular
tone-mapping. The parameter can be used as an additional linear gain
coefficient (defaulting to 1.0).
tonemapping_param
For tunable tone mapping functions, this parameter can be used to fine-tune the
curve behavior. Refer to the documentation of tonemapping. The default
value of 0.0 is replaced by the curve’s preferred default setting.
inverse_tonemapping
If enabled, this filter will also attempt stretching SDR signals to fill HDR
output color volumes. Disabled by default.
tonemapping_lut_size
Size of the tone-mapping LUT, between 2 and 1024. Defaults to
256. Note that this figure is squared when combined with
peak_detect.
contrast_recovery
Contrast recovery strength. If set to a value above 0.0, the source
image will be divided into high-frequency and low-frequency components, and a
portion of the high-frequency image is added back onto the tone-mapped output.
May cause excessive ringing artifacts for some HDR sources, but can improve the
subjective sharpness and detail left over in the image after tone-mapping.
Defaults to 0.30.
contrast_smoothness
Contrast recovery lowpass kernel size. Defaults to 3.5. Increasing or
decreasing this will affect the visual appearance substantially. Has no effect
when contrast_recovery is disabled.
39.145.1.7 Dithering
By default, libplacebo will dither whenever necessary, which includes rendering
to any integer format below 16-bit precision. It’s recommended to always leave
this on, since not doing so may result in visible banding in the output, even
if the debanding filter is enabled. If maximum performance is needed,
use ordered_fixed instead of disabling dithering.
dithering
Dithering method to use. Accepts the following values:
‘none’
Disables dithering completely. May result in visible banding.
‘blue’
Dither with pseudo-blue noise. This is the default.
‘ordered’
Tunable ordered dither pattern.
‘ordered_fixed’
Faster ordered dither with a fixed size of 6. Texture-less.
‘white’
Dither with white noise. Texture-less.
dither_lut_size
Dither LUT size, as log base2 between 1 and 8. Defaults to
6, corresponding to a LUT size of 64x64.
dither_temporal
Enables temporal dithering. Disabled by default.
39.145.1.8 Custom shaders
libplacebo supports a number of custom shaders based on the mpv .hook GLSL
syntax. A collection of such shaders can be found here:
https://github.com/mpv-player/mpv/wiki/User-Scripts#user-shaders
A full description of the mpv shader format is beyond the scope of this
section, but a summary can be found here:
https://mpv.io/manual/master/#options-glsl-shader
custom_shader_path
Specifies a path to a custom shader file to load at runtime.
custom_shader_bin
Specifies a complete custom shader as a raw string.
39.145.1.9 Debugging / performance
All of the options in this section default off. They may be of assistance when
attempting to squeeze the maximum performance at the cost of quality.
skip_aa
Disable anti-aliasing when downscaling.
polar_cutoff
Truncate polar (EWA) scaler kernels below this absolute magnitude, between
0.0 and 1.0.
disable_linear
Disable linear light scaling.
disable_builtin
Disable built-in GPU sampling (forces LUT).
disable_fbos
Forcibly disable FBOs, resulting in loss of almost all functionality, but
offering the maximum possible speed.
39.145.2 Commands
This filter supports almost all of the above options as commands.
39.145.3 Examples
Tone-map input to standard gamut BT.709 output:
libplacebo=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv
Rescale input to fit into standard 1080p, with high quality scaling:
libplacebo=w=1920:h=1080:force_original_aspect_ratio=decrease:normalize_sar=true:upscaler=ewa_lanczos:downscaler=ewa_lanczos
Interpolate low FPS / VFR input to smoothed constant 60 fps output:
libplacebo=fps=60:frame_mixer=mitchell_clamp
Convert input to standard sRGB JPEG:
libplacebo=format=yuv420p:colorspace=bt470bg:color_primaries=bt709:color_trc=iec61966-2-1:range=pc
Use higher quality debanding settings:
libplacebo=deband=true:deband_iterations=3:deband_radius=8:deband_threshold=6
Run this filter on the CPU, on systems with Mesa installed (and with the most
expensive options disabled):
ffmpeg ... -init_hw_device vulkan:llvmpipe ... -vf libplacebo=upscaler=none:downscaler=none:peak_detect=false
Suppress CPU-based AV1/H.274 film grain application in the decoder, in favor of
doing it with this filter. Note that this is only a gain if the frames are
either already on the GPU, or if you’re using libplacebo for other purposes,
since otherwise the VRAM roundtrip will more than offset any expected speedup.
ffmpeg -export_side_data +film_grain ... -vf libplacebo=apply_filmgrain=true
Interop with VAAPI hwdec to avoid round-tripping through RAM:
ffmpeg -init_hw_device vulkan -hwaccel vaapi -hwaccel_output_format vaapi ... -vf libplacebo
39.146 libvmaf
Calculate the VMAF (Video Multi-Method Assessment Fusion) score for a
reference/distorted pair of input videos.
The first input is the distorted video, and the second input is the reference video.
The obtained VMAF score is printed through the logging system.
It requires Netflix’s vmaf library (libvmaf) as a pre-requisite.
After installing the library it can be enabled using:
./configure --enable-libvmaf.
The filter has following options:
model
A ‘|‘ delimited list of vmaf models. Each model can be configured with a number of parameters.
Default value: "version=vmaf_v0.6.1"
feature
A ‘|‘ delimited list of features. Each feature can be configured with a number of parameters.
log_path
Set the file path to be used to store log files.
log_fmt
Set the format of the log file (xml, json, csv, or sub).
pool
Set the pool method to be used for computing vmaf.
Options are min, harmonic_mean or mean (default).
n_threads
Set number of threads to be used when initializing libvmaf.
Default value: 0, no threads.
n_subsample
Set frame subsampling interval to be used.
This filter also supports the framesync options.
39.146.1 Examples
In the examples below, a distorted video distorted.mpg is
compared with a reference file reference.mpg.
Basic usage:
ffmpeg -i distorted.mpg -i reference.mpg -lavfi libvmaf=log_path=output.xml -f null -
Example with multiple models:
ffmpeg -i distorted.mpg -i reference.mpg -lavfi libvmaf='model=version=vmaf_v0.6.1\\:name=vmaf|version=vmaf_v0.6.1neg\\:name=vmaf_neg' -f null -
Example with multiple additional features:
ffmpeg -i distorted.mpg -i reference.mpg -lavfi libvmaf='feature=name=psnr|name=ciede' -f null -
Example with options and different containers:
ffmpeg -i distorted.mpg -i reference.mkv -lavfi "[0:v]settb=AVTB,setpts=PTS-STARTPTS[main];[1:v]settb=AVTB,setpts=PTS-STARTPTS[ref];[main][ref]libvmaf=log_fmt=json:log_path=output.json" -f null -
39.147 libvmaf_cuda
This is the CUDA variant of the libvmaf filter. It only accepts CUDA frames.
It requires Netflix’s vmaf library (libvmaf) as a pre-requisite.
After installing the library it can be enabled using:
./configure --enable-nonfree --enable-ffnvcodec --enable-libvmaf.
39.147.1 Examples
Basic usage showing CUVID hardware decoding and CUDA scaling with scale_cuda:
ffmpeg \
-hwaccel cuda -hwaccel_output_format cuda -codec:v av1_cuvid -i dis.obu \
-hwaccel cuda -hwaccel_output_format cuda -codec:v av1_cuvid -i ref.obu \
-filter_complex "
[0:v]scale_cuda=format=yuv420p[dis]; \
[1:v]scale_cuda=format=yuv420p[ref]; \
[dis][ref]libvmaf_cuda=log_fmt=json:log_path=output.json
" \
-f null -
39.148 limitdiff
Apply limited difference filter using second and optionally third video stream.
The filter accepts the following options:
threshold
Set the threshold to use when allowing certain differences between video streams.
Any absolute difference value lower or exact than this threshold will pick pixel components from
first video stream.
elasticity
Set the elasticity of soft thresholding when processing video streams.
This value multiplied with first one sets second threshold.
Any absolute difference value greater or exact than second threshold will pick pixel components
from second video stream. For values between those two threshold
linear interpolation between first and second video stream will be used.
reference
Enable the reference (third) video stream processing. By default is disabled.
If set, this video stream will be used for calculating absolute difference with first video
stream.
planes
Specify which planes will be processed. Defaults to all available.
39.148.1 Commands
This filter supports the all above options as commands except option ‘reference’.
39.149 limiter
Limits the pixel components values to the specified range [min, max].
The filter accepts the following options:
min
Lower bound. Defaults to the lowest allowed value for the input.
max
Upper bound. Defaults to the highest allowed value for the input.
planes
Specify which planes will be processed. Defaults to all available.
39.149.1 Commands
This filter supports the all above options as commands.
39.150 loop
Loop video frames.
The filter accepts the following options:
loop
Set the number of loops. Setting this value to -1 will result in infinite loops.
Default is 0.
size
Set maximal size in number of frames. Default is 0.
start
Set first frame of loop. Default is 0.
time
Set the time of loop start in seconds.
Only used if option named start is set to -1.
39.150.1 Examples
Loop single first frame infinitely:
loop=loop=-1:size=1:start=0
Loop single first frame 10 times:
loop=loop=10:size=1:start=0
Loop 10 first frames 5 times:
loop=loop=5:size=10:start=0
39.151 lut1d
Apply a 1D LUT to an input video.
The filter accepts the following options:
file
Set the 1D LUT file name.
Currently supported formats:
‘cube’
Iridas
‘csp’
cineSpace
interp
Select interpolation mode.
Available values are:
‘nearest’
Use values from the nearest defined point.
‘linear’
Interpolate values using the linear interpolation.
‘cosine’
Interpolate values using the cosine interpolation.
‘cubic’
Interpolate values using the cubic interpolation.
‘spline’
Interpolate values using the spline interpolation.
39.151.1 Commands
This filter supports the all above options as commands.
39.152 lut3d
Apply a 3D LUT to an input video.
The filter accepts the following options:
file
Set the 3D LUT file name.
Currently supported formats:
‘3dl’
AfterEffects
‘cube’
Iridas
‘dat’
DaVinci
‘m3d’
Pandora
‘csp’
cineSpace
interp
Select interpolation mode.
Available values are:
‘nearest’
Use values from the nearest defined point.
‘trilinear’
Interpolate values using the 8 points defining a cube.
‘tetrahedral’
Interpolate values using a tetrahedron.
‘pyramid’
Interpolate values using a pyramid.
‘prism’
Interpolate values using a prism.
39.152.1 Commands
This filter supports the interp option as commands.
39.153 lumakey
Turn certain luma values into transparency.
The filter accepts the following options:
threshold
Set the luma which will be used as base for transparency.
Default value is 0.
tolerance
Set the range of luma values to be keyed out.
Default value is 0.01.
softness
Set the range of softness. Default value is 0.
Use this to control gradual transition from zero to full transparency.
39.153.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.154 lut, lutrgb, lutyuv
Compute a look-up table for binding each pixel component input value
to an output value, and apply it to the input video.
lutyuv applies a lookup table to a YUV input video, lutrgb
to an RGB input video.
These filters accept the following parameters:
c0
set first pixel component expression
c1
set second pixel component expression
c2
set third pixel component expression
c3
set fourth pixel component expression, corresponds to the alpha component
r
set red component expression
g
set green component expression
b
set blue component expression
a
alpha component expression
y
set Y/luma component expression
u
set U/Cb component expression
v
set V/Cr component expression
Each of them specifies the expression to use for computing the lookup table for
the corresponding pixel component values.
The exact component associated to each of the c* options depends on the
format in input.
The lut filter requires either YUV or RGB pixel formats in input,
lutrgb requires RGB pixel formats in input, and lutyuv requires YUV.
The expressions can contain the following constants and functions:
w
h
The input width and height.
val
The input value for the pixel component.
clipval
The input value, clipped to the minval-maxval range.
maxval
The maximum value for the pixel component.
minval
The minimum value for the pixel component.
negval
The negated value for the pixel component value, clipped to the
minval-maxval range; it corresponds to the expression
"maxval-clipval+minval".
clip(val)
The computed value in val, clipped to the
minval-maxval range.
gammaval(gamma)
The computed gamma correction value of the pixel component value,
clipped to the minval-maxval range. It corresponds to the
expression
"pow((clipval-minval)/(maxval-minval)\,gamma)*(maxval-minval)+minval"
All expressions default to "clipval".
39.154.1 Commands
This filter supports same commands as options.
39.154.2 Examples
Negate input video:
lutrgb="r=maxval+minval-val:g=maxval+minval-val:b=maxval+minval-val"
lutyuv="y=maxval+minval-val:u=maxval+minval-val:v=maxval+minval-val"
The above is the same as:
lutrgb="r=negval:g=negval:b=negval"
lutyuv="y=negval:u=negval:v=negval"
Negate luma:
lutyuv=y=negval
Remove chroma components, turning the video into a graytone image:
lutyuv="u=128:v=128"
Apply a luma burning effect:
lutyuv="y=2*val"
Remove green and blue components:
lutrgb="g=0:b=0"
Set a constant alpha channel value on input:
format=rgba,lutrgb=a="maxval-minval/2"
Correct luma gamma by a factor of 0.5:
lutyuv=y=gammaval(0.5)
Discard least significant bits of luma:
lutyuv=y='bitand(val, 128+64+32)'
Technicolor like effect:
lutyuv=u='(val-maxval/2)*2+maxval/2':v='(val-maxval/2)*2+maxval/2'
39.155 lut2, tlut2
The lut2 filter takes two input streams and outputs one
stream.
The tlut2 (time lut2) filter takes two consecutive frames
from one single stream.
This filter accepts the following parameters:
c0
set first pixel component expression
c1
set second pixel component expression
c2
set third pixel component expression
c3
set fourth pixel component expression, corresponds to the alpha component
d
set output bit depth, only available for lut2 filter. By default is 0,
which means bit depth is automatically picked from first input format.
The lut2 filter also supports the framesync options.
Each of them specifies the expression to use for computing the lookup table for
the corresponding pixel component values.
The exact component associated to each of the c* options depends on the
format in inputs.
The expressions can contain the following constants:
w
h
The input width and height.
x
The first input value for the pixel component.
y
The second input value for the pixel component.
bdx
The first input video bit depth.
bdy
The second input video bit depth.
All expressions default to "x".
39.155.1 Commands
This filter supports the all above options as commands except option d.
39.155.2 Examples
Highlight differences between two RGB video streams:
lut2='ifnot(x-y,0,pow(2,bdx)-1):ifnot(x-y,0,pow(2,bdx)-1):ifnot(x-y,0,pow(2,bdx)-1)'
Highlight differences between two YUV video streams:
lut2='ifnot(x-y,0,pow(2,bdx)-1):ifnot(x-y,pow(2,bdx-1),pow(2,bdx)-1):ifnot(x-y,pow(2,bdx-1),pow(2,bdx)-1)'
Show max difference between two video streams:
lut2='if(lt(x,y),0,if(gt(x,y),pow(2,bdx)-1,pow(2,bdx-1))):if(lt(x,y),0,if(gt(x,y),pow(2,bdx)-1,pow(2,bdx-1))):if(lt(x,y),0,if(gt(x,y),pow(2,bdx)-1,pow(2,bdx-1)))'
39.156 maskedclamp
Clamp the first input stream with the second input and third input stream.
Returns the value of first stream to be between second input
stream - undershoot and third input stream + overshoot.
This filter accepts the following options:
undershoot
Default value is 0.
overshoot
Default value is 0.
planes
Set which planes will be processed as bitmap, unprocessed planes will be
copied from first stream.
By default value 0xf, all planes will be processed.
39.156.1 Commands
This filter supports the all above options as commands.
39.157 maskedmax
Merge the second and third input stream into output stream using absolute differences
between second input stream and first input stream and absolute difference between
third input stream and first input stream. The picked value will be from second input
stream if second absolute difference is greater than first one or from third input stream
otherwise.
This filter accepts the following options:
planes
Set which planes will be processed as bitmap, unprocessed planes will be
copied from first stream.
By default value 0xf, all planes will be processed.
39.157.1 Commands
This filter supports the all above options as commands.
39.158 maskedmerge
Merge the first input stream with the second input stream using per pixel
weights in the third input stream.
A value of 0 in the third stream pixel component means that pixel component
from first stream is returned unchanged, while maximum value (eg. 255 for
8-bit videos) means that pixel component from second stream is returned
unchanged. Intermediate values define the amount of merging between both
input stream’s pixel components.
This filter accepts the following options:
planes
Set which planes will be processed as bitmap, unprocessed planes will be
copied from first stream.
By default value 0xf, all planes will be processed.
39.158.1 Commands
This filter supports the all above options as commands.
39.159 maskedmin
Merge the second and third input stream into output stream using absolute differences
between second input stream and first input stream and absolute difference between
third input stream and first input stream. The picked value will be from second input
stream if second absolute difference is less than first one or from third input stream
otherwise.
This filter accepts the following options:
planes
Set which planes will be processed as bitmap, unprocessed planes will be
copied from first stream.
By default value 0xf, all planes will be processed.
39.159.1 Commands
This filter supports the all above options as commands.
39.160 maskedthreshold
Pick pixels comparing absolute difference of two video streams with fixed
threshold.
If absolute difference between pixel component of first and second video
stream is equal or lower than user supplied threshold than pixel component
from first video stream is picked, otherwise pixel component from second
video stream is picked.
This filter accepts the following options:
threshold
Set threshold used when picking pixels from absolute difference from two input
video streams.
planes
Set which planes will be processed as bitmap, unprocessed planes will be
copied from second stream.
By default value 0xf, all planes will be processed.
mode
Set mode of filter operation. Can be abs or diff.
Default is abs.
39.160.1 Commands
This filter supports the all above options as commands.
39.161 maskfun
Create mask from input video.
For example it is useful to create motion masks after tblend filter.
This filter accepts the following options:
low
Set low threshold. Any pixel component lower or exact than this value will be set to 0.
high
Set high threshold. Any pixel component higher than this value will be set to max value
allowed for current pixel format.
planes
Set planes to filter, by default all available planes are filtered.
fill
Fill all frame pixels with this value.
sum
Set max average pixel value for frame. If sum of all pixel components is higher that this
average, output frame will be completely filled with value set by fill option.
Typically useful for scene changes when used in combination with tblend filter.
39.161.1 Commands
This filter supports the all above options as commands.
39.162 mcdeint
Apply motion-compensation deinterlacing.
It needs one field per frame as input and must thus be used together
with yadif=1/3 or equivalent.
This filter accepts the following options:
mode
Set the deinterlacing mode.
It accepts one of the following values:
‘fast’
‘medium’
‘slow’
use iterative motion estimation
‘extra_slow’
like ‘slow’, but use multiple reference frames.
Default value is ‘fast’.
parity
Set the picture field parity assumed for the input video. It must be
one of the following values:
‘0, tff’
assume top field first
‘1, bff’
assume bottom field first
Default value is ‘bff’.
qp
Set per-block quantization parameter (QP) used by the internal
encoder.
Higher values should result in a smoother motion vector field but less
optimal individual vectors. Default value is 1.
39.163 median
Pick median pixel from certain rectangle defined by radius.
This filter accepts the following options:
radius
Set horizontal radius size. Default value is 1.
Allowed range is integer from 1 to 127.
planes
Set which planes to process. Default is 15, which is all available planes.
radiusV
Set vertical radius size. Default value is 0.
Allowed range is integer from 0 to 127.
If it is 0, value will be picked from horizontal radius option.
percentile
Set median percentile. Default value is 0.5.
Default value of 0.5 will pick always median values, while 0 will pick
minimum values, and 1 maximum values.
39.163.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.164 mergeplanes
Merge color channel components from several video streams.
The filter accepts up to 4 input streams, and merge selected input
planes to the output video.
This filter accepts the following options:
mapping
Set input to output plane mapping. Default is 0.
The mappings is specified as a bitmap. It should be specified as a
hexadecimal number in the form 0xAa[Bb[Cc[Dd]]]. ’Aa’ describes the
mapping for the first plane of the output stream. ’A’ sets the number of
the input stream to use (from 0 to 3), and ’a’ the plane number of the
corresponding input to use (from 0 to 3). The rest of the mappings is
similar, ’Bb’ describes the mapping for the output stream second
plane, ’Cc’ describes the mapping for the output stream third plane and
’Dd’ describes the mapping for the output stream fourth plane.
format
Set output pixel format. Default is yuva444p.
map0s
map1s
map2s
map3s
Set input to output stream mapping for output Nth plane. Default is 0.
map0p
map1p
map2p
map3p
Set input to output plane mapping for output Nth plane. Default is 0.
39.164.1 Examples
Merge three gray video streams of same width and height into single video stream:
[a0][a1][a2]mergeplanes=0x001020:yuv444p
Merge 1st yuv444p stream and 2nd gray video stream into yuva444p video stream:
[a0][a1]mergeplanes=0x00010210:yuva444p
Swap Y and A plane in yuva444p stream:
format=yuva444p,mergeplanes=0x03010200:yuva444p
Swap U and V plane in yuv420p stream:
format=yuv420p,mergeplanes=0x000201:yuv420p
Cast a rgb24 clip to yuv444p:
format=rgb24,mergeplanes=0x000102:yuv444p
39.165 mestimate
Estimate and export motion vectors using block matching algorithms.
Motion vectors are stored in frame side data to be used by other filters.
This filter accepts the following options:
method
Specify the motion estimation method. Accepts one of the following values:
‘esa’
Exhaustive search algorithm.
‘tss’
Three step search algorithm.
‘tdls’
Two dimensional logarithmic search algorithm.
‘ntss’
New three step search algorithm.
‘fss’
Four step search algorithm.
‘ds’
Diamond search algorithm.
‘hexbs’
Hexagon-based search algorithm.
‘epzs’
Enhanced predictive zonal search algorithm.
‘umh’
Uneven multi-hexagon search algorithm.
Default value is ‘esa’.
mb_size
Macroblock size. Default 16.
search_param
Search parameter. Default 7.
39.166 midequalizer
Apply Midway Image Equalization effect using two video streams.
Midway Image Equalization adjusts a pair of images to have the same
histogram, while maintaining their dynamics as much as possible. It’s
useful for e.g. matching exposures from a pair of stereo cameras.
This filter has two inputs and one output, which must be of same pixel format, but
may be of different sizes. The output of filter is first input adjusted with
midway histogram of both inputs.
This filter accepts the following option:
planes
Set which planes to process. Default is 15, which is all available planes.
39.167 minterpolate
Convert the video to specified frame rate using motion interpolation.
This filter accepts the following options:
fps
Specify the output frame rate. This can be rational e.g. 60000/1001. Frames are dropped if fps is lower than source fps. Default 60.
mi_mode
Motion interpolation mode. Following values are accepted:
‘dup’
Duplicate previous or next frame for interpolating new ones.
‘blend’
Blend source frames. Interpolated frame is mean of previous and next frames.
‘mci’
Motion compensated interpolation. Following options are effective when this mode is selected:
‘mc_mode’
Motion compensation mode. Following values are accepted:
‘obmc’
Overlapped block motion compensation.
‘aobmc’
Adaptive overlapped block motion compensation. Window weighting coefficients are controlled adaptively according to the reliabilities of the neighboring motion vectors to reduce oversmoothing.
Default mode is ‘obmc’.
‘me_mode’
Motion estimation mode. Following values are accepted:
‘bidir’
Bidirectional motion estimation. Motion vectors are estimated for each source frame in both forward and backward directions.
‘bilat’
Bilateral motion estimation. Motion vectors are estimated directly for interpolated frame.
Default mode is ‘bilat’.
‘me’
The algorithm to be used for motion estimation. Following values are accepted:
‘esa’
Exhaustive search algorithm.
‘tss’
Three step search algorithm.
‘tdls’
Two dimensional logarithmic search algorithm.
‘ntss’
New three step search algorithm.
‘fss’
Four step search algorithm.
‘ds’
Diamond search algorithm.
‘hexbs’
Hexagon-based search algorithm.
‘epzs’
Enhanced predictive zonal search algorithm.
‘umh’
Uneven multi-hexagon search algorithm.
Default algorithm is ‘epzs’.
‘mb_size’
Macroblock size. Default 16.
‘search_param’
Motion estimation search parameter. Default 32.
‘vsbmc’
Enable variable-size block motion compensation. Motion estimation is applied with smaller block sizes at object boundaries in order to make them less blurry. Default is 0 (disabled).
scd
Scene change detection method. Scene change leads motion vectors to be in random direction. Scene change detection replace interpolated frames by duplicate ones. May not be needed for other modes. Following values are accepted:
‘none’
Disable scene change detection.
‘fdiff’
Frame difference. Corresponding pixel values are compared and if it satisfies scd_threshold scene change is detected.
Default method is ‘fdiff’.
scd_threshold
Scene change detection threshold. Default is 10..
39.168 mix
Mix several video input streams into one video stream.
A description of the accepted options follows.
inputs
The number of inputs. If unspecified, it defaults to 2.
weights
Specify weight of each input video stream as sequence.
Each weight is separated by space. If number of weights
is smaller than number of frames last specified
weight will be used for all remaining unset weights.
scale
Specify scale, if it is set it will be multiplied with sum
of each weight multiplied with pixel values to give final destination
pixel value. By default scale is auto scaled to sum of weights.
planes
Set which planes to filter. Default is all. Allowed range is from 0 to 15.
duration
Specify how end of stream is determined.
‘longest’
The duration of the longest input. (default)
‘shortest’
The duration of the shortest input.
‘first’
The duration of the first input.
39.168.1 Commands
This filter supports the following commands:
weights
scale
planes
Syntax is same as option with same name.
39.169 monochrome
Convert video to gray using custom color filter.
A description of the accepted options follows.
cb
Set the chroma blue spot. Allowed range is from -1 to 1.
Default value is 0.
cr
Set the chroma red spot. Allowed range is from -1 to 1.
Default value is 0.
size
Set the color filter size. Allowed range is from .1 to 10.
Default value is 1.
high
Set the highlights strength. Allowed range is from 0 to 1.
Default value is 0.
39.169.1 Commands
This filter supports the all above options as commands.
39.170 morpho
This filter allows to apply main morphological grayscale transforms,
erode and dilate with arbitrary structures set in second input stream.
Unlike naive implementation and much slower performance in erosion
and dilation filters, when speed is critical morpho filter
should be used instead.
A description of accepted options follows,
mode
Set morphological transform to apply, can be:
‘erode’
‘dilate’
‘open’
‘close’
‘gradient’
‘tophat’
‘blackhat’
Default is erode.
planes
Set planes to filter, by default all planes except alpha are filtered.
structure
Set which structure video frames will be processed from second input stream,
can be first or all. Default is all.
The morpho filter also supports the framesync options.
39.170.1 Commands
This filter supports same commands as options.
39.171 mpdecimate
Drop frames that do not differ greatly from the previous frame in
order to reduce frame rate.
The main use of this filter is for very-low-bitrate encoding
(e.g. streaming over dialup modem), but it could in theory be used for
fixing movies that were inverse-telecined incorrectly.
A description of the accepted options follows.
max
Set the maximum number of consecutive frames which can be dropped (if
positive), or the minimum interval between dropped frames (if
negative). If the value is 0, the frame is dropped disregarding the
number of previous sequentially dropped frames.
Default value is 0.
keep
Set the maximum number of consecutive similar frames to ignore before to start dropping them.
If the value is 0, the frame is dropped disregarding the
number of previous sequentially similar frames.
Default value is 0.
hi
lo
frac
Set the dropping threshold values.
Values for hi and lo are for 8x8 pixel blocks and
represent actual pixel value differences, so a threshold of 64
corresponds to 1 unit of difference for each pixel, or the same spread
out differently over the block.
A frame is a candidate for dropping if no 8x8 blocks differ by more
than a threshold of hi, and if no more than frac blocks (1
meaning the whole image) differ by more than a threshold of lo.
Default value for hi is 64*12, default value for lo is
64*5, and default value for frac is 0.33.
39.172 msad
Obtain the MSAD (Mean Sum of Absolute Differences) between two input videos.
This filter takes two input videos.
Both input videos must have the same resolution and pixel format for
this filter to work correctly. Also it assumes that both inputs
have the same number of frames, which are compared one by one.
The obtained per component, average, min and max MSAD is printed through
the logging system.
The filter stores the calculated MSAD of each frame in frame metadata.
This filter also supports the framesync options.
In the below example the input file main.mpg being processed is compared
with the reference file ref.mpg.
ffmpeg -i main.mpg -i ref.mpg -lavfi msad -f null -
39.173 multiply
Multiply first video stream pixels values with second video stream pixels values.
The filter accepts the following options:
scale
Set the scale applied to second video stream. By default is 1.
Allowed range is from 0 to 9.
offset
Set the offset applied to second video stream. By default is 0.5.
Allowed range is from -1 to 1.
planes
Specify planes from input video stream that will be processed.
By default all planes are processed.
39.173.1 Commands
This filter supports same commands as options.
39.174 negate
Negate (invert) the input video.
It accepts the following option:
components
Set components to negate.
Available values for components are:
‘y’
‘u’
‘v’
‘a’
‘r’
‘g’
‘b’
negate_alpha
With value 1, it negates the alpha component, if present. Default value is 0.
39.174.1 Commands
This filter supports same commands as options.
39.175 nlmeans
Denoise frames using Non-Local Means algorithm.
Each pixel is adjusted by looking for other pixels with similar contexts. This
context similarity is defined by comparing their surrounding patches of size
pxp. Patches are searched in an area of rxr
around the pixel.
Note that the research area defines centers for patches, which means some
patches will be made of pixels outside that research area.
The filter accepts the following options.
s
Set denoising strength. Default is 1.0. Must be in range [1.0, 30.0].
p
Set patch size. Default is 7. Must be odd number in range [0, 99].
pc
Same as p but for chroma planes.
The default value is 0 and means automatic.
r
Set research size. Default is 15. Must be odd number in range [0, 99].
rc
Same as r but for chroma planes.
The default value is 0 and means automatic.
39.176 nnedi
Deinterlace video using neural network edge directed interpolation.
This filter accepts the following options:
weights
Mandatory option, without binary file filter can not work.
Currently file can be found here:
https://github.com/dubhater/vapoursynth-nnedi3/blob/master/src/nnedi3_weights.bin
deint
Set which frames to deinterlace, by default it is all.
Can be all or interlaced.
field
Set mode of operation.
Can be one of the following:
‘af’
Use frame flags, both fields.
‘a’
Use frame flags, single field.
‘t’
Use top field only.
‘b’
Use bottom field only.
‘tf’
Use both fields, top first.
‘bf’
Use both fields, bottom first.
planes
Set which planes to process, by default filter process all frames.
nsize
Set size of local neighborhood around each pixel, used by the predictor neural
network.
Can be one of the following:
‘s8x6’
‘s16x6’
‘s32x6’
‘s48x6’
‘s8x4’
‘s16x4’
‘s32x4’
nns
Set the number of neurons in predictor neural network.
Can be one of the following:
‘n16’
‘n32’
‘n64’
‘n128’
‘n256’
qual
Controls the number of different neural network predictions that are blended
together to compute the final output value. Can be fast, default or
slow.
etype
Set which set of weights to use in the predictor.
Can be one of the following:
‘a, abs’
weights trained to minimize absolute error
‘s, mse’
weights trained to minimize squared error
pscrn
Controls whether or not the prescreener neural network is used to decide
which pixels should be processed by the predictor neural network and which
can be handled by simple cubic interpolation.
The prescreener is trained to know whether cubic interpolation will be
sufficient for a pixel or whether it should be predicted by the predictor nn.
The computational complexity of the prescreener nn is much less than that of
the predictor nn. Since most pixels can be handled by cubic interpolation,
using the prescreener generally results in much faster processing.
The prescreener is pretty accurate, so the difference between using it and not
using it is almost always unnoticeable.
Can be one of the following:
‘none’
‘original’
‘new’
‘new2’
‘new3’
Default is new.
39.176.1 Commands
This filter supports same commands as options, excluding weights option.
39.177 noformat
Force libavfilter not to use any of the specified pixel formats for the
input to the next filter.
It accepts the following parameters:
pix_fmts
A ’|’-separated list of pixel format names, such as
pix_fmts=yuv420p|monow|rgb24".
39.177.1 Examples
Force libavfilter to use a format different from yuv420p for the
input to the vflip filter:
noformat=pix_fmts=yuv420p,vflip
Convert the input video to any of the formats not contained in the list:
noformat=yuv420p|yuv444p|yuv410p
39.178 noise
Add noise on video input frame.
The filter accepts the following options:
all_seed
c0_seed
c1_seed
c2_seed
c3_seed
Set noise seed for specific pixel component or all pixel components in case
of all_seed. Default value is 123457.
all_strength, alls
c0_strength, c0s
c1_strength, c1s
c2_strength, c2s
c3_strength, c3s
Set noise strength for specific pixel component or all pixel components in case
all_strength. Default value is 0. Allowed range is [0, 100].
all_flags, allf
c0_flags, c0f
c1_flags, c1f
c2_flags, c2f
c3_flags, c3f
Set pixel component flags or set flags for all components if all_flags.
Available values for component flags are:
‘a’
averaged temporal noise (smoother)
‘p’
mix random noise with a (semi)regular pattern
‘t’
temporal noise (noise pattern changes between frames)
‘u’
uniform noise (gaussian otherwise)
39.178.1 Examples
Add temporal and uniform noise to input video:
noise=alls=20:allf=t+u
39.179 normalize
Normalize RGB video (aka histogram stretching, contrast stretching).
See: https://en.wikipedia.org/wiki/Normalization_(image_processing)
For each channel of each frame, the filter computes the input range and maps
it linearly to the user-specified output range. The output range defaults
to the full dynamic range from pure black to pure white.
Temporal smoothing can be used on the input range to reduce flickering (rapid
changes in brightness) caused when small dark or bright objects enter or leave
the scene. This is similar to the auto-exposure (automatic gain control) on a
video camera, and, like a video camera, it may cause a period of over- or
under-exposure of the video.
The R,G,B channels can be normalized independently, which may cause some
color shifting, or linked together as a single channel, which prevents
color shifting. Linked normalization preserves hue. Independent normalization
does not, so it can be used to remove some color casts. Independent and linked
normalization can be combined in any ratio.
The normalize filter accepts the following options:
blackpt
whitept
Colors which define the output range. The minimum input value is mapped to
the blackpt. The maximum input value is mapped to the whitept.
The defaults are black and white respectively. Specifying white for
blackpt and black for whitept will give color-inverted,
normalized video. Shades of grey can be used to reduce the dynamic range
(contrast). Specifying saturated colors here can create some interesting
effects.
smoothing
The number of previous frames to use for temporal smoothing. The input range
of each channel is smoothed using a rolling average over the current frame
and the smoothing previous frames. The default is 0 (no temporal
smoothing).
independence
Controls the ratio of independent (color shifting) channel normalization to
linked (color preserving) normalization. 0.0 is fully linked, 1.0 is fully
independent. Defaults to 1.0 (fully independent).
strength
Overall strength of the filter. 1.0 is full strength. 0.0 is a rather
expensive no-op. Defaults to 1.0 (full strength).
39.179.1 Commands
This filter supports same commands as options, excluding smoothing option.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.179.2 Examples
Stretch video contrast to use the full dynamic range, with no temporal
smoothing; may flicker depending on the source content:
normalize=blackpt=black:whitept=white:smoothing=0
As above, but with 50 frames of temporal smoothing; flicker should be
reduced, depending on the source content:
normalize=blackpt=black:whitept=white:smoothing=50
As above, but with hue-preserving linked channel normalization:
normalize=blackpt=black:whitept=white:smoothing=50:independence=0
As above, but with half strength:
normalize=blackpt=black:whitept=white:smoothing=50:independence=0:strength=0.5
Map the darkest input color to red, the brightest input color to cyan:
normalize=blackpt=red:whitept=cyan
39.180 null
Pass the video source unchanged to the output.
39.181 ocr
Optical Character Recognition
This filter uses Tesseract for optical character recognition. To enable
compilation of this filter, you need to configure FFmpeg with
--enable-libtesseract.
It accepts the following options:
datapath
Set datapath to tesseract data. Default is to use whatever was
set at installation.
language
Set language, default is "eng".
whitelist
Set character whitelist.
blacklist
Set character blacklist.
The filter exports recognized text as the frame metadata lavfi.ocr.text.
The filter exports confidence of recognized words as the frame metadata lavfi.ocr.confidence.
39.182 ocv
Apply a video transform using libopencv.
To enable this filter, install the libopencv library and headers and
configure FFmpeg with --enable-libopencv.
It accepts the following parameters:
filter_name
The name of the libopencv filter to apply.
filter_params
The parameters to pass to the libopencv filter. If not specified, the default
values are assumed.
Refer to the official libopencv documentation for more precise
information:
http://docs.opencv.org/master/modules/imgproc/doc/filtering.html
Several libopencv filters are supported; see the following subsections.
39.182.1 dilate
Dilate an image by using a specific structuring element.
It corresponds to the libopencv function cvDilate.
It accepts the parameters: struct_el|nb_iterations.
struct_el represents a structuring element, and has the syntax:
colsxrows+anchor_xxanchor_y/shape
cols and rows represent the number of columns and rows of
the structuring element, anchor_x and anchor_y the anchor
point, and shape the shape for the structuring element. shape
must be "rect", "cross", "ellipse", or "custom".
If the value for shape is "custom", it must be followed by a
string of the form "=filename". The file with name
filename is assumed to represent a binary image, with each
printable character corresponding to a bright pixel. When a custom
shape is used, cols and rows are ignored, the number
or columns and rows of the read file are assumed instead.
The default value for struct_el is "3x3+0x0/rect".
nb_iterations specifies the number of times the transform is
applied to the image, and defaults to 1.
Some examples:
# Use the default values
ocv=dilate
# Dilate using a structuring element with a 5x5 cross, iterating two times
ocv=filter_name=dilate:filter_params=5x5+2x2/cross|2
# Read the shape from the file diamond.shape, iterating two times.
# The file diamond.shape may contain a pattern of characters like this
#   *
#  ***
# *****
#  ***
#   *
# The specified columns and rows are ignored
# but the anchor point coordinates are not
ocv=dilate:0x0+2x2/custom=diamond.shape|2
39.182.2 erode
Erode an image by using a specific structuring element.
It corresponds to the libopencv function cvErode.
It accepts the parameters: struct_el:nb_iterations,
with the same syntax and semantics as the dilate filter.
39.182.3 smooth
Smooth the input video.
The filter takes the following parameters:
type|param1|param2|param3|param4.
type is the type of smooth filter to apply, and must be one of
the following values: "blur", "blur_no_scale", "median", "gaussian",
or "bilateral". The default value is "gaussian".
The meaning of param1, param2, param3, and param4
depends on the smooth type. param1 and
param2 accept integer positive values or 0. param3 and
param4 accept floating point values.
The default value for param1 is 3. The default value for the
other parameters is 0.
These parameters correspond to the parameters assigned to the
libopencv function cvSmooth.
39.183 oscilloscope
2D Video Oscilloscope.
Useful to measure spatial impulse, step responses, chroma delays, etc.
It accepts the following parameters:
x
Set scope center x position.
y
Set scope center y position.
s
Set scope size, relative to frame diagonal.
t
Set scope tilt/rotation.
o
Set trace opacity.
tx
Set trace center x position.
ty
Set trace center y position.
tw
Set trace width, relative to width of frame.
th
Set trace height, relative to height of frame.
c
Set which components to trace. By default it traces first three components.
g
Draw trace grid. By default is enabled.
st
Draw some statistics. By default is enabled.
sc
Draw scope. By default is enabled.
39.183.1 Commands
This filter supports same commands as options.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.183.2 Examples
Inspect full first row of video frame.
oscilloscope=x=0.5:y=0:s=1
Inspect full last row of video frame.
oscilloscope=x=0.5:y=1:s=1
Inspect full 5th line of video frame of height 1080.
oscilloscope=x=0.5:y=5/1080:s=1
Inspect full last column of video frame.
oscilloscope=x=1:y=0.5:s=1:t=1
39.184 overlay
Overlay one video on top of another.
It takes two inputs and has one output. The first input is the "main"
video on which the second input is overlaid.
It accepts the following parameters:
A description of the accepted options follows.
x
y
Set the expression for the x and y coordinates of the overlaid video
on the main video. Default value is "0" for both expressions. In case
the expression is invalid, it is set to a huge value (meaning that the
overlay will not be displayed within the output visible area).
eof_action
See framesync.
eval
Set when the expressions for x, and y are evaluated.
It accepts the following values:
‘init’
only evaluate expressions once during the filter initialization or
when a command is processed
‘frame’
evaluate expressions for each incoming frame
Default value is ‘frame’.
shortest
See framesync.
format
Set the format for the output video.
It accepts the following values:
‘yuv420’
force YUV 4:2:0 8-bit planar output
‘yuv420p10’
force YUV 4:2:0 10-bit planar output
‘yuv422’
force YUV 4:2:2 8-bit planar output
‘yuv422p10’
force YUV 4:2:2 10-bit planar output
‘yuv444’
force YUV 4:4:4 8-bit planar output
‘yuv444p10’
force YUV 4:4:4 10-bit planar output
‘rgb’
force RGB 8-bit packed output
‘gbrp’
force RGB 8-bit planar output
‘auto’
automatically pick format
Default value is ‘yuv420’.
repeatlast
See framesync.
alpha
Set format of alpha of the overlaid video, it can be straight or
premultiplied. Default is straight.
The x, and y expressions can contain the following
parameters.
main_w, W
main_h, H
The main input width and height.
overlay_w, w
overlay_h, h
The overlay input width and height.
x
y
The computed values for x and y. They are evaluated for
each new frame.
hsub
vsub
horizontal and vertical chroma subsample values of the output
format. For example for the pixel format "yuv422p" hsub is 2 and
vsub is 1.
n
the number of input frame, starting from 0
pos
the position in the file of the input frame, NAN if unknown; deprecated,
do not use
t
The timestamp, expressed in seconds. It’s NAN if the input timestamp is unknown.
This filter also supports the framesync options.
Note that the n, t variables are available only
when evaluation is done per frame, and will evaluate to NAN
when eval is set to ‘init’.
Be aware that frames are taken from each input video in timestamp
order, hence, if their initial timestamps differ, it is a good idea
to pass the two inputs through a setpts=PTS-STARTPTS filter to
have them begin in the same zero timestamp, as the example for
the movie filter does.
You can chain together more overlays but you should test the
efficiency of such approach.
39.184.1 Commands
This filter supports the following commands:
x
y
Modify the x and y of the overlay input.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.184.2 Examples
Draw the overlay at 10 pixels from the bottom right corner of the main
video:
overlay=main_w-overlay_w-10:main_h-overlay_h-10
Using named options the example above becomes:
overlay=x=main_w-overlay_w-10:y=main_h-overlay_h-10
Insert a transparent PNG logo in the bottom left corner of the input,
using the ffmpeg tool with the -filter_complex option:
ffmpeg -i input -i logo -filter_complex 'overlay=10:main_h-overlay_h-10' output
Insert 2 different transparent PNG logos (second logo on bottom
right corner) using the ffmpeg tool:
ffmpeg -i input -i logo1 -i logo2 -filter_complex 'overlay=x=10:y=H-h-10,overlay=x=W-w-10:y=H-h-10' output
Add a transparent color layer on top of the main video; WxH
must specify the size of the main input to the overlay filter:
[email protected]:size=WxH [over]; [in][over] overlay [out]
Play an original video and a filtered version (here with the deshake
filter) side by side using the ffplay tool:
ffplay input.avi -vf 'split[a][b]; [a]pad=iw*2:ih[src]; [b]deshake[filt]; [src][filt]overlay=w'
The above command is the same as:
ffplay input.avi -vf 'split[b], pad=iw*2[src], [b]deshake, [src]overlay=w'
Make a sliding overlay appearing from the left to the right top part of the
screen starting since time 2:
overlay=x='if(gte(t,2), -w+(t-2)*20, NAN)':y=0
Compose output by putting two input videos side to side:
ffmpeg -i left.avi -i right.avi -filter_complex "
nullsrc=size=200x100 [background];
[0:v] setpts=PTS-STARTPTS, scale=100x100 [left];
[1:v] setpts=PTS-STARTPTS, scale=100x100 [right];
[background][left]       overlay=shortest=1       [background+left];
[background+left][right] overlay=shortest=1:x=100 [left+right]
"
Mask 10-20 seconds of a video by applying the delogo filter to a section
ffmpeg -i test.avi -codec:v:0 wmv2 -ar 11025 -b:v 9000k
-vf '[in]split[split_main][split_delogo];[split_delogo]trim=start=360:end=371,delogo=0:0:640:480[delogoed];[split_main][delogoed]overlay=eof_action=pass[out]'
masked.avi
Chain several overlays in cascade:
nullsrc=s=200x200 [bg];
testsrc=s=100x100, split=4 [in0][in1][in2][in3];
[in0] lutrgb=r=0, [bg]   overlay=0:0     [mid0];
[in1] lutrgb=g=0, [mid0] overlay=100:0   [mid1];
[in2] lutrgb=b=0, [mid1] overlay=0:100   [mid2];
[in3] null,       [mid2] overlay=100:100 [out0]
39.185 overlay_cuda
Overlay one video on top of another.
This is the CUDA variant of the overlay filter.
It only accepts CUDA frames. The underlying input pixel formats have to match.
It takes two inputs and has one output. The first input is the "main"
video on which the second input is overlaid.
It accepts the following parameters:
x
y
Set expressions for the x and y coordinates of the overlaid video
on the main video.
They can contain the following parameters:
main_w, W
main_h, H
The main input width and height.
overlay_w, w
overlay_h, h
The overlay input width and height.
x
y
The computed values for x and y. They are evaluated for
each new frame.
n
The ordinal index of the main input frame, starting from 0.
pos
The byte offset position in the file of the main input frame, NAN if unknown.
Deprecated, do not use.
t
The timestamp of the main input frame, expressed in seconds, NAN if unknown.
Default value is "0" for both expressions.
eval
Set when the expressions for x and y are evaluated.
It accepts the following values:
init
Evaluate expressions once during filter initialization or
when a command is processed.
frame
Evaluate expressions for each incoming frame
Default value is frame.
eof_action
See framesync.
shortest
See framesync.
repeatlast
See framesync.
This filter also supports the framesync options.
39.186 owdenoise
Apply Overcomplete Wavelet denoiser.
The filter accepts the following options:
depth
Set depth.
Larger depth values will denoise lower frequency components more, but
slow down filtering.
Must be an int in the range 8-16, default is 8.
luma_strength, ls
Set luma strength.
Must be a double value in the range 0-1000, default is 1.0.
chroma_strength, cs
Set chroma strength.
Must be a double value in the range 0-1000, default is 1.0.
39.187 pad
Add paddings to the input image, and place the original input at the
provided x, y coordinates.
It accepts the following parameters:
width, w
height, h
Specify an expression for the size of the output image with the
paddings added. If the value for width or height is 0, the
corresponding input size is used for the output.
The width expression can reference the value set by the
height expression, and vice versa.
The default value of width and height is 0.
x
y
Specify the offsets to place the input image at within the padded area,
with respect to the top/left border of the output image.
The x expression can reference the value set by the y
expression, and vice versa.
The default value of x and y is 0.
If x or y evaluate to a negative number, they’ll be changed
so the input image is centered on the padded area.
color
Specify the color of the padded area. For the syntax of this option,
check the (ffmpeg-utils)"Color" section in the ffmpeg-utils
manual.
The default value of color is "black".
eval
Specify when to evaluate  width, height, x and y expression.
It accepts the following values:
‘init’
Only evaluate expressions once during the filter initialization or when
a command is processed.
‘frame’
Evaluate expressions for each incoming frame.
Default value is ‘init’.
aspect
Pad to aspect instead to a resolution.
The value for the width, height, x, and y
options are expressions containing the following constants:
in_w
in_h
The input video width and height.
iw
ih
These are the same as in_w and in_h.
out_w
out_h
The output width and height (the size of the padded area), as
specified by the width and height expressions.
ow
oh
These are the same as out_w and out_h.
x
y
The x and y offsets as specified by the x and y
expressions, or NAN if not yet specified.
a
same as iw / ih
sar
input sample aspect ratio
dar
input display aspect ratio, it is the same as (iw / ih) * sar
hsub
vsub
The horizontal and vertical chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
39.187.1 Examples
Add paddings with the color "violet" to the input video. The output video
size is 640x480, and the top-left corner of the input video is placed at
column 0, row 40
pad=640:480:0:40:violet
The example above is equivalent to the following command:
pad=width=640:height=480:x=0:y=40:color=violet
Pad the input to get an output with dimensions increased by 3/2,
and put the input video at the center of the padded area:
pad="3/2*iw:3/2*ih:(ow-iw)/2:(oh-ih)/2"
Pad the input to get a squared output with size equal to the maximum
value between the input width and height, and put the input video at
the center of the padded area:
pad="max(iw\,ih):ow:(ow-iw)/2:(oh-ih)/2"
Pad the input to get a final w/h ratio of 16:9:
pad="ih*16/9:ih:(ow-iw)/2:(oh-ih)/2"
In case of anamorphic video, in order to set the output display aspect
correctly, it is necessary to use sar in the expression,
according to the relation:
(ih * X / ih) * sar = output_dar
X = output_dar / sar
Thus the previous example needs to be modified to:
pad="ih*16/9/sar:ih:(ow-iw)/2:(oh-ih)/2"
Double the output size and put the input video in the bottom-right
corner of the output padded area:
pad="2*iw:2*ih:ow-iw:oh-ih"
39.188 palettegen
Generate one palette for a whole video stream.
It accepts the following options:
max_colors
Set the maximum number of colors to quantize in the palette.
Note: the palette will still contain 256 colors; the unused palette entries
will be black.
reserve_transparent
Create a palette of 255 colors maximum and reserve the last one for
transparency. Reserving the transparency color is useful for GIF optimization.
If not set, the maximum of colors in the palette will be 256. You probably want
to disable this option for a standalone image.
Set by default.
transparency_color
Set the color that will be used as background for transparency.
stats_mode
Set statistics mode.
It accepts the following values:
‘full’
Compute full frame histograms.
‘diff’
Compute histograms only for the part that differs from previous frame. This
might be relevant to give more importance to the moving part of your input if
the background is static.
‘single’
Compute new histogram for each frame.
Default value is full.
The filter also exports the frame metadata lavfi.color_quant_ratio
(nb_color_in / nb_color_out) which you can use to evaluate the degree of
color quantization of the palette. This information is also visible at
info logging level.
39.188.1 Examples
Generate a representative palette of a given video using ffmpeg:
ffmpeg -i input.mkv -vf palettegen palette.png
39.189 paletteuse
Use a palette to downsample an input video stream.
The filter takes two inputs: one video stream and a palette. The palette must
be a 256 pixels image.
It accepts the following options:
dither
Select dithering mode. Available algorithms are:
‘bayer’
Ordered 8x8 bayer dithering (deterministic)
‘heckbert’
Dithering as defined by Paul Heckbert in 1982 (simple error diffusion).
Note: this dithering is sometimes considered "wrong" and is included as a
reference.
‘floyd_steinberg’
Floyd and Steingberg dithering (error diffusion)
‘sierra2’
Frankie Sierra dithering v2 (error diffusion)
‘sierra2_4a’
Frankie Sierra dithering v2 "Lite" (error diffusion)
‘sierra3’
Frankie Sierra dithering v3 (error diffusion)
‘burkes’
Burkes dithering (error diffusion)
‘atkinson’
Atkinson dithering by Bill Atkinson at Apple Computer (error diffusion)
‘none’
Disable dithering.
Default is sierra2_4a.
bayer_scale
When bayer dithering is selected, this option defines the scale of the
pattern (how much the crosshatch pattern is visible). A low value means more
visible pattern for less banding, and higher value means less visible pattern
at the cost of more banding.
The option must be an integer value in the range [0,5]. Default is 2.
diff_mode
If set, define the zone to process
‘rectangle’
Only the changing rectangle will be reprocessed. This is similar to GIF
cropping/offsetting compression mechanism. This option can be useful for speed
if only a part of the image is changing, and has use cases such as limiting the
scope of the error diffusal dither to the rectangle that bounds the
moving scene (it leads to more deterministic output if the scene doesn’t change
much, and as a result less moving noise and better GIF compression).
Default is none.
new
Take new palette for each output frame.
alpha_threshold
Sets the alpha threshold for transparency. Alpha values above this threshold
will be treated as completely opaque, and values below this threshold will be
treated as completely transparent.
The option must be an integer value in the range [0,255]. Default is 128.
39.189.1 Examples
Use a palette (generated for example with palettegen) to encode a GIF
using ffmpeg:
ffmpeg -i input.mkv -i palette.png -lavfi paletteuse output.gif
39.190 perspective
Correct perspective of video not recorded perpendicular to the screen.
A description of the accepted parameters follows.
x0
y0
x1
y1
x2
y2
x3
y3
Set coordinates expression for top left, top right, bottom left and bottom right corners.
Default values are 0:0:W:0:0:H:W:H with which perspective will remain unchanged.
If the sense option is set to source, then the specified points will be sent
to the corners of the destination. If the sense option is set to destination,
then the corners of the source will be sent to the specified coordinates.
The expressions can use the following variables:
W
H
the width and height of video frame.
in
Input frame count.
on
Output frame count.
interpolation
Set interpolation for perspective correction.
It accepts the following values:
‘linear’
‘cubic’
Default value is ‘linear’.
sense
Set interpretation of coordinate options.
It accepts the following values:
‘0, source’
Send point in the source specified by the given coordinates to
the corners of the destination.
‘1, destination’
Send the corners of the source to the point in the destination specified
by the given coordinates.
Default value is ‘source’.
eval
Set when the expressions for coordinates x0,y0,...x3,y3 are evaluated.
It accepts the following values:
‘init’
only evaluate expressions once during the filter initialization or
when a command is processed
‘frame’
evaluate expressions for each incoming frame
Default value is ‘init’.
39.191 phase
Delay interlaced video by one field time so that the field order changes.
The intended use is to fix PAL movies that have been captured with the
opposite field order to the film-to-video transfer.
A description of the accepted parameters follows.
mode
Set phase mode.
It accepts the following values:
‘t’
Capture field order top-first, transfer bottom-first.
Filter will delay the bottom field.
‘b’
Capture field order bottom-first, transfer top-first.
Filter will delay the top field.
‘p’
Capture and transfer with the same field order. This mode only exists
for the documentation of the other options to refer to, but if you
actually select it, the filter will faithfully do nothing.
‘a’
Capture field order determined automatically by field flags, transfer
opposite.
Filter selects among ‘t’ and ‘b’ modes on a frame by frame
basis using field flags. If no field information is available,
then this works just like ‘u’.
‘u’
Capture unknown or varying, transfer opposite.
Filter selects among ‘t’ and ‘b’ on a frame by frame basis by
analyzing the images and selecting the alternative that produces best
match between the fields.
‘T’
Capture top-first, transfer unknown or varying.
Filter selects among ‘t’ and ‘p’ using image analysis.
‘B’
Capture bottom-first, transfer unknown or varying.
Filter selects among ‘b’ and ‘p’ using image analysis.
‘A’
Capture determined by field flags, transfer unknown or varying.
Filter selects among ‘t’, ‘b’ and ‘p’ using field flags and
image analysis. If no field information is available, then this works just
like ‘U’. This is the default mode.
‘U’
Both capture and transfer unknown or varying.
Filter selects among ‘t’, ‘b’ and ‘p’ using image analysis only.
39.191.1 Commands
This filter supports the all above options as commands.
39.192 photosensitivity
Reduce various flashes in video, so to help users with epilepsy.
It accepts the following options:
frames, f
Set how many frames to use when filtering. Default is 30.
threshold, t
Set detection threshold factor. Default is 1.
Lower is stricter.
skip
Set how many pixels to skip when sampling frames. Default is 1.
Allowed range is from 1 to 1024.
bypass
Leave frames unchanged. Default is disabled.
39.193 pixdesctest
Pixel format descriptor test filter, mainly useful for internal
testing. The output video should be equal to the input video.
For example:
format=monow, pixdesctest
can be used to test the monowhite pixel format descriptor definition.
39.194 pixelize
Apply pixelization to video stream.
The filter accepts the following options:
width, w
height, h
Set block dimensions that will be used for pixelization.
Default value is 16.
mode, m
Set the mode of pixelization used.
Possible values are:
‘avg’
‘min’
‘max’
Default value is avg.
planes, p
Set what planes to filter. Default is to filter all planes.
39.194.1 Commands
This filter supports all options as commands.
39.195 pixscope
Display sample values of color channels. Mainly useful for checking color
and levels. Minimum supported resolution is 640x480.
The filters accept the following options:
x
Set scope X position, relative offset on X axis.
y
Set scope Y position, relative offset on Y axis.
w
Set scope width.
h
Set scope height.
o
Set window opacity. This window also holds statistics about pixel area.
wx
Set window X position, relative offset on X axis.
wy
Set window Y position, relative offset on Y axis.
39.195.1 Commands
This filter supports same commands as options.
39.196 pp
Enable the specified chain of postprocessing subfilters using libpostproc. This
library should be automatically selected with a GPL build (--enable-gpl).
Subfilters must be separated by ’/’ and can be disabled by prepending a ’-’.
Each subfilter and some options have a short and a long name that can be used
interchangeably, i.e. dr/dering are the same.
The filters accept the following options:
subfilters
Set postprocessing subfilters string.
All subfilters share common options to determine their scope:
a/autoq
Honor the quality commands for this subfilter.
c/chrom
Do chrominance filtering, too (default).
y/nochrom
Do luma filtering only (no chrominance).
n/noluma
Do chrominance filtering only (no luma).
These options can be appended after the subfilter name, separated by a ’|’.
Available subfilters are:
hb/hdeblock[|difference[|flatness]]
Horizontal deblocking filter
difference
Difference factor where higher values mean more deblocking (default: 32).
flatness
Flatness threshold where lower values mean more deblocking (default: 39).
vb/vdeblock[|difference[|flatness]]
Vertical deblocking filter
difference
Difference factor where higher values mean more deblocking (default: 32).
flatness
Flatness threshold where lower values mean more deblocking (default: 39).
ha/hadeblock[|difference[|flatness]]
Accurate horizontal deblocking filter
difference
Difference factor where higher values mean more deblocking (default: 32).
flatness
Flatness threshold where lower values mean more deblocking (default: 39).
va/vadeblock[|difference[|flatness]]
Accurate vertical deblocking filter
difference
Difference factor where higher values mean more deblocking (default: 32).
flatness
Flatness threshold where lower values mean more deblocking (default: 39).
The horizontal and vertical deblocking filters share the difference and
flatness values so you cannot set different horizontal and vertical
thresholds.
h1/x1hdeblock
Experimental horizontal deblocking filter
v1/x1vdeblock
Experimental vertical deblocking filter
dr/dering
Deringing filter
tn/tmpnoise[|threshold1[|threshold2[|threshold3]]], temporal noise reducer
threshold1
larger -> stronger filtering
threshold2
larger -> stronger filtering
threshold3
larger -> stronger filtering
al/autolevels[:f/fullyrange], automatic brightness / contrast correction
f/fullyrange
Stretch luma to 0-255.
lb/linblenddeint
Linear blend deinterlacing filter that deinterlaces the given block by
filtering all lines with a (1 2 1) filter.
li/linipoldeint
Linear interpolating deinterlacing filter that deinterlaces the given block by
linearly interpolating every second line.
ci/cubicipoldeint
Cubic interpolating deinterlacing filter deinterlaces the given block by
cubically interpolating every second line.
md/mediandeint
Median deinterlacing filter that deinterlaces the given block by applying a
median filter to every second line.
fd/ffmpegdeint
FFmpeg deinterlacing filter that deinterlaces the given block by filtering every
second line with a (-1 4 2 4 -1) filter.
l5/lowpass5
Vertically applied FIR lowpass deinterlacing filter that deinterlaces the given
block by filtering all lines with a (-1 2 6 2 -1) filter.
fq/forceQuant[|quantizer]
Overrides the quantizer table from the input with the constant quantizer you
specify.
quantizer
Quantizer to use
de/default
Default pp filter combination (hb|a,vb|a,dr|a)
fa/fast
Fast pp filter combination (h1|a,v1|a,dr|a)
ac
High quality pp filter combination (ha|a|128|7,va|a,dr|a)
39.196.1 Examples
Apply horizontal and vertical deblocking, deringing and automatic
brightness/contrast:
pp=hb/vb/dr/al
Apply default filters without brightness/contrast correction:
pp=de/-al
Apply default filters and temporal denoiser:
pp=default/tmpnoise|1|2|3
Apply deblocking on luma only, and switch vertical deblocking on or off
automatically depending on available CPU time:
pp=hb|y/vb|a
39.197 pp7
Apply Postprocessing filter 7. It is variant of the spp filter,
similar to spp = 6 with 7 point DCT, where only the center sample is
used after IDCT.
The filter accepts the following options:
qp
Force a constant quantization parameter. It accepts an integer in range
0 to 63. If not set, the filter will use the QP from the video stream
(if available).
mode
Set thresholding mode. Available modes are:
‘hard’
Set hard thresholding.
‘soft’
Set soft thresholding (better de-ringing effect, but likely blurrier).
‘medium’
Set medium thresholding (good results, default).
39.198 premultiply
Apply alpha premultiply effect to input video stream using first plane
of second stream as alpha.
Both streams must have same dimensions and same pixel format.
The filter accepts the following option:
planes
Set which planes will be processed, unprocessed planes will be copied.
By default value 0xf, all planes will be processed.
inplace
Do not require 2nd input for processing, instead use alpha plane from input stream.
39.199 prewitt
Apply prewitt operator to input video stream.
The filter accepts the following option:
planes
Set which planes will be processed, unprocessed planes will be copied.
By default value 0xf, all planes will be processed.
scale
Set value which will be multiplied with filtered result.
delta
Set value which will be added to filtered result.
39.199.1 Commands
This filter supports the all above options as commands.
39.200 pseudocolor
Alter frame colors in video with pseudocolors.
This filter accepts the following options:
c0
set pixel first component expression
c1
set pixel second component expression
c2
set pixel third component expression
c3
set pixel fourth component expression, corresponds to the alpha component
index, i
set component to use as base for altering colors
preset, p
Pick one of built-in LUTs. By default is set to none.
Available LUTs:
‘magma’
‘inferno’
‘plasma’
‘viridis’
‘turbo’
‘cividis’
‘range1’
‘range2’
‘shadows’
‘highlights’
‘solar’
‘nominal’
‘preferred’
‘total’
‘spectral’
‘cool’
‘heat’
‘fiery’
‘blues’
‘green’
‘helix’
opacity
Set opacity of output colors. Allowed range is from 0 to 1.
Default value is set to 1.
Each of the expression options specifies the expression to use for computing
the lookup table for the corresponding pixel component values.
The expressions can contain the following constants and functions:
w
h
The input width and height.
val
The input value for the pixel component.
ymin, umin, vmin, amin
The minimum allowed component value.
ymax, umax, vmax, amax
The maximum allowed component value.
All expressions default to "val".
39.200.1 Commands
This filter supports the all above options as commands.
39.200.2 Examples
Change too high luma values to gradient:
pseudocolor="'if(between(val,ymax,amax),lerp(ymin,ymax,(val-ymax)/(amax-ymax)),-1):if(between(val,ymax,amax),lerp(umax,umin,(val-ymax)/(amax-ymax)),-1):if(between(val,ymax,amax),lerp(vmin,vmax,(val-ymax)/(amax-ymax)),-1):-1'"
39.201 psnr
Obtain the average, maximum and minimum PSNR (Peak Signal to Noise
Ratio) between two input videos.
This filter takes in input two input videos, the first input is
considered the "main" source and is passed unchanged to the
output. The second input is used as a "reference" video for computing
the PSNR.
Both video inputs must have the same resolution and pixel format for
this filter to work correctly. Also it assumes that both inputs
have the same number of frames, which are compared one by one.
The obtained average PSNR is printed through the logging system.
The filter stores the accumulated MSE (mean squared error) of each
frame, and at the end of the processing it is averaged across all frames
equally, and the following formula is applied to obtain the PSNR:
PSNR = 10*log10(MAX^2/MSE)
Where MAX is the average of the maximum values of each component of the
image.
The description of the accepted parameters follows.
stats_file, f
If specified the filter will use the named file to save the PSNR of
each individual frame. When filename equals "-" the data is sent to
standard output.
stats_version
Specifies which version of the stats file format to use. Details of
each format are written below.
Default value is 1.
stats_add_max
Determines whether the max value is output to the stats log.
Default value is 0.
Requires stats_version >= 2. If this is set and stats_version < 2,
the filter will return an error.
This filter also supports the framesync options.
The file printed if stats_file is selected, contains a sequence of
key/value pairs of the form key:value for each compared
couple of frames.
If a stats_version greater than 1 is specified, a header line precedes
the list of per-frame-pair stats, with key value pairs following the frame
format with the following parameters:
psnr_log_version
The version of the log file format. Will match stats_version.
fields
A comma separated list of the per-frame-pair parameters included in
the log.
A description of each shown per-frame-pair parameter follows:
n
sequential number of the input frame, starting from 1
mse_avg
Mean Square Error pixel-by-pixel average difference of the compared
frames, averaged over all the image components.
mse_y, mse_u, mse_v, mse_r, mse_g, mse_b, mse_a
Mean Square Error pixel-by-pixel average difference of the compared
frames for the component specified by the suffix.
psnr_y, psnr_u, psnr_v, psnr_r, psnr_g, psnr_b, psnr_a
Peak Signal to Noise ratio of the compared frames for the component
specified by the suffix.
max_avg, max_y, max_u, max_v
Maximum allowed value for each channel, and average over all
channels.
39.201.1 Examples
For example:
movie=ref_movie.mpg, setpts=PTS-STARTPTS [main];
[main][ref] psnr="stats_file=stats.log" [out]
On this example the input file being processed is compared with the
reference file ref_movie.mpg. The PSNR of each individual frame
is stored in stats.log.
Another example with different containers:
ffmpeg -i main.mpg -i ref.mkv -lavfi  "[0:v]settb=AVTB,setpts=PTS-STARTPTS[main];[1:v]settb=AVTB,setpts=PTS-STARTPTS[ref];[main][ref]psnr" -f null -
39.202 pullup
Pulldown reversal (inverse telecine) filter, capable of handling mixed
hard-telecine, 24000/1001 fps progressive, and 30000/1001 fps progressive
content.
The pullup filter is designed to take advantage of future context in making
its decisions. This filter is stateless in the sense that it does not lock
onto a pattern to follow, but it instead looks forward to the following
fields in order to identify matches and rebuild progressive frames.
To produce content with an even framerate, insert the fps filter after
pullup, use fps=24000/1001 if the input frame rate is 29.97fps,
fps=24 for 30fps and the (rare) telecined 25fps input.
The filter accepts the following options:
jl
jr
jt
jb
These options set the amount of "junk" to ignore at the left, right, top, and
bottom of the image, respectively. Left and right are in units of 8 pixels,
while top and bottom are in units of 2 lines.
The default is 8 pixels on each side.
sb
Set the strict breaks. Setting this option to 1 will reduce the chances of
filter generating an occasional mismatched frame, but it may also cause an
excessive number of frames to be dropped during high motion sequences.
Conversely, setting it to -1 will make filter match fields more easily.
This may help processing of video where there is slight blurring between
the fields, but may also cause there to be interlaced frames in the output.
Default value is 0.
mp
Set the metric plane to use. It accepts the following values:
‘l’
Use luma plane.
‘u’
Use chroma blue plane.
‘v’
Use chroma red plane.
This option may be set to use chroma plane instead of the default luma plane
for doing filter’s computations. This may improve accuracy on very clean
source material, but more likely will decrease accuracy, especially if there
is chroma noise (rainbow effect) or any grayscale video.
The main purpose of setting mp to a chroma plane is to reduce CPU
load and make pullup usable in realtime on slow machines.
For best results (without duplicated frames in the output file) it is
necessary to change the output frame rate. For example, to inverse
telecine NTSC input:
ffmpeg -i input -vf pullup -r 24000/1001 ...
39.203 qp
Change video quantization parameters (QP).
The filter accepts the following option:
qp
Set expression for quantization parameter.
The expression is evaluated through the eval API and can contain, among others,
the following constants:
known
1 if index is not 129, 0 otherwise.
qp
Sequential index starting from -129 to 128.
39.203.1 Examples
Some equation like:
qp=2+2*sin(PI*qp)
39.204 qrencode
Generate a QR code using the libqrencode library (see
https://fukuchi.org/works/qrencode/), and overlay it on top of the current
frame.
To enable the compilation of this filter, you need to configure FFmpeg with
--enable-libqrencode.
The QR code is generated from the provided text or text pattern. The
corresponding QR code is scaled and overlayed into the video output according to
the specified options.
In case no text is specified, no QR code is overlaied.
This filter accepts the following options:
qrcode_width, q
padded_qrcode_width, Q
Specify an expression for the width of the rendered QR code, with and without
padding. The qrcode_width expression can reference the value set by the
padded_qrcode_width expression, and vice versa.
By default padded_qrcode_width is set to qrcode_width, meaning that
there is no padding.
These expressions are evaluated for each new frame.
See the qrencode Expressions section for details.
x
y
Specify an expression for positioning the padded QR code top-left corner.  The
x expression can reference the value set by the y expression, and
vice.
By default x and y are set set to 0, meaning that the QR code
is placed in the top left corner of the input.
These expressions are evaluated for each new frame.
See the qrencode Expressions section for details.
case_sensitive, cs
Instruct libqrencode to use case sensitive encoding. This is enabled by
default. This can be disabled to reduce the QR encoding size.
level, l
Specify the QR encoding error correction level. With an higher correction level,
the encoding size will increase but the code will be more robust to corruption.
Lower level is L.
It accepts the following values:
‘L’
‘M’
‘Q’
‘H’
expansion
Select how the input text is expanded. Can be either none, or
normal (default). See the qrencode Text expansion
section below for details.
text
textfile
Define the text to be rendered. In case neither is specified, no QR is encoded
(just an empty colored frame).
In case expansion is enabled, the text is treated as a text template, using the
qrencode expansion mechanism. See the qrencode
Text expansion section below for details.
background_color, bc
foreground_color, fc
Set the QR code and background color. The default value of
foreground_color is "black", the default value of background_color
is "white".
For the syntax of the color options, check the (ffmpeg-utils)"Color"
section in the ffmpeg-utils manual.
39.204.1 qrencode Expressions
The expressions set by the options contain the following constants and functions.
dar
input display aspect ratio, it is the same as (w / h) * sar
duration
the current frame’s duration, in seconds
hsub
vsub
horizontal and vertical chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
main_h, H
the input height
main_w, W
the input width
n
the number of input frame, starting from 0
pict_type
a number representing the picture type
qr_w, w
the width of the encoded QR code
rendered_qr_w, q
rendered_padded_qr_w, Q
the width of the rendered QR code, without and without padding.
These parameters allow the q and Q expressions to refer to each
other, so you can for example specify q=3/4*Q.
rand(min, max)
return a random number included between min and max
sar
the input sample aspect ratio
t
timestamp expressed in seconds, NAN if the input timestamp is unknown
x
y
the x and y offset coordinates where the text is drawn.
These parameters allow the x and y expressions to refer to each
other, so you can for example specify y=x/dar.
39.204.2 qrencode Text expansion
If expansion is set to none, the text is printed verbatim.
If expansion is set to normal (which is the default),
the following expansion mechanism is used.
The backslash character ‘\’, followed by any character, always expands to
the second character.
Sequences of the form %{...} are expanded. The text between the
braces is a function name, possibly followed by arguments separated by ’:’.
If the arguments contain special characters or delimiters (’:’ or ’}’),
they should be escaped.
Note that they probably must also be escaped as the value for the text
option in the filter argument string and as the filter argument in the
filtergraph description, and possibly also for the shell, that makes up to four
levels of escaping; using a text file with the textfile option avoids
these problems.
The following functions are available:
n, frame_num
return the frame number
pts
Return the presentation timestamp of the current frame.
It can take up to two arguments.
The first argument is the format of the timestamp; it defaults to flt for
seconds as a decimal number with microsecond accuracy; hms stands for a
formatted [-]HH:MM:SS.mmm timestamp with millisecond accuracy.
gmtime stands for the timestamp of the frame formatted as UTC time;
localtime stands for the timestamp of the frame formatted as local time
zone time. If the format is set to hms24hh, the time is formatted in 24h
format (00-23).
The second argument is an offset added to the timestamp.
If the format is set to localtime or gmtime, a third argument may
be supplied: a strftime C function format string. By default,
YYYY-MM-DD HH:MM:SS format will be used.
expr, e
Evaluate the expression’s value and output as a double.
It must take one argument specifying the expression to be evaluated, accepting
the constants and functions defined in qrencode_expressions.
expr_formatted, ef
Evaluate the expression’s value and output as a formatted string.
The first argument is the expression to be evaluated, just as for the expr function.
The second argument specifies the output format. Allowed values are ‘x’,
‘X’, ‘d’ and ‘u’. They are treated exactly as in the
printf function.
The third parameter is optional and sets the number of positions taken by the output.
It can be used to add padding with zeros from the left.
gmtime
The time at which the filter is running, expressed in UTC.
It can accept an argument: a strftime C function format string.
The format string is extended to support the variable %[1-6]N
which prints fractions of the second with optionally specified number of digits.
localtime
The time at which the filter is running, expressed in the local time zone.
It can accept an argument: a strftime C function format string.
The format string is extended to support the variable %[1-6]N
which prints fractions of the second with optionally specified number of digits.
metadata
Frame metadata. Takes one or two arguments.
The first argument is mandatory and specifies the metadata key.
The second argument is optional and specifies a default value, used when the
metadata key is not found or empty.
Available metadata can be identified by inspecting entries starting with TAG
included within each frame section printed by running ffprobe
-show_frames.
String metadata generated in filters leading to the qrencode filter are also
available.
rand(min, max)
return a random number included between min and max
39.204.3 Examples
Generate a QR code encoding the specified text with the default size, overalaid
in the top left corner of the input video, with the default size:
qrencode=text=www.ffmpeg.org
Same as below, but select blue on pink colors:
qrencode=text=www.ffmpeg.org:[email protected]:fc=blue
Place the QR code in the bottom right corner of the input video:
qrencode=text=www.ffmpeg.org:x=W-Q:y=H-Q
Generate a QR code with width of 200 pixels and padding, making the padded width
4/3 of the QR code width:
qrencode=text=www.ffmpeg.org:q=200:Q=4/3*q
Generate a QR code with padded width of 200 pixels and padding, making the QR
code width 3/4 of the padded width:
qrencode=text=www.ffmpeg.org:Q=200:q=3/4*Q
Make the QR code a fraction of the input video width:
qrencode=text=www.ffmpeg.org:q=W/5
Generate a QR code encoding the frame number:
qrencode=text=%{n}
Generate a QR code encoding the GMT timestamp:
qrencode=text=%{gmtime}
Generate a QR code encoding the timestamp expressed as a float:
qrencode=text=%{pts}
39.205 quirc
Identify and decode a QR code using the libquirc library (see
https://github.com/dlbeer/quirc/), and print the identified QR codes
positions and payload as metadata.
To enable the compilation of this filter, you need to configure FFmpeg with
--enable-libquirc.
For each found QR code in the input video, some metadata entries are added with
the prefix lavfi.quirc.N, where N is the index, starting from 0,
associated to the QR code.
A description of each metadata value follows:
lavfi.quirc.count
the number of found QR codes, it is not set in case none was found
lavfi.quirc.N.corner.M.x
lavfi.quirc.N.coreer.M.y
the x/y positions of the four corners of the square containing the QR code,
where M is the index of the corner starting from 0
lavfi.quirc.N.payload
the payload of the QR code
39.206 random
Flush video frames from internal cache of frames into a random order.
No frame is discarded.
Inspired by frei0r nervous filter.
frames
Set size in number of frames of internal cache, in range from 2 to
512. Default is 30.
seed
Set seed for random number generator, must be an integer included between
0 and UINT32_MAX. If not specified, or if explicitly set to
less than 0, the filter will try to use a good random seed on a
best effort basis.
39.207 readeia608
Read closed captioning (EIA-608) information from the top lines of a video frame.
This filter adds frame metadata for lavfi.readeia608.X.cc and
lavfi.readeia608.X.line, where X is the number of the identified line
with EIA-608 data (starting from 0). A description of each metadata value follows:
lavfi.readeia608.X.cc
The two bytes stored as EIA-608 data (printed in hexadecimal).
lavfi.readeia608.X.line
The number of the line on which the EIA-608 data was identified and read.
This filter accepts the following options:
scan_min
Set the line to start scanning for EIA-608 data. Default is 0.
scan_max
Set the line to end scanning for EIA-608 data. Default is 29.
spw
Set the ratio of width reserved for sync code detection.
Default is 0.27. Allowed range is [0.1 - 0.7].
chp
Enable checking the parity bit. In the event of a parity error, the filter will output
0x00 for that character. Default is false.
lp
Lowpass lines prior to further processing. Default is enabled.
39.207.1 Commands
This filter supports the all above options as commands.
39.207.2 Examples
Output a csv with presentation time and the first two lines of identified EIA-608 captioning data.
ffprobe -f lavfi -i movie=captioned_video.mov,readeia608 -show_entries frame=pts_time:frame_tags=lavfi.readeia608.0.cc,lavfi.readeia608.1.cc -of csv
39.208 readvitc
Read vertical interval timecode (VITC) information from the top lines of a
video frame.
The filter adds frame metadata key lavfi.readvitc.tc_str with the
timecode value, if a valid timecode has been detected. Further metadata key
lavfi.readvitc.found is set to 0/1 depending on whether
timecode data has been found or not.
This filter accepts the following options:
scan_max
Set the maximum number of lines to scan for VITC data. If the value is set to
-1 the full video frame is scanned. Default is 45.
thr_b
Set the luma threshold for black. Accepts float numbers in the range [0.0,1.0],
default value is 0.2. The value must be equal or less than thr_w.
thr_w
Set the luma threshold for white. Accepts float numbers in the range [0.0,1.0],
default value is 0.6. The value must be equal or greater than thr_b.
39.208.1 Examples
Detect and draw VITC data onto the video frame; if no valid VITC is detected,
draw --:--:--:-- as a placeholder:
ffmpeg -i input.avi -filter:v 'readvitc,drawtext=fontfile=FreeMono.ttf:text=%{metadata\\:lavfi.readvitc.tc_str\\:--\\\\\\:--\\\\\\:--\\\\\\:--}:x=(w-tw)/2:y=400-ascent'
39.209 remap
Remap pixels using 2nd: Xmap and 3rd: Ymap input video stream.
Destination pixel at position (X, Y) will be picked from source (x, y) position
where x = Xmap(X, Y) and y = Ymap(X, Y). If mapping values are out of range, zero
value for pixel will be used for destination pixel.
Xmap and Ymap input video streams must be of same dimensions. Output video stream
will have Xmap/Ymap video stream dimensions.
Xmap and Ymap input video streams are 16bit depth, single channel.
format
Specify pixel format of output from this filter. Can be color or gray.
Default is color.
fill
Specify the color of the unmapped pixels. For the syntax of this option,
check the (ffmpeg-utils)"Color" section in the ffmpeg-utils
manual. Default color is black.
39.210 removegrain
The removegrain filter is a spatial denoiser for progressive video.
m0
Set mode for the first plane.
m1
Set mode for the second plane.
m2
Set mode for the third plane.
m3
Set mode for the fourth plane.
Range of mode is from 0 to 24. Description of each mode follows:
0
Leave input plane unchanged. Default.
1
Clips the pixel with the minimum and maximum of the 8 neighbour pixels.
2
Clips the pixel with the second minimum and maximum of the 8 neighbour pixels.
3
Clips the pixel with the third minimum and maximum of the 8 neighbour pixels.
4
Clips the pixel with the fourth minimum and maximum of the 8 neighbour pixels.
This is equivalent to a median filter.
5
Line-sensitive clipping giving the minimal change.
6
Line-sensitive clipping, intermediate.
7
Line-sensitive clipping, intermediate.
8
Line-sensitive clipping, intermediate.
9
Line-sensitive clipping on a line where the neighbours pixels are the closest.
10
Replaces the target pixel with the closest neighbour.
11
[1 2 1] horizontal and vertical kernel blur.
12
Same as mode 11.
13
Bob mode, interpolates top field from the line where the neighbours
pixels are the closest.
14
Bob mode, interpolates bottom field from the line where the neighbours
pixels are the closest.
15
Bob mode, interpolates top field. Same as 13 but with a more complicated
interpolation formula.
16
Bob mode, interpolates bottom field. Same as 14 but with a more complicated
interpolation formula.
17
Clips the pixel with the minimum and maximum of respectively the maximum and
minimum of each pair of opposite neighbour pixels.
18
Line-sensitive clipping using opposite neighbours whose greatest distance from
the current pixel is minimal.
19
Replaces the pixel with the average of its 8 neighbours.
20
Averages the 9 pixels ([1 1 1] horizontal and vertical blur).
21
Clips pixels using the averages of opposite neighbour.
22
Same as mode 21 but simpler and faster.
23
Small edge and halo removal, but reputed useless.
24
Similar as 23.
39.211 removelogo
Suppress a TV station logo, using an image file to determine which
pixels comprise the logo. It works by filling in the pixels that
comprise the logo with neighboring pixels.
The filter accepts the following options:
filename, f
Set the filter bitmap file, which can be any image format supported by
libavformat. The width and height of the image file must match those of the
video stream being processed.
Pixels in the provided bitmap image with a value of zero are not
considered part of the logo, non-zero pixels are considered part of
the logo. If you use white (255) for the logo and black (0) for the
rest, you will be safe. For making the filter bitmap, it is
recommended to take a screen capture of a black frame with the logo
visible, and then using a threshold filter followed by the erode
filter once or twice.
If needed, little splotches can be fixed manually. Remember that if
logo pixels are not covered, the filter quality will be much
reduced. Marking too many pixels as part of the logo does not hurt as
much, but it will increase the amount of blurring needed to cover over
the image and will destroy more information than necessary, and extra
pixels will slow things down on a large logo.
39.212 repeatfields
This filter uses the repeat_field flag from the Video ES headers and hard repeats
fields based on its value.
39.213 reverse
Reverse a video clip.
Warning: This filter requires memory to buffer the entire clip, so trimming
is suggested.
39.213.1 Examples
Take the first 5 seconds of a clip, and reverse it.
trim=end=5,reverse
39.214 rgbashift
Shift R/G/B/A pixels horizontally and/or vertically.
The filter accepts the following options:
rh
Set amount to shift red horizontally.
rv
Set amount to shift red vertically.
gh
Set amount to shift green horizontally.
gv
Set amount to shift green vertically.
bh
Set amount to shift blue horizontally.
bv
Set amount to shift blue vertically.
ah
Set amount to shift alpha horizontally.
av
Set amount to shift alpha vertically.
edge
Set edge mode, can be smear, default, or warp.
39.214.1 Commands
This filter supports the all above options as commands.
39.215 roberts
Apply roberts cross operator to input video stream.
The filter accepts the following option:
planes
Set which planes will be processed, unprocessed planes will be copied.
By default value 0xf, all planes will be processed.
scale
Set value which will be multiplied with filtered result.
delta
Set value which will be added to filtered result.
39.215.1 Commands
This filter supports the all above options as commands.
39.216 rotate
Rotate video by an arbitrary angle expressed in radians.
The filter accepts the following options:
A description of the optional parameters follows.
angle, a
Set an expression for the angle by which to rotate the input video
clockwise, expressed as a number of radians. A negative value will
result in a counter-clockwise rotation. By default it is set to "0".
This expression is evaluated for each frame.
out_w, ow
Set the output width expression, default value is "iw".
This expression is evaluated just once during configuration.
out_h, oh
Set the output height expression, default value is "ih".
This expression is evaluated just once during configuration.
bilinear
Enable bilinear interpolation if set to 1, a value of 0 disables
it. Default value is 1.
fillcolor, c
Set the color used to fill the output area not covered by the rotated
image. For the general syntax of this option, check the
(ffmpeg-utils)"Color" section in the ffmpeg-utils manual.
If the special value "none" is selected then no
background is printed (useful for example if the background is never shown).
Default value is "black".
The expressions for the angle and the output size can contain the
following constants and functions:
n
sequential number of the input frame, starting from 0. It is always NAN
before the first frame is filtered.
t
time in seconds of the input frame, it is set to 0 when the filter is
configured. It is always NAN before the first frame is filtered.
hsub
vsub
horizontal and vertical chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
in_w, iw
in_h, ih
the input video width and height
out_w, ow
out_h, oh
the output width and height, that is the size of the padded area as
specified by the width and height expressions
rotw(a)
roth(a)
the minimal width/height required for completely containing the input
video rotated by a radians.
These are only available when computing the out_w and
out_h expressions.
39.216.1 Examples
Rotate the input by PI/6 radians clockwise:
rotate=PI/6
Rotate the input by PI/6 radians counter-clockwise:
rotate=-PI/6
Rotate the input by 45 degrees clockwise:
rotate=45*PI/180
Apply a constant rotation with period T, starting from an angle of PI/3:
rotate=PI/3+2*PI*t/T
Make the input video rotation oscillating with a period of T
seconds and an amplitude of A radians:
rotate=A*sin(2*PI/T*t)
Rotate the video, output size is chosen so that the whole rotating
input video is always completely contained in the output:
rotate='2*PI*t:ow=hypot(iw,ih):oh=ow'
Rotate the video, reduce the output size so that no background is ever
shown:
rotate=2*PI*t:ow='min(iw,ih)/sqrt(2)':oh=ow:c=none
39.216.2 Commands
The filter supports the following commands:
a, angle
Set the angle expression.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.217 sab
Apply Shape Adaptive Blur.
The filter accepts the following options:
luma_radius, lr
Set luma blur filter strength, must be a value in range 0.1-4.0, default
value is 1.0. A greater value will result in a more blurred image, and
in slower processing.
luma_pre_filter_radius, lpfr
Set luma pre-filter radius, must be a value in the 0.1-2.0 range, default
value is 1.0.
luma_strength, ls
Set luma maximum difference between pixels to still be considered, must
be a value in the 0.1-100.0 range, default value is 1.0.
chroma_radius, cr
Set chroma blur filter strength, must be a value in range -0.9-4.0. A
greater value will result in a more blurred image, and in slower
processing.
chroma_pre_filter_radius, cpfr
Set chroma pre-filter radius, must be a value in the -0.9-2.0 range.
chroma_strength, cs
Set chroma maximum difference between pixels to still be considered,
must be a value in the -0.9-100.0 range.
Each chroma option value, if not explicitly specified, is set to the
corresponding luma option value.
39.218 scale
Scale (resize) the input video, using the libswscale library.
The scale filter forces the output display aspect ratio to be the same
of the input, by changing the output sample aspect ratio.
If the input image format is different from the format requested by
the next filter, the scale filter will convert the input to the
requested format.
39.218.1 Options
The filter accepts the following options, any of the options supported
by the libswscale scaler, as well as any of the framesync options.
See (ffmpeg-scaler)the ffmpeg-scaler manual for
the complete list of scaler options.
width, w
height, h
Set the output video dimension expression. Default value is the input
dimension.
If the width or w value is 0, the input width is used for
the output. If the height or h value is 0, the input height
is used for the output.
If one and only one of the values is -n with n >= 1, the scale filter
will use a value that maintains the aspect ratio of the input image,
calculated from the other specified dimension. After that it will,
however, make sure that the calculated dimension is divisible by n and
adjust the value if necessary.
If both values are -n with n >= 1, the behavior will be identical to
both values being set to 0 as previously detailed.
See below for the list of accepted constants for use in the dimension
expression.
eval
Specify when to evaluate width and height expression. It accepts the following values:
‘init’
Only evaluate expressions once during the filter initialization or when a command is processed.
‘frame’
Evaluate expressions for each incoming frame.
Default value is ‘init’.
interl
Set the interlacing mode. It accepts the following values:
‘1’
Force interlaced aware scaling.
‘0’
Do not apply interlaced scaling.
‘-1’
Select interlaced aware scaling depending on whether the source frames
are flagged as interlaced or not.
Default value is ‘0’.
flags
Set libswscale scaling flags. See
(ffmpeg-scaler)the ffmpeg-scaler manual for the
complete list of values. If not explicitly specified the filter applies
the default flags.
param0, param1
Set libswscale input parameters for scaling algorithms that need them. See
(ffmpeg-scaler)the ffmpeg-scaler manual for the
complete documentation. If not explicitly specified the filter applies
empty parameters.
intent
Set the ICC rendering intent to use when transforming between different color
spaces. It accepts the following values:
‘perceptual’
Use a perceptually guided tone and gamut mapping curve. The exact details of
the mapping used may change at any time and should not be relied on as stable.
This intent is recommended for final viewing of image/video content in typical
viewing settings.
‘relative_colorimetric’
Statically clip out-of-gamut colors using a colorimetric clipping curve which
attempts to find the colorimetrically least dissimilar in-gamut color. This
intent performs white point adaptation and black point adaptation. This is
the default. This intent is recommended wherever faithful color reproduction
is of the utmost importance, even at the cost of clipping.
‘absolute_colorimetric’
Hard clip out-of-gamut colors with no attempt at white or black point
reproduction. This intent will reproduce in-gamut colors 1:1 on the output
display as they would appear on the reference display, assuming the output
display is appropriately calibrated.
‘saturation’
Performs saturation mapping - that is, stretches the input color volume
directly onto the output color volume, in non-linear fashion that preserves the
original signal appearance as much as possible. This intent is recommended for
signal content evaluation, as it will not lead to any clipping. It is roughly
analogous to not performing any color mapping, although it still takes into
account the mastering display primaries and any differences in encoding TRC.
size, s
Set the video size. For the syntax of this option, check the
(ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.
in_color_matrix
out_color_matrix
Set in/output YCbCr color space type.
This allows the autodetected value to be overridden as well as allows forcing
a specific value used for the output and encoder.
If not specified, the color space type depends on the pixel format.
Possible values:
‘auto’
Choose automatically.
‘bt709’
Format conforming to International Telecommunication Union (ITU)
Recommendation BT.709.
‘fcc’
Set color space conforming to the United States Federal Communications
Commission (FCC) Code of Federal Regulations (CFR) Title 47 (2003) 73.682 (a).
‘bt601’
‘bt470’
‘smpte170m’
Set color space conforming to:
ITU Radiocommunication Sector (ITU-R) Recommendation BT.601
ITU-R Rec. BT.470-6 (1998) Systems B, B1, and G
Society of Motion Picture and Television Engineers (SMPTE) ST 170:2004
‘smpte240m’
Set color space conforming to SMPTE ST 240:1999.
‘bt2020’
Set color space conforming to ITU-R BT.2020 non-constant luminance system.
in_range
out_range
Set in/output YCbCr sample range.
This allows the autodetected value to be overridden as well as allows forcing
a specific value used for the output and encoder. If not specified, the
range depends on the pixel format. Possible values:
‘auto/unknown’
Choose automatically.
‘jpeg/full/pc’
Set full range (0-255 in case of 8-bit luma).
‘mpeg/limited/tv’
Set "MPEG" range (16-235 in case of 8-bit luma).
in_chroma_loc
out_chroma_loc
Set in/output chroma sample location. If not specified, center-sited chroma
is used by default. Possible values:
‘auto, unknown’
‘left’
‘center’
‘topleft’
‘top’
‘bottomleft’
‘bottom’
in_primaries
out_primaries
Set in/output RGB primaries.
This allows the autodetected value to be overridden as well as allows forcing
a specific value used for the output and encoder. Possible values:
‘auto’
Choose automatically. This is the default.
‘bt709’
‘bt470m’
‘bt470bg’
‘smpte170m’
‘smpte240m’
‘film’
‘bt2020’
‘smpte428’
‘smpte431’
‘smpte432’
‘jedec-p22’
‘ebu3213’
in_transfer
out_transfer
Set in/output transfer response curve (TRC).
This allows the autodetected value to be overridden as well as allows forcing
a specific value used for the output and encoder. Possible values:
‘auto’
Choose automatically. This is the default.
‘bt709’
‘bt470m’
‘gamma22’
‘bt470bg’
‘gamma28’
‘smpte170m’
‘smpte240m’
‘linear’
‘iec61966-2-1’
‘srgb’
‘iec61966-2-4’
‘xvycc’
‘bt1361e’
‘bt2020-10’
‘bt2020-12’
‘smpte2084’
‘smpte428’
‘arib-std-b67’
force_original_aspect_ratio
Enable decreasing or increasing output video width or height if necessary to
keep the original aspect ratio. Possible values:
‘disable’
Scale the video as specified and disable this feature.
‘decrease’
The output video dimensions will automatically be decreased if needed.
‘increase’
The output video dimensions will automatically be increased if needed.
One useful instance of this option is that when you know a specific device’s
maximum allowed resolution, you can use this to limit the output video to
that, while retaining the aspect ratio. For example, device A allows
1280x720 playback, and your video is 1920x800. Using this option (set it to
decrease) and specifying 1280x720 to the command line makes the output
1280x533.
Please note that this is a different thing than specifying -1 for w
or h, you still need to specify the output resolution for this option
to work.
force_divisible_by
Ensures that both the output dimensions, width and height, are divisible by the
given integer when used together with force_original_aspect_ratio. This
works similar to using -n in the w and h options.
This option respects the value set for force_original_aspect_ratio,
increasing or decreasing the resolution accordingly. The video’s aspect ratio
may be slightly modified.
This option can be handy if you need to have a video fit within or exceed
a defined resolution using force_original_aspect_ratio but also have
encoder restrictions on width or height divisibility.
The values of the w and h options are expressions
containing the following constants:
in_w
in_h
The input width and height
iw
ih
These are the same as in_w and in_h.
out_w
out_h
The output (scaled) width and height
ow
oh
These are the same as out_w and out_h
a
The same as iw / ih
sar
input sample aspect ratio
dar
The input display aspect ratio. Calculated from (iw / ih) * sar.
hsub
vsub
horizontal and vertical input chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
ohsub
ovsub
horizontal and vertical output chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
n
The (sequential) number of the input frame, starting from 0.
Only available with eval=frame.
t
The presentation timestamp of the input frame, expressed as a number of
seconds. Only available with eval=frame.
pos
The position (byte offset) of the frame in the input stream, or NaN if
this information is unavailable and/or meaningless (for example in case of synthetic video).
Only available with eval=frame.
Deprecated, do not use.
ref_w, rw
ref_h, rh
ref_a
ref_dar, rdar
ref_n
ref_t
ref_pos
Eqvuialent to the above, but for a second reference input. If any of these
variables are present, this filter accepts two inputs.
39.218.2 Examples
Scale the input video to a size of 200x100
scale=w=200:h=100
This is equivalent to:
scale=200:100
or:
scale=200x100
Specify a size abbreviation for the output size:
scale=qcif
which can also be written as:
scale=size=qcif
Scale the input to 2x:
scale=w=2*iw:h=2*ih
The above is the same as:
scale=2*in_w:2*in_h
Scale the input to 2x with forced interlaced scaling:
scale=2*iw:2*ih:interl=1
Scale the input to half size:
scale=w=iw/2:h=ih/2
Increase the width, and set the height to the same size:
scale=3/2*iw:ow
Seek Greek harmony:
scale=iw:1/PHI*iw
scale=ih*PHI:ih
Increase the height, and set the width to 3/2 of the height:
scale=w=3/2*oh:h=3/5*ih
Increase the size, making the size a multiple of the chroma
subsample values:
scale="trunc(3/2*iw/hsub)*hsub:trunc(3/2*ih/vsub)*vsub"
Increase the width to a maximum of 500 pixels,
keeping the same aspect ratio as the input:
scale=w='min(500\, iw*3/2):h=-1'
Make pixels square by combining scale and setsar:
scale='trunc(ih*dar):ih',setsar=1/1
Make pixels square by combining scale and setsar,
making sure the resulting resolution is even (required by some codecs):
scale='trunc(ih*dar/2)*2:trunc(ih/2)*2',setsar=1/1
Scale a subtitle stream (sub) to match the main video (main) in size before
overlaying. ("scale2ref")
'[main]split[a][b]; [ref][a]scale=rw:rh[c]; [b][c]overlay'
Scale a logo to 1/10th the height of a video, while preserving its display
aspect ratio.
[logo-in][video-in]scale=w=oh*dar:h=rh/10[logo-out]
39.218.3 Commands
This filter supports the following commands:
width, w
height, h
Set the output video dimension expression.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.
39.219 scale_cuda
Scale (resize) and convert (pixel format) the input video, using accelerated CUDA kernels.
Setting the output width and height works in the same way as for the scale filter.
The filter accepts the following options:
w
h
Set the output video dimension expression. Default value is the input dimension.
Allows for the same expressions as the scale filter.
interp_algo
Sets the algorithm used for scaling:
nearest
Nearest neighbour
Used by default if input parameters match the desired output.
bilinear
Bilinear
bicubic
Bicubic
This is the default.
lanczos
Lanczos
format
Controls the output pixel format. By default, or if none is specified, the input
pixel format is used.
The filter does not support converting between YUV and RGB pixel formats.
passthrough
If set to 0, every frame is processed, even if no conversion is necessary.
This mode can be useful to use the filter as a buffer for a downstream
frame-consumer that exhausts the limited decoder frame pool.
If set to 1, frames are passed through as-is if they match the desired output
parameters. This is the default behaviour.
param
Algorithm-Specific parameter.
Affects the curves of the bicubic algorithm.
force_original_aspect_ratio
force_divisible_by
Work the same as the identical scale filter options.
39.219.1 Examples
Scale input to 720p, keeping aspect ratio and ensuring the output is yuv420p.
scale_cuda=-2:720:format=yuv420p
Upscale to 4K using nearest neighbour algorithm.
scale_cuda=4096:2160:interp_algo=nearest
Don’t do any conversion or scaling, but copy all input frames into newly allocated ones.
This can be useful to deal with a filter and encode chain that otherwise exhausts the
decoders frame pool.
scale_cuda=passthrough=0
39.220 scale_npp
Use the NVIDIA Performance Primitives (libnpp) to perform scaling and/or pixel
format conversion on CUDA video frames. Setting the output width and height
works in the same way as for the scale filter.
The following additional options are accepted:
format
The pixel format of the output CUDA frames. If set to the string "same" (the
default), the input format will be kept. Note that automatic format negotiation
and conversion is not yet supported for hardware frames
interp_algo
The interpolation algorithm used for resizing. One of the following:
nn
Nearest neighbour.
linear
cubic
cubic2p_bspline
2-parameter cubic (B=1, C=0)
cubic2p_catmullrom
2-parameter cubic (B=0, C=1/2)
cubic2p_b05c03
2-parameter cubic (B=1/2, C=3/10)
super
Supersampling
lanczos
force_original_aspect_ratio
Enable decreasing or increasing output video width or height if necessary to
keep the original aspect ratio. Possible values:
‘disable’
Scale the video as specified and disable this feature.
‘decrease’
The output video dimensions will automatically be decreased if needed.
‘increase’
The output video dimensions will automatically be increased if needed.
One useful instance of this option is that when you know a specific device’s
maximum allowed resolution, you can use this to limit the output video to
that, while retaining the aspect ratio. For example, device A allows
1280x720 playback, and your video is 1920x800. Using this option (set it to
decrease) and specifying 1280x720 to the command line makes the output
1280x533.
Please note that this is a different thing than specifying -1 for w
or h, you still need to specify the output resolution for this option
to work.
force_divisible_by
Ensures that both the output dimensions, width and height, are divisible by the
given integer when used together with force_original_aspect_ratio. This
works similar to using -n in the w and h options.
This option respects the value set for force_original_aspect_ratio,
increasing or decreasing the resolution accordingly. The video’s aspect ratio
may be slightly modified.
This option can be handy if you need to have a video fit within or exceed
a defined resolution using force_original_aspect_ratio but also have
encoder restrictions on width or height divisibility.
eval
Specify when to evaluate width and height expression. It accepts the following values:
‘init’
Only evaluate expressions once during the filter initialization or when a command is processed.
‘frame’
Evaluate expressions for each incoming frame.
The values of the w and h options are expressions
containing the following constants:
in_w
in_h
The input width and height
iw
ih
These are the same as in_w and in_h.
out_w
out_h
The output (scaled) width and height
ow
oh
These are the same as out_w and out_h
a
The same as iw / ih
sar
input sample aspect ratio
dar
The input display aspect ratio. Calculated from (iw / ih) * sar.
n
The (sequential) number of the input frame, starting from 0.
Only available with eval=frame.
t
The presentation timestamp of the input frame, expressed as a number of
seconds. Only available with eval=frame.
pos
The position (byte offset) of the frame in the input stream, or NaN if
this information is unavailable and/or meaningless (for example in case of synthetic video).
Only available with eval=frame.
Deprecated, do not use.
39.221 scale2ref_npp
Use the NVIDIA Performance Primitives (libnpp) to scale (resize) the input
video, based on a reference video.
See the scale_npp filter for available options, scale2ref_npp supports the same
but uses the reference video instead of the main input as basis. scale2ref_npp
also supports the following additional constants for the w and
h options:
main_w
main_h
The main input video’s width and height
main_a
The same as main_w / main_h
main_sar
The main input video’s sample aspect ratio
main_dar, mdar
The main input video’s display aspect ratio. Calculated from
(main_w / main_h) * main_sar.
main_n
The (sequential) number of the main input frame, starting from 0.
Only available with eval=frame.
main_t
The presentation timestamp of the main input frame, expressed as a number of
seconds. Only available with eval=frame.
main_pos
The position (byte offset) of the frame in the main input stream, or NaN if
this information is unavailable and/or meaningless (for example in case of synthetic video).
Only available with eval=frame.
39.221.1 Examples
Scale a subtitle stream (b) to match the main video (a) in size before overlaying
'scale2ref_npp[b][a];[a][b]overlay_cuda'
Scale a logo to 1/10th the height of a video, while preserving its display aspect ratio.
[logo-in][video-in]scale2ref_npp=w=oh*mdar:h=ih/10[logo-out][video-out]
39.222 scale_vt
Scale and convert the color parameters using VTPixelTransferSession.
The filter accepts the following options:
w
h
Set the output video dimension expression. Default value is the input dimension.
color_matrix
Set the output colorspace matrix.
color_primaries
Set the output color primaries.
color_transfer
Set the output transfer characteristics.
39.223 scharr
Apply scharr operator to input video stream.
The filter accepts the following option:
planes
Set which planes will be processed, unprocessed planes will be copied.
By default value 0xf, all planes will be processed.
scale
Set value which will be multiplied with filtered result.
delta
Set value which will be added to filtered result.
39.223.1 Commands
This filter supports the all above options as commands.
39.224 scroll
Scroll input video horizontally and/or vertically by constant speed.
The filter accepts the following options:
horizontal, h
Set the horizontal scrolling speed. Default is 0. Allowed range is from -1 to 1.
Negative values changes scrolling direction.
vertical, v
Set the vertical scrolling speed. Default is 0. Allowed range is from -1 to 1.
Negative values changes scrolling direction.
hpos
Set the initial horizontal scrolling position. Default is 0. Allowed range is from 0 to 1.
vpos
Set the initial vertical scrolling position. Default is 0. Allowed range is from 0 to 1.
39.224.1 Commands
This filter supports the following commands:
horizontal, h
Set the horizontal scrolling speed.
vertical, v
Set the vertical scrolling speed.
39.225 scdet
Detect video scene change.
This filter sets frame metadata with mafd between frame, the scene score, and
forward the frame to the next filter, so they can use these metadata to detect
scene change or others.
In addition, this filter logs a message and sets frame metadata when it detects
a scene change by threshold.
lavfi.scd.mafd metadata keys are set with mafd for every frame.
lavfi.scd.score metadata keys are set with scene change score for every frame
to detect scene change.
lavfi.scd.time metadata keys are set with current filtered frame time which
detect scene change with threshold.
The filter accepts the following options:
threshold, t
Set the scene change detection threshold as a percentage of maximum change. Good
values are in the [8.0, 14.0] range. The range for threshold is
[0., 100.].
Default value is 10..
sc_pass, s
Set the flag to pass scene change frames to the next filter. Default value is 0
You can enable it if you want to get snapshot of scene change frames only.
39.226 selectivecolor
Adjust cyan, magenta, yellow and black (CMYK) to certain ranges of colors (such
as "reds", "yellows", "greens", "cyans", ...). The adjustment range is defined
by the "purity" of the color (that is, how saturated it already is).
This filter is similar to the Adobe Photoshop Selective Color tool.
The filter accepts the following options:
correction_method
Select color correction method.
Available values are:
‘absolute’
Specified adjustments are applied "as-is" (added/subtracted to original pixel
component value).
‘relative’
Specified adjustments are relative to the original component value.
Default is absolute.
reds
Adjustments for red pixels (pixels where the red component is the maximum)
yellows
Adjustments for yellow pixels (pixels where the blue component is the minimum)
greens
Adjustments for green pixels (pixels where the green component is the maximum)
cyans
Adjustments for cyan pixels (pixels where the red component is the minimum)
blues
Adjustments for blue pixels (pixels where the blue component is the maximum)
magentas
Adjustments for magenta pixels (pixels where the green component is the minimum)
whites
Adjustments for white pixels (pixels where all components are greater than 128)
neutrals
Adjustments for all pixels except pure black and pure white
blacks
Adjustments for black pixels (pixels where all components are lesser than 128)
psfile
Specify a Photoshop selective color file (.asv) to import the settings from.
All the adjustment settings (reds, yellows, ...) accept up to
4 space separated floating point adjustment values in the [-1,1] range,
respectively to adjust the amount of cyan, magenta, yellow and black for the
pixels of its range.
39.226.1 Examples
Increase cyan by 50% and reduce yellow by 33% in every green areas, and
increase magenta by 27% in blue areas:
selectivecolor=greens=.5 0 -.33 0:blues=0 .27
Use a Photoshop selective color preset:
selectivecolor=psfile=MySelectiveColorPresets/Misty.asv
39.227 separatefields
The separatefields takes a frame-based video input and splits
each frame into its components fields, producing a new half height clip
with twice the frame rate and twice the frame count.
This filter use field-dominance information in frame to decide which
of each pair of fields to place first in the output.
If it gets it wrong use setfield filter before separatefields filter.
39.228 setdar, setsar
The setdar filter sets the Display Aspect Ratio for the filter
output video.
This is done by changing the specified Sample (aka Pixel) Aspect
Ratio, according to the following equation:
DAR = HORIZONTAL_RESOLUTION / VERTICAL_RESOLUTION * SAR
Keep in mind that the setdar filter does not modify the pixel
dimensions of the video frame. Also, the display aspect ratio set by
this filter may be changed by later filters in the filterchain,
e.g. in case of scaling or if another "setdar" or a "setsar" filter is
applied.
The setsar filter sets the Sample (aka Pixel) Aspect Ratio for
the filter output video.
Note that as a consequence of the application of this filter, the
output display aspect ratio will change according to the equation
above.
Keep in mind that the sample aspect ratio set by the setsar
filter may be changed by later filters in the filterchain, e.g. if
another "setsar" or a "setdar" filter is applied.
It accepts the following parameters:
r, ratio, dar (setdar only), sar (setsar only)
Set the aspect ratio used by the filter.
The parameter can be a floating point number string, or an expression. If the
parameter is not specified, the value "0" is assumed, meaning that the same
input value is used.
max
Set the maximum integer value to use for expressing numerator and
denominator when reducing the expressed aspect ratio to a rational.
Default value is 100.
The parameter sar is an expression containing the following constants:
w, h
The input width and height.
a
Same as w / h.
sar
The input sample aspect ratio.
dar
The input display aspect ratio. It is the same as
(w / h) * sar.
hsub, vsub
Horizontal and vertical chroma subsample values. For example, for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
39.228.1 Examples
To change the display aspect ratio to 16:9, specify one of the following:
setdar=dar=1.77777
setdar=dar=16/9
To change the sample aspect ratio to 10:11, specify:
setsar=sar=10/11
To set a display aspect ratio of 16:9, and specify a maximum integer value of
1000 in the aspect ratio reduction, use the command:
setdar=ratio=16/9:max=1000
39.229 setfield
Force field for the output video frame.
The setfield filter marks the interlace type field for the
output frames. It does not change the input frame, but only sets the
corresponding property, which affects how the frame is treated by
following filters (e.g. fieldorder or yadif).
The filter accepts the following options:
mode
Available values are:
‘auto’
Keep the same field property.
‘bff’
Mark the frame as bottom-field-first.
‘tff’
Mark the frame as top-field-first.
‘prog’
Mark the frame as progressive.
39.230 setparams
Force frame parameter for the output video frame.
The setparams filter marks interlace and color range for the
output frames. It does not change the input frame, but only sets the
corresponding property, which affects how the frame is treated by
filters/encoders.
field_mode
Available values are:
‘auto’
Keep the same field property (default).
‘bff’
Mark the frame as bottom-field-first.
‘tff’
Mark the frame as top-field-first.
‘prog’
Mark the frame as progressive.
range
Available values are:
‘auto’
Keep the same color range property (default).
‘unspecified, unknown’
Mark the frame as unspecified color range.
‘limited, tv, mpeg’
Mark the frame as limited range.
‘full, pc, jpeg’
Mark the frame as full range.
color_primaries
Set the color primaries.
Available values are:
‘auto’
Keep the same color primaries property (default).
‘bt709’
‘unknown’
‘bt470m’
‘bt470bg’
‘smpte170m’
‘smpte240m’
‘film’
‘bt2020’
‘smpte428’
‘smpte431’
‘smpte432’
‘jedec-p22’
color_trc
Set the color transfer.
Available values are:
‘auto’
Keep the same color trc property (default).
‘bt709’
‘unknown’
‘bt470m’
‘bt470bg’
‘smpte170m’
‘smpte240m’
‘linear’
‘log100’
‘log316’
‘iec61966-2-4’
‘bt1361e’
‘iec61966-2-1’
‘bt2020-10’
‘bt2020-12’
‘smpte2084’
‘smpte428’
‘arib-std-b67’
colorspace
Set the colorspace.
Available values are:
‘auto’
Keep the same colorspace property (default).
‘gbr’
‘bt709’
‘unknown’
‘fcc’
‘bt470bg’
‘smpte170m’
‘smpte240m’
‘ycgco’
‘bt2020nc’
‘bt2020c’
‘smpte2085’
‘chroma-derived-nc’
‘chroma-derived-c’
‘ictcp’
chroma_location
Set the chroma sample location.
Available values are:
‘auto’
Keep the same chroma location (default).
‘unspecified, unknown’
‘left’
‘center’
‘topleft’
‘top’
‘bottomleft’
‘bottom’
39.231 sharpen_npp
Use the NVIDIA Performance Primitives (libnpp) to perform image sharpening with
border control.
The following additional options are accepted:
border_type
Type of sampling to be used ad frame borders. One of the following:
replicate
Replicate pixel values.
39.232 shear
Apply shear transform to input video.
This filter supports the following options:
shx
Shear factor in X-direction. Default value is 0.
Allowed range is from -2 to 2.
shy
Shear factor in Y-direction. Default value is 0.
Allowed range is from -2 to 2.
fillcolor, c
Set the color used to fill the output area not covered by the transformed
video. For the general syntax of this option, check the
(ffmpeg-utils)"Color" section in the ffmpeg-utils manual.
If the special value "none" is selected then no
background is printed (useful for example if the background is never shown).
Default value is "black".
interp
Set interpolation type. Can be bilinear or nearest. Default is bilinear.
39.232.1 Commands
This filter supports the all above options as commands.
39.233 showinfo
Show a line containing various information for each input video frame.
The input video is not modified.
This filter supports the following options:
checksum
Calculate checksums of each plane. By default enabled.
udu_sei_as_ascii
Try to print user data unregistered SEI as ascii character when possible,
in hex format otherwise.
The shown line contains a sequence of key/value pairs of the form
key:value.
The following values are shown in the output:
n
The (sequential) number of the input frame, starting from 0.
pts
The Presentation TimeStamp of the input frame, expressed as a number of
time base units. The time base unit depends on the filter input pad.
pts_time
The Presentation TimeStamp of the input frame, expressed as a number of
seconds.
fmt
The pixel format name.
sar
The sample aspect ratio of the input frame, expressed in the form
num/den.
s
The size of the input frame. For the syntax of this option, check the
(ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.
i
The type of interlaced mode ("P" for "progressive", "T" for top field first, "B"
for bottom field first).
iskey
This is 1 if the frame is a key frame, 0 otherwise.
type
The picture type of the input frame ("I" for an I-frame, "P" for a
P-frame, "B" for a B-frame, or "?" for an unknown type).
Also refer to the documentation of the AVPictureType enum and of
the av_get_picture_type_char function defined in
libavutil/avutil.h.
checksum
The Adler-32 checksum (printed in hexadecimal) of all the planes of the input frame.
plane_checksum
The Adler-32 checksum (printed in hexadecimal) of each plane of the input frame,
expressed in the form "[c0 c1 c2 c3]".
mean
The mean value of pixels in each plane of the input frame, expressed in the form
"[mean0 mean1 mean2 mean3]".
stdev
The standard deviation of pixel values in each plane of the input frame, expressed
in the form "[stdev0 stdev1 stdev2 stdev3]".
39.234 showpalette
Displays the 256 colors palette of each frame. This filter is only relevant for
pal8 pixel format frames.
It accepts the following option:
s
Set the size of the box used to represent one palette color entry. Default is
30 (for a 30x30 pixel box).
39.235 shuffleframes
Reorder and/or duplicate and/or drop video frames.
It accepts the following parameters:
mapping
Set the destination indexes of input frames.
This is space or ’|’ separated list of indexes that maps input frames to output
frames. Number of indexes also sets maximal value that each index may have.
’-1’ index have special meaning and that is to drop frame.
The first frame has the index 0. The default is to keep the input unchanged.
39.235.1 Examples
Swap second and third frame of every three frames of the input:
ffmpeg -i INPUT -vf "shuffleframes=0 2 1" OUTPUT
Swap 10th and 1st frame of every ten frames of the input:
ffmpeg -i INPUT -vf "shuffleframes=9 1 2 3 4 5 6 7 8 0" OUTPUT
39.236 shufflepixels
Reorder pixels in video frames.
This filter accepts the following options:
direction, d
Set shuffle direction. Can be forward or inverse direction.
Default direction is forward.
mode, m
Set shuffle mode. Can be horizontal, vertical or block mode.
width, w
height, h
Set shuffle block_size. In case of horizontal shuffle mode only width
part of size is used, and in case of vertical shuffle mode only height
part of size is used.
seed, s
Set random seed used with shuffling pixels. Mainly useful to set to be able
to reverse filtering process to get original input.
For example, to reverse forward shuffle you need to use same parameters
and exact same seed and to set direction to inverse.
39.237 shuffleplanes
Reorder and/or duplicate video planes.
It accepts the following parameters:
map0
The index of the input plane to be used as the first output plane.
map1
The index of the input plane to be used as the second output plane.
map2
The index of the input plane to be used as the third output plane.
map3
The index of the input plane to be used as the fourth output plane.
The first plane has the index 0. The default is to keep the input unchanged.
39.237.1 Examples
Swap the second and third planes of the input:
ffmpeg -i INPUT -vf shuffleplanes=0:2:1:3 OUTPUT
39.238 signalstats
Evaluate various visual metrics that assist in determining issues associated
with the digitization of analog video media.
By default the filter will log these metadata values:
YMIN
Display the minimal Y value contained within the input frame. Expressed in
range of [0-255].
YLOW
Display the Y value at the 10% percentile within the input frame. Expressed in
range of [0-255].
YAVG
Display the average Y value within the input frame. Expressed in range of
[0-255].
YHIGH
Display the Y value at the 90% percentile within the input frame. Expressed in
range of [0-255].
YMAX
Display the maximum Y value contained within the input frame. Expressed in
range of [0-255].
UMIN
Display the minimal U value contained within the input frame. Expressed in
range of [0-255].
ULOW
Display the U value at the 10% percentile within the input frame. Expressed in
range of [0-255].
UAVG
Display the average U value within the input frame. Expressed in range of
[0-255].
UHIGH
Display the U value at the 90% percentile within the input frame. Expressed in
range of [0-255].
UMAX
Display the maximum U value contained within the input frame. Expressed in
range of [0-255].
VMIN
Display the minimal V value contained within the input frame. Expressed in
range of [0-255].
VLOW
Display the V value at the 10% percentile within the input frame. Expressed in
range of [0-255].
VAVG
Display the average V value within the input frame. Expressed in range of
[0-255].
VHIGH
Display the V value at the 90% percentile within the input frame. Expressed in
range of [0-255].
VMAX
Display the maximum V value contained within the input frame. Expressed in
range of [0-255].
SATMIN
Display the minimal saturation value contained within the input frame.
Expressed in range of [0-~181.02].
SATLOW
Display the saturation value at the 10% percentile within the input frame.
Expressed in range of [0-~181.02].
SATAVG
Display the average saturation value within the input frame. Expressed in range
of [0-~181.02].
SATHIGH
Display the saturation value at the 90% percentile within the input frame.
Expressed in range of [0-~181.02].
SATMAX
Display the maximum saturation value contained within the input frame.
Expressed in range of [0-~181.02].
HUEMED
Display the median value for hue within the input frame. Expressed in range of
[0-360].
HUEAVG
Display the average value for hue within the input frame. Expressed in range of
[0-360].
YDIF
Display the average of sample value difference between all values of the Y
plane in the current frame and corresponding values of the previous input frame.
Expressed in range of [0-255].
UDIF
Display the average of sample value difference between all values of the U
plane in the current frame and corresponding values of the previous input frame.
Expressed in range of [0-255].
VDIF
Display the average of sample value difference between all values of the V
plane in the current frame and corresponding values of the previous input frame.
Expressed in range of [0-255].
YBITDEPTH
Display bit depth of Y plane in current frame.
Expressed in range of [0-16].
UBITDEPTH
Display bit depth of U plane in current frame.
Expressed in range of [0-16].
VBITDEPTH
Display bit depth of V plane in current frame.
Expressed in range of [0-16].
The filter accepts the following options:
stat
out
stat specify an additional form of image analysis.
out output video with the specified type of pixel highlighted.
Both options accept the following values:
‘tout’
Identify temporal outliers pixels. A temporal outlier is a pixel
unlike the neighboring pixels of the same field. Examples of temporal outliers
include the results of video dropouts, head clogs, or tape tracking issues.
‘vrep’
Identify vertical line repetition. Vertical line repetition includes
similar rows of pixels within a frame. In born-digital video vertical line
repetition is common, but this pattern is uncommon in video digitized from an
analog source. When it occurs in video that results from the digitization of an
analog source it can indicate concealment from a dropout compensator.
‘brng’
Identify pixels that fall outside of legal broadcast range.
color, c
Set the highlight color for the out option. The default color is
yellow.
39.238.1 Examples
Output data of various video metrics:
ffprobe -f lavfi movie=example.mov,signalstats="stat=tout+vrep+brng" -show_frames
Output specific data about the minimum and maximum values of the Y plane per frame:
ffprobe -f lavfi movie=example.mov,signalstats -show_entries frame_tags=lavfi.signalstats.YMAX,lavfi.signalstats.YMIN
Playback video while highlighting pixels that are outside of broadcast range in red.
ffplay example.mov -vf signalstats="out=brng:color=red"
Playback video with signalstats metadata drawn over the frame.
ffplay example.mov -vf signalstats=stat=brng+vrep+tout,drawtext=fontfile=FreeSerif.ttf:textfile=signalstat_drawtext.txt
The contents of signalstat_drawtext.txt used in the command are:
time %{pts:hms}
Y (%{metadata:lavfi.signalstats.YMIN}-%{metadata:lavfi.signalstats.YMAX})
U (%{metadata:lavfi.signalstats.UMIN}-%{metadata:lavfi.signalstats.UMAX})
V (%{metadata:lavfi.signalstats.VMIN}-%{metadata:lavfi.signalstats.VMAX})
saturation maximum: %{metadata:lavfi.signalstats.SATMAX}
39.239 signature
Calculates the MPEG-7 Video Signature. The filter can handle more than one
input. In this case the matching between the inputs can be calculated additionally.
The filter always passes through the first input. The signature of each stream can
be written into a file.
It accepts the following options:
detectmode
Enable or disable the matching process.
Available values are:
‘off’
Disable the calculation of a matching (default).
‘full’
Calculate the matching for the whole video and output whether the whole video
matches or only parts.
‘fast’
Calculate only until a matching is found or the video ends. Should be faster in
some cases.
nb_inputs
Set the number of inputs. The option value must be a non negative integer.
Default value is 1.
filename
Set the path to which the output is written. If there is more than one input,
the path must be a prototype, i.e. must contain %d or %0nd (where n is a positive
integer), that will be replaced with the input number. If no filename is
specified, no output will be written. This is the default.
format
Choose the output format.
Available values are:
‘binary’
Use the specified binary representation (default).
‘xml’
Use the specified xml representation.
th_d
Set threshold to detect one word as similar. The option value must be an integer
greater than zero. The default value is 9000.
th_dc
Set threshold to detect all words as similar. The option value must be an integer
greater than zero. The default value is 60000.
th_xh
Set threshold to detect frames as similar. The option value must be an integer
greater than zero. The default value is 116.
th_di
Set the minimum length of a sequence in frames to recognize it as matching
sequence. The option value must be a non negative integer value.
The default value is 0.
th_it
Set the minimum relation, that matching frames to all frames must have.
The option value must be a double value between 0 and 1. The default value is 0.5.
39.239.1 Examples
To calculate the signature of an input video and store it in signature.bin:
ffmpeg -i input.mkv -vf signature=filename=signature.bin -map 0:v -f null -
To detect whether two videos match and store the signatures in XML format in
signature0.xml and signature1.xml:
ffmpeg -i input1.mkv -i input2.mkv -filter_complex "[0:v][1:v] signature=nb_inputs=2:detectmode=full:format=xml:filename=signature%d.xml" -map :v -f null -
39.240 siti
Calculate Spatial Information (SI) and Temporal Information (TI) scores for a video,
as defined in ITU-T Rec. P.910 (11/21): Subjective video quality assessment methods
for multimedia applications. Available PDF at https://www.itu.int/rec/T-REC-P.910-202111-S/en.
Note that this is a legacy implementation that corresponds to a superseded recommendation.
Refer to ITU-T Rec. P.910 (07/22) for the latest version: https://www.itu.int/rec/T-REC-P.910-202207-I/en
It accepts the following option:
print_summary
If set to 1, Summary statistics will be printed to the console. Default 0.
39.240.1 Examples
To calculate SI/TI metrics and print summary:
ffmpeg -i input.mp4 -vf siti=print_summary=1 -f null -
39.241 smartblur
Blur the input video without impacting the outlines.
It accepts the following options:
luma_radius, lr
Set the luma radius. The option value must be a float number in
the range [0.1,5.0] that specifies the variance of the gaussian filter
used to blur the image (slower if larger). Default value is 1.0.
luma_strength, ls
Set the luma strength. The option value must be a float number
in the range [-1.0,1.0] that configures the blurring. A value included
in [0.0,1.0] will blur the image whereas a value included in
[-1.0,0.0] will sharpen the image. Default value is 1.0.
luma_threshold, lt
Set the luma threshold used as a coefficient to determine
whether a pixel should be blurred or not. The option value must be an
integer in the range [-30,30]. A value of 0 will filter all the image,
a value included in [0,30] will filter flat areas and a value included
in [-30,0] will filter edges. Default value is 0.
chroma_radius, cr
Set the chroma radius. The option value must be a float number in
the range [0.1,5.0] that specifies the variance of the gaussian filter
used to blur the image (slower if larger). Default value is luma_radius.
chroma_strength, cs
Set the chroma strength. The option value must be a float number
in the range [-1.0,1.0] that configures the blurring. A value included
in [0.0,1.0] will blur the image whereas a value included in
[-1.0,0.0] will sharpen the image. Default value is luma_strength.
chroma_threshold, ct
Set the chroma threshold used as a coefficient to determine
whether a pixel should be blurred or not. The option value must be an
integer in the range [-30,30]. A value of 0 will filter all the image,
a value included in [0,30] will filter flat areas and a value included
in [-30,0] will filter edges. Default value is luma_threshold.
alpha_radius, ar
Set the alpha radius. The option value must be a float number in
the range [0.1,5.0] that specifies the variance of the gaussian filter
used to blur the image (slower if larger). Default value is luma_radius.
alpha_strength, as
Set the alpha strength. The option value must be a float number
in the range [-1.0,1.0] that configures the blurring. A value included
in [0.0,1.0] will blur the image whereas a value included in
[-1.0,0.0] will sharpen the image. Default value is luma_strength.
alpha_threshold, at
Set the alpha threshold used as a coefficient to determine
whether a pixel should be blurred or not. The option value must be an
integer in the range [-30,30]. A value of 0 will filter all the image,
a value included in [0,30] will filter flat areas and a value included
in [-30,0] will filter edges. Default value is luma_threshold.
If a chroma or alpha option is not explicitly set, the corresponding luma value
is set.
39.242 sobel
Apply sobel operator to input video stream.
The filter accepts the following option:
planes
Set which planes will be processed, unprocessed planes will be copied.
By default value 0xf, all planes will be processed.
scale
Set value which will be multiplied with filtered result.
delta
Set value which will be added to filtered result.
39.242.1 Commands
This filter supports the all above options as commands.
39.243 spp
Apply a simple postprocessing filter that compresses and decompresses the image
at several (or - in the case of quality level 6 - all) shifts
and average the results.
The filter accepts the following options:
quality
Set quality. This option defines the number of levels for averaging. It accepts
an integer in the range 0-6. If set to 0, the filter will have no
effect. A value of 6 means the higher quality. For each increment of
that value the speed drops by a factor of approximately 2.  Default value is
3.
qp
Force a constant quantization parameter. If not set, the filter will use the QP
from the video stream (if available).
mode
Set thresholding mode. Available modes are:
‘hard’
Set hard thresholding (default).
‘soft’
Set soft thresholding (better de-ringing effect, but likely blurrier).
use_bframe_qp
Enable the use of the QP from the B-Frames if set to 1. Using this
option may cause flicker since the B-Frames have often larger QP. Default is
0 (not enabled).
39.243.1 Commands
This filter supports the following commands:
quality, level
Set quality level. The value max can be used to set the maximum level,
currently 6.
39.244 sr
Scale the input by applying one of the super-resolution methods based on
convolutional neural networks. Supported models:
Super-Resolution Convolutional Neural Network model (SRCNN).
See https://arxiv.org/abs/1501.00092.
Efficient Sub-Pixel Convolutional Neural Network model (ESPCN).
See https://arxiv.org/abs/1609.05158.
Training scripts as well as scripts for model file (.pb) saving can be found at
https://github.com/XueweiMeng/sr/tree/sr_dnn_native. Original repository
is at https://github.com/HighVoltageRocknRoll/sr.git.
The filter accepts the following options:
dnn_backend
Specify which DNN backend to use for model loading and execution. This option accepts
the following values:
‘tensorflow’
TensorFlow backend. To enable this backend you
need to install the TensorFlow for C library (see
https://www.tensorflow.org/install/lang_c) and configure FFmpeg with
--enable-libtensorflow
model
Set path to model file specifying network architecture and its parameters.
Note that different backends use different file formats. TensorFlow, OpenVINO backend
can load files for only its format.
scale_factor
Set scale factor for SRCNN model. Allowed values are 2, 3 and 4.
Default value is 2. Scale factor is necessary for SRCNN model, because it accepts
input upscaled using bicubic upscaling with proper scale factor.
To get full functionality (such as async execution), please use the dnn_processing filter.
39.245 ssim
Obtain the SSIM (Structural SImilarity Metric) between two input videos.
This filter takes in input two input videos, the first input is
considered the "main" source and is passed unchanged to the
output. The second input is used as a "reference" video for computing
the SSIM.
Both video inputs must have the same resolution and pixel format for
this filter to work correctly. Also it assumes that both inputs
have the same number of frames, which are compared one by one.
The filter stores the calculated SSIM of each frame.
The description of the accepted parameters follows.
stats_file, f
If specified the filter will use the named file to save the SSIM of
each individual frame. When filename equals "-" the data is sent to
standard output.
The file printed if stats_file is selected, contains a sequence of
key/value pairs of the form key:value for each compared
couple of frames.
A description of each shown parameter follows:
n
sequential number of the input frame, starting from 1
Y, U, V, R, G, B
SSIM of the compared frames for the component specified by the suffix.
All
SSIM of the compared frames for the whole frame.
dB
Same as above but in dB representation.
This filter also supports the framesync options.
39.245.1 Examples
For example:
movie=ref_movie.mpg, setpts=PTS-STARTPTS [main];
[main][ref] ssim="stats_file=stats.log" [out]
On this example the input file being processed is compared with the
reference file ref_movie.mpg. The SSIM of each individual frame
is stored in stats.log.
Another example with both psnr and ssim at same time:
ffmpeg -i main.mpg -i ref.mpg -lavfi  "ssim;[0:v][1:v]psnr" -f null -
Another example with different containers:
ffmpeg -i main.mpg -i ref.mkv -lavfi  "[0:v]settb=AVTB,setpts=PTS-STARTPTS[main];[1:v]settb=AVTB,setpts=PTS-STARTPTS[ref];[main][ref]ssim" -f null -
39.246 stereo3d
Convert between different stereoscopic image formats.
The filters accept the following options:
in
Set stereoscopic image format of input.
Available values for input image formats are:
‘sbsl’
side by side parallel (left eye left, right eye right)
‘sbsr’
side by side crosseye (right eye left, left eye right)
‘sbs2l’
side by side parallel with half width resolution
(left eye left, right eye right)
‘sbs2r’
side by side crosseye with half width resolution
(right eye left, left eye right)
‘abl’
‘tbl’
above-below (left eye above, right eye below)
‘abr’
‘tbr’
above-below (right eye above, left eye below)
‘ab2l’
‘tb2l’
above-below with half height resolution
(left eye above, right eye below)
‘ab2r’
‘tb2r’
above-below with half height resolution
(right eye above, left eye below)
‘al’
alternating frames (left eye first, right eye second)
‘ar’
alternating frames (right eye first, left eye second)
‘irl’
interleaved rows (left eye has top row, right eye starts on next row)
‘irr’
interleaved rows (right eye has top row, left eye starts on next row)
‘icl’
interleaved columns, left eye first
‘icr’
interleaved columns, right eye first
Default value is ‘sbsl’.
out
Set stereoscopic image format of output.
‘sbsl’
side by side parallel (left eye left, right eye right)
‘sbsr’
side by side crosseye (right eye left, left eye right)
‘sbs2l’
side by side parallel with half width resolution
(left eye left, right eye right)
‘sbs2r’
side by side crosseye with half width resolution
(right eye left, left eye right)
‘abl’
‘tbl’
above-below (left eye above, right eye below)
‘abr’
‘tbr’
above-below (right eye above, left eye below)
‘ab2l’
‘tb2l’
above-below with half height resolution
(left eye above, right eye below)
‘ab2r’
‘tb2r’
above-below with half height resolution
(right eye above, left eye below)
‘al’
alternating frames (left eye first, right eye second)
‘ar’
alternating frames (right eye first, left eye second)
‘irl’
interleaved rows (left eye has top row, right eye starts on next row)
‘irr’
interleaved rows (right eye has top row, left eye starts on next row)
‘arbg’
anaglyph red/blue gray
(red filter on left eye, blue filter on right eye)
‘argg’
anaglyph red/green gray
(red filter on left eye, green filter on right eye)
‘arcg’
anaglyph red/cyan gray
(red filter on left eye, cyan filter on right eye)
‘arch’
anaglyph red/cyan half colored
(red filter on left eye, cyan filter on right eye)
‘arcc’
anaglyph red/cyan color
(red filter on left eye, cyan filter on right eye)
‘arcd’
anaglyph red/cyan color optimized with the least squares projection of dubois
(red filter on left eye, cyan filter on right eye)
‘agmg’
anaglyph green/magenta gray
(green filter on left eye, magenta filter on right eye)
‘agmh’
anaglyph green/magenta half colored
(green filter on left eye, magenta filter on right eye)
‘agmc’
anaglyph green/magenta colored
(green filter on left eye, magenta filter on right eye)
‘agmd’
anaglyph green/magenta color optimized with the least squares projection of dubois
(green filter on left eye, magenta filter on right eye)
‘aybg’
anaglyph yellow/blue gray
(yellow filter on left eye, blue filter on right eye)
‘aybh’
anaglyph yellow/blue half colored
(yellow filter on left eye, blue filter on right eye)
‘aybc’
anaglyph yellow/blue colored
(yellow filter on left eye, blue filter on right eye)
‘aybd’
anaglyph yellow/blue color optimized with the least squares projection of dubois
(yellow filter on left eye, blue filter on right eye)
‘ml’
mono output (left eye only)
‘mr’
mono output (right eye only)
‘chl’
checkerboard, left eye first
‘chr’
checkerboard, right eye first
‘icl’
interleaved columns, left eye first
‘icr’
interleaved columns, right eye first
‘hdmi’
HDMI frame pack
Default value is ‘arcd’.
39.246.1 Examples
Convert input video from side by side parallel to anaglyph yellow/blue dubois:
stereo3d=sbsl:aybd
Convert input video from above below (left eye above, right eye below) to side by side crosseye.
stereo3d=abl:sbsr
39.247 streamselect, astreamselect
Select video or audio streams.
The filter accepts the following options:
inputs
Set number of inputs. Default is 2.
map
Set input indexes to remap to outputs.
39.247.1 Commands
The streamselect and astreamselect filter supports the following
commands:
map
Set input indexes to remap to outputs.
39.247.2 Examples
Select first 5 seconds 1st stream and rest of time 2nd stream:
sendcmd='5.0 streamselect map 1',streamselect=inputs=2:map=0
Same as above, but for audio:
asendcmd='5.0 astreamselect map 1',astreamselect=inputs=2:map=0
39.248 subtitles
Draw subtitles on top of input video using the libass library.
To enable compilation of this filter you need to configure FFmpeg with
--enable-libass. This filter also requires a build with libavcodec and
libavformat to convert the passed subtitles file to ASS (Advanced Substation
Alpha) subtitles format.
The filter accepts the following options:
filename, f
Set the filename of the subtitle file to read. It must be specified.
original_size
Specify the size of the original video, the video for which the ASS file
was composed. For the syntax of this option, check the
(ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.
Due to a misdesign in ASS aspect ratio arithmetic, this is necessary to
correctly scale the fonts if the aspect ratio has been changed.
fontsdir
Set a directory path containing fonts that can be used by the filter.
These fonts will be used in addition to whatever the font provider uses.
alpha
Process alpha channel, by default alpha channel is untouched.
charenc
Set subtitles input character encoding. subtitles filter only. Only
useful if not UTF-8.
stream_index, si
Set subtitles stream index. subtitles filter only.
force_style
Override default style or script info parameters of the subtitles. It accepts a
string containing ASS style format KEY=VALUE couples separated by ",".
wrap_unicode
Break lines according to the Unicode Line Breaking Algorithm. Availability requires
at least libass release 0.17.0 (or LIBASS_VERSION 0x01600010), and libass must
have been built with libunibreak.
The option is enabled by default except for native ASS.
If the first key is not specified, it is assumed that the first value
specifies the filename.
For example, to render the file sub.srt on top of the input
video, use the command:
subtitles=sub.srt
which is equivalent to:
subtitles=filename=sub.srt
To render the default subtitles stream from file video.mkv, use:
subtitles=video.mkv
To render the second subtitles stream from that file, use:
subtitles=video.mkv:si=1
To make the subtitles stream from sub.srt appear in 80% transparent blue
DejaVu Serif, use:
subtitles=sub.srt:force_style='Fontname=DejaVu Serif,PrimaryColour=&HCCFF0000'
39.249 super2xsai
Scale the input by 2x and smooth using the Super2xSaI (Scale and
Interpolate) pixel art scaling algorithm.
Useful for enlarging pixel art images without reducing sharpness.
39.250 swaprect
Swap two rectangular objects in video.
This filter accepts the following options:
w
Set object width.
h
Set object height.
x1
Set 1st rect x coordinate.
y1
Set 1st rect y coordinate.
x2
Set 2nd rect x coordinate.
y2
Set 2nd rect y coordinate.
All expressions are evaluated once for each frame.
The all options are expressions containing the following constants:
w
h
The input width and height.
a
same as w / h
sar
input sample aspect ratio
dar
input display aspect ratio, it is the same as (w / h) * sar
n
The number of the input frame, starting from 0.
t
The timestamp expressed in seconds. It’s NAN if the input timestamp is unknown.
pos
the position in the file of the input frame, NAN if unknown; deprecated,
do not use
39.250.1 Commands
This filter supports the all above options as commands.
39.251 swapuv
Swap U & V plane.
39.252 tblend
Blend successive video frames.
See blend
39.253 telecine
Apply telecine process to the video.
This filter accepts the following options:
first_field
‘top, t’
top field first
‘bottom, b’
bottom field first
The default value is top.
pattern
A string of numbers representing the pulldown pattern you wish to apply.
The default value is 23.
Some typical patterns:
NTSC output (30i):
27.5p: 32222
24p: 23 (classic)
24p: 2332 (preferred)
20p: 33
18p: 334
16p: 3444
PAL output (25i):
27.5p: 12222
24p: 222222222223 ("Euro pulldown")
16.67p: 33
16p: 33333334
39.254 thistogram
Compute and draw a color distribution histogram for the input video across time.
Unlike histogram video filter which only shows histogram of single input frame
at certain time, this filter shows also past histograms of number of frames defined
by width option.
The computed histogram is a representation of the color component
distribution in an image.
The filter accepts the following options:
width, w
Set width of single color component output. Default value is 0.
Value of 0 means width will be picked from input video.
This also set number of passed histograms to keep.
Allowed range is [0, 8192].
display_mode, d
Set display mode.
It accepts the following values:
‘stack’
Per color component graphs are placed below each other.
‘parade’
Per color component graphs are placed side by side.
‘overlay’
Presents information identical to that in the parade, except
that the graphs representing color components are superimposed directly
over one another.
Default is stack.
levels_mode, m
Set mode. Can be either linear, or logarithmic.
Default is linear.
components, c
Set what color components to display.
Default is 7.
bgopacity, b
Set background opacity. Default is 0.9.
envelope, e
Show envelope. Default is disabled.
ecolor, ec
Set envelope color. Default is gold.
slide
Set slide mode.
Available values for slide is:
‘frame’
Draw new frame when right border is reached.
‘replace’
Replace old columns with new ones.
‘scroll’
Scroll from right to left.
‘rscroll’
Scroll from left to right.
‘picture’
Draw single picture.
Default is replace.
39.255 threshold
Apply threshold effect to video stream.
This filter needs four video streams to perform thresholding.
First stream is stream we are filtering.
Second stream is holding threshold values, third stream is holding min values,
and last, fourth stream is holding max values.
The filter accepts the following option:
planes
Set which planes will be processed, unprocessed planes will be copied.
By default value 0xf, all planes will be processed.
For example if first stream pixel’s component value is less then threshold value
of pixel component from 2nd threshold stream, third stream value will picked,
otherwise fourth stream pixel component value will be picked.
Using color source filter one can perform various types of thresholding:
39.255.1 Commands
This filter supports the all options as commands.
39.255.2 Examples
Binary threshold, using gray color as threshold:
ffmpeg -i 320x240.avi -f lavfi -i color=gray -f lavfi -i color=black -f lavfi -i color=white -lavfi threshold output.avi
Inverted binary threshold, using gray color as threshold:
ffmpeg -i 320x240.avi -f lavfi -i color=gray -f lavfi -i color=white -f lavfi -i color=black -lavfi threshold output.avi
Truncate binary threshold, using gray color as threshold:
ffmpeg -i 320x240.avi -f lavfi -i color=gray -i 320x240.avi -f lavfi -i color=gray -lavfi threshold output.avi
Threshold to zero, using gray color as threshold:
ffmpeg -i 320x240.avi -f lavfi -i color=gray -f lavfi -i color=white -i 320x240.avi -lavfi threshold output.avi
Inverted threshold to zero, using gray color as threshold:
ffmpeg -i 320x240.avi -f lavfi -i color=gray -i 320x240.avi -f lavfi -i color=white -lavfi threshold output.avi
39.256 thumbnail
Select the most representative frame in a given sequence of consecutive frames.
The filter accepts the following options:
n
Set the frames batch size to analyze; in a set of n frames, the filter
will pick one of them, and then handle the next batch of n frames until
the end. Default is 100.
log
Set the log level to display picked frame stats.
Default is info.
Since the filter keeps track of the whole frames sequence, a bigger n
value will result in a higher memory usage, so a high value is not recommended.
39.256.1 Examples
Extract one picture each 50 frames:
thumbnail=50
Complete example of a thumbnail creation with ffmpeg:
ffmpeg -i in.avi -vf thumbnail,scale=300:200 -frames:v 1 out.png
39.257 tile
Tile several successive frames together.
The untile filter can do the reverse.
The filter accepts the following options:
layout
Set the grid size in the form COLUMNSxROWS. Range is up to UINT_MAX cells.
Default is 6x5.
nb_frames
Set the maximum number of frames to render in the given area. It must be less
than or equal to wxh. The default value is 0, meaning all
the area will be used.
margin
Set the outer border margin in pixels. Range is 0 to 1024. Default is 0.
padding
Set the inner border thickness (i.e. the number of pixels between frames). For
more advanced padding options (such as having different values for the edges),
refer to the pad video filter. Range is 0 to 1024. Default is 0.
color
Specify the color of the unused area. For the syntax of this option, check the
(ffmpeg-utils)"Color" section in the ffmpeg-utils manual.
The default value of color is "black".
overlap
Set the number of frames to overlap when tiling several successive frames together.
The value must be between 0 and nb_frames - 1. Default is 0.
init_padding
Set the number of frames to initially be empty before displaying first output frame.
This controls how soon will one get first output frame.
The value must be between 0 and nb_frames - 1. Default is 0.
39.257.1 Examples
Produce 8x8 PNG tiles of all keyframes (-skip_frame nokey) in a movie:
ffmpeg -skip_frame nokey -i file.avi -vf 'scale=128:72,tile=8x8' -an -vsync 0 keyframes%03d.png
The -vsync 0 is necessary to prevent ffmpeg from
duplicating each output frame to accommodate the originally detected frame
rate.
Display 5 pictures in an area of 3x2 frames,
with 7 pixels between them, and 2 pixels of initial margin, using
mixed flat and named options:
tile=3x2:nb_frames=5:padding=7:margin=2
39.258 tiltandshift
Apply tilt-and-shift effect.
What happens when you invert time and space?
Normally a video is composed of several frames that represent a different
instant of time and shows a scene that evolves in the space captured by the
frame. This filter is the antipode of that concept, taking inspiration from
tilt and shift photography.
A filtered frame contains the whole timeline of events composing the sequence,
and this is obtained by placing a slice of pixels from each frame into a single
one. However, since there are no infinite-width frames, this is done up the
width of the input frame, and a video is recomposed by shifting away one
column for each subsequent frame. In order to map space to time, the filter
tilts each input frame as well, so that motion is preserved. This is accomplished
by progressively selecting a different column from each input frame.
The end result is a sort of inverted parallax, so that far away objects move
much faster that the ones in the front. The ideal conditions for this video
effect are when there is either very little motion and the backgroud is static,
or when there is a lot of motion and a very wide depth of field (e.g. wide
panorama, while moving on a train).
The filter accepts the following parameters:
tilt
Tilt video while shifting (default). When unset, video will be sliding a
static image, composed of the first column of each frame.
start
What to do at the start of filtering (see below).
end
What to do at the end of filtering (see below).
hold
How many columns should pass through before start of filtering.
pad
How many columns should be inserted before end of filtering.
Normally the filter shifts and tilts from the very first frame, and stops when
the last one is received. However, before filtering starts, normal video may
be preseved, so that the effect is slowly shifted in its place. Similarly,
the last video frame may be reconstructed at the end. Alternatively it is
possible to just start and end with black.
‘none’
Filtering starts immediately and ends when the last frame is received.
‘frame’
The first frames or the very last frame are kept intact during processing.
‘black’
Black is padded at the beginning or at the end of filtering.
39.259 tinterlace
Perform various types of temporal field interlacing.
Frames are counted starting from 1, so the first input frame is
considered odd.
The filter accepts the following options:
mode
Specify the mode of the interlacing. This option can also be specified
as a value alone. See below for a list of values for this option.
Available values are:
‘merge, 0’
Move odd frames into the upper field, even into the lower field,
generating a double height frame at half frame rate.
------> time
Input:
Frame 1         Frame 2         Frame 3         Frame 4
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
Output:
11111                           33333
22222                           44444
11111                           33333
22222                           44444
11111                           33333
22222                           44444
11111                           33333
22222                           44444
‘drop_even, 1’
Only output odd frames, even frames are dropped, generating a frame with
unchanged height at half frame rate.
------> time
Input:
Frame 1         Frame 2         Frame 3         Frame 4
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
Output:
11111                           33333
11111                           33333
11111                           33333
11111                           33333
‘drop_odd, 2’
Only output even frames, odd frames are dropped, generating a frame with
unchanged height at half frame rate.
------> time
Input:
Frame 1         Frame 2         Frame 3         Frame 4
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
Output:
22222                           44444
22222                           44444
22222                           44444
22222                           44444
‘pad, 3’
Expand each frame to full height, but pad alternate lines with black,
generating a frame with double height at the same input frame rate.
------> time
Input:
Frame 1         Frame 2         Frame 3         Frame 4
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
Output:
11111           .....           33333           .....
.....           22222           .....           44444
11111           .....           33333           .....
.....           22222           .....           44444
11111           .....           33333           .....
.....           22222           .....           44444
11111           .....           33333           .....
.....           22222           .....           44444
‘interleave_top, 4’
Interleave the upper field from odd frames with the lower field from
even frames, generating a frame with unchanged height at half frame rate.
------> time
Input:
Frame 1         Frame 2         Frame 3         Frame 4
11111<-         22222           33333<-         44444
11111           22222<-         33333           44444<-
11111<-         22222           33333<-         44444
11111           22222<-         33333           44444<-
Output:
11111                           33333
22222                           44444
11111                           33333
22222                           44444
‘interleave_bottom, 5’
Interleave the lower field from odd frames with the upper field from
even frames, generating a frame with unchanged height at half frame rate.
------> time
Input:
Frame 1         Frame 2         Frame 3         Frame 4
11111           22222<-         33333           44444<-
11111<-         22222           33333<-         44444
11111           22222<-         33333           44444<-
11111<-         22222           33333<-         44444
Output:
22222                           44444
11111                           33333
22222                           44444
11111                           33333
‘interlacex2, 6’
Double frame rate with unchanged height. Frames are inserted each
containing the second temporal field from the previous input frame and
the first temporal field from the next input frame. This mode relies on
the top_field_first flag. Useful for interlaced video displays with no
field synchronisation.
------> time
Input:
Frame 1         Frame 2         Frame 3         Frame 4
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
Output:
11111   22222   22222   33333   33333   44444   44444
11111   11111   22222   22222   33333   33333   44444
11111   22222   22222   33333   33333   44444   44444
11111   11111   22222   22222   33333   33333   44444
‘mergex2, 7’
Move odd frames into the upper field, even into the lower field,
generating a double height frame at same frame rate.
------> time
Input:
Frame 1         Frame 2         Frame 3         Frame 4
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
11111           22222           33333           44444
Output:
11111           33333           33333           55555
22222           22222           44444           44444
11111           33333           33333           55555
22222           22222           44444           44444
11111           33333           33333           55555
22222           22222           44444           44444
11111           33333           33333           55555
22222           22222           44444           44444
Numeric values are deprecated but are accepted for backward
compatibility reasons.
Default mode is merge.
flags
Specify flags influencing the filter process.
Available value for flags is:
low_pass_filter, vlpf
Enable linear vertical low-pass filtering in the filter.
Vertical low-pass filtering is required when creating an interlaced
destination from a progressive source which contains high-frequency
vertical detail. Filtering will reduce interlace ’twitter’ and Moire
patterning.
complex_filter, cvlpf
Enable complex vertical low-pass filtering.
This will slightly less reduce interlace ’twitter’ and Moire
patterning but better retain detail and subjective sharpness impression.
bypass_il
Bypass already interlaced frames, only adjust the frame rate.
Vertical low-pass filtering and bypassing already interlaced frames can only be
enabled for mode interleave_top and interleave_bottom.
39.260 tmedian
Pick median pixels from several successive input video frames.
The filter accepts the following options:
radius
Set radius of median filter.
Default is 1. Allowed range is from 1 to 127.
planes
Set which planes to filter. Default value is 15, by which all planes are processed.
percentile
Set median percentile. Default value is 0.5.
Default value of 0.5 will pick always median values, while 0 will pick
minimum values, and 1 maximum values.
39.260.1 Commands
This filter supports all above options as commands, excluding option radius.
39.261 tmidequalizer
Apply Temporal Midway Video Equalization effect.
Midway Video Equalization adjusts a sequence of video frames to have the same
histograms, while maintaining their dynamics as much as possible. It’s
useful for e.g. matching exposures from a video frames sequence.
This filter accepts the following option:
radius
Set filtering radius. Default is 5. Allowed range is from 1 to 127.
sigma
Set filtering sigma. Default is 0.5. This controls strength of filtering.
Setting this option to 0 effectively does nothing.
planes
Set which planes to process. Default is 15, which is all available planes.
39.262 tmix
Mix successive video frames.
A description of the accepted options follows.
frames
The number of successive frames to mix. If unspecified, it defaults to 3.
weights
Specify weight of each input video frame.
Each weight is separated by space. If number of weights is smaller than
number of frames last specified weight will be used for all remaining
unset weights.
scale
Specify scale, if it is set it will be multiplied with sum
of each weight multiplied with pixel values to give final destination
pixel value. By default scale is auto scaled to sum of weights.
planes
Set which planes to filter. Default is all. Allowed range is from 0 to 15.
39.262.1 Examples
Average 7 successive frames:
tmix=frames=7:weights="1 1 1 1 1 1 1"
Apply simple temporal convolution:
tmix=frames=3:weights="-1 3 -1"
Similar as above but only showing temporal differences:
tmix=frames=3:weights="-1 2 -1":scale=1
39.262.2 Commands
This filter supports the following commands:
weights
scale
planes
Syntax is same as option with same name.
39.263 tonemap
Tone map colors from different dynamic ranges.
This filter expects data in single precision floating point, as it needs to
operate on (and can output) out-of-range values. Another filter, such as
zscale, is needed to convert the resulting frame to a usable format.
The tonemapping algorithms implemented only work on linear light, so input
data should be linearized beforehand (and possibly correctly tagged).
ffmpeg -i INPUT -vf zscale=transfer=linear,tonemap=clip,zscale=transfer=bt709,format=yuv420p OUTPUT
39.263.1 Options
The filter accepts the following options.
tonemap
Set the tone map algorithm to use.
Possible values are:
none
Do not apply any tone map, only desaturate overbright pixels.
clip
Hard-clip any out-of-range values. Use it for perfect color accuracy for
in-range values, while distorting out-of-range values.
linear
Stretch the entire reference gamut to a linear multiple of the display.
gamma
Fit a logarithmic transfer between the tone curves.
reinhard
Preserve overall image brightness with a simple curve, using nonlinear
contrast, which results in flattening details and degrading color accuracy.
hable
Preserve both dark and bright details better than reinhard, at the cost
of slightly darkening everything. Use it when detail preservation is more
important than color and brightness accuracy.
mobius
Smoothly map out-of-range values, while retaining contrast and colors for
in-range material as much as possible. Use it when color accuracy is more
important than detail preservation.
Default is none.
param
Tune the tone mapping algorithm.
This affects the following algorithms:
none
Ignored.
linear
Specifies the scale factor to use while stretching.
Default to 1.0.
gamma
Specifies the exponent of the function.
Default to 1.8.
clip
Specify an extra linear coefficient to multiply into the signal before clipping.
Default to 1.0.
reinhard
Specify the local contrast coefficient at the display peak.
Default to 0.5, which means that in-gamut values will be about half as bright
as when clipping.
hable
Ignored.
mobius
Specify the transition point from linear to mobius transform. Every value
below this point is guaranteed to be mapped 1:1. The higher the value, the
more accurate the result will be, at the cost of losing bright details.
Default to 0.3, which due to the steep initial slope still preserves in-range
colors fairly accurately.
desat
Apply desaturation for highlights that exceed this level of brightness. The
higher the parameter, the more color information will be preserved. This
setting helps prevent unnaturally blown-out colors for super-highlights, by
(smoothly) turning into white instead. This makes images feel more natural,
at the cost of reducing information about out-of-range colors.
The default of 2.0 is somewhat conservative and will mostly just apply to
skies or directly sunlit surfaces. A setting of 0.0 disables this option.
This option works only if the input frame has a supported color tag.
peak
Override signal/nominal/reference peak with this value. Useful when the
embedded peak information in display metadata is not reliable or when tone
mapping from a lower range to a higher range.
39.264 tpad
Temporarily pad video frames.
The filter accepts the following options:
start
Specify number of delay frames before input video stream. Default is 0.
stop
Specify number of padding frames after input video stream.
Set to -1 to pad indefinitely. Default is 0.
start_mode
Set kind of frames added to beginning of stream.
Can be either add or clone.
With add frames of solid-color are added.
With clone frames are clones of first frame.
Default is add.
stop_mode
Set kind of frames added to end of stream.
Can be either add or clone.
With add frames of solid-color are added.
With clone frames are clones of last frame.
Default is add.
start_duration, stop_duration
Specify the duration of the start/stop delay. See
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
These options override start and stop. Default is 0.
color
Specify the color of the padded area. For the syntax of this option,
check the (ffmpeg-utils)"Color" section in the ffmpeg-utils
manual.
The default value of color is "black".
39.265 transpose
Transpose rows with columns in the input video and optionally flip it.
It accepts the following parameters:
dir
Specify the transposition direction.
Can assume the following values:
‘0, 4, cclock_flip’
Rotate by 90 degrees counterclockwise and vertically flip (default), that is:
L.R     L.l
. . ->  . .
l.r     R.r
‘1, 5, clock’
Rotate by 90 degrees clockwise, that is:
L.R     l.L
. . ->  . .
l.r     r.R
‘2, 6, cclock’
Rotate by 90 degrees counterclockwise, that is:
L.R     R.r
. . ->  . .
l.r     L.l
‘3, 7, clock_flip’
Rotate by 90 degrees clockwise and vertically flip, that is:
L.R     r.R
. . ->  . .
l.r     l.L
For values between 4-7, the transposition is only done if the input
video geometry is portrait and not landscape. These values are
deprecated, the passthrough option should be used instead.
Numerical values are deprecated, and should be dropped in favor of
symbolic constants.
passthrough
Do not apply the transposition if the input geometry matches the one
specified by the specified value. It accepts the following values:
‘none’
Always apply transposition.
‘portrait’
Preserve portrait geometry (when height >= width).
‘landscape’
Preserve landscape geometry (when width >= height).
Default value is none.
For example to rotate by 90 degrees clockwise and preserve portrait
layout:
transpose=dir=1:passthrough=portrait
The command above can also be specified as:
transpose=1:portrait
39.266 transpose_npp
Transpose rows with columns in the input video and optionally flip it.
For more in depth examples see the transpose video filter, which shares mostly the same options.
It accepts the following parameters:
dir
Specify the transposition direction.
Can assume the following values:
‘cclock_flip’
Rotate by 90 degrees counterclockwise and vertically flip. (default)
‘clock’
Rotate by 90 degrees clockwise.
‘cclock’
Rotate by 90 degrees counterclockwise.
‘clock_flip’
Rotate by 90 degrees clockwise and vertically flip.
passthrough
Do not apply the transposition if the input geometry matches the one
specified by the specified value. It accepts the following values:
‘none’
Always apply transposition. (default)
‘portrait’
Preserve portrait geometry (when height >= width).
‘landscape’
Preserve landscape geometry (when width >= height).
39.267 trim
Trim the input so that the output contains one continuous subpart of the input.
It accepts the following parameters:
start
Specify the time of the start of the kept section, i.e. the frame with the
timestamp start will be the first frame in the output.
end
Specify the time of the first frame that will be dropped, i.e. the frame
immediately preceding the one with the timestamp end will be the last
frame in the output.
start_pts
This is the same as start, except this option sets the start timestamp
in timebase units instead of seconds.
end_pts
This is the same as end, except this option sets the end timestamp
in timebase units instead of seconds.
duration
The maximum duration of the output in seconds.
start_frame
The number of the first frame that should be passed to the output.
end_frame
The number of the first frame that should be dropped.
start, end, and duration are expressed as time
duration specifications; see
(ffmpeg-utils)the Time duration section in the ffmpeg-utils(1) manual
for the accepted syntax.
Note that the first two sets of the start/end options and the duration
option look at the frame timestamp, while the _frame variants simply count the
frames that pass through the filter. Also note that this filter does not modify
the timestamps. If you wish for the output timestamps to start at zero, insert a
setpts filter after the trim filter.
If multiple start or end options are set, this filter tries to be greedy and
keep all the frames that match at least one of the specified constraints. To keep
only the part that matches all the constraints at once, chain multiple trim
filters.
The defaults are such that all the input is kept. So it is possible to set e.g.
just the end values to keep everything before the specified time.
Examples:
Drop everything except the second minute of input:
ffmpeg -i INPUT -vf trim=60:120
Keep only the first second:
ffmpeg -i INPUT -vf trim=duration=1
39.268 unpremultiply
Apply alpha unpremultiply effect to input video stream using first plane
of second stream as alpha.
Both streams must have same dimensions and same pixel format.
The filter accepts the following option:
planes
Set which planes will be processed, unprocessed planes will be copied.
By default value 0xf, all planes will be processed.
If the format has 1 or 2 components, then luma is bit 0.
If the format has 3 or 4 components:
for RGB formats bit 0 is green, bit 1 is blue and bit 2 is red;
for YUV formats bit 0 is luma, bit 1 is chroma-U and bit 2 is chroma-V.
If present, the alpha channel is always the last bit.
inplace
Do not require 2nd input for processing, instead use alpha plane from input stream.
39.269 unsharp
Sharpen or blur the input video.
It accepts the following parameters:
luma_msize_x, lx
Set the luma matrix horizontal size. It must be an odd integer between
3 and 23. The default value is 5.
luma_msize_y, ly
Set the luma matrix vertical size. It must be an odd integer between 3
and 23. The default value is 5.
luma_amount, la
Set the luma effect strength. It must be a floating point number, reasonable
values lay between -1.5 and 1.5.
Negative values will blur the input video, while positive values will
sharpen it, a value of zero will disable the effect.
Default value is 1.0.
chroma_msize_x, cx
Set the chroma matrix horizontal size. It must be an odd integer
between 3 and 23. The default value is 5.
chroma_msize_y, cy
Set the chroma matrix vertical size. It must be an odd integer
between 3 and 23. The default value is 5.
chroma_amount, ca
Set the chroma effect strength. It must be a floating point number, reasonable
values lay between -1.5 and 1.5.
Negative values will blur the input video, while positive values will
sharpen it, a value of zero will disable the effect.
Default value is 0.0.
alpha_msize_x, ax
Set the alpha matrix horizontal size. It must be an odd integer
between 3 and 23. The default value is 5.
alpha_msize_y, ay
Set the alpha matrix vertical size. It must be an odd integer
between 3 and 23. The default value is 5.
alpha_amount, aa
Set the alpha effect strength. It must be a floating point number, reasonable
values lay between -1.5 and 1.5.
Negative values will blur the input video, while positive values will
sharpen it, a value of zero will disable the effect.
Default value is 0.0.
All parameters are optional and default to the equivalent of the
string ’5:5:1.0:5:5:0.0’.
39.269.1 Examples
Apply strong luma sharpen effect:
unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=2.5
Apply a strong blur of both luma and chroma parameters:
unsharp=7:7:-2:7:7:-2
39.270 untile
Decompose a video made of tiled images into the individual images.
The frame rate of the output video is the frame rate of the input video
multiplied by the number of tiles.
This filter does the reverse of tile.
The filter accepts the following options:
layout
Set the grid size (i.e. the number of lines and columns). For the syntax of
this option, check the
(ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.
39.270.1 Examples
Produce a 1-second video from a still image file made of 25 frames stacked
vertically, like an analogic film reel:
ffmpeg -r 1 -i image.jpg -vf untile=1x25 movie.mkv
39.271 uspp
Apply ultra slow/simple postprocessing filter that compresses and decompresses
the image at several (or - in the case of quality level 8 - all)
shifts and average the results.
The way this differs from the behavior of spp is that uspp actually encodes &
decodes each case with libavcodec Snow, whereas spp uses a simplified intra only 8x8
DCT similar to MJPEG.
This filter is not available in ffmpeg versions between 5.0 and 6.0.
The filter accepts the following options:
quality
Set quality. This option defines the number of levels for averaging. It accepts
an integer in the range 0-8. If set to 0, the filter will have no
effect. A value of 8 means the higher quality. For each increment of
that value the speed drops by a factor of approximately 2.  Default value is
3.
qp
Force a constant quantization parameter. If not set, the filter will use the QP
from the video stream (if available).
codec
Use specified codec instead of snow.
39.272 v360
Convert 360 videos between various formats.
The filter accepts the following options:
input
output
Set format of the input/output video.
Available formats:
‘e’
‘equirect’
Equirectangular projection.
‘c3x2’
‘c6x1’
‘c1x6’
Cubemap with 3x2/6x1/1x6 layout.
Format specific options:
in_pad
out_pad
Set padding proportion for the input/output cubemap. Values in decimals.
Example values:
‘0’
No padding.
‘0.01’
1% of face is padding. For example, with 1920x1280 resolution face size would be 640x640 and padding would be 3 pixels from each side. (640 * 0.01 = 6 pixels)
Default value is ‘0’.
Maximum value is ‘0.1’.
fin_pad
fout_pad
Set fixed padding for the input/output cubemap. Values in pixels.
Default value is ‘0’. If greater than zero it overrides other padding options.
in_forder
out_forder
Set order of faces for the input/output cubemap. Choose one direction for each position.
Designation of directions:
‘r’
right
‘l’
left
‘u’
up
‘d’
down
‘f’
forward
‘b’
back
Default value is ‘rludfb’.
in_frot
out_frot
Set rotation of faces for the input/output cubemap. Choose one angle for each position.
Designation of angles:
‘0’
0 degrees clockwise
‘1’
90 degrees clockwise
‘2’
180 degrees clockwise
‘3’
270 degrees clockwise
Default value is ‘000000’.
‘eac’
Equi-Angular Cubemap.
‘flat’
‘gnomonic’
‘rectilinear’
Regular video.
Format specific options:
h_fov
v_fov
d_fov
Set output horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
ih_fov
iv_fov
id_fov
Set input horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
‘dfisheye’
Dual fisheye.
Format specific options:
h_fov
v_fov
d_fov
Set output horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
ih_fov
iv_fov
id_fov
Set input horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
‘barrel’
‘fb’
‘barrelsplit’
Facebook’s 360 formats.
‘sg’
Stereographic format.
Format specific options:
h_fov
v_fov
d_fov
Set output horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
ih_fov
iv_fov
id_fov
Set input horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
‘mercator’
Mercator format.
‘ball’
Ball format, gives significant distortion toward the back.
‘hammer’
Hammer-Aitoff map projection format.
‘sinusoidal’
Sinusoidal map projection format.
‘fisheye’
Fisheye projection.
Format specific options:
h_fov
v_fov
d_fov
Set output horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
ih_fov
iv_fov
id_fov
Set input horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
‘pannini’
Pannini projection.
Format specific options:
h_fov
Set output pannini parameter.
ih_fov
Set input pannini parameter.
‘cylindrical’
Cylindrical projection.
Format specific options:
h_fov
v_fov
d_fov
Set output horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
ih_fov
iv_fov
id_fov
Set input horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
‘perspective’
Perspective projection. (output only)
Format specific options:
v_fov
Set perspective parameter.
‘tetrahedron’
Tetrahedron projection.
‘tsp’
Truncated square pyramid projection.
‘he’
‘hequirect’
Half equirectangular projection.
‘equisolid’
Equisolid format.
Format specific options:
h_fov
v_fov
d_fov
Set output horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
ih_fov
iv_fov
id_fov
Set input horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
‘og’
Orthographic format.
Format specific options:
h_fov
v_fov
d_fov
Set output horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
ih_fov
iv_fov
id_fov
Set input horizontal/vertical/diagonal field of view. Values in degrees.
If diagonal field of view is set it overrides horizontal and vertical field of view.
‘octahedron’
Octahedron projection.
‘cylindricalea’
Cylindrical Equal Area projection.
interp
Set interpolation method.
Note: more complex interpolation methods require much more memory to run.
Available methods:
‘near’
‘nearest’
Nearest neighbour.
‘line’
‘linear’
Bilinear interpolation.
‘lagrange9’
Lagrange9 interpolation.
‘cube’
‘cubic’
Bicubic interpolation.
‘lanc’
‘lanczos’
Lanczos interpolation.
‘sp16’
‘spline16’
Spline16 interpolation.
‘gauss’
‘gaussian’
Gaussian interpolation.
‘mitchell’
Mitchell interpolation.
Default value is ‘line’.
w
h
Set the output video resolution.
Default resolution depends on formats.
in_stereo
out_stereo
Set the input/output stereo format.
‘2d’
2D mono
‘sbs’
Side by side
‘tb’
Top bottom
Default value is ‘2d’ for input and output format.
yaw
pitch
roll
Set rotation for the output video. Values in degrees.
rorder
Set rotation order for the output video. Choose one item for each position.
‘y, Y’
yaw
‘p, P’
pitch
‘r, R’
roll
Default value is ‘ypr’.
h_flip
v_flip
d_flip
Flip the output video horizontally(swaps left-right)/vertically(swaps up-down)/in-depth(swaps back-forward). Boolean values.
ih_flip
iv_flip
Set if input video is flipped horizontally/vertically. Boolean values.
in_trans
Set if input video is transposed. Boolean value, by default disabled.
out_trans
Set if output video needs to be transposed. Boolean value, by default disabled.
h_offset
v_offset
Set output horizontal/vertical off-axis offset. Default is set to 0.
Allowed range is from -1 to 1.
alpha_mask
Build mask in alpha plane for all unmapped pixels by marking them fully transparent. Boolean value, by default disabled.
reset_rot
Reset rotation of output video. Boolean value, by default disabled.
39.272.1 Examples
Convert equirectangular video to cubemap with 3x2 layout and 1% padding using bicubic interpolation:
ffmpeg -i input.mkv -vf v360=e:c3x2:cubic:out_pad=0.01 output.mkv
Extract back view of Equi-Angular Cubemap:
ffmpeg -i input.mkv -vf v360=eac:flat:yaw=180 output.mkv
Convert transposed and horizontally flipped Equi-Angular Cubemap in side-by-side stereo format to equirectangular top-bottom stereo format:
v360=eac:equirect:in_stereo=sbs:in_trans=1:ih_flip=1:out_stereo=tb
39.272.2 Commands
This filter supports subset of above options as commands.
39.273 vaguedenoiser
Apply a wavelet based denoiser.
It transforms each frame from the video input into the wavelet domain,
using Cohen-Daubechies-Feauveau 9/7. Then it applies some filtering to
the obtained coefficients. It does an inverse wavelet transform after.
Due to wavelet properties, it should give a nice smoothed result, and
reduced noise, without blurring picture features.
This filter accepts the following options:
threshold
The filtering strength. The higher, the more filtered the video will be.
Hard thresholding can use a higher threshold than soft thresholding
before the video looks overfiltered. Default value is 2.
method
The filtering method the filter will use.
It accepts the following values:
‘hard’
All values under the threshold will be zeroed.
‘soft’
All values under the threshold will be zeroed. All values above will be
reduced by the threshold.
‘garrote’
Scales or nullifies coefficients - intermediary between (more) soft and
(less) hard thresholding.
Default is garrote.
nsteps
Number of times, the wavelet will decompose the picture. Picture can’t
be decomposed beyond a particular point (typically, 8 for a 640x480
frame - as 2^9 = 512 > 480). Valid values are integers between 1 and 32. Default value is 6.
percent
Partial of full denoising (limited coefficients shrinking), from 0 to 100. Default value is 85.
planes
A list of the planes to process. By default all planes are processed.
type
The threshold type the filter will use.
It accepts the following values:
‘universal’
Threshold used is same for all decompositions.
‘bayes’
Threshold used depends also on each decomposition coefficients.
Default is universal.
39.274 varblur
Apply variable blur filter by using 2nd video stream to set blur radius.
The 2nd stream must have the same dimensions.
This filter accepts the following options:
min_r
Set min allowed radius. Allowed range is from 0 to 254. Default is 0.
max_r
Set max allowed radius. Allowed range is from 1 to 255. Default is 8.
planes
Set which planes to process. By default, all are used.
The varblur filter also supports the framesync options.
39.274.1 Commands
This filter supports all the above options as commands.
39.275 vectorscope
Display 2 color component values in the two dimensional graph (which is called
a vectorscope).
This filter accepts the following options:
mode, m
Set vectorscope mode.
It accepts the following values:
‘gray’
‘tint’
Gray values are displayed on graph, higher brightness means more pixels have
same component color value on location in graph. This is the default mode.
‘color’
Gray values are displayed on graph. Surrounding pixels values which are not
present in video frame are drawn in gradient of 2 color components which are
set by option x and y. The 3rd color component is static.
‘color2’
Actual color components values present in video frame are displayed on graph.
‘color3’
Similar as color2 but higher frequency of same values x and y
on graph increases value of another color component, which is luminance by
default values of x and y.
‘color4’
Actual colors present in video frame are displayed on graph. If two different
colors map to same position on graph then color with higher value of component
not present in graph is picked.
‘color5’
Gray values are displayed on graph. Similar to color but with 3rd color
component picked from radial gradient.
x
Set which color component will be represented on X-axis. Default is 1.
y
Set which color component will be represented on Y-axis. Default is 2.
intensity, i
Set intensity, used by modes: gray, color, color3 and color5 for increasing brightness
of color component which represents frequency of (X, Y) location in graph.
envelope, e
‘none’
No envelope, this is default.
‘instant’
Instant envelope, even darkest single pixel will be clearly highlighted.
‘peak’
Hold maximum and minimum values presented in graph over time. This way you
can still spot out of range values without constantly looking at vectorscope.
‘peak+instant’
Peak and instant envelope combined together.
graticule, g
Set what kind of graticule to draw.
‘none’
‘green’
‘color’
‘invert’
opacity, o
Set graticule opacity.
flags, f
Set graticule flags.
‘white’
Draw graticule for white point.
‘black’
Draw graticule for black point.
‘name’
Draw color points short names.
bgopacity, b
Set background opacity.
lthreshold, l
Set low threshold for color component not represented on X or Y axis.
Values lower than this value will be ignored. Default is 0.
Note this value is multiplied with actual max possible value one pixel component
can have. So for 8-bit input and low threshold value of 0.1 actual threshold
is 0.1 * 255 = 25.
hthreshold, h
Set high threshold for color component not represented on X or Y axis.
Values higher than this value will be ignored. Default is 1.
Note this value is multiplied with actual max possible value one pixel component
can have. So for 8-bit input and high threshold value of 0.9 actual threshold
is 0.9 * 255 = 230.
colorspace, c
Set what kind of colorspace to use when drawing graticule.
‘auto’
‘601’
‘709’
Default is auto.
tint0, t0
tint1, t1
Set color tint for gray/tint vectorscope mode. By default both options are zero.
This means no tint, and output will remain gray.
39.276 vidstabdetect
Analyze video stabilization/deshaking. Perform pass 1 of 2, see
vidstabtransform for pass 2.
This filter generates a file with relative translation and rotation
transform information about subsequent frames, which is then used by
the vidstabtransform filter.
To enable compilation of this filter you need to configure FFmpeg with
--enable-libvidstab.
This filter accepts the following options:
result
Set the path to the file used to write the transforms information.
Default value is transforms.trf.
shakiness
Set how shaky the video is and how quick the camera is. It accepts an
integer in the range 1-10, a value of 1 means little shakiness, a
value of 10 means strong shakiness. Default value is 5.
accuracy
Set the accuracy of the detection process. It must be a value in the
range 1-15. A value of 1 means low accuracy, a value of 15 means high
accuracy. Default value is 15.
stepsize
Set stepsize of the search process. The region around minimum is
scanned with 1 pixel resolution. Default value is 6.
mincontrast
Set minimum contrast. Below this value a local measurement field is
discarded. Must be a floating point value in the range 0-1. Default
value is 0.3.
tripod
Set reference frame number for tripod mode.
If enabled, the motion of the frames is compared to a reference frame
in the filtered stream, identified by the specified number. The idea
is to compensate all movements in a more-or-less static scene and keep
the camera view absolutely still.
If set to 0, it is disabled. The frames are counted starting from 1.
show
Show fields and transforms in the resulting frames. It accepts an
integer in the range 0-2. Default value is 0, which disables any
visualization.
fileformat
Format for the transforms data file to be written.
Acceptable values are
‘ascii’
Human-readable plain text
‘binary’
Binary format, roughly 40% smaller than ascii. (default)
39.276.1 Examples
Use default values:
vidstabdetect
Analyze strongly shaky movie and put the results in file
mytransforms.trf:
vidstabdetect=shakiness=10:accuracy=15:result="mytransforms.trf"
Visualize the result of internal transformations in the resulting
video:
vidstabdetect=show=1
Analyze a video with medium shakiness using ffmpeg:
ffmpeg -i input -vf vidstabdetect=shakiness=5:show=1 dummy.avi
39.277 vidstabtransform
Video stabilization/deshaking: pass 2 of 2,
see vidstabdetect for pass 1.
Read a file with transform information for each frame and
apply/compensate them. Together with the vidstabdetect
filter this can be used to deshake videos. See also
http://public.hronopik.de/vid.stab. It is important to also use
the unsharp filter, see below.
To enable compilation of this filter you need to configure FFmpeg with
--enable-libvidstab.
39.277.1 Options
input
Set path to the file used to read the transforms. Default value is
transforms.trf.
smoothing
Set the number of frames (value*2 + 1) used for lowpass filtering the
camera movements. Default value is 10.
For example a number of 10 means that 21 frames are used (10 in the
past and 10 in the future) to smoothen the motion in the video. A
larger value leads to a smoother video, but limits the acceleration of
the camera (pan/tilt movements). 0 is a special case where a static
camera is simulated.
optalgo
Set the camera path optimization algorithm.
Accepted values are:
‘gauss’
gaussian kernel low-pass filter on camera motion (default)
‘avg’
averaging on transformations
maxshift
Set maximal number of pixels to translate frames. Default value is -1,
meaning no limit.
maxangle
Set maximal angle in radians (degree*PI/180) to rotate frames. Default
value is -1, meaning no limit.
crop
Specify how to deal with borders that may be visible due to movement
compensation.
Available values are:
‘keep’
keep image information from previous frame (default)
‘black’
fill the border black
invert
Invert transforms if set to 1. Default value is 0.
relative
Consider transforms as relative to previous frame if set to 1,
absolute if set to 0. Default value is 0.
zoom
Set percentage to zoom. A positive value will result in a zoom-in
effect, a negative value in a zoom-out effect. Default value is 0 (no
zoom).
optzoom
Set optimal zooming to avoid borders.
Accepted values are:
‘0’
disabled
‘1’
optimal static zoom value is determined (only very strong movements
will lead to visible borders) (default)
‘2’
optimal adaptive zoom value is determined (no borders will be
visible), see zoomspeed
Note that the value given at zoom is added to the one calculated here.
zoomspeed
Set percent to zoom maximally each frame (enabled when
optzoom is set to 2). Range is from 0 to 5, default value is
0.25.
interpol
Specify type of interpolation.
Available values are:
‘no’
no interpolation
‘linear’
linear only horizontal
‘bilinear’
linear in both directions (default)
‘bicubic’
cubic in both directions (slow)
tripod
Enable virtual tripod mode if set to 1, which is equivalent to
relative=0:smoothing=0. Default value is 0.
Use also tripod option of vidstabdetect.
debug
Increase log verbosity if set to 1. Also the detected global motions
are written to the temporary file global_motions.trf. Default
value is 0.
39.277.2 Examples
Use ffmpeg for a typical stabilization with default values:
ffmpeg -i inp.mpeg -vf vidstabtransform,unsharp=5:5:0.8:3:3:0.4 inp_stabilized.mpeg
Note the use of the unsharp filter which is always recommended.
Zoom in a bit more and load transform data from a given file:
vidstabtransform=zoom=5:input="mytransforms.trf"
Smoothen the video even more:
vidstabtransform=smoothing=30
39.278 vflip
Flip the input video vertically.
For example, to vertically flip a video with ffmpeg:
ffmpeg -i in.avi -vf "vflip" out.avi
39.279 vfrdet
Detect variable frame rate video.
This filter tries to detect if the input is variable or constant frame rate.
At end it will output number of frames detected as having variable delta pts,
and ones with constant delta pts.
If there was frames with variable delta, than it will also show min, max and
average delta encountered.
39.280 vibrance
Boost or alter saturation.
The filter accepts the following options:
intensity
Set strength of boost if positive value or strength of alter if negative value.
Default is 0. Allowed range is from -2 to 2.
rbal
Set the red balance. Default is 1. Allowed range is from -10 to 10.
gbal
Set the green balance. Default is 1. Allowed range is from -10 to 10.
bbal
Set the blue balance. Default is 1. Allowed range is from -10 to 10.
rlum
Set the red luma coefficient.
glum
Set the green luma coefficient.
blum
Set the blue luma coefficient.
alternate
If intensity is negative and this is set to 1, colors will change,
otherwise colors will be less saturated, more towards gray.
39.280.1 Commands
This filter supports the all above options as commands.
39.281 vif
Obtain the average VIF (Visual Information Fidelity) between two input videos.
This filter takes two input videos.
Both input videos must have the same resolution and pixel format for
this filter to work correctly. Also it assumes that both inputs
have the same number of frames, which are compared one by one.
The obtained average VIF score is printed through the logging system.
The filter stores the calculated VIF score of each frame.
This filter also supports the framesync options.
In the below example the input file main.mpg being processed is compared
with the reference file ref.mpg.
ffmpeg -i main.mpg -i ref.mpg -lavfi vif -f null -
39.282 vignette
Make or reverse a natural vignetting effect.
The filter accepts the following options:
angle, a
Set lens angle expression as a number of radians.
The value is clipped in the [0,PI/2] range.
Default value: "PI/5"
x0
y0
Set center coordinates expressions. Respectively "w/2" and "h/2"
by default.
mode
Set forward/backward mode.
Available modes are:
‘forward’
The larger the distance from the central point, the darker the image becomes.
‘backward’
The larger the distance from the central point, the brighter the image becomes.
This can be used to reverse a vignette effect, though there is no automatic
detection to extract the lens angle and other settings (yet). It can
also be used to create a burning effect.
Default value is ‘forward’.
eval
Set evaluation mode for the expressions (angle, x0, y0).
It accepts the following values:
‘init’
Evaluate expressions only once during the filter initialization.
‘frame’
Evaluate expressions for each incoming frame. This is way slower than the
‘init’ mode since it requires all the scalers to be re-computed, but it
allows advanced dynamic expressions.
Default value is ‘init’.
dither
Set dithering to reduce the circular banding effects. Default is 1
(enabled).
aspect
Set vignette aspect. This setting allows one to adjust the shape of the vignette.
Setting this value to the SAR of the input will make a rectangular vignetting
following the dimensions of the video.
Default is 1/1.
39.282.1 Expressions
The alpha, x0 and y0 expressions can contain the
following parameters.
w
h
input width and height
n
the number of input frame, starting from 0
pts
the PTS (Presentation TimeStamp) time of the filtered video frame, expressed in
TB units, NAN if undefined
r
frame rate of the input video, NAN if the input frame rate is unknown
t
the PTS (Presentation TimeStamp) of the filtered video frame,
expressed in seconds, NAN if undefined
tb
time base of the input video
39.282.2 Examples
Apply simple strong vignetting effect:
vignette=PI/4
Make a flickering vignetting:
vignette='PI/4+random(1)*PI/50':eval=frame
39.283 vmafmotion
Obtain the average VMAF motion score of a video.
It is one of the component metrics of VMAF.
The obtained average motion score is printed through the logging system.
The filter accepts the following options:
stats_file
If specified, the filter will use the named file to save the motion score of
each frame with respect to the previous frame.
When filename equals "-" the data is sent to standard output.
Example:
ffmpeg -i ref.mpg -vf vmafmotion -f null -
39.284 vstack
Stack input videos vertically.
All streams must be of same pixel format and of same width.
Note that this filter is faster than using overlay and pad filter
to create same output.
The filter accepts the following options:
inputs
Set number of input streams. Default is 2.
shortest
If set to 1, force the output to terminate when the shortest input
terminates. Default value is 0.
39.285 w3fdif
Deinterlace the input video ("w3fdif" stands for "Weston 3 Field
Deinterlacing Filter").
Based on the process described by Martin Weston for BBC R&D, and
implemented based on the de-interlace algorithm written by Jim
Easterbrook for BBC R&D, the Weston 3 field deinterlacing filter
uses filter coefficients calculated by BBC R&D.
This filter uses field-dominance information in frame to decide which
of each pair of fields to place first in the output.
If it gets it wrong use setfield filter before w3fdif filter.
There are two sets of filter coefficients, so called "simple"
and "complex". Which set of filter coefficients is used can
be set by passing an optional parameter:
filter
Set the interlacing filter coefficients. Accepts one of the following values:
‘simple’
Simple filter coefficient set.
‘complex’
More-complex filter coefficient set.
Default value is ‘complex’.
mode
The interlacing mode to adopt. It accepts one of the following values:
frame
Output one frame for each frame.
field
Output one frame for each field.
The default value is field.
parity
The picture field parity assumed for the input interlaced video. It accepts one
of the following values:
tff
Assume the top field is first.
bff
Assume the bottom field is first.
auto
Enable automatic detection of field parity.
The default value is auto.
If the interlacing is unknown or the decoder does not export this information,
top field first will be assumed.
deint
Specify which frames to deinterlace. Accepts one of the following values:
‘all’
Deinterlace all frames,
‘interlaced’
Only deinterlace frames marked as interlaced.
Default value is ‘all’.
39.285.1 Commands
This filter supports same commands as options.
39.286 waveform
Video waveform monitor.
The waveform monitor plots color component intensity. By default luma
only. Each column of the waveform corresponds to a column of pixels in the
source video.
It accepts the following options:
mode, m
Can be either row, or column. Default is column.
In row mode, the graph on the left side represents color component value 0 and
the right side represents value = 255. In column mode, the top side represents
color component value = 0 and bottom side represents value = 255.
intensity, i
Set intensity. Smaller values are useful to find out how many values of the same
luminance are distributed across input rows/columns.
Default value is 0.04. Allowed range is [0, 1].
mirror, r
Set mirroring mode. 0 means unmirrored, 1 means mirrored.
In mirrored mode, higher values will be represented on the left
side for row mode and at the top for column mode. Default is
1 (mirrored).
display, d
Set display mode.
It accepts the following values:
‘overlay’
Presents information identical to that in the parade, except
that the graphs representing color components are superimposed directly
over one another.
This display mode makes it easier to spot relative differences or similarities
in overlapping areas of the color components that are supposed to be identical,
such as neutral whites, grays, or blacks.
‘stack’
Display separate graph for the color components side by side in
row mode or one below the other in column mode.
‘parade’
Display separate graph for the color components side by side in
column mode or one below the other in row mode.
Using this display mode makes it easy to spot color casts in the highlights
and shadows of an image, by comparing the contours of the top and the bottom
graphs of each waveform. Since whites, grays, and blacks are characterized
by exactly equal amounts of red, green, and blue, neutral areas of the picture
should display three waveforms of roughly equal width/height. If not, the
correction is easy to perform by making level adjustments the three waveforms.
Default is stack.
components, c
Set which color components to display. Default is 1, which means only luma
or red color component if input is in RGB colorspace. If is set for example to
7 it will display all 3 (if) available color components.
envelope, e
‘none’
No envelope, this is default.
‘instant’
Instant envelope, minimum and maximum values presented in graph will be easily
visible even with small step value.
‘peak’
Hold minimum and maximum values presented in graph across time. This way you
can still spot out of range values without constantly looking at waveforms.
‘peak+instant’
Peak and instant envelope combined together.
filter, f
‘lowpass’
No filtering, this is default.
‘flat’
Luma and chroma combined together.
‘aflat’
Similar as above, but shows difference between blue and red chroma.
‘xflat’
Similar as above, but use different colors.
‘yflat’
Similar as above, but again with different colors.
‘chroma’
Displays only chroma.
‘color’
Displays actual color value on waveform.
‘acolor’
Similar as above, but with luma showing frequency of chroma values.
graticule, g
Set which graticule to display.
‘none’
Do not display graticule.
‘green’
Display green graticule showing legal broadcast ranges.
‘orange’
Display orange graticule showing legal broadcast ranges.
‘invert’
Display invert graticule showing legal broadcast ranges.
opacity, o
Set graticule opacity.
flags, fl
Set graticule flags.
‘numbers’
Draw numbers above lines. By default enabled.
‘dots’
Draw dots instead of lines.
scale, s
Set scale used for displaying graticule.
‘digital’
‘millivolts’
‘ire’
Default is digital.
bgopacity, b
Set background opacity.
tint0, t0
tint1, t1
Set tint for output.
Only used with lowpass filter and when display is not overlay and input
pixel formats are not RGB.
fitmode, fm
Set sample aspect ratio of video output frames.
Can be used to configure waveform so it is not
streched too much in one of directions.
‘none’
Set sample aspect ration to 1/1.
‘size’
Set sample aspect ratio to match input size of video
Default is ‘none’.
input
Set input formats for filter to pick from.
Can be ‘all’, for selecting from all available formats,
or ‘first’, for selecting first available format.
Default is ‘first’.
39.287 weave, doubleweave
The weave takes a field-based video input and join
each two sequential fields into single frame, producing a new double
height clip with half the frame rate and half the frame count.
The doubleweave works same as weave but without
halving frame rate and frame count.
It accepts the following option:
first_field
Set first field. Available values are:
‘top, t’
Set the frame as top-field-first.
‘bottom, b’
Set the frame as bottom-field-first.
39.287.1 Examples
Interlace video using select and separatefields filter:
separatefields,select=eq(mod(n,4),0)+eq(mod(n,4),3),weave
39.288 xbr
Apply the xBR high-quality magnification filter which is designed for pixel
art. It follows a set of edge-detection rules, see
https://forums.libretro.com/t/xbr-algorithm-tutorial/123.
It accepts the following option:
n
Set the scaling dimension: 2 for 2xBR, 3 for
3xBR and 4 for 4xBR.
Default is 3.
39.289 xcorrelate
Apply normalized cross-correlation between first and second input video stream.
Second input video stream dimensions must be lower than first input video stream.
The filter accepts the following options:
planes
Set which planes to process.
secondary
Set which secondary video frames will be processed from second input video stream,
can be first or all. Default is all.
The xcorrelate filter also supports the framesync options.
39.290 xfade
Apply cross fade from one input video stream to another input video stream.
The cross fade is applied for specified duration.
Both inputs must be constant frame-rate and have the same resolution, pixel format,
frame rate and timebase.
The filter accepts the following options:
transition
Set one of available transition effects:
‘custom’
‘fade’
‘wipeleft’
‘wiperight’
‘wipeup’
‘wipedown’
‘slideleft’
‘slideright’
‘slideup’
‘slidedown’
‘circlecrop’
‘rectcrop’
‘distance’
‘fadeblack’
‘fadewhite’
‘radial’
‘smoothleft’
‘smoothright’
‘smoothup’
‘smoothdown’
‘circleopen’
‘circleclose’
‘vertopen’
‘vertclose’
‘horzopen’
‘horzclose’
‘dissolve’
‘pixelize’
‘diagtl’
‘diagtr’
‘diagbl’
‘diagbr’
‘hlslice’
‘hrslice’
‘vuslice’
‘vdslice’
‘hblur’
‘fadegrays’
‘wipetl’
‘wipetr’
‘wipebl’
‘wipebr’
‘squeezeh’
‘squeezev’
‘zoomin’
‘fadefast’
‘fadeslow’
‘hlwind’
‘hrwind’
‘vuwind’
‘vdwind’
‘coverleft’
‘coverright’
‘coverup’
‘coverdown’
‘revealleft’
‘revealright’
‘revealup’
‘revealdown’
Default transition effect is fade.
duration
Set cross fade duration in seconds.
Range is 0 to 60 seconds.
Default duration is 1 second.
offset
Set cross fade start relative to first input stream in seconds.
Default offset is 0.
expr
Set expression for custom transition effect.
The expressions can use the following variables and functions:
X
Y
The coordinates of the current sample.
W
H
The width and height of the image.
P
Progress of transition effect.
PLANE
Currently processed plane.
A
Return value of first input at current location and plane.
B
Return value of second input at current location and plane.
a0(x, y)
a1(x, y)
a2(x, y)
a3(x, y)
Return the value of the pixel at location (x,y) of the
first/second/third/fourth component of first input.
b0(x, y)
b1(x, y)
b2(x, y)
b3(x, y)
Return the value of the pixel at location (x,y) of the
first/second/third/fourth component of second input.
39.290.1 Examples
Cross fade from one input video to another input video, with fade transition and duration of transition
of 2 seconds starting at offset of 5 seconds:
ffmpeg -i first.mp4 -i second.mp4 -filter_complex xfade=transition=fade:duration=2:offset=5 output.mp4
39.291 xmedian
Pick median pixels from several input videos.
The filter accepts the following options:
inputs
Set number of inputs.
Default is 3. Allowed range is from 3 to 255.
If number of inputs is even number, than result will be mean value between two median values.
planes
Set which planes to filter. Default value is 15, by which all planes are processed.
percentile
Set median percentile. Default value is 0.5.
Default value of 0.5 will pick always median values, while 0 will pick
minimum values, and 1 maximum values.
39.291.1 Commands
This filter supports all above options as commands, excluding option inputs.
39.292 xpsnr
Obtain the average (across all input frames) and minimum (across all color plane averages)
eXtended Perceptually weighted peak Signal-to-Noise Ratio (XPSNR) between two input videos.
The XPSNR is a low-complexity psychovisually motivated distortion measurement algorithm for
assessing the difference between two video streams or images. This is especially useful for
objectively quantifying the distortions caused by video and image codecs, as an alternative
to a formal subjective test. The logarithmic XPSNR output values are in a similar range as
those of traditional psnr assessments but better reflect human impressions of visual
coding quality. More details on the XPSNR measure, which essentially represents a blockwise
weighted variant of the PSNR measure, can be found in the following freely available papers:
C. R. Helmrich, M. Siekmann, S. Becker, S. Bosse, D. Marpe, and T. Wiegand, "XPSNR: A
Low-Complexity Extension of the Perceptually Weighted Peak Signal-to-Noise Ratio for
High-Resolution Video Quality Assessment," in Proc. IEEE Int. Conf. Acoustics, Speech,
Sig. Process. (ICASSP), virt./online, May 2020. www.ecodis.de/xpsnr.htm
C. R. Helmrich, S. Bosse, H. Schwarz, D. Marpe, and T. Wiegand, "A Study of the
Extended Perceptually Weighted Peak Signal-to-Noise Ratio (XPSNR) for Video Compression
with Different Resolutions and Bit Depths," ITU Journal: ICT Discoveries, vol. 3, no.
1, pp. 65 - 72, May 2020. http://handle.itu.int/11.1002/pub/8153d78b-en
When publishing the results of XPSNR assessments obtained using, e.g., this FFmpeg filter, a
reference to the above papers as a means of documentation is strongly encouraged. The filter
requires two input videos. The first input is considered a (usually not distorted) reference
source and is passed unchanged to the output, whereas the second input is a (distorted) test
signal. Except for the bit depth, these two video inputs must have the same pixel format. In
addition, for best performance, both compared input videos should be in YCbCr color format.
The obtained overall XPSNR values mentioned above are printed through the logging system. In
case of input with multiple color planes, we suggest reporting of the minimum XPSNR average.
The following parameter, which behaves like the one for the psnr filter, is accepted:
stats_file, f
If specified, the filter will use the named file to save the XPSNR value of each individual
frame and color plane. When the file name equals "-", that data is sent to standard output.
This filter also supports the framesync options.
39.292.1 Examples
XPSNR analysis of two 1080p HD videos, ref_source.yuv and test_video.yuv, both at 24 frames
per second, with color format 4:2:0, bit depth 8, and output of a logfile named "xpsnr.log":
ffmpeg -s 1920x1080 -framerate 24 -pix_fmt yuv420p -i ref_source.yuv -s 1920x1080 -framerate
24 -pix_fmt yuv420p -i test_video.yuv -lavfi xpsnr="stats_file=xpsnr.log" -f null -
XPSNR analysis of two 2160p UHD videos, ref_source.yuv with bit depth 8 and test_video.yuv
with bit depth 10, both at 60 frames per second with color format 4:2:0, no logfile output:
ffmpeg -s 3840x2160 -framerate 60 -pix_fmt yuv420p -i ref_source.yuv -s 3840x2160 -framerate
60 -pix_fmt yuv420p10le -i test_video.yuv -lavfi xpsnr="stats_file=-" -f null -
39.293 xstack
Stack video inputs into custom layout.
All streams must be of same pixel format.
The filter accepts the following options:
inputs
Set number of input streams. Default is 2.
layout
Specify layout of inputs.
This option requires the desired layout configuration to be explicitly set by the user.
This sets position of each video input in output. Each input
is separated by ’|’.
The first number represents the column, and the second number represents the row.
Numbers start at 0 and are separated by ’_’. Optionally one can use wX and hX,
where X is video input from which to take width or height.
Multiple values can be used when separated by ’+’. In such
case values are summed together.
Note that if inputs are of different sizes gaps may appear, as not all of
the output video frame will be filled. Similarly, videos can overlap each
other if their position doesn’t leave enough space for the full frame of
adjoining videos.
For 2 inputs, a default layout of 0_0|w0_0 (equivalent to
grid=2x1) is set. In all other cases, a layout or a grid must be set by
the user. Either grid or layout can be specified at a time.
Specifying both will result in an error.
grid
Specify a fixed size grid of inputs.
This option is used to create a fixed size grid of the input streams. Set the
grid size in the form COLUMNSxROWS. There must be ROWS * COLUMNS
input streams and they will be arranged as a grid with ROWS rows and
COLUMNS columns. When using this option, each input stream within a row
must have the same height and all the rows must have the same width.
If grid is set, then inputs option is ignored and is implicitly
set to ROWS * COLUMNS.
For 2 inputs, a default grid of 2x1 (equivalent to
layout=0_0|w0_0) is set. In all other cases, a layout or a grid must be
set by the user. Either grid or layout can be specified at a time.
Specifying both will result in an error.
shortest
If set to 1, force the output to terminate when the shortest input
terminates. Default value is 0.
fill
If set to valid color, all unused pixels will be filled with that color.
By default fill is set to none, so it is disabled.
39.293.1 Examples
Display 4 inputs into 2x2 grid.
Layout:
input1(0, 0)  | input3(w0, 0)
input2(0, h0) | input4(w0, h0)
xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0
Note that if inputs are of different sizes, gaps or overlaps may occur.
Display 4 inputs into 1x4 grid.
Layout:
input1(0, 0)
input2(0, h0)
input3(0, h0+h1)
input4(0, h0+h1+h2)
xstack=inputs=4:layout=0_0|0_h0|0_h0+h1|0_h0+h1+h2
Note that if inputs are of different widths, unused space will appear.
Display 9 inputs into 3x3 grid.
Layout:
input1(0, 0)       | input4(w0, 0)      | input7(w0+w3, 0)
input2(0, h0)      | input5(w0, h0)     | input8(w0+w3, h0)
input3(0, h0+h1)   | input6(w0, h0+h1)  | input9(w0+w3, h0+h1)
xstack=inputs=9:layout=0_0|0_h0|0_h0+h1|w0_0|w0_h0|w0_h0+h1|w0+w3_0|w0+w3_h0|w0+w3_h0+h1
Note that if inputs are of different sizes, gaps or overlaps may occur.
Display 16 inputs into 4x4 grid.
Layout:
input1(0, 0)       | input5(w0, 0)       | input9 (w0+w4, 0)       | input13(w0+w4+w8, 0)
input2(0, h0)      | input6(w0, h0)      | input10(w0+w4, h0)      | input14(w0+w4+w8, h0)
input3(0, h0+h1)   | input7(w0, h0+h1)   | input11(w0+w4, h0+h1)   | input15(w0+w4+w8, h0+h1)
input4(0, h0+h1+h2)| input8(w0, h0+h1+h2)| input12(w0+w4, h0+h1+h2)| input16(w0+w4+w8, h0+h1+h2)
xstack=inputs=16:layout=0_0|0_h0|0_h0+h1|0_h0+h1+h2|w0_0|w0_h0|w0_h0+h1|w0_h0+h1+h2|w0+w4_0|
w0+w4_h0|w0+w4_h0+h1|w0+w4_h0+h1+h2|w0+w4+w8_0|w0+w4+w8_h0|w0+w4+w8_h0+h1|w0+w4+w8_h0+h1+h2
Note that if inputs are of different sizes, gaps or overlaps may occur.
39.294 yadif
Deinterlace the input video ("yadif" means "yet another deinterlacing
filter").
It accepts the following parameters:
mode
The interlacing mode to adopt. It accepts one of the following values:
0, send_frame
Output one frame for each frame.
1, send_field
Output one frame for each field.
2, send_frame_nospatial
Like send_frame, but it skips the spatial interlacing check.
3, send_field_nospatial
Like send_field, but it skips the spatial interlacing check.
The default value is send_frame.
parity
The picture field parity assumed for the input interlaced video. It accepts one
of the following values:
0, tff
Assume the top field is first.
1, bff
Assume the bottom field is first.
-1, auto
Enable automatic detection of field parity.
The default value is auto.
If the interlacing is unknown or the decoder does not export this information,
top field first will be assumed.
deint
Specify which frames to deinterlace. Accepts one of the following
values:
0, all
Deinterlace all frames.
1, interlaced
Only deinterlace frames marked as interlaced.
The default value is all.
39.295 yadif_cuda
Deinterlace the input video using the yadif algorithm, but implemented
in CUDA so that it can work as part of a GPU accelerated pipeline with nvdec
and/or nvenc.
It accepts the following parameters:
mode
The interlacing mode to adopt. It accepts one of the following values:
0, send_frame
Output one frame for each frame.
1, send_field
Output one frame for each field.
2, send_frame_nospatial
Like send_frame, but it skips the spatial interlacing check.
3, send_field_nospatial
Like send_field, but it skips the spatial interlacing check.
The default value is send_frame.
parity
The picture field parity assumed for the input interlaced video. It accepts one
of the following values:
0, tff
Assume the top field is first.
1, bff
Assume the bottom field is first.
-1, auto
Enable automatic detection of field parity.
The default value is auto.
If the interlacing is unknown or the decoder does not export this information,
top field first will be assumed.
deint
Specify which frames to deinterlace. Accepts one of the following
values:
0, all
Deinterlace all frames.
1, interlaced
Only deinterlace frames marked as interlaced.
The default value is all.
39.296 yaepblur
Apply blur filter while preserving edges ("yaepblur" means "yet another edge preserving blur filter").
The algorithm is described in
"J. S. Lee, Digital image enhancement and noise filtering by use of local statistics, IEEE Trans. Pattern Anal. Mach. Intell. PAMI-2, 1980."
It accepts the following parameters:
radius, r
Set the window radius. Default value is 3.
planes, p
Set which planes to filter. Default is only the first plane.
sigma, s
Set blur strength. Default value is 128.
39.296.1 Commands
This filter supports same commands as options.
39.297 zoompan
Apply Zoom & Pan effect.
This filter accepts the following options:
zoom, z
Set the zoom expression. Range is 1-10. Default is 1.
x
y
Set the x and y expression. Default is 0.
d
Set the duration expression in number of frames.
This sets for how many number of frames effect will last for
single input image. Default is 90.
s
Set the output image size, default is ’hd720’.
fps
Set the output frame rate, default is ’25’.
Each expression can contain the following constants:
in_w, iw
Input width.
in_h, ih
Input height.
out_w, ow
Output width.
out_h, oh
Output height.
in
Input frame count.
on
Output frame count.
in_time, it
The input timestamp expressed in seconds. It’s NAN if the input timestamp is unknown.
out_time, time, ot
The output timestamp expressed in seconds.
x
y
Last calculated ’x’ and ’y’ position from ’x’ and ’y’ expression
for current input frame.
px
py
’x’ and ’y’ of last output frame of previous input frame or 0 when there was
not yet such frame (first input frame).
zoom
Last calculated zoom from ’z’ expression for current input frame.
pzoom
Last calculated zoom of last output frame of previous input frame.
duration
Number of output frames for current input frame. Calculated from ’d’ expression
for each input frame.
pduration
number of output frames created for previous input frame
a
Rational number: input width / input height
sar
sample aspect ratio
dar
display aspect ratio
39.297.1 Examples
Zoom in up to 1.5x and pan at same time to some spot near center of picture:
zoompan=z='min(zoom+0.0015,1.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a)':y='if(gte(zoom,1.5),y,y+1)':s=640x360
Zoom in up to 1.5x and pan always at center of picture:
zoompan=z='min(zoom+0.0015,1.5)':d=700:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'
Same as above but without pausing:
zoompan=z='min(max(zoom,pzoom)+0.0015,1.5)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'
Zoom in 2x into center of picture only for the first second of the input video:
zoompan=z='if(between(in_time,0,1),2,1)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'
39.298 zscale
Scale (resize) the input video, using the z.lib library:
https://github.com/sekrit-twc/zimg. To enable compilation of this
filter, you need to configure FFmpeg with --enable-libzimg.
The zscale filter forces the output display aspect ratio to be the same
as the input, by changing the output sample aspect ratio.
If the input image format is different from the format requested by
the next filter, the zscale filter will convert the input to the
requested format.
39.298.1 Options
The filter accepts the following options.
width, w
height, h
Set the output video dimension expression. Default value is the input
dimension.
If the width or w value is 0, the input width is used for
the output. If the height or h value is 0, the input height
is used for the output.
If one and only one of the values is -n with n >= 1, the zscale filter
will use a value that maintains the aspect ratio of the input image,
calculated from the other specified dimension. After that it will,
however, make sure that the calculated dimension is divisible by n and
adjust the value if necessary.
If both values are -n with n >= 1, the behavior will be identical to
both values being set to 0 as previously detailed.
See below for the list of accepted constants for use in the dimension
expression.
size, s
Set the video size. For the syntax of this option, check the
(ffmpeg-utils)"Video size" section in the ffmpeg-utils manual.
dither, d
Set the dither type.
Possible values are:
none
ordered
random
error_diffusion
Default is none.
filter, f
Set the resize filter type.
Possible values are:
point
bilinear
bicubic
spline16
spline36
lanczos
Default is bilinear.
range, r
Set the color range.
Possible values are:
input
limited
full
Default is same as input.
primaries, p
Set the color primaries.
Possible values are:
input
709
unspecified
170m
240m
2020
Default is same as input.
transfer, t
Set the transfer characteristics.
Possible values are:
input
709
unspecified
601
linear
2020_10
2020_12
smpte2084
iec61966-2-1
arib-std-b67
Default is same as input.
matrix, m
Set the colorspace matrix.
Possible value are:
input
709
unspecified
470bg
170m
2020_ncl
2020_cl
Default is same as input.
rangein, rin
Set the input color range.
Possible values are:
input
limited
full
Default is same as input.
primariesin, pin
Set the input color primaries.
Possible values are:
input
709
unspecified
170m
240m
2020
Default is same as input.
transferin, tin
Set the input transfer characteristics.
Possible values are:
input
709
unspecified
601
linear
2020_10
2020_12
Default is same as input.
matrixin, min
Set the input colorspace matrix.
Possible value are:
input
709
unspecified
470bg
170m
2020_ncl
2020_cl
chromal, c
Set the output chroma location.
Possible values are:
input
left
center
topleft
top
bottomleft
bottom
chromalin, cin
Set the input chroma location.
Possible values are:
input
left
center
topleft
top
bottomleft
bottom
npl
Set the nominal peak luminance.
param_a
Parameter A for scaling filters. Parameter "b" for bicubic, and the number of
filter taps for lanczos.
param_b
Parameter B for scaling filters. Parameter "c" for bicubic.
The values of the w and h options are expressions
containing the following constants:
in_w
in_h
The input width and height
iw
ih
These are the same as in_w and in_h.
out_w
out_h
The output (scaled) width and height
ow
oh
These are the same as out_w and out_h
a
The same as iw / ih
sar
input sample aspect ratio
dar
The input display aspect ratio. Calculated from (iw / ih) * sar.
hsub
vsub
horizontal and vertical input chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
ohsub
ovsub
horizontal and vertical output chroma subsample values. For example for the
pixel format "yuv422p" hsub is 2 and vsub is 1.
39.298.2 Commands
This filter supports the following commands:
width, w
height, h
Set the output video dimension expression.
The command accepts the same syntax of the corresponding option.
If the specified expression is not valid, it is kept at its current
value.