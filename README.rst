##########
DoneXBlock
##########
| |License: AGPL v3| |Python CI| |Publish package to PyPi|

.. |License: AGPL v3| image:: https://img.shields.io/badge/License-AGPL_v3-blue.svg
  :target: https://www.gnu.org/licenses/agpl-3.0

.. |Python CI| image:: https://github.com/openedx/DoneXBlock/actions/workflows/ci.yml/badge.svg
  :target: https://github.com/openedx/DoneXBlock/actions/workflows/ci.yml

.. |Publish package to PyPi| image:: https://github.com/openedx/DoneXBlock/actions/workflows/pypi-release.yml/badge.svg
  :target: https://github.com/openedx/DoneXBlock/actions/workflows/pypi-release.yml

Purpose
=======

Lets a student mark they've finished an activity. The student can
click through two states of the XBlock, shown below:

| |mark|
| |undo|

.. |mark| image:: completionxblock_mark.png
.. |undo| image:: completionxblock_undo.png

Status
======

Maintained

Getting Help
============

If you're having trouble, we have discussion forums at https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a `Slack invitation`_, then join our `community Slack workspace`_.

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx-slack-invite.herokuapp.com/
.. _community Slack workspace: https://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help


How to Contribute
=================

Details about how to become a contributor to the Open edX project may
be found in the wiki at `How to contribute`_

.. _How to contribute: https://openedx.atlassian.net/wiki/spaces/COMM/pages/941457737/How+to+start+contributing+to+the+Open+edX+code+base

The Open edX Code of Conduct
----------------------------

All community members should familarize themselves with the `Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

People
======

The assigned maintainers for this component and other project details
may be found in `Backstage`_ or groked from inspecting catalog-info.yaml.

.. _Backstage: https://open-edx-backstage.herokuapp.com/catalog/default/component/DoneXBlock,

Reporting Security Issues
=========================

Please do not report security issues in public. Please email security@edx.org.


History
=======

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
