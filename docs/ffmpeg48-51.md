48 External libraries
48.1 Alliance for Open Media (AOM)
48.2 AMD AMF/VCE
48.3 AviSynth
48.4 Chromaprint
48.5 codec2
48.6 dav1d
48.7 davs2
48.8 uavs3d
48.9 Game Music Emu
48.10 Intel QuickSync Video
48.11 Kvazaar
48.12 LAME
48.13 LCEVCdec
48.14 libilbc
48.15 libjxl
48.16 libvpx
48.17 ModPlug
48.18 OpenCORE, VisualOn, and Fraunhofer libraries
48.18.1 OpenCORE AMR
48.18.2 VisualOn AMR-WB encoder library
48.18.3 Fraunhofer AAC library
48.18.4 LC3 library
48.19 OpenH264
48.20 OpenJPEG
48.21 rav1e
48.22 SVT-AV1
48.23 TwoLAME
48.24 VapourSynth
48.25 x264
48.26 x265
48.27 xavs
48.28 xavs2
48.29 eXtra-fast Essential Video Encoder (XEVE)
48.30 eXtra-fast Essential Video Decoder (XEVD)
48.31 ZVBI
49 Supported File Formats, Codecs or Features
49.1 File Formats
49.2 Image Formats
49.3 Video Codecs
49.4 Audio Codecs
49.5 Subtitle Formats
49.6 Network Protocols
49.7 Input/Output Devices
49.8 Timecode
50 See Also
51 Authors

