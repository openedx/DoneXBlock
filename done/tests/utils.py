"""
Utility methods for test cases
"""


from workbench.runtime import WorkbenchRuntime
from xblock.fields import ScopeIds
from xblock.runtime import DictKeyValueStore, KvsFieldData
from done import DoneXBlock


def make_block():
    """ Instantiate a Done XBlock inside a WorkbenchRuntime """
    block_type = 'done-xblock'
    key_store = DictKeyValueStore()
    field_data = KvsFieldData(key_store)
    runtime = WorkbenchRuntime()
    runtime.course_id = "dummy_course_id"
    def_id = runtime.id_generator.create_definition(block_type)
    usage_id = runtime.id_generator.create_usage(def_id)
    scope_ids = ScopeIds('user', block_type, def_id, usage_id)
    return DoneXBlock(runtime, field_data, scope_ids=scope_ids)


def make_url():
    runtime = WorkbenchRuntime()
    xblock = make_block()
    url = runtime.handler_url(xblock, 'toggle_button')
    return url
