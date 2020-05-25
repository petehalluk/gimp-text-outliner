#!/usr/bin/env python

# This is a GIMP script written in Python for putting an outline around text (or indeed anything
# else).
# 
# To use this script, make sure that the selected layer is the one that you want to outline, then
# choose "Text Outliner" from the "Decor" submenu of the "Filters" menu
#
# You will then be able to set various parameters for the outline. They are:
#		Colour - what colour you want the outline to be
#		Thickness - thickness of the outline (in pixels)
#		Feather - how soft you want the edge of the outline to be
#		Output Layers - whether you want the outline to be in a wholly separate transparent layer,
#			or merged with the original
#
# Recent changes:
#		May 2020 - Added an option to merge the outline and original layer together
#		May 2020 - Fix for compatibility with layer groups

from gimpfu import *

# Adds a new layer beneath the given layer. Return value is the new layer
def add_new_layer_beneath(image, layer):
	position = pdb.gimp_image_get_item_position(image, layer)
	parent_layer = layer.parent
	
	if image.base_type is RGB:
		type = RGBA_IMAGE
	else:
		type = GRAYA_IMAGE
		
	# Add a new layer below the selected one
	new_layer = gimp.Layer(image, "Outline for %s" % (layer.name), image.width, image.height, type, 100, NORMAL_MODE)
	pdb.gimp_image_insert_layer(image, new_layer, parent_layer, position+1)
	return new_layer

# Selects the contents of the given layer, then grows it by "thickness"
# and feathers it by "feather" pixels
def create_selection(image, layer, thickness, feather):
	pdb.gimp_selection_layer_alpha(layer)
	pdb.gimp_selection_grow(image, thickness)
	if (feather > 0):
		pdb.gimp_selection_feather(image, feather)		
	return

# Fills the current selection using the given colour, painting onto the
# given layer.
def fill_selection(layer, colour):
	old_fg = pdb.gimp_palette_get_foreground()
	pdb.gimp_palette_set_foreground(colour)	
	pdb.gimp_bucket_fill(layer, 0, 0, 100, 0, 0, 1, 1)	
	pdb.gimp_palette_set_foreground(old_fg)	
	return

# our script
def add_text_outline(image, layer, colour, thickness, feather, output_layers) :
	gimp.progress_init("Drawing outline around text")
	new_layer = add_new_layer_beneath(image, layer)
	gimp.progress_update(25)
	create_selection(image, layer, thickness, feather)
	gimp.progress_update(50)
	fill_selection(new_layer, colour)	
	gimp.progress_update(75)
	if (output_layers == 'merge'):
		layer_name = layer.name
		new_layer = pdb.gimp_image_merge_down(image, layer, 0)
		new_layer.name = layer_name
		gimp.progress_update(85)
	pdb.plug_in_autocrop_layer(image, new_layer)
	gimp.progress_update(100)
	return

# This is the plugin registration function
register(
	"text_outliner",	
	"Text Outliner",   
	"Will draw an outline around text (or indeed anything else). The outline is drawn to a separate layer underneath the selected layer.",
	"Pete Hall", 
	"Pete Hall", 
	"2015-2020",
	"<Image>/Filters/Decor/Text Outliner", 
	"*", 
	[
		(PF_COLOUR, 'outline_colour', 'Colour', (0, 0, 0)),
		(PF_INT, 'outline_thickness', 'Thickness', 6),
		(PF_INT, 'outline_featheriness', 'Feather', 7),
		(PF_RADIO, 'outline_layer', 'Output Layers', 'distinct',
			(('Keep outline on separate layer', 'distinct'),
			('Merge outline and original layer', 'merge')))
	], 
	[],
	add_text_outline)

main()