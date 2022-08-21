import sys

# https://github.com/openai/gym/issues/673#issuecomment-501981467
import os
os.environ['LANG'] = 'en_US'

import pyglet
import pyglet.app
import pyglet.canvas
import pyglet.extlibs
import pyglet.libs
import pyglet.font
import pyglet.gl
import pyglet.graphics
import pyglet.image
import pyglet.image.codecs
import pyglet.input
import pyglet.media
import pyglet.media.drivers
if sys.platform != 'darwin':  # FIXME: Upstream library loader doesn't consider CONDA_PREFIX
    import pyglet.media.codecs.ffmpeg
import pyglet.window
import pyglet.text
import pyglet.text.formats

# Skip to avoid having to install audio drivers.
# import pyglet.media.drivers.openal
# import pyglet.media.drivers.pulse

# Platform-specific tests.

if sys.platform == 'win32':
    import pyglet.libs.win32
    import pyglet.window.win32
    import pyglet.media.drivers.directsound

if sys.platform == 'darwin':
    import pyglet.libs.darwin
    import pyglet.libs.darwin.cocoapy
    import pyglet.window.cocoa

if sys.platform == 'linux':
    import pyglet.libs.x11
    import pyglet.window.xlib
