huckPersonExtender: customize the person object for the Huck Institutes

Versions

  Developed for Plone 3.3.1 and copied from the MobilePhoneExtender example
  provided with FacultyStaffDirectory so it should work fine in Plone 2.5 
  but will extend all Plone sites. Works even better in Plone 3, where it 
  can be installed or uninstalled on individual Plone sites independently.

Dependencies

  * "FacultyStaffDirectory":http://plone.org/products/faculty-staff-directory/ 2.x
  
  * archetypes.schemaextender 1.x

Description
  
     Fields added:
          * fax: fax number
          * campus: campus they are located at
          * building: building they are located in
               used for the DirectorySolutions building directory PCs
               (choices are: LSB, Wartik, or MSC)
          * room: room number they are located in
               used for the DirectorySolutions building directory PCs

     Fields hidden:


     Other changes:

Installing the Example Extender

  1. Install FacultyStaffDirectory according to that product's README.txt.
  
  2. Place FSDPersonExtender folder in the Products folder.
  
  3. Restart Zope.
  
  4. If you're using Plone 3 or later, go to your-plone-site &rarr; site setup
     &rarr; Add/Remove Products, and install FacultyStaffDirectoryExtender.
     In Plone 2.5, it will be installed simply by virtue of being in the
     Products folder.

Using the Example Extender
    
  1. In your Faculty/Staff Directory object, add a Person.
  
  2. Click the Person's Edit tab.

Version History
  
      2.0 -- Revised version for Plone 3.x
      
      1.0 -- Initial release for Plone 2.5

Authorship

  This product was developed by Paul Rentschler of the Huck Institutes of the 
  Life Sciences at Penn State University.
  
Support

  * Please report bugs to the
    "WebLion issue tracker": https://weblion.psu.edu/trac/weblion/newticket?component=FacultyStaffDirectory&version=2.0.

  * More documentation: https://weblion.psu.edu/trac/weblion/wiki/FacultyStaffDirectory

  * Contact us:

    Huck Institutes Web Team
    Penn State University
    401 Life Sciences Building
    University Park, PA 16802
    webteam@huck.psu.edu

License

    Copyright (c) 2006-2008 The Pennsylvania State University. WebLion is
    developed and maintained by the WebLion Project Team, its partners, and
    members of the Penn State Zope Users Group.

    This program is free software; you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation; either version 2 of the License, or (at your option)
    any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
    more details.

    You should have received a copy of the GNU General Public License along with
    this program; if not, write to the Free Software Foundation, Inc., 59 Temple
    Place, Suite 330, Boston, MA 02111-1307 USA.

    This document is written using the Structured Text format for conversion
    into alternative formats.
