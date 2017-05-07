# Portable Presentation Format

The idea is to create a portable slideshow presentation format, somewhat like what PDF is for written documents. The purpose is that it should be:

* Self-contained (should not rely on external files such as fonts, images, movies)
* Cross-platform (should work on Linux/Windows/Mac)
* Editor-independent (ideally one should be able to convert existing presentations into this format to be able to display them anywhere).
* Robust (don't you hate that spinning wheel of death in the middle of your presentation)
* Free Open Source (and properly standardised)
* Simple (no fancy slide transitions)

I haven't found any presentation tool that has all of the above properties.

If such a format were defined, then the neat thing is that one can create an application to show the slideshow that caters to one's specific needs and preferences. Also, it should make it easy to have a single presentation computer during a scientific conference where everybody can upload their slides and have them actually show up the way they intended.



## Structure definition
A Portable Presentation (`.pp`) is a Gzipped file that contains an XML main file and several dependent files such as images, fonts, videos.

Note that the format itself is a bit rigid, and that's okay because it's not designed with the idea t
hat a human would write their presentation in this format, but rather that you can convert other, more user friendly formats into this format for presentation purposes.

### Master XML file

First, let me give an overview of roughly the way this works. A more precise presentation will follow.

Everything is embedded in a `slideshow` tag. Each slide is contained in a `slide` tag. You basically define all contents (things that go on a slide) using dedicated tags, e.g. `text`, `image`, `video`, `rect`. These tags have attributes such as `x` or `y` which specify where it goes, and possibly `height` or `width` (for rectangles). Each of these items has an ID which is a unique number that we can use to show or hide these elements on different overlays.

```{xml}
<slideshow>
<slide>
<overlay>
<text>
</overlay>
</slide>
</slideshow>
```


Each slide contains various `overlays` items that define what will show up when. Each overlay can contain elements `show` or `hide` or `play` (for a video) or `fade`. 






## TODO

* Define a nice way to control opacity of overlays.
* Define an overview slide that you can come back to?




## Alternatives

What about **PDF**? Actually PDF is quite close to this, and it could work relatively well for a number of issues defined above, except: (a) overlays are not naturally defined in PDF, meaning that it's difficult to create a presenter view slide sorter where you can easily jump from slide to slide, and (b) I've had little luck with embedding video's in PDFs although it should be possible.

What about **Powerpoint**? Powerpoint has also a great deal of useful features coming quite close to what is defined above. However, I have had trouble getting it to work under Linux. And of course it's proprietary.

What about **Open Document Presentation** (`.odp`)? Pretty neat as well, but I don't think you can embed fonts, and I also keep having issues with videos.

