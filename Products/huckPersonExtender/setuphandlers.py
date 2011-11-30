#import logging
#logger = logging.getLogger('huckPersonExtender: setuphandlers')
#from huckPersonExtender.config import PROJECTNAME
#from huckPersonExtender.config import DEPENDENCIES
from App.Common import package_home
from Products.CMFCore.utils import getToolByName
import os.path
#import transaction


def installRelationsRules(context):
    if context.readDataFile('installRelationsRules.txt') is None:
        return
        
    portal = context.getSite()
    relations_tool = getToolByName(portal, 'relations_library')
    
    xmlpath = os.path.join(package_home(globals()), 'relations.xml')
    try:
        f = open(xmlpath)
        xml = f.read()
        f.close()
        relations_tool.importXML(xml)
    except:
        print "File not found to import: %s\n" % xmlpath
