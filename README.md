DoneXBlock
==========
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python CI](https://github.com/openedx/DoneXBlock/actions/workflows/ci.yml/badge.svg)](https://github.com/openedx/DoneXBlock/actions/workflows/ci.yml)
[![Publish package to PyPi](https://github.com/openedx/DoneXBlock/actions/workflows/pypi-release.yml/badge.svg)](https://github.com/openedx/DoneXBlock/actions/workflows/pypi-release.yml)

Purpose
-------

Lets a student mark they've finished an activity. The student can
click through two states of the XBlock, shown below:

![Done screenshot](completionxblock_mark.png)

![Done screenshot](completionxblock_undo.png)

Status
------

Maintained

Getting Help
------------

To be Written

How to Contribute
-----------------

Details about how to become a contributor to the Open edX project may
be found
[here](https://miro.com/app/board/uXjVOEVVXJY=/?moveToWidget=3458764527654681386&cot=14).

### The Open edX Code of Conduct

All community members should familarize themselves with the [Open edX
Code of Conduct](https://openedx.org/code-of-conduct/).

People
------

The assigned maintainers for this component and other project details
may be found in
[Backstage](https://open-edx-backstage.herokuapp.com/catalog/default/component/DoneXBlock),
or groked from inspecting catalog-info.yaml.

History
-------

FutureLearn uses this kind of thing to great effect. Students can read
text, watch videos, etc., and indicate when their done. This is
convenient both for progress indication to the student (know what
they've done, and for honor code grading (indicating to us that they
believe they've finished an activity).

I copied some of the UX patterns from FutureLearn so that users of
both platforms would have consistency of user experience between
MOOCs. I didn't copy them exactly since I wanted to be unambiguously 
in the clear with IP issues around look-and-feel, and this was on a short
anough timeline that I did not have a chance to reach out to
FutureLearn for permission. As a footnote, this kind of collaboration
between MOOC providers is probably worth pursuing -- it'd be to the
benefit of learners on all platforms, and ultimately, the industry as
a whole if we had consistency of experience between platforms where
convenient.
