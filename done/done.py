"""
Show a toggle which lets students mark things as done.
"""


import uuid

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Boolean, DateTime, Float, Scope, String
try:
    from xblock.utils.resources import ResourceLoader
except ModuleNotFoundError:  # For backward compatibility with releases older than Quince.
    from xblockutils.resources import ResourceLoader

resource_loader = ResourceLoader(__name__)


def _(text):
    """
    Make '_' a no-op, so we can scrape strings
    """
    return text


def resource_string(path):
    """Retrieves the contents of a file as a string from the specified path."""
    return resource_loader.load_unicode(path)


@XBlock.needs('i18n')
class DoneXBlock(XBlock):
    """
    Show a toggle which lets students mark things as done.
    """

    done = Boolean(
        scope=Scope.user_state,
        help=_("Is the student done?"),
        default=False
    )

    align = String(
        scope=Scope.settings,
        help=_("Align left/right/center"),
        default="left"
    )

    has_score = True

    # pylint: disable=unused-argument
    @XBlock.json_handler
    def toggle_button(self, data, suffix=''):
        """
        Ajax call when the button is clicked. Input is a JSON dictionary
        with one boolean field: `done`. This will save this in the
        XBlock field, and then issue an appropriate grade.
        """
        if 'done' in data:
            self.done = data['done']
            if data['done']:
                grade = 1
            else:
                grade = 0
            grade_event = {'value': grade, 'max_value': 1}
            self.runtime.publish(self, 'grade', grade_event)
            # This should move to self.runtime.publish, once that pipeline
            # is finished for XBlocks.
            self.runtime.publish(self, "edx.done.toggled", {'done': self.done})

        return {'state': self.done}

    def student_view(self, context=None):  # pylint: disable=unused-argument
        """
        The primary view of the DoneXBlock, shown to students
        when viewing courses.
        """
        frag = Fragment()
        frag.add_content(resource_loader.render_django_template(
            'templates/done.html',
            {
                'id': uuid.uuid1(0),
                'done': self.done,
            },
            i18n_service=self.runtime.service(self, 'i18n')
        ))
        (unchecked_png, checked_png) = (
            self.runtime.local_resource_url(self, x) for x in
            ('public/check-empty.png', 'public/check-full.png')
        )
        frag.add_css(resource_string("static/css/done.css"))
        frag.add_javascript(resource_string("static/js/src/done.js"))
        frag.initialize_js("DoneXBlock", {'state': self.done,
                                          'unchecked': unchecked_png,
                                          'checked': checked_png,
                                          'align': self.align.lower()})
        return frag

    def studio_view(self, _context=None):
        """
        Minimal view with no configuration options giving some help text.
        """
        frag = Fragment()
        frag.add_content(resource_loader.render_django_template(
            'templates/studioview.html',
            {},
            i18n_service=self.runtime.service(self, 'i18n')
        ))
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("DoneXBlock",
             """<vertical_demo>
                  <done align="left"> </done>
                  <done align="right"> </done>
                  <done align="center"> </done>
                </vertical_demo>
             """),
        ]

    # Everything below is stolen from
    # https://github.com/openedx/edx-ora2/blob/master/apps/openassessment/
    #        xblock/lms_mixin.py
    # It's needed to keep the LMS+Studio happy.
    # It should be included as a mixin.

    display_name = String(
        default="Completion", scope=Scope.settings,
        help=_("Display name")
    )

    start = DateTime(
        default=None, scope=Scope.settings,
        help=_("ISO-8601 formatted string representing the start date of this assignment. We ignore this.")
    )

    due = DateTime(
        default=None, scope=Scope.settings,
        help=_("ISO-8601 formatted string representing the due date of this assignment. We ignore this.")
    )

    weight = Float(
        display_name=_("Problem Weight"),
        help=_(
            "Defines the number of points each problem is worth. "
            "If the value is not set, the problem is worth the sum of the "
            "option point values."
        ),
        values={"min": 0, "step": .1},
        scope=Scope.settings
    )

    def has_dynamic_children(self):
        """
        Do we dynamically determine our children? No, we don't have any.
        """
        return False

    def max_score(self):
        """
        The maximum raw score of our problem.
        """
        return 1
