from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.FacultyStaffDirectory.extenderInstallation import installExtenderGloballyIfLocallyIsNotSupported
from Products.GenericSetup import EXTENSION, profile_registry

from Products.huckPersonExtender.person import additionalInfoExtender
from Products.huckPersonExtender.person import bldgDirExtender
from Products.huckPersonExtender.person import modifyHuckFields

installExtenderGloballyIfLocallyIsNotSupported(additionalInfoExtender, 'huckPersonExtender.additionalInfoExtender')
installExtenderGloballyIfLocallyIsNotSupported(bldgDirExtender, 'huckPersonExtender.bldgDirExtender')
installExtenderGloballyIfLocallyIsNotSupported(modifyHuckFields, 'huckPersonExtender.modifyHuckFields')

registerDirectory('skins', globals())

def initialize(context):
    profile_registry.registerProfile(
        "default",
        "huckPersonExtender",
        "Customize the Faculty/Staff Directory's Person type for the Huck Institutes.",
        "profiles/default",
        product="Products.huckPersonExtender",
        profile_type=EXTENSION,
        for_=IPloneSiteRoot)
    profile_registry.registerProfile(
        "uninstall",
        "huckPersonExtender Uninstall",
        "Removes the changes to the Faculty/Staff Directory's Person type to customize it for the Huck Institutes.",
        "profiles/uninstall",
        product="Products.huckPersonExtender",
        profile_type=EXTENSION,
        for_=IPloneSiteRoot)








