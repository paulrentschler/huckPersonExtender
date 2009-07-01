from Products.FacultyStaffDirectory.extenderInstallation import declareInstallRoutines

from Products.huckPersonExtender.person import additionalInfoExtender
from Products.huckPersonExtender.person import bldgDirExtender
from Products.huckPersonExtender.person import modifyHuckFields

declareInstallRoutines(globals(), additionalInfoExtender, 'huckPersonExtender.additionalInfoExtender')
declareInstallRoutines(globals(), bldgDirExtender, 'huckPersonExtender.bldgDirExtender')
declareInstallRoutines(globals(), modifyHuckFields, 'huckPersonExtender.modifyHuckFields')

# If you need to do further things at installation, declare your own install() and uninstall() rather than using declareInstallRoutines(). Do what you need to, and also call extenderInstallation.installExtender() (and uninstallExtender(), respectively) if extenderInstallation.localAdaptersAreSupported is True.


# the code below only works in Plone 3, not Plone 2.5

#def install(portal):
#    """Register the extender so it takes effect on this Plone site."""
#    sm = portal.getSiteManager()  # local components are not per-container; they are per-sitemanager. It just so happens that every Plone site has a sitemanager.
#    sm.registerAdapter(additionalInfoExtender, name='huckPersonExtenderAdditionalInfoExtender')
#    sm.registerAdapter(bldgDirExtender, name='huckPersonExtenderBldgDirExtender')
#    sm.registerAdapter(modifyHuckFields, name='huckPersonExtenderModifyHuckFields')

#    return "Registered the extender at the root of the Plone site."


#def uninstall(portal):
#    """Unregister the schema extender so it no longer takes effect on this Plone site."""
#    sm = portal.getSiteManager()
#    sm.unregisterAdapter(additionalInfoExtender, name='huckPersonExtenderAdditionalInfoExtender')
#    sm.unregisterAdapter(bldgDirExtender, name='huckPersonExtenderBldgDirExtender')
#    sm.unregisterAdapter(modifyHuckFields, name='huckPersonExtenderModifyHuckFields')

#    return "Removed the extender from the root of the Plone site."

