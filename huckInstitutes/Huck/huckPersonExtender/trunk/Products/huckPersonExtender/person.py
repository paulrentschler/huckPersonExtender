from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, ISchemaModifier
from Products.Archetypes.atapi import *
from zope.interface import implements, Interface
from zope.component import adapts, provideAdapter

from Products.CMFCore.permissions import View, ModifyPortalContent
from AccessControl import ClassSecurityInfo

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.Relations.field import RelationField

from Products.FacultyStaffDirectory.interfaces.person import IPerson
from Products.huckPersonExtender import PersonExtenderMessageFactory


# Any field you tack on must have ExtensionField as its first subclass:
class _StringExtensionField(ExtensionField, StringField):
    pass
class _TextExtensionField(ExtensionField, TextField):
    pass
class _BooleanExtensionField(ExtensionField, BooleanField):
    pass
class _RelationExtensionField(ExtensionField, RelationField):
    pass


class addHuckFields(object):
    """Adapter that adds new fields to Person.
       """
    adapts(IPerson)
    implements(ISchemaExtender)

    _fields = [
            _StringExtensionField('nickName',
                required=False,
                searchable=True,
                schemata="General",
                widget=StringWidget(
                    label=u"Nickname",
                    description=u"If you use a different form of your first name, provide it here. (example: Bob for a first name of Robert)."
                )
            ),
            
            _StringExtensionField('fax',
                required=False,
                searchable=True,
                schemata="General",
                widget=StringWidget(
                    label=u"Office Fax",
                    description=u"Example: 555-555-5555"
                )
            ),

            _StringExtensionField('campus',
                required=False,
                searchable=True,
                schemata="General",
                widget=MultiSelectionWidget(
                    label=u"Campus",
                    description=u"Indicate the campus(es) you have an office at.",
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
                schemata="Administrative",
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
                schemata="Administrative",
                widget=StringWidget(
                    label=u"Room number",
                    description=u"Example: 401B. Only used for certain buildings that have computerized directories."
                )
            ),
            
            _RelationExtensionField('advisors',
                required=False,
                searchable=False,
                schemata="Administrative",
                validators=(),
                widget=ReferenceBrowserWidget(
                    label=u'Advisors',
                    base_query="_search_people_in_this_fsd",
                    allow_browse=0,
                    allow_search=1,
                    show_results_without_query=1,
                    startup_directory_method="_get_parent_fsd_path",
                    restrict_browsing_to_startup_directory=True,
                ),
                write_permission="Modify portal content",
                allowed_types=('FSDPerson'),
                multiValued=True,
                relationship='people_advisors'
            ),
            
        ]


    def __init__(self, context):
        self.context = context
    
    def getFields(self):
        return self._fields


class modifyHuckFields(object):
    """Change the wording and order of a few fields; hide fields that will 
       not be used
       """
    adapts(IPerson)
    implements(ISchemaModifier)
    
    security = ClassSecurityInfo()

    def __init__(self, context):
        self.context = context

    from Products.FacultyStaffDirectory.Person import schema

    def fiddle(object, schema):
        """Move fields into a General or Administrative schemata and 
           hide the fields we will not be using at all
           """
        tmp_field = schema['firstName'].copy()
        tmp_field.schemata = "General"
        schema['firstName'] = tmp_field
        
        tmp_field = schema['middleName'].copy()
        tmp_field.schemata = "General"
        schema['middleName'] = tmp_field

        tmp_field = schema['lastName'].copy()
        tmp_field.schemata = "General"
        schema['lastName'] = tmp_field

        tmp_field = schema['suffix'].copy()
        tmp_field.schemata = "General"
        schema['suffix'] = tmp_field

        tmp_field = schema['email'].copy()
        tmp_field.widget.label = "E-mail Address"
        tmp_field.schemata = "General"
        schema['email'] = tmp_field

        tmp_field = schema['jobTitles'].copy()
        tmp_field.schemata = "Administrative"
        schema['jobTitles'] = tmp_field

        tmp_field = schema['officeAddress'].copy()
        tmp_field.widget.label = "Office Address (room and building ONLY)"
        tmp_field.widget.description = "The campus will be listed along with this information."
        tmp_field.schemata = "General"
        schema['officeAddress'] = tmp_field

        tmp_field = schema['officeCity'].copy()
        #tmp_field.widget.visible={'edit':'invisible','view':'invisible'}
        tmp_field.schemata = "General"
        schema['officeCity'] = tmp_field

        tmp_field = schema['officeState'].copy()
        #tmp_field.widget.visible={'edit':'invisible','view':'invisible'}
        tmp_field.schemata = "General"
        schema['officeState'] = tmp_field

        tmp_field = schema['officePostalCode'].copy()
        #tmp_field.widget.visible={'edit':'invisible','view':'invisible'}
        tmp_field.schemata = "General"
        schema['officePostalCode'] = tmp_field

        tmp_field = schema['officePhone'].copy()
        tmp_field.schemata = "General"
        schema['officePhone'] = tmp_field

        tmp_field = schema['fax'].copy()
        tmp_field.schemata = "General"
        schema['fax'] = tmp_field

        tmp_field = schema['image'].copy()
        tmp_field.widget.description = "Upload a professional image of yourself that focuses on your face. The image should be 200px wide."
        tmp_field.schemata = "General"
        schema['image'] = tmp_field

        tmp_field = schema['biography'].copy()
        tmp_field.widget.label = "Research Interests / Contact Regarding"
        tmp_field.widget.description = "Describe your research or work duties as they relate to the Huck Institutes."
        tmp_field.schemata = "General"
        schema['biography'] = tmp_field

        tmp_field = schema['education'].copy()
        tmp_field.widget.label = "Degrees Obtained"
        tmp_field.widget.description = "One degree per line. Example: PhD (1995) Penn State: Subject area or thesis title"
        tmp_field.schemata = "General"
        schema['education'] = tmp_field

        tmp_field = schema['websites'].copy()
        tmp_field.widget.label = "Other Web Sites About You"
        tmp_field.widget.description = "You can specify one or more websites (one per line) that people can go to read more about you, for instance, your departmental web page and/or lab web site. Example: http://www.example.com/"
        tmp_field.schemata = "General"
        schema['websites'] = tmp_field

        tmp_field = schema['id'].copy()
        tmp_field.widget.description = "Example: abc123 (the part of your default Penn State email address before @psu.edu)."
        tmp_field.schemata = "Administrative"
        schema['id'] = tmp_field

        tmp_field = schema['classifications'].copy()
        tmp_field.widget.label = "Choose a category that best describes the person"
        tmp_field.widget.description = "You can select more than one if necessary."
        tmp_field.schemata = "Administrative"
        schema['classifications'] = tmp_field

        tmp_field = schema['departments'].copy()
        tmp_field.widget.label = "Home Department(s)"
        tmp_field.widget.description = "(Faculty ONLY) Select the departments you are affiliated with."
        tmp_field.schemata = "General"
        schema['departments'] = tmp_field

        tmp_field = schema['committees'].copy()
        tmp_field.widget.label = "Labs"
        tmp_field.widget.description = "Select the labs this person is a member of."
        tmp_field.schemata = "Administrative"
        schema['committees'] = tmp_field

        tmp_field = schema['specialties'].copy()
        tmp_field.widget.label = "Specialties / Areas of Expertise"
        tmp_field.widget.description = "Select one or more areas where the person has expertise or research interests. Note: some areas have sub-areas you can select (e.g. cognitive neuroscience is a sub-area of neuroscience)."
        tmp_field.schemata = "Administrative"
        schema['specialties'] = tmp_field

        tmp_field = schema['assistants'].copy()
        tmp_field.schemata = "General"
        schema['assistants'] = tmp_field

        tmp_field = schema['campus'].copy()
        tmp_field.widget.description = "Indicate the campus(es) you have an office at."
        tmp_field.schemata = "General"
        schema['campus'] = tmp_field

        tmp_field = schema['building'].copy()
        tmp_field.widget.visible={'edit':'invisible','view':'invisible'}
        schema['building'] = tmp_field

        tmp_field = schema['room'].copy()
        tmp_field.widget.visible={'edit':'invisible','view':'invisible'}
        schema['room'] = tmp_field

        #tmp_field = schema['advisor'].copy()
        #tmp_field.widget.label = ""
        #tmp_field.widget.description = ""
        #tmp_field.schemata = "General"
        #schema['advisor'] = tmp_field
        
        tmp_field = schema['subject'].copy()
        tmp_field.schemata = "Administrative"
        schema['subject'] = tmp_field
        
        tmp_field = schema['effectiveDate'].copy()
        tmp_field.schemata = "Administrative"
        tmp_field.widget.description = "If this date is in the future, the person will not show up in listings and searches until this date. If this date is in the past, it can be used to control the order of the person's appearance in listings."
        schema['effectiveDate'] = tmp_field
        
        tmp_field = schema['expirationDate'].copy()
        tmp_field.schemata = "Administrative"
        tmp_field.widget.description = "When this date is reached, the person will be marked as having left the Huck Institutes."
        schema['expirationDate'] = tmp_field
        
        # move some typically hidden fields to the right schemata
        for fieldName in ['title', 'password', 'confirmPassword']:
            tmp_field = schema[fieldName].copy()
            tmp_field.schemata = "General"
            schema[fieldName] = tmp_field
        
        
        # reorder how the fields are displayed in the General schemata
        schema.moveField('nickName', after='suffix')
        schema.moveField('campus', before='officeAddress')
        schema.moveField('fax', after='officePhone')
        schema.moveField('email', after='fax')
        schema.moveField('websites', after='biography')
        schema.moveField('assistants', after='departments')
        schema.moveField('password', after='assistants')
        schema.moveField('confirmPassword', after='password')
        
        # reorder how the fields are displayed in the Administrative schemata
        schema.moveField('id', after='confirmPassword')
        schema.moveField('classifications', after='id')
        schema.moveField('jobTitles', after='classifications')
        schema.moveField('specialties', after='jobTitles')
        schema.moveField('committees', after='specialties')
        schema.moveField('advisors', after='committees')
        schema.moveField('subject', after='advisors')
        schema.moveField('building', after='subject')
        schema.moveField('room', after='building')
        
        
        # set permission conditions on some of the schemata
        for schemataName in ['User Settings', 
                             'categorization', 
                             'dates', 
                             'ownership', 
                             'settings',
                             ]:
            for fieldName in schema.getSchemataFields(schemataName):
                fieldName.widget.condition="python:member.has_role('Manager')"

        for fieldName in schema.getSchemataFields('Administrative'):
            fieldName.widget.condition="python:member.checkPermission('FacultyStaffDirectory: Assign Specialties to People', here)"                 


        # convenient commands for figuring out what fields are in which
        #  schemata and in what order the fields are REALLY in
        #for x in schema.fields(): print x
        #print schema.getSchemataNames()
        #import pdb; pdb.set_trace()

        return schema
