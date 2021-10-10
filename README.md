# Introduction

One of the things that has always seemed needlessly frustrating about using [GIMP](http://gimp.org/) is the multi-step process required to add an outline to a piece of text. This plugin aims to rectify that.

## Installation

While GIMP is not running, save the plugin to your plugins directory. This might vary depending on your platform, but on Windows 7/8 it might be:
- C:/Users/[username]/AppData/Roaming/GIMP/2.10/plug-ins
- C:/Users/[username]/.gimp-2.8/plug-ins

## How does it work?

The plugin will create a new layer underneath the currently-selected layer. It will then draw the outline into that new layer, and optionally merge the two together.

## Usage

1. Make sure that the selected layer is the one containing the text you want to outline
2. Choose "Text Outliner" from the "Decor" submenu of the "Filters" menu
3. Choose the colour, thickness and feather values you wish to use (or keep the defaults).
4. If desired, select the option to merge the original layer and outline layer into one.
5. Click OK

## Changes

* May 2020: Added an option to merge the original layer and outline layer together
* May 2020: Now works with layers within layer groups
* Jan 2019: The name of the text layer has changed from "text outline" to "Outline for blah" where blah is the name of the layer being outlined
* Jan 2019: The outline layer will be automatically cropped so it is no longer larger than it needs to be.
* Mar 2017: The plugin has been updated to work with greyscale images

## Compatibility Note

Note that there is a bug in certain versions of GIMP that prevent this plugin from working. If you are running any version 2.10 or higher, then you need to update to at least version 2.10.12 if you want to use this plugin. [More information here](https://gitlab.gnome.org/GNOME/gimp/issues/1438).

If you have any questions, please drop me a line.
