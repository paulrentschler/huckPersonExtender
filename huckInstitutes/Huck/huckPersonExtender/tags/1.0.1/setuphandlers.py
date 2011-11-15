import logging
logger = logging.getLogger('huckPersonExtender: setuphandlers')
#from huckPersonExtender.config import PROJECTNAME
#from huckPersonExtender.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction

def isNotHuckPersonExtenderProfile(context):
    return context.readDataFile("huckPersonExtender_marker.txt") is None



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotHuckPersonExtenderProfile(context): return 
    shortContext = context._profile_path.split(os.path.sep)[-3]
    if shortContext != 'huckPersonExtender': # avoid infinite recursions
        return
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()


def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotHuckPersonExtenderProfile(context): return 
    shortContext = context._profile_path.split(os.path.sep)[-3]
    if shortContext != 'huckPersonExtender': # avoid infinite recursions
        return
    site = context.getSite()


def setupRelations(context):
    """Setup the Relations configuration."""
    shortContext = context._profile_path.split(os.path.sep)[:-2]
    shortContext.append('relations.xml')
    xmlpath = os.path.sep.join(shortContext)

    relations_tool = getToolByName(context.getSite(), 'relations_library')
    
    try:
        f = open(xmlpath)
        xml = f.read()
        f.close()
        relations_tool.importXML(xml)
    except:
        print "File not found to import: %s\n" % xmlpath

