from Products.CMFCore.utils import getToolByName
from Products.FacultyStaffDirectory.extenderInstallation import localAdaptersAreSupported, installExtender, uninstallExtender
from Products.huckPersonExtender.person import addHuckFields
from Products.huckPersonExtender.person import modifyHuckFields

_adapterName = 'huckPersonExtender'

def _runProfile(profile, portal):
    setupTool = getToolByName(portal, 'portal_setup')
    setupTool.runAllImportStepsFromProfile(profile)

def install(portal):
    if localAdaptersAreSupported:
        installExtender(portal, addHuckFields, _adapterName)
        installExtender(portal, modifyHuckFields, _adapterName)
    _runProfile('profile-Products.huckPersonExtender:default', portal)

def uninstall(portal):
    if localAdaptersAreSupported:
        uninstallExtender(portal, addHuckFields, _adapterName)
        uninstallExtender(portal, modifyHuckFields, _adapterName)
    _runProfile('profile-Products.huckPersonExtender:uninstall', portal)
