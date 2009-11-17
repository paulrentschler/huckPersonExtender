from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, ISchemaModifier
from Products.Archetypes.atapi import *
from zope.interface import implements, Interface
from zope.component import adapts, provideAdapter

from Products.FacultyStaffDirectory.interfaces.person import IPerson


# Any field you tack on must have ExtensionField as its first subclass:
class _StringExtensionField(ExtensionField, StringField):
    pass


# Add fields for a fax number and the campus the person is located at
# Add fields for use in building the data file for the Building Directory computers
class addHuckFields(object):
    """Adapter that adds a building and room number field to Person."""
    adapts(IPerson)
    implements(ISchemaExtender)

    _fields = [
            _StringExtensionField('fax',
                required=False,
                searchable=True,
                schemata="Contact Information",
                widget=StringWidget(
                    label=u"Fax number",
                    description=u"Example: 814-865-4321"
                )
            ),

            _StringExtensionField('campus',
                required=False,
                searchable=True,
                schemata="Contact Information",
                widget=MultiSelectionWidget(
                    label=u"Campus",
                    description=u"Campus name",
                    format="checkbox"
                ),
                enforceVocabulary=True,
                vocabulary=[
                    ("University Park", "University Park"),
                    ("Hershey", "Hershey"),
                    ("Altoona", "Altoona"),
                    ("Mont Alto", "Mont Alto"),
                    ("Worthington Scranton", "Worthington Scranton"),
                ]
            ),
            
            _StringExtensionField('building',
                required=False,
                searchable=False,
                schemata="Contact Information",
                widget=SelectionWidget(
                    label=u"Building",
                    description=u"Building the person's office is in. Only used for certain buildings that have computerized directories.",
                    format="radio"
                ),
                enforceVocabulary=True,
                vocabulary=[
                    ("LSB", "Life Sciences Building"),
                    ("Wartik", "Wartik Laboratory"),
                    ("MSC", "Millennium Science Complex")
                ]
            ),

            _StringExtensionField('room',
                required=False,
                searchable=False,
                schemata="Contact Information",
                widget=StringWidget(
                    label=u"Room number",
                    description=u"Example: 401B. Only used for certain buildings that have computerized directories."
                )
            ),
        ]


    def __init__(self, context):
        self.context = context
    
    def getFields(self):
        return self._fields


# Change the wording and order of a few fields; hide fields that will not be used
class modifyHuckFields(object):
    adapts(IPerson)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    from Products.FacultyStaffDirectory.Person import schema

    def fiddle(object, schema):

        schema.moveField('education', before='jobTitles')
        schema.moveField('websites', after='classifications')
        schema.moveField('campus', before='officeAddress')
        schema.moveField('fax', after='officePhone')
        schema.moveField('building', after='campus')
        schema.moveField('room', after='building')

        schema['biography'].widget.label = "Responsibilities / Research interests"
        schema['classifications'].widget.label = "Choose a category that best describes you"
        schema['education'].widget.description = "One degree per line. Example: PhD (1995) Penn State: Subject area or thesis title"
        schema['firstName'].widget.description = "Required"
        schema['id'].widget.description = "Required. Example: abc123 (the part of your default Penn State email address before @psu.edu)"
        schema['image'].widget.description = "You can upload an image up to 200px wide by 250px high"
        schema['lastName'].widget.description = "Required"
        schema['specialties'].widget.description = "Browse to choose one or more areas where you have expertise or research interests. Note: some areas have sub-areas you can select (e.g. cognitive neuroscience is a sub-area of neuroscience)."
        schema['websites'].widget.label = "Other websites about you"
        schema['websites'].widget.description = "You can specify one or more websites (one per line) that people can go to read more about you, for instance, your departmental web page and/or lab website. Example: http://www.example.com/"
        schema['officeAddress'].widget.label = "Office Address (room and building)"

        schema['officeCity'].widget.visible={'edit':'invisible','view':'invisible'}
        schema['officeState'].widget.visible={'edit':'invisible','view':'invisible'}
        schema['officePostalCode'].widget.visible={'edit':'invisible','view':'invisible'}
        schema['departments'].widget.visible={'edit':'invisible','view':'invisible'}
        schema['committees'].widget.visible={'edit':'invisible','view':'invisible'}


        return schema

