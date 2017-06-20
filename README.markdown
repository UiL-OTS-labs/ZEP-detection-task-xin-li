## Overview
Auditory discrimination. Participant is to learn which audio fragments are part
of the language and which are not.

Current button setup is SPACE_BAR continue and LEFT and RIGHT SHIFT for the choice.

Alternative one can use an attached [BeexyBox](http://www.beexy.org/responseboxes/) which will result in more accurate reaction time measurements.

## Instructions on how to Zep
* [Installing an Experiment](https://www.beexy.nl/zep/wiki/doku.php?id=experiment:installing)
* [Running an Experiment](https://www.beexy.nl/zep/wiki/doku.php?id=experiment:running)
* [Extracting Experiment Results](https://www.beexy.nl/zep/wiki/doku.php?id=experiment:results)

## Pseudorandomisation
For word_leaning:
* Two similar images are not allowed; even if it loops.
*
For detection_practice:
* No more than two of the same expected answer trials in sequence
*
For detection_test:
* No two of the same target audio files in sequence.

## Particpant fields
* Left or right-handedness (this will swap the buttons)
* Language (NL or BJ)

## Adding Stimuli
See `modules/stimuli.zm` for how stimuli should be configured.

## Custom Instruction Text
Edit the variables found in `modules/texts_en.zm` to change the instructions shown to the participant.

## Misc settings
See `test/defs.zm` for settings.

The width of images can be globally set by changing the value of `IMAGE_WIDTH_PX` to some pixel value.

## DISCLAIMER
This experiment script is released under the terms of the GNU General Public License (see http://www.gnu.org/licenses/gpl-2.0.html). It is distributed in the hope that it will be useful, but with absolutely no warranty. It is your responsibility to carefully study and test the script before using it with real participants.

## Request details
### Script Author
[C. van Run, MSc](http://www.uu.nl/staff/CPAvanRun)
### Client
[Xin Li, MA](https://www.uu.nl/staff/XLi3/0)
