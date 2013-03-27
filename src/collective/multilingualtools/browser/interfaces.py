from collective.multilingualtools import _
from zope import interface, schema
from z3c.form import button


class INamingSchema(interface.Interface):
    """ Base Schema for the edit form. It is dynamically extended by plugins
    """
    text = schema.Text(
        title=_("title_text", default=u"Text"),
        description=_(
            "description_text", default=u"Type some text. This text will then "
            u"be written on all translations as Title or Description, "
            u"depending on your further choices in this form."),
        required=True,
    )

    po_domain = schema.TextLine(
        title=_("title_po_domain", default=u"PO Domain"),
        description=_(
            "description_po_domain", default=u"Give a po domain here, if you "
            u"have typed a message id in the field above. The translation for "
            u"this domain of the message you have typed will then be written "
            u"as Title / Description. If you leave the domain empty or state a"
            u"non-existing one, the text above will be written verbatim."),
        default=u"plone",
        required=False,
    )

    set_title = button.Button(title=u'Set text as Title')
    set_description = button.Button(title=u'Set text as Description')


class IObjectHandlingSchema(interface.Interface):
    """ object handling """

    old_id = schema.Choice(
        title=_("title_old_id", default=u"Object to rename"),
        description=_(
            "description_old_id", default=u"Choose an object to rename. The "
            u"drop-down displays the available objects with their titles plus "
            u"their id in bracktets."),
        required=False,
        vocabulary="collective.multilingualtools.vocabularies.available_ids",
    )

    new_id = schema.TextLine(
        title=_("title_new_id", default=u"New id"),
        description=_(
            "description_new_id", default=u"Enter the id (short name) that"
            u"all translations of this item should receive."
        ),
        required=False,
    )

    id_to_delete = schema.Choice(
        title=_("title_id_to_delete", default=u"Object to delete"),
        description=_(
            "description_id_to_delete", default=u"Select an object that should"
            u" be deleted in all languages."),
        required=False,
        vocabulary="collective.multilingualtools.vocabularies.available_ids",
    )

    id_to_move = schema.Choice(
        title=_("title_id_to_move", default=u"Object to move"),
        description=_(
            "description_id_to_move", default=u"Choose an object to move."),
        required=False,
        vocabulary="collective.multilingualtools.vocabularies.available_ids",
    )

    target_path = schema.TextLine(
        title=_("title_target_path", default=u"Target path"),
        description=_(
            "description_target_path", default=u"Enter either an absolute path"
            u" or a path relative to the current location. Examples: "
            u"'/en/path/to/folder' (absolute); 'subfolder/from/here' or '../'"
            u" (relative)"),
        required=False,
    )

    rename = button.Button(title=u'Rename')
    delete = button.Button(title=u'Delete')
    cut_and_paste = button.Button(title=u'Cut and paste')


class IPortletSchema(interface.Interface):
    """ Portlet Schema for the edit form. """
    propagate_portlets = button.Button(title=u'Propagate Portlets')

    block_portlets = button.Button(title=u'Block Portlets')

    blockstatus = schema.Bool(
        title=_("title_blockstatus", default=u"Check to block"),
        description=u"",
        required=False,
    )

    portlet_manager = schema.Choice(
        title=_("title_portlet_manager", default=u"Portlet manager"),
        description=_(
            "description_portlet_manager", default=u"Select a portlet manager"
            u" on which to perform the desired action. Leave unselected to "
            u"perform the action for all portlet slots."),
        required=False,
        vocabulary="collective.multilingualtools.vocabularies.portletmanagers",
    )


class IReindexSchema(interface.Interface):
    """ Schema for the Reindex All form. """
    reindex_all = button.Button(title=u'Reindex all')


class IWorkflowSchema(interface.Interface):
    """ Schema for the Publish All form. """
    do_action = button.Button(title=u'Perform workflow change')

    transition = schema.Choice(
        title=_("title_transition", default=u"Available actions"),
        description=_(
            "description_transition", default=u"Use this form to change the "
            u"workflow status of the current object and all translations."),
        required=False,
        vocabulary="collective.multilingualtools.vocabularies.available_wf_transitions",
    )


class IDuplicaterSchema(interface.Interface):
    """ Schema for object duplication"""
    translate_this = button.Button(title=u'Translate this object')

    attributes_to_copy = schema.List(
        title=_("title_attributes_to_copy", default=u'Attributes to copy'),
        description=_(
            "description_attributes_to_copy", default=u'Select one or more '
            u'attributes to have their values copied over to the '
            u'translations.'),
        default=list(),
        required=False,
        value_type=schema.Choice(
            vocabulary="collective.multilingualtools.vocabularies.translatable_fields",
        ),
    )

    target_languages = schema.List(title=u'Manual language selection',
            description=u'Select the languages to which you want to make a '\
            u'copy of the current object. Leave blank to select all '\
            u'available languages.',
            default=list(),
            required=False,
            value_type=schema.Choice(
                vocabulary="collective.multilingualtools.vocabularies.supported_languages",
                ),
            )

    use_parent_languages = schema.Bool(title=u"Use parent folder's languages",
            description=u'Tick this box to copy the object to all languages '\
            u'in which the folder that contains it (= parent folder) is '\
            u'available. This setting takes precedence over the manual '\
            u'selection above.',
            required=False,
            )

    translation_exists = schema.Bool(
            title=u"Translation exists",
            description=u"Tick this box if a translation alreay exits and "\
                u"you just want to propagate attributes or Collection "\
                u"criteria.",
            required=False,
            )


class IPropertySchema(interface.Interface):
    """ Schema for setting and removing properties """

    property_id = schema.TextLine(
        title=u"Property id",
        description=u"Enter a property id",
        required=False,
        )

    property_type = schema.Choice(
            title=u"Property type",
            description=u"Select the correct property type",
            required=False,
            vocabulary="collective.multilingualtools.vocabularies.available_property_types",
            )

    property_value = schema.TextLine(
        title=u"Property value",
        description=u"Enter a value for the property",
        required=False,
        )

    property_to_delete = schema.Choice(
            title=u"Property to delete",
            description=u"Select a property to delete",
            required=False,
            vocabulary="collective.multilingualtools.vocabularies.available_property_ids",
            )

    set_property = button.Button(title=u'Set property')
    delete_property = button.Button(title=u'Delete property')


class IMarkerInterfacesSchema(interface.Interface):
    """ Schema for the marker interface form. """
    remove_interface = button.Button(title=u'Remove selected interface')
    add_interface = button.Button(title=u'Add selected interface')

    interface_to_add = schema.Choice(
            title=u"Available interfaces",
            description=u"Select a marker interface to add to all " \
                u"translations",
            required=False,
            vocabulary="collective.multilingualtools.vocabularies.available_interfaces",
            )

    interface_to_remove = schema.Choice(
            title=u"Provided interfaces",
            description=u"Select a marker interface to remove from all " \
                u"translations",
            required=False,
            vocabulary="collective.multilingualtools.vocabularies.provided_interfaces",
            )


class IOutdatedSchema(interface.Interface):
    """ Schema for the toggle-outdated form """
    toggle_outdated = button.Button(title=u'Set outdated status')

    outdated_status = schema.Bool(
            title=u"Tick the box to mark as outdated, or leave it unchecked "\
                "to remove the outdated status flag.",
            description=u"",
            required=False)