48 External libraries
FFmpeg can be hooked up with a number of external libraries to add support
for more formats. None of them are used by default, their use has to be
explicitly requested by passing the appropriate flags to
./configure.
48.1 Alliance for Open Media (AOM)
FFmpeg can make use of the AOM library for AV1 decoding and encoding.
Go to http://aomedia.org/ and follow the instructions for
installing the library. Then pass --enable-libaom to configure to
enable it.
48.2 AMD AMF/VCE
FFmpeg can use the AMD Advanced Media Framework library
for accelerated H.264 and HEVC(only windows) encoding on hardware with Video Coding Engine (VCE).
To enable support you must obtain the AMF framework header files(version 1.4.9+) from
https://github.com/GPUOpen-LibrariesAndSDKs/AMF.git.
Create an AMF/ directory in the system include path.
Copy the contents of AMF/amf/public/include/ into that directory.
Then configure FFmpeg with --enable-amf.
Initialization of amf encoder occurs in this order:
1) trying to initialize through dx11(only windows)
2) trying to initialize through dx9(only windows)
3) trying to initialize through vulkan
To use h.264(AMD VCE) encoder on linux amdgru-pro version 19.20+ and amf-amdgpu-pro
package(amdgru-pro contains, but does not install automatically) are required.
This driver can be installed using amdgpu-pro-install script in official amd driver archive.
48.3 AviSynth
FFmpeg can read AviSynth scripts as input. To enable support, pass
--enable-avisynth to configure after installing the headers
provided by AviSynth+.
AviSynth+ can be configured to install only the headers by either
passing -DHEADERS_ONLY:bool=on to the normal CMake-based build
system, or by using the supplied GNUmakefile.
For Windows, supported AviSynth variants are
AviSynth 2.6 RC1 or higher for 32-bit builds and
AviSynth+ r1718 or higher for 32-bit and 64-bit builds.
For Linux, macOS, and BSD, the only supported AviSynth variant is
AviSynth+, starting with version 3.5.
In 2016, AviSynth+ added support for building with GCC. However, due to
the eccentricities of Windows’ calling conventions, 32-bit GCC builds
of AviSynth+ are not compatible with typical 32-bit builds of FFmpeg.
By default, FFmpeg assumes compatibility with 32-bit MSVC builds of
AviSynth+ since that is the most widely-used and entrenched build
configuration.  Users can override this and enable support for 32-bit
GCC builds of AviSynth+ by passing -DAVSC_WIN32_GCC32 to
--extra-cflags when configuring FFmpeg.
64-bit builds of FFmpeg are not affected, and can use either MSVC or
GCC builds of AviSynth+ without any special flags.
AviSynth(+) is loaded dynamically.  Distributors can build FFmpeg
with --enable-avisynth, and the binaries will work regardless
of the end user having AviSynth installed.  If/when an end user
would like to use AviSynth scripts, then they can install AviSynth(+)
and FFmpeg will be able to find and use it to open scripts.
48.4 Chromaprint
FFmpeg can make use of the Chromaprint library for generating audio fingerprints.
Pass --enable-chromaprint to configure to
enable it. See https://acoustid.org/chromaprint.
48.5 codec2
FFmpeg can make use of the codec2 library for codec2 decoding and encoding.
There is currently no native decoder, so libcodec2 must be used for decoding.
Go to http://freedv.org/, download "Codec 2 source archive".
Build and install using CMake. Debian users can install the libcodec2-dev package instead.
Once libcodec2 is installed you can pass --enable-libcodec2 to configure to enable it.
The easiest way to use codec2 is with .c2 files, since they contain the mode information required for decoding.
To encode such a file, use a .c2 file extension and give the libcodec2 encoder the -mode option:
ffmpeg -i input.wav -mode 700C output.c2.
Playback is as simple as ffplay output.c2.
For a list of supported modes, run ffmpeg -h encoder=libcodec2.
Raw codec2 files are also supported.
To make sense of them the mode in use needs to be specified as a format option:
ffmpeg -f codec2raw -mode 1300 -i input.raw output.wav.
48.6 dav1d
FFmpeg can make use of the dav1d library for AV1 video decoding.
Go to https://code.videolan.org/videolan/dav1d and follow the instructions for
installing the library. Then pass --enable-libdav1d to configure to enable it.
48.7 davs2
FFmpeg can make use of the davs2 library for AVS2-P2/IEEE1857.4 video decoding.
Go to https://github.com/pkuvcl/davs2 and follow the instructions for
installing the library. Then pass --enable-libdavs2 to configure to
enable it.
libdavs2 is under the GNU Public License Version 2 or later
(see http://www.gnu.org/licenses/old-licenses/gpl-2.0.html for
details), you must upgrade FFmpeg’s license to GPL in order to use it.
48.8 uavs3d
FFmpeg can make use of the uavs3d library for AVS3-P2/IEEE1857.10 video decoding.
Go to https://github.com/uavs3/uavs3d and follow the instructions for
installing the library. Then pass --enable-libuavs3d to configure to
enable it.
48.9 Game Music Emu
FFmpeg can make use of the Game Music Emu library to read audio from supported video game
music file formats. Pass --enable-libgme to configure to
enable it. See https://bitbucket.org/mpyne/game-music-emu/overview.
48.10 Intel QuickSync Video
FFmpeg can use Intel QuickSync Video (QSV) for accelerated decoding and encoding
of multiple codecs. To use QSV, FFmpeg must be linked against the libmfx
dispatcher, which loads the actual decoding libraries.
The dispatcher is open source and can be downloaded from
https://github.com/lu-zero/mfx_dispatch.git. FFmpeg needs to be configured
with the --enable-libmfx option and pkg-config needs to be able to
locate the dispatcher’s .pc files.
48.11 Kvazaar
FFmpeg can make use of the Kvazaar library for HEVC encoding.
Go to https://github.com/ultravideo/kvazaar and follow the
instructions for installing the library. Then pass
--enable-libkvazaar to configure to enable it.
48.12 LAME
FFmpeg can make use of the LAME library for MP3 encoding.
Go to http://lame.sourceforge.net/ and follow the
instructions for installing the library.
Then pass --enable-libmp3lame to configure to enable it.
48.13 LCEVCdec
FFmpeg can make use of the liblcevc_dec library for LCEVC enhacement layer
decoding on supported bitstreams.
Go to https://github.com/v-novaltd/LCEVCdec and follow the instructions
for installing the library. Then pass --enable-liblcevc-dec to configure to
enable it.
LCEVCdec is under the BSD-3-Clause-Clear License.
48.14 libilbc
iLBC is a narrowband speech codec that has been made freely available
by Google as part of the WebRTC project. libilbc is a packaging friendly
copy of the iLBC codec. FFmpeg can make use of the libilbc library for
iLBC decoding and encoding.
Go to https://github.com/TimothyGu/libilbc and follow the instructions for
installing the library. Then pass --enable-libilbc to configure to
enable it.
48.15 libjxl
JPEG XL is an image format intended to fully replace legacy JPEG for an extended
period of life. See https://jpegxl.info/ for more information, and see
https://github.com/libjxl/libjxl for the library source. You can pass
--enable-libjxl to configure in order enable the libjxl wrapper.
48.16 libvpx
FFmpeg can make use of the libvpx library for VP8/VP9 decoding and encoding.
Go to http://www.webmproject.org/ and follow the instructions for
installing the library. Then pass --enable-libvpx to configure to
enable it.
48.17 ModPlug
FFmpeg can make use of this library, originating in Modplug-XMMS, to read from MOD-like music files.
See https://github.com/Konstanty/libmodplug. Pass --enable-libmodplug to configure to
enable it.
48.18 OpenCORE, VisualOn, and Fraunhofer libraries
Spun off Google Android sources, OpenCore, VisualOn and Fraunhofer
libraries provide encoders for a number of audio codecs.
OpenCORE and VisualOn libraries are under the Apache License 2.0
(see http://www.apache.org/licenses/LICENSE-2.0 for details), which is
incompatible to the LGPL version 2.1 and GPL version 2. You have to
upgrade FFmpeg’s license to LGPL version 3 (or if you have enabled
GPL components, GPL version 3) by passing --enable-version3 to configure in
order to use it.
The license of the Fraunhofer AAC library is incompatible with the GPL.
Therefore, for GPL builds, you have to pass --enable-nonfree to
configure in order to use it. To the best of our knowledge, it is
compatible with the LGPL.
48.18.1 OpenCORE AMR
FFmpeg can make use of the OpenCORE libraries for AMR-NB
decoding/encoding and AMR-WB decoding.
Go to http://sourceforge.net/projects/opencore-amr/ and follow the
instructions for installing the libraries.
Then pass --enable-libopencore-amrnb and/or
--enable-libopencore-amrwb to configure to enable them.
48.18.2 VisualOn AMR-WB encoder library
FFmpeg can make use of the VisualOn AMR-WBenc library for AMR-WB encoding.
Go to http://sourceforge.net/projects/opencore-amr/ and follow the
instructions for installing the library.
Then pass --enable-libvo-amrwbenc to configure to enable it.
48.18.3 Fraunhofer AAC library
FFmpeg can make use of the Fraunhofer AAC library for AAC decoding & encoding.
Go to http://sourceforge.net/projects/opencore-amr/ and follow the
instructions for installing the library.
Then pass --enable-libfdk-aac to configure to enable it.
48.18.4 LC3 library
FFmpeg can make use of the Google LC3 library for LC3 decoding & encoding.
Go to https://github.com/google/liblc3/ and follow the instructions for
installing the library.
Then pass --enable-liblc3 to configure to enable it.
48.19 OpenH264
FFmpeg can make use of the OpenH264 library for H.264 decoding and encoding.
Go to http://www.openh264.org/ and follow the instructions for
installing the library. Then pass --enable-libopenh264 to configure to
enable it.
For decoding, this library is much more limited than the built-in decoder
in libavcodec; currently, this library lacks support for decoding B-frames
and some other main/high profile features. (It currently only supports
constrained baseline profile and CABAC.) Using it is mostly useful for
testing and for taking advantage of Cisco’s patent portfolio license
(http://www.openh264.org/BINARY_LICENSE.txt).
48.20 OpenJPEG
FFmpeg can use the OpenJPEG libraries for decoding/encoding J2K videos.  Go to
http://www.openjpeg.org/ to get the libraries and follow the installation
instructions.  To enable using OpenJPEG in FFmpeg, pass --enable-libopenjpeg to
./configure.
48.21 rav1e
FFmpeg can make use of rav1e (Rust AV1 Encoder) via its C bindings to encode videos.
Go to https://github.com/xiph/rav1e/ and follow the instructions to build
the C library. To enable using rav1e in FFmpeg, pass --enable-librav1e
to ./configure.
48.22 SVT-AV1
FFmpeg can make use of the Scalable Video Technology for AV1 library for AV1 encoding.
Go to https://gitlab.com/AOMediaCodec/SVT-AV1/ and follow the instructions
for installing the library. Then pass --enable-libsvtav1 to configure to
enable it.
48.23 TwoLAME
FFmpeg can make use of the TwoLAME library for MP2 encoding.
Go to http://www.twolame.org/ and follow the
instructions for installing the library.
Then pass --enable-libtwolame to configure to enable it.
48.24 VapourSynth
FFmpeg can read VapourSynth scripts as input. To enable support, pass
--enable-vapoursynth to configure. Vapoursynth is detected via
pkg-config. Versions 42 or greater supported.
See http://www.vapoursynth.com/.
Due to security concerns, Vapoursynth scripts will not
be autodetected so the input format has to be forced. For ff* CLI tools,
add -f vapoursynth before the input -i yourscript.vpy.
48.25 x264
FFmpeg can make use of the x264 library for H.264 encoding.
Go to http://www.videolan.org/developers/x264.html and follow the
instructions for installing the library. Then pass --enable-libx264 to
configure to enable it.
x264 is under the GNU Public License Version 2 or later
(see http://www.gnu.org/licenses/old-licenses/gpl-2.0.html for
details), you must upgrade FFmpeg’s license to GPL in order to use it.
48.26 x265
FFmpeg can make use of the x265 library for HEVC encoding.
Go to http://x265.org/developers.html and follow the instructions
for installing the library. Then pass --enable-libx265 to configure
to enable it.
x265 is under the GNU Public License Version 2 or later
(see http://www.gnu.org/licenses/old-licenses/gpl-2.0.html for
details), you must upgrade FFmpeg’s license to GPL in order to use it.
48.27 xavs
FFmpeg can make use of the xavs library for AVS encoding.
Go to http://xavs.sf.net/ and follow the instructions for
installing the library. Then pass --enable-libxavs to configure to
enable it.
48.28 xavs2
FFmpeg can make use of the xavs2 library for AVS2-P2/IEEE1857.4 video encoding.
Go to https://github.com/pkuvcl/xavs2 and follow the instructions for
installing the library. Then pass --enable-libxavs2 to configure to
enable it.
libxavs2 is under the GNU Public License Version 2 or later
(see http://www.gnu.org/licenses/old-licenses/gpl-2.0.html for
details), you must upgrade FFmpeg’s license to GPL in order to use it.
48.29 eXtra-fast Essential Video Encoder (XEVE)
FFmpeg can make use of the XEVE library for EVC video encoding.
Go to https://github.com/mpeg5/xeve and follow the instructions for
installing the XEVE library. Then pass --enable-libxeve to configure to
enable it.
48.30 eXtra-fast Essential Video Decoder (XEVD)
FFmpeg can make use of the XEVD library for EVC video decoding.
Go to https://github.com/mpeg5/xevd and follow the instructions for
installing the XEVD library. Then pass --enable-libxevd to configure to
enable it.
48.31 ZVBI
ZVBI is a VBI decoding library which can be used by FFmpeg to decode DVB
teletext pages and DVB teletext subtitles.
Go to http://sourceforge.net/projects/zapping/ and follow the instructions for
installing the library. Then pass --enable-libzvbi to configure to
enable it.
49 Supported File Formats, Codecs or Features
You can use the -formats and -codecs options to have an exhaustive list.
49.1 File Formats
FFmpeg supports the following file formats through the libavformat
library:
NameEncodingDecodingComments
3dostrX
4xmX4X Technologies format, used in some games.
8088flex TMVX
AAXXAudible Enhanced Audio format, used in audiobooks.
AAXAudible Format 2, 3, and 4, used in audiobooks.
ACT VoiceXcontains G.729 audio
Adobe FilmstripXX
Audio IFF (AIFF)XX
American Laser Games MMXMultimedia format used in games like Mad Dog McCree.
3GPP AMRXX
Amazing Studio Packed Animation FileXMultimedia format used in game Heart Of Darkness.
Apple HTTP Live StreamingX
Artworx Data FormatX
Interplay ACMXAudio only format used in some Interplay games.
ADPXAudio format used on the Nintendo Gamecube.
AFCXAudio format used on the Nintendo Gamecube.
ADS/SS2XAudio format used on the PS2.
APNGXX
ASFXXAdvanced / Active Streaming Format.
ASTXXAudio format used on the Nintendo Wii.
AVIXX
AviSynthX
AVRXAudio format used on Mac.
AVSXMultimedia format used by the Creature Shock game.
Beam Software SIFFXAudio and video format used in some games by Beam Software.
Bethesda Softworks VIDXUsed in some games from Bethesda Softworks.
Binary textX
BinkXMultimedia format used by many games.
Bink AudioXAudio only multimedia format used by some games.
Bitmap Brothers JVXUsed in Z and Z95 games.
BRPXArgonaut Games format.
Brute Force & IgnoranceXUsed in the game Flash Traffic: City of Angels.
BFSTMXAudio format used on the Nintendo WiiU (based on BRSTM).
BRSTMXAudio format used on the Nintendo Wii.
BW64XBroadcast Wave 64bit.
BWFXX
codec2 (raw)XXMust be given -mode format option to decode correctly.
codec2 (.c2 files)XXContains header with version and mode info, simplifying playback.
CRI ADXXXAudio-only format used in console video games.
CRI AIXX
CRI HCAXAudio-only format used in console video games.
Discworld II BMVX
Interplay C93XUsed in the game Cyberia from Interplay.
Delphine Software International CINXMultimedia format used by Delphine Software games.
Digital Speech Standard (DSS)X
CD+GXVideo format used by CD+G karaoke disks
Phantom CineX
Commodore CDXLXAmiga CD video format
Core Audio FormatXXApple Core Audio Format
CRC testing formatX
Creative VoiceXXCreated for the Sound Blaster Pro.
CRYO APCXAudio format used in some games by CRYO Interactive Entertainment.
D-Cinema audioXX
Deluxe Paint AnimationX
DCSTRX
DFAXThis format is used in Chronomaster game
DirectDraw SurfaceX
DSD Stream File (DSF)X
DV videoXX
DXAXThis format is used in the non-Windows version of the Feeble Files
game and different game cutscenes repacked for use with ScummVM.
Electronic Arts cdataX
Electronic Arts MultimediaXUsed in various EA games; files have extensions like WVE and UV2.
Ensoniq Paris Audio FileX
FFM (FFserver live feed)XX
Flash (SWF)XX
Flash 9 (AVM2)XXOnly embedded audio is decoded.
FLI/FLC/FLX animationX.fli/.flc files
Flash Video (FLV)XXMacromedia Flash video files
framecrc testing formatX
FunCom ISSXAudio format used in various games from FunCom like The Longest Journey.
G.723.1XX
G.726XBoth left- and right-justified.
G.729 BITXX
G.729 rawX
GENHXAudio format for various games.
GIF AnimationXX
GXFXXGeneral eXchange Format SMPTE 360M, used by Thomson Grass Valley
playout servers.
HNMXOnly version 4 supported, used in some games from Cryo Interactive
iCEDraw FileX
ICOXXMicrosoft Windows ICO
id Quake II CIN videoX
id RoQXXUsed in Quake III, Jedi Knight 2 and other computer games.
IEC61937 encapsulationXX
IFFXInterchange File Format
IFVXA format used by some old CCTV DVRs.
iLBCXX
Interplay MVEXFormat used in various Interplay computer games.
Iterated Systems ClearVideoXI-frames only
IV8XA format generated by IndigoVision 8000 video server.
IVF (On2)XXA format used by libvpx
Internet Video RecordingX
IRCAMXX
LAFXLimitless Audio Format
LATMXX
LMLM4XUsed by Linux Media Labs MPEG-4 PCI boards
LOASXcontains LATM multiplexed AAC audio
LRCXX
LVFX
LXFXVR native stream format, used by Leitch/Harris’ video servers.
Magic Lantern Video (MLV)X
MatroskaXX
Matroska audioX
FFmpeg metadataXXMetadata in text format.
MAXIS XAXUsed in Sim City 3000; file extension .xa.
MCAXUsed in some games from Capcom; file extension .mca.
MD StudioX
Metal Gear Solid: The Twin SnakesX
Megalux FrameXUsed by Megalux Ultimate Paint
MobiClip MODSX
MobiClip MOFLEXX
Mobotix .mxgX
Monkey’s AudioX
Motion Pixels MVIX
MOV/QuickTime/MP4XX3GP, 3GP2, PSP, iPod variants supported
MP2XX
MP3XX
MPEG-1 SystemXXmuxed audio and video, VCD format supported
MPEG-PS (program stream)XXalso known as VOB file, SVCD and DVD format supported
MPEG-TS (transport stream)XXalso known as DVB Transport Stream
MPEG-4XXMPEG-4 is a variant of QuickTime.
MSFXAudio format used on the PS3.
Mirillis FIC videoXNo cursor rendering.
MIDI Sample Dump StandardX
MIME multipart JPEGX
MSN TCP webcamXUsed by MSN Messenger webcam streams.
MTVX
MusepackX
Musepack SV8X
Material eXchange Format (MXF)XXSMPTE 377M, used by D-Cinema, broadcast industry.
Material eXchange Format (MXF), D-10 MappingXXSMPTE 386M, D-10/IMX Mapping.
NC camera feedXNC (AVIP NC4600) camera streams
NIST SPeech HEader REsourcesX
Computerized Speech Lab NSPX
NTT TwinVQ (VQF)XNippon Telegraph and Telephone Corporation TwinVQ.
Nullsoft Streaming VideoX
NuppelVideoX
NUTXXNUT Open Container Format
OggXX
Playstation Portable PMPX
Portable Voice FormatX
RK Audio (RKA)X
TechnoTrend PVAXUsed by TechnoTrend DVB PCI boards.
QCPX
raw ADTS (AAC)XX
raw AC-3XX
raw AMR-NBX
raw AMR-WBX
raw APACX
raw aptXXX
raw aptX HDXX
raw BonkX
raw Chinese AVS videoXX
raw DFPWMXX
raw DiracXX
raw DNxHDXX
raw DTSXX
raw DTS-HDX
raw E-AC-3XX
raw EVCXX
raw FLACXX
raw GSMX
raw H.261XX
raw H.263XX
raw H.264XX
raw HEVCXX
raw Ingenient MJPEGX
raw MJPEGXX
raw MLPX
raw MPEGX
raw MPEG-1X
raw MPEG-2X
raw MPEG-4XX
raw NULLX
raw videoXX
raw id RoQX
raw OBUXX
raw OSQX
raw SBCXX
raw ShortenX
raw TAKX
raw TrueHDXX
raw VC-1XX
raw PCM A-lawXX
raw PCM mu-lawXX
raw PCM Archimedes VIDCXX
raw PCM signed 8 bitXX
raw PCM signed 16 bit big-endianXX
raw PCM signed 16 bit little-endianXX
raw PCM signed 24 bit big-endianXX
raw PCM signed 24 bit little-endianXX
raw PCM signed 32 bit big-endianXX
raw PCM signed 32 bit little-endianXX
raw PCM signed 64 bit big-endianXX
raw PCM signed 64 bit little-endianXX
raw PCM unsigned 8 bitXX
raw PCM unsigned 16 bit big-endianXX
raw PCM unsigned 16 bit little-endianXX
raw PCM unsigned 24 bit big-endianXX
raw PCM unsigned 24 bit little-endianXX
raw PCM unsigned 32 bit big-endianXX
raw PCM unsigned 32 bit little-endianXX
raw PCM 16.8 floating point little-endianX
raw PCM 24.0 floating point little-endianX
raw PCM floating-point 32 bit big-endianXX
raw PCM floating-point 32 bit little-endianXX
raw PCM floating-point 64 bit big-endianXX
raw PCM floating-point 64 bit little-endianXX
RDTX
REDCODE R3DXFile format used by RED Digital cameras, contains JPEG 2000 frames and PCM audio.
RealMediaXX
RedirectorX
RedSparkX
Renderware TeXture DictionaryX
Resolume DXVXXEncoding is only supported for the DXT1 (Normal Quality, No Alpha) texture format.
RF64X
RL2XAudio and video format used in some games by Entertainment Software Partners.
RPL/ARMovieX
Lego Mindstorms RSOXX
RSDX
RTMPXXOutput is performed by publishing stream to RTMP server
RTPXX
RTSPXX
Sample Dump eXchangeX
SAPXX
SBGX
SDNSX
SDPX
SERX
Digital Pictures SGAX
Sega FILM/CPKXXUsed in many Sega Saturn console games.
Silicon Graphics MovieX
Sierra SOLX.sol files used in Sierra Online games.
Sierra VMDXUsed in Sierra CD-ROM games.
SmackerXMultimedia format used by many games.
SMJPEGXXUsed in certain Loki game ports.
SMPTE 337M encapsulationX
SmushXMultimedia format used in some LucasArts games.
Sony OpenMG (OMA)XXAudio format used in Sony Sonic Stage and Sony Vegas.
Sony PlayStation STRX
Sony Wave64 (W64)XX
SoX native formatXX
SUN AU formatXX
SUP raw PGS subtitlesXX
SVAGXAudio format used in Konami PS2 games.
TDSCX
Text filesX
THPXUsed on the Nintendo GameCube.
Tiertex Limited SEQXTiertex .seq files used in the DOS CD-ROM version of the game Flashback.
True AudioXX
VAGXAudio format used in many Sony PS2 games.
VC-1 test bitstreamXX
Vidvox HapXX
VivoX
VPKXAudio format used in Sony PS games.
Marble WADYX
WAVXX
Waveform ArchiverX
WavPackXX
WebMXX
Windows Televison (WTV)XX
Wing Commander III movieXMultimedia format used in Origin’s Wing Commander III computer game.
Westwood Studios audioXXMultimedia format used in Westwood Studios games.
Westwood Studios VQAXMultimedia format used in Westwood Studios games.
Wideband Single-bit Data (WSD)X
WVEX
Konami XMDX
XMVXMicrosoft video container used in Xbox games.
XVAGXAudio format used on the PS3.
xWMAXMicrosoft audio container used by XAudio 2.
eXtended BINary text (XBIN)X
YUV4MPEG pipeXX
Psygnosis YOPX
X means that the feature in that column (encoding / decoding) is supported.
49.2 Image Formats
FFmpeg can read and write images for each frame of a video sequence. The
following image formats are supported:
NameEncodingDecodingComments
.Y.U.VXXone raw file per component
Alias PIXXXAlias/Wavefront PIX image format
animated GIFXX
APNGXXAnimated Portable Network Graphics
BMPXXMicrosoft BMP image
BRender PIXXArgonaut BRender 3D engine image format.
CRIXCintel RAW
DPXXXDigital Picture Exchange
EXRXOpenEXR
FITSXXFlexible Image Transport System
HDRXXRadiance HDR RGBE Image format
IMGXGEM Raster image
JPEGXXProgressive JPEG is not supported.
JPEG 2000XX
JPEG-LSXX
LJPEGXLossless JPEG
Media 100X
MSPXMicrosoft Paint image
PAMXXPAM is a PNM extension with alpha support.
PBMXXPortable BitMap image
PCDXPhotoCD
PCXXXPC Paintbrush
PFMXXPortable FloatMap image
PGMXXPortable GrayMap image
PGMYUVXXPGM with U and V components in YUV 4:2:0
PGXXPGX file decoder
PHMXXPortable HalfFloatMap image
PICXPictor/PC Paint
PNGXXPortable Network Graphics image
PPMXXPortable PixelMap image
PSDXPhotoshop
PTXXV.Flash PTX format
QOIXXQuite OK Image format
SGIXXSGI RGB image format
Sun RasterfileXXSun RAS image format
TIFFXXYUV, JPEG and some extension is not supported yet.
Truevision TargaXXTarga (.TGA) image format
VBNXXVizrt Binary Image format
WBMPXXWireless Application Protocol Bitmap image format
WebPEXWebP image format, encoding supported through external library libwebp
XBMXXX BitMap image format
XFaceXXX-Face image format
XPMXX PixMap image format
XWDXXX Window Dump image format
X means that the feature in that column (encoding / decoding) is supported.
E means that support is provided through an external library.
49.3 Video Codecs
NameEncodingDecodingComments
4X MovieXUsed in certain computer games.
8088flex TMVX
A64 multicolorXCreates video suitable to be played on a commodore 64 (multicolor mode).
Amazing Studio PAF VideoX
American Laser Games MMXUsed in games like Mad Dog McCree.
Amuse Graphics MovieX
AMV VideoXXUsed in Chinese MP3 players.
ANSI/ASCII artX
Apple Intermediate CodecX
Apple MJPEG-BX
Apple PixletX
Apple ProResXXfourcc: apch,apcn,apcs,apco,ap4h,ap4x
Apple QuickDrawXfourcc: qdrw
Argonaut VideoXUsed in some Argonaut games.
Asus v1XXfourcc: ASV1
Asus v2XXfourcc: ASV2
ATI VCR1Xfourcc: VCR1
ATI VCR2Xfourcc: VCR2
Auravision AuraX
Auravision Aura 2X
Autodesk Animator Flic videoX
Autodesk RLEXfourcc: AASC
AV1EESupported through external libraries libaom, libdav1d, librav1e and libsvtav1
Avid 1:1 10-bit RGB PackerXXfourcc: AVrp
AVS (Audio Video Standard) videoXVideo encoding used by the Creature Shock game.
AVS2-P2/IEEE1857.4EESupported through external libraries libxavs2 and libdavs2
AVS3-P2/IEEE1857.10ESupported through external library libuavs3d
AYUVXXMicrosoft uncompressed packed 4:4:4:4
Beam Software VBX
Bethesda VID videoXUsed in some games from Bethesda Softworks.
Bink VideoX
BitJazz SheerVideoX
Bitmap Brothers JV videoX
y41p Brooktree uncompressed 4:1:1 12-bitXX
Brooktree ProSumer VideoXfourcc: BT20
Brute Force & IgnoranceXUsed in the game Flash Traffic: City of Angels.
C93 videoXCodec used in Cyberia game.
CamStudioXfourcc: CSCD
CD+GXVideo codec for CD+G karaoke disks
CDXLXAmiga CD video codec
Chinese AVS videoEXAVS1-P2, JiZhun profile, encoding through external library libxavs
Delphine Software International CIN videoXCodec used in Delphine Software International games.
Discworld II BMV VideoX
CineForm HDXX
Canopus HQX
Canopus HQAX
Canopus HQXX
Canopus Lossless CodecX
CDToonsXCodec used in various Broderbund games.
CinepakX
Cirrus Logic AccuPakXXfourcc: CLJR
CPiA Video FormatX
Creative YUV (CYUV)X
DFAXCodec used in Chronomaster game.
DiracEXsupported though the native vc2 (Dirac Pro) encoder
Deluxe Paint AnimationX
DNxHDXXaka SMPTE VC3
Duck TrueMotion 1.0Xfourcc: DUCK
Duck TrueMotion 2.0Xfourcc: TM20
Duck TrueMotion 2.0 RTXfourcc: TR20
DV (Digital Video)XX
Dxtory capture formatX
Feeble Files/ScummVM DXAXCodec originally used in Feeble Files game.
Electronic Arts CMV videoXUsed in NHL 95 game.
Electronic Arts Madcow videoX
Electronic Arts TGV videoX
Electronic Arts TGQ videoX
Electronic Arts TQI videoX
Escape 124X
Escape 130X
EVC / MPEG-5 Part 1EEencoding and decoding supported through external libraries libxeve and libxevd
FFmpeg video codec #1XXlossless codec (fourcc: FFV1)
Flash Screen Video v1XXfourcc: FSV1
Flash Screen Video v2XX
Flash Video (FLV)XXSorenson H.263 used in Flash
FM Screen Capture CodecX
Forward UncompressedX
FrapsX
Go2MeetingXfourcc: G2M2, G2M3
Go2WebinarXfourcc: G2M4
Gremlin Digital VideoX
H.261XX
H.263 / H.263-1996XX
H.263+ / H.263-1998 / H.263 version 2XX
H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10EXencoding supported through external library libx264 and OpenH264
HEVCXXencoding supported through external library libx265 and libkvazaar
HNM version 4X
HuffYUVXX
HuffYUV FFmpeg variantXX
IBM UltimotionXfourcc: ULTI
id Cinematic videoXUsed in Quake II.
id RoQ videoXXUsed in Quake III, Jedi Knight 2, other computer games.
IFF ILBMXIFF interleaved bitmap
IFF ByteRun1XIFF run length encoded bitmap
Infinity IMM4X
Intel H.263X
Intel Indeo 2X
Intel Indeo 3X
Intel Indeo 4X
Intel Indeo 5X
Interplay C93XUsed in the game Cyberia from Interplay.
Interplay MVE videoXUsed in Interplay .MVE files.
J2KXX
Karl Morton’s video codecXCodec used in Worms games.
Kega Game Video (KGV1)XKega emulator screen capture codec.
LagarithX
LCEVC / MPEG-5 LCEVC / MPEG-5 Part 2Edecoding supported through external library liblcevc-dec
LCL (LossLess Codec Library) MSZHX
LCL (LossLess Codec Library) ZLIBEE
LEAD MCMPX
LOCOX
LucasArts SANM/SmushXUsed in LucasArts games / SMUSH animations.
lossless MJPEGXX
MagicYUV VideoXX
Mandsoft Screen Capture CodecX
Microsoft ATC ScreenXAlso known as Microsoft Screen 3.
Microsoft Expression Encoder ScreenXAlso known as Microsoft Titanium Screen 2.
Microsoft RLEXX
Microsoft Screen 1XAlso known as Windows Media Video V7 Screen.
Microsoft Screen 2XAlso known as Windows Media Video V9 Screen.
Microsoft Video 1X
MimicXUsed in MSN Messenger Webcam streams.
Miro VideoXLXfourcc: VIXL
MJPEG (Motion JPEG)XX
Mobotix MxPEG videoX
Motion Pixels videoX
MPEG-1 videoXX
MPEG-2 videoXX
MPEG-4 part 2XXlibxvidcore can be used alternatively for encoding.
MPEG-4 part 2 Microsoft variant version 1X
MPEG-4 part 2 Microsoft variant version 2XX
MPEG-4 part 2 Microsoft variant version 3XX
Newtek SpeedHQXX
Nintendo Gamecube THP videoX
NotchLCX
NuppelVideo/RTjpegXVideo encoding used in NuppelVideo files.
On2 VP3Xstill experimental
On2 VP4Xfourcc: VP40
On2 VP5Xfourcc: VP50
On2 VP6Xfourcc: VP60,VP61,VP62
On2 VP7Xfourcc: VP70,VP71
VP8EXfourcc: VP80, encoding supported through external library libvpx
VP9EXencoding supported through external library libvpx
Pinnacle TARGA CineWave YUV16Xfourcc: Y216
Q-team QPEGXfourccs: QPEG, Q1.0, Q1.1
QuickTime 8BPS videoX
QuickTime Animation (RLE) videoXXfourcc: ’rle ’
QuickTime Graphics (SMC)XXfourcc: ’smc ’
QuickTime video (RPZA)XXfourcc: rpza
R10K AJA Kona 10-bit RGB CodecXX
R210 Quicktime Uncompressed RGB 10-bitXX
Raw VideoXX
RealVideo 1.0XX
RealVideo 2.0XX
RealVideo 3.0Xstill far from ideal
RealVideo 4.0X
RealVideo 6.0X
Renderware TXD (TeXture Dictionary)XTexture dictionaries used by the Renderware Engine.
RivaTuner VideoXfourcc: ’RTV1’
RL2 videoXused in some games by Entertainment Software Partners
ScreenPressorX
ScreenpressoX
Screen Recorder Gold CodecX
Sierra VMD videoXUsed in Sierra VMD files.
Silicon Graphics Motion Video Compressor 1 (MVC1)X
Silicon Graphics Motion Video Compressor 2 (MVC2)X
Silicon Graphics RLE 8-bit videoX
Smacker videoXVideo encoding used in Smacker.
SMPTE VC-1X
SnowXXexperimental wavelet codec (fourcc: SNOW)
Sony PlayStation MDEC (Motion DECoder)X
Sorenson Vector Quantizer 1XXfourcc: SVQ1
Sorenson Vector Quantizer 3Xfourcc: SVQ3
Sunplus JPEG (SP5X)Xfourcc: SP5X
TechSmith Screen Capture CodecXfourcc: TSCC
TechSmith Screen Capture Codec 2Xfourcc: TSC2
TheoraEXencoding supported through external library libtheora
Tiertex Limited SEQ videoXCodec used in DOS CD-ROM FlashBack game.
Ut VideoXX
v210 QuickTime uncompressed 4:2:2 10-bitXX
v308 QuickTime uncompressed 4:4:4XX
v408 QuickTime uncompressed 4:4:4:4XX
v410 QuickTime uncompressed 4:4:4 10-bitXX
VBLE Lossless CodecX
vMix VideoXfourcc: ’VMX1’
VMware Screen Codec / VMware VideoXCodec used in videos captured by VMware.
Westwood Studios VQA (Vector Quantized Animation) videoX
Windows Media ImageX
Windows Media Video 7XX
Windows Media Video 8XX
Windows Media Video 9Xnot completely working
Wing Commander III / XanXUsed in Wing Commander III .MVE files.
Wing Commander IV / XanXUsed in Wing Commander IV.
Winnov WNV1X
WMV7XX
YAMAHA SMAFXX
Psygnosis YOP VideoX
yuv4XXlibquicktime uncompressed packed 4:2:0
ZeroCodec Lossless VideoX
ZLIBXXpart of LCL, encoder experimental
Zip Motion Blocks VideoXXEncoder works only in PAL8.
X means that the feature in that column (encoding / decoding) is supported.
E means that support is provided through an external library.
49.4 Audio Codecs
NameEncodingDecodingComments
8SVX exponentialX
8SVX fibonacciX
AACEXXencoding supported through internal encoder and external library libfdk-aac
AAC+EIXencoding supported through external library libfdk-aac
AC-3IXIX
ACELP.KELVINX
ADPCM 4X MovieX
ADPCM Yamaha AICAX
ADPCM AmuseGraphics MovieX
ADPCM Argonaut GamesXX
ADPCM CDROM XAX
ADPCM Creative TechnologyX16 -> 4, 8 -> 4, 8 -> 3, 8 -> 2
ADPCM Electronic ArtsXUsed in various EA titles.
ADPCM Electronic Arts Maxis CDROM XSXUsed in Sim City 3000.
ADPCM Electronic Arts R1X
ADPCM Electronic Arts R2X
ADPCM Electronic Arts R3X
ADPCM Electronic Arts XASX
ADPCM G.722XX
ADPCM G.726XX
ADPCM IMA Acorn ReplayX
ADPCM IMA AMVXXUsed in AMV files
ADPCM IMA Cunning DevelopmentsX
ADPCM IMA Electronic Arts EACSX
ADPCM IMA Electronic Arts SEADX
ADPCM IMA FuncomX
ADPCM IMA High Voltage Software ALPXX
ADPCM IMA Mobiclip MOFLEXX
ADPCM IMA QuickTimeXX
ADPCM IMA Simon & Schuster InteractiveXX
ADPCM IMA Ubisoft APMXX
ADPCM IMA Loki SDL MJPEGX
ADPCM IMA WAVXX
ADPCM IMA WestwoodX
ADPCM ISS IMAXUsed in FunCom games.
ADPCM IMA DialogicX
ADPCM IMA Duck DK3XUsed in some Sega Saturn console games.
ADPCM IMA Duck DK4XUsed in some Sega Saturn console games.
ADPCM IMA RadicalX
ADPCM IMA XboxX
ADPCM MicrosoftXX
ADPCM MS IMAXX
ADPCM Nintendo Gamecube AFCX
ADPCM Nintendo Gamecube DTKX
ADPCM Nintendo THPX
ADPCM PlaystationX
ADPCM QT IMAXX
ADPCM SEGA CRI ADXXXUsed in Sega Dreamcast games.
ADPCM Shockwave FlashXX
ADPCM Sound Blaster Pro 2-bitX
ADPCM Sound Blaster Pro 2.6-bitX
ADPCM Sound Blaster Pro 4-bitX
ADPCM VIMAXUsed in LucasArts SMUSH animations.
ADPCM Konami XMDX
ADPCM Westwood Studios IMAXXUsed in Westwood Studios games like Command and Conquer.
ADPCM YamahaXX
ADPCM ZorkX
AMR-NBEXencoding supported through external library libopencore-amrnb
AMR-WBEXencoding supported through external library libvo-amrwbenc
Amazing Studio PAF AudioX
Apple lossless audioXXQuickTime fourcc ’alac’
aptXXXUsed in Bluetooth A2DP
aptX HDXXUsed in Bluetooth A2DP
ATRAC1X
ATRAC3X
ATRAC3+X
ATRAC9X
Bink AudioXUsed in Bink and Smacker files in many games.
Bonk audioX
CELTEdecoding supported through external library libcelt
codec2EEen/decoding supported through external library libcodec2
CRI HCAX
Delphine Software International CIN audioXCodec used in Delphine Software International games.
DFPWMXX
Digital Speech Standard - Standard Play mode (DSS SP)X
Discworld II BMV AudioX
COOKXAll versions except 5.1 are supported.
DCA (DTS Coherent Acoustics)XXsupported extensions: XCh, XXCH, X96, XBR, XLL, LBR (partially)
Dolby EX
DPCM Cuberoot-Delta-ExactXUsed in few games.
DPCM GremlinX
DPCM id RoQXXUsed in Quake III, Jedi Knight 2 and other computer games.
DPCM Marble WADYX
DPCM InterplayXUsed in various Interplay computer games.
DPCM Squareroot-Delta-ExactXUsed in various games.
DPCM Sierra OnlineXUsed in Sierra Online game audio files.
DPCM SolX
DPCM XanXUsed in Origin’s Wing Commander IV AVI files.
DPCM Xilam DERFX
DSD (Direct Stream Digital), least significant bit firstX
DSD (Direct Stream Digital), most significant bit firstX
DSD (Direct Stream Digital), least significant bit first, planarX
DSD (Direct Stream Digital), most significant bit first, planarX
DSP Group TrueSpeechX
DST (Direct Stream Transfer)X
DV audioX
Enhanced AC-3XX
EVRC (Enhanced Variable Rate Codec)X
FLAC (Free Lossless Audio Codec)XIX
FTR VoiceX
G.723.1XX
G.729X
GSMEXencoding supported through external library libgsm
GSM Microsoft variantEXencoding supported through external library libgsm
IAC (Indeo Audio Coder)X
iLBC (Internet Low Bitrate Codec)EEXencoding and decoding supported through external library libilbc
IMC (Intel Music Coder)X
Interplay ACMX
LC3EEsupported through external library liblc3
MACE (Macintosh Audio Compression/Expansion) 6:1X
Marian’s A-pac audioX
MI-SC4 (Micronas SC-4 Audio)X
MLP (Meridian Lossless Packing)XXUsed in DVD-Audio discs.
Monkey’s AudioX
MP1 (MPEG audio layer 1)IX
MP2 (MPEG audio layer 2)IXIXencoding supported also through external library TwoLAME
MP3 (MPEG audio layer 3)EIXencoding supported through external library LAME, ADU MP3 and MP3onMP4 also supported
MPEG-4 Audio Lossless Coding (ALS)X
MobiClip FastAudioX
Musepack SV7X
Musepack SV8X
Nellymoser AsaoXX
On2 AVC (Audio for Video Codec)X
OpusEXencoding supported through external library libopus
OSQ (Original Sound Quality)X
PCM A-lawXX
PCM mu-lawXX
PCM Archimedes VIDCXX
PCM signed 8-bit planarXX
PCM signed 16-bit big-endian planarXX
PCM signed 16-bit little-endian planarXX
PCM signed 24-bit little-endian planarXX
PCM signed 32-bit little-endian planarXX
PCM 32-bit floating point big-endianXX
PCM 32-bit floating point little-endianXX
PCM 64-bit floating point big-endianXX
PCM 64-bit floating point little-endianXX
PCM D-Cinema audio signed 24-bitXX
PCM signed 8-bitXX
PCM signed 16-bit big-endianXX
PCM signed 16-bit little-endianXX
PCM signed 24-bit big-endianXX
PCM signed 24-bit little-endianXX
PCM signed 32-bit big-endianXX
PCM signed 32-bit little-endianXX
PCM signed 16/20/24-bit big-endian in MPEG-TSX
PCM unsigned 8-bitXX
PCM unsigned 16-bit big-endianXX
PCM unsigned 16-bit little-endianXX
PCM unsigned 24-bit big-endianXX
PCM unsigned 24-bit little-endianXX
PCM unsigned 32-bit big-endianXX
PCM unsigned 32-bit little-endianXX
PCM SGAX
QCELP / PureVoiceX
QDesign Music Codec 1X
QDesign Music Codec 2XThere are still some distortions.
RealAudio 1.0 (14.4K)XXReal 14400 bit/s codec
RealAudio 2.0 (28.8K)XReal 28800 bit/s codec
RealAudio 3.0 (dnet)IXXReal low bitrate AC-3 codec
RealAudio LosslessX
RealAudio SIPR / ACELP.NETX
RK Audio (RKA)X
SBC (low-complexity subband codec)XXUsed in Bluetooth A2DP
ShortenX
Sierra VMD audioXUsed in Sierra VMD files.
Smacker audioX
SMPTE 302M AES3 audioXX
SonicXXexperimental codec
Sonic losslessXXexperimental codec
SpeexEEXsupported through external library libspeex
TAK (Tom’s lossless Audio Kompressor)X
True Audio (TTA)XX
TrueHDXXUsed in HD-DVD and Blu-Ray discs.
TwinVQ (VQF flavor)X
VIMAXUsed in LucasArts SMUSH animations.
ViewQuest VQCX
VorbisEXA native but very primitive encoder exists.
Voxware MetaSoundX
Waveform ArchiverX
WavPackXX
Westwood Audio (SND1)X
Windows Media Audio 1XX
Windows Media Audio 2XX
Windows Media Audio LosslessX
Windows Media Audio ProX
Windows Media Audio VoiceX
Xbox Media Audio 1X
Xbox Media Audio 2X
X means that the feature in that column (encoding / decoding) is supported.
E means that support is provided through an external library.
I means that an integer-only version is available, too (ensures high
performance on systems without hardware floating point support).
49.5 Subtitle Formats
NameMuxingDemuxingEncodingDecoding
3GPP Timed TextXX
AQTitleXX
DVBXXXX
DVB teletextXE
DVDXXXX
JACOsubXXX
MicroDVDXXX
MPL2XX
MPsub (MPlayer)XX
PGSX
PJS (Phoenix)XX
RealTextXX
SAMIXX
Spruce format (STL)XX
SSA/ASSXXXX
SubRip (SRT)XXXX
SubViewer v1XX
SubViewerXX
TED Talks captionsXX
TTMLXX
VobSub (IDX+SUB)XX
VPlayerXX
WebVTTXXXX
XSUBXX
X means that the feature is supported.
E means that support is provided through an external library.
49.6 Network Protocols
NameSupport
AMQPE
fileX
FTPX
GopherX
GophersX
HLSX
HTTPX
HTTPSX
IcecastX
MMSHX
MMSTX
pipeX
Pro-MPEG FECX
RTMPX
RTMPEX
RTMPSX
RTMPTX
RTMPTEX
RTMPTSX
RTPX
SAMBAE
SCTPX
SFTPE
TCPX
TLSX
UDPX
ZMQE
X means that the protocol is supported.
E means that support is provided through an external library.
49.7 Input/Output Devices
NameInputOutput
ALSAXX
BKTRX
cacaX
DV1394X
Lavfi virtual deviceX
Linux framebufferXX
JACKX
LIBCDIOX
LIBDC1394X
OpenALX
OpenGLX
OSSXX
PulseAudioXX
SDLX
Video4Linux2XX
VfW captureX
X11 grabbingX
Win32 grabbingX
X means that input/output is supported.
49.8 Timecode
Codec/formatReadWrite
AVIXX
DVXX
GXFXX
MOVXX
MPEG1/2XX
MXFXX
50 See Also
ffmpeg
ffplay, ffprobe,
ffmpeg-utils,
ffmpeg-scaler,
ffmpeg-resampler,
ffmpeg-codecs,
ffmpeg-bitstream-filters,
ffmpeg-formats,
ffmpeg-devices,
ffmpeg-protocols,
ffmpeg-filters
51 Authors
The FFmpeg developers.
For details about the authorship, see the Git history of the project
(https://git.ffmpeg.org/ffmpeg), e.g. by typing the command
git log in the FFmpeg source directory, or browsing the
online repository at https://git.ffmpeg.org/ffmpeg.
Maintainers for the specific components are listed in the file
MAINTAINERS in the source code tree.
This document was generated on January 25, 2025 using makeinfo.