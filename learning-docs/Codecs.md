# Codecs

#### Suggested reading

http://nofilmschool.com/2014/09/everything-you-need-know-about-codecs 
https://images.apple.com/final-cut-pro/docs/Apple_ProRes_White_Paper.pdf
https://postproduction.emerson.edu/hc/en-us/articles/226166767-Raw-Log-and-Uncompressed-Footage-Overview


----------


Codec stands for compressor/decompressor
Propriety – codec owned by a company so you have to license them
Some are not so you can use them for free
This is why some computers can’t deal with videos made with certain codecs
<br>

#### Container vs Codec

Codec = h.264, Prores, DNxHD
Container = file type e.g. example.mov .avi .mp4

<br>
#### Types of Codecs
**Capture codec** – what your camera is recording, varies from low bitrate to RAW
**Edit codec** – turn capture codec into something to edit with
**Delivery codec** – the end file
**Archival codec** – something to keep long term

Let’s say we capture in h.264
Then edit in DN x HD
Render out to h.264 for deliver
Then archive DNxHD

**Speed over quality** , big factor in choosing codec e.g. editing want speed, archival want quality 
<br>
#### Bit Depth
Values you have between pure black and white
High bit depth you won’t have any banding, 
Low bit depth you get artefacts 
8-bit depth, real world
28 for RGB = 256 values for each of these

10-bit is 210 = 1024 values 
So a big difference
<br>
#### Chroma subsampling 
4:4:4  | &nbsp; 4:2:2 | 4:2:0
none | some | lots

4:4:4 – each pixel has its own colour

Green screen, chroma keying has an issue with this, starts grabbing things you don’t expect
<br>
#### Spatial Compression
Cuts out the bits that don’t need to be compressed.
In areas of low contrast, codecs do a lot of spatial compression, I’ll make this whole block the same colour

Why does having the same colour pixels save space?

#### Temporal compression
**Inter-frame compression** – Long GOP (group of pictures)
Calculates pixels that change from frame to frame, only saves those that change
Good for talking heads, not good for editing as you are hopping around the timeline and will only load the difference
**Good for storing info, not for editing**
All - I = no inter-frame compression, stores every frame

**Intra-frame, all stuff from pixels in the same frame**

Lossless Compression vs Lossy compression
Lossy – throwing away data that won’t be detrimental to final file
Lossless, view data as numbers, won’t lose data
.zip .rar , Huffman
<br>
#### Bit rate
Bits per second, kb per second - kbps
Mbps - mb/s not MBm BITS NOT BYTES
1 byte = 8 bits

1000 kbps = 1,000,000 Mbps
 Higher bit rate, higher quality
Different codecs vary widely how efficient

If you had
h.264 at 8Mbps vs MPEG2 (not as advanced as h.264) 20Mbps
h.264 would be better quality as is far more efficient


