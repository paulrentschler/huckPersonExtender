from Products.CMFCore.utils import getToolByName
from Products.FacultyStaffDirectory.extenderInstallation import localAdaptersAreSupported, installExtender, uninstallExtender
from Products.huckPersonExtender.person import additionalInfoExtender
from Products.huckPersonExtender.person import bldgDirExtender
from Products.huckPersonExtender.person import modifyHuckFields

_adapterName = 'huckPersonExtender'

def _runProfile(profile, portal):
    setupTool = getToolByName(portal, 'portal_setup')
    setupTool.runAllImportStepsFromProfile(profile)

def install(portal):
    if localAdaptersAreSupported:
        installExtender(portal, additionalInfoExtender, _adapterName)
        installExtender(portal, bldgDirExtender, _adapterName)
        installExtender(portal, modifyHuckFields, _adapterName)
    _runProfile('profile-Products.huckPersonExtender:default', portal)

def uninstall(portal):
    if localAdaptersAreSupported:
        uninstallExtender(portal, additionalInfoExtender, _adapterName)
        uninstallExtender(portal, bldgDirExtender, _adapterName)
        uninstallExtender(portal, modifyHuckFields, _adapterName)
    _runProfile('profile-Products.huckPersonExtender:uninstall', portal)
