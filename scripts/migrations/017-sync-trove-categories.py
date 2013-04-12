#       Licensed to the Apache Software Foundation (ASF) under one
#       or more contributor license agreements.  See the NOTICE file
#       distributed with this work for additional information
#       regarding copyright ownership.  The ASF licenses this file
#       to you under the Apache License, Version 2.0 (the
#       "License"); you may not use this file except in compliance
#       with the License.  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#       Unless required by applicable law or agreed to in writing,
#       software distributed under the License is distributed on an
#       "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#       KIND, either express or implied.  See the License for the
#       specific language governing permissions and limitations
#       under the License.

import sys
import logging

from pylons import tmpl_context as c
from ming.orm import session
from ming.orm.ormsession import ThreadLocalORMSession

from allura import model as M

log = logging.getLogger(__name__)

def create_trove_cat(cat_data):
    M.TroveCategory(trove_cat_id=cat_data[0], trove_parent_id=cat_data[1],
                    shortname=cat_data[2], fullname=cat_data[3], fullpath=cat_data[4])

def main():
    create_trove_cat((639,14,"cpal","Common Public Attribution License 1.0 (CPAL)","License :: OSI-Approved Open Source :: Common Public Attribution License 1.0 (CPAL)"))
    create_trove_cat((640,99,"dvd","DVD","Topic :: Multimedia :: DVD"))
    create_trove_cat((641,576,"workflow","Workflow","Topic :: Office/Business :: Enterprise :: Workflow"))
    create_trove_cat((642,292,"linuxdrivers","Linux","Topic :: System :: Hardware :: Hardware Drivers :: Linux"))
    create_trove_cat((643,582,"uml","UML","Topic :: Software Development :: Design :: UML"))
    create_trove_cat((644,92,"cms","CMS Systems","Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CMS Systems"))
    create_trove_cat((645,92,"blogging","Blogging","Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Blogging"))
    create_trove_cat((646,52,"subversion","Subversion","Topic :: Software Development :: Version Control :: Subversion"))
    create_trove_cat((647,612,"webservices","Web Services","Topic :: Formats and Protocols :: Protocols :: Web Services"))
    create_trove_cat((648,554,"json","JSON","Topic :: Formats and Protocols :: Data Formats :: JSON"))
    create_trove_cat((649,100,"imagegalleries","Image Galleries","Topic :: Multimedia :: Graphics :: Image Galleries"))
    create_trove_cat((650,612,"ajax","AJAX","Topic :: Formats and Protocols :: Protocols :: AJAX"))
    create_trove_cat((651,92,"wiki","Wiki","Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki"))
    create_trove_cat((652,45,"appservers","Application Servers","Topic :: Software Development :: Application Servers"))
    create_trove_cat((653,20,"rssreaders","RSS Feed Readers","Topic :: Communications :: RSS Feed Readers"))
    create_trove_cat((654,129,"ecommerce","E-Commerce / Shopping","Topic :: Office/Business :: E-Commerce / Shopping"))
    create_trove_cat((656,99,"htpc","Home Theater PC","Topic :: Multimedia :: Home Theater PC"))
    create_trove_cat((658,22,"jabber","Jabber","Topic :: Communications :: Chat :: Jabber"))
    create_trove_cat((659,576,"enterprisebpm","Business Performance Management","Topic :: Office/Business :: Enterprise :: Business Performance Management"))
    create_trove_cat((660,576,"enterprisebi","Business Intelligence","Topic :: Office/Business :: Enterprise :: Business Intelligence"))
    create_trove_cat((661,75,"budgetingandforecasting","Budgeting and Forecasting","Topic :: Office/Business :: Financial :: Budgeting and Forecasting"))
    create_trove_cat((662,497,"ingres","Ingres","Database Environment :: Network-based DBMS :: Ingres"))
    create_trove_cat((663,92,"socialnetworking","Social Networking","Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Social Networking"))
    create_trove_cat((664,199,"virtualization","Virtualization","Operating System :: Virtualization"))
    create_trove_cat((665,664,"vmware","VMware","Operating System :: Virtualization :: VMware"))
    create_trove_cat((666,664,"xen","Xen","Operating System :: Virtualization :: Xen"))
    create_trove_cat((667,247,"voip","VoIP","Topic :: Communications :: Telephony :: VoIP"))
    create_trove_cat((668,92,"ticketing","Ticketing Systems","Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Ticketing Systems"))
    create_trove_cat((669,315,"blackberryos","Blackberry RIM OS","Operating System :: Handheld/Embedded Operating Systems :: Blackberry RIM OS"))
    create_trove_cat((671,14,"ms-pl","Microsoft Public License","License :: OSI-Approved Open Source :: Microsoft Public License"))
    create_trove_cat((672,14,"ms-rl","Microsoft Reciprocal License","License :: OSI-Approved Open Source :: Microsoft Reciprocal License"))
    create_trove_cat((673,576,"bsm","Business Service Management","Topic :: Office/Business :: Enterprise :: Business Service Management"))
    create_trove_cat((674,673,"servicesupport","Service Support","Topic :: Office/Business :: Enterprise :: Business Service Management :: Service Support"))
    create_trove_cat((675,673,"serviceassurance","Service Assurance","Topic :: Office/Business :: Enterprise :: Business Service Management :: Service Assurance"))
    create_trove_cat((676,673,"serviceautomation","Service Automation","Topic :: Office/Business :: Enterprise :: Business Service Management :: Service Automation"))
    create_trove_cat((677,14,"artisticv2","Artistic License 2.0","License :: OSI-Approved Open Source :: Artistic License 2.0"))
    create_trove_cat((678,14,"boostlicense","Boost Software License (BSL1.0)","License :: OSI-Approved Open Source :: Boost Software License (BSL1.0)"))
    create_trove_cat((679,14,"gplv3","GNU General Public License version 3.0 (GPLv3)","License :: OSI-Approved Open Source :: GNU General Public License version 3.0 (GPLv3)"))
    create_trove_cat((680,14,"lgplv3","GNU Library or ""Lesser"" General Public License version 3.0 (LGPLv3)","License :: OSI-Approved Open Source :: GNU Library or ""Lesser"" General Public License version 3.0 (LGPLv3)"))
    create_trove_cat((681,14,"isclicense","ISC License","License :: OSI-Approved Open Source :: ISC License"))
    create_trove_cat((682,14,"multicslicense","Multics License","License :: OSI-Approved Open Source :: Multics License"))
    create_trove_cat((683,14,"ntplicense","NTP License","License :: OSI-Approved Open Source :: NTP License"))
    create_trove_cat((684,14,"nposl3","Non-Profit Open Software License 3.0 (Non-Profit OSL 3.0)","License :: OSI-Approved Open Source :: Non-Profit Open Software License 3.0 (Non-Profit OSL 3.0)"))
    create_trove_cat((685,14,"rpl15","Reciprocal Public License 1.5 (RPL1.5)","License :: OSI-Approved Open Source :: Reciprocal Public License 1.5 (RPL1.5)"))
    create_trove_cat((686,14,"splicense2","Simple Public License 2.0","License :: OSI-Approved Open Source :: Simple Public License 2.0"))
    create_trove_cat((687,673,"cmdb","Configuration Management Database (CMDB)","Topic :: Office/Business :: Enterprise :: Business Service Management :: Configuration Management Database (CMDB)"))
    create_trove_cat((688,18,"mobileapps","Mobile","Topic :: Mobile"))
    create_trove_cat((689,315,"winmobile","Windows Mobile","Operating System :: Handheld/Embedded Operating Systems :: Windows Mobile"))
    create_trove_cat((690,315,"brew","BREW (Binary Runtime Environment for Wireless)","Operating System :: Handheld/Embedded Operating Systems :: BREW (Binary Runtime Environment for Wireless)"))
    create_trove_cat((691,315,"j2me","J2ME (Java Platform, Micro Edition)","Operating System :: Handheld/Embedded Operating Systems :: J2ME (Java Platform, Micro Edition)"))
    create_trove_cat((692,315,"maemo","Maemo","Operating System :: Handheld/Embedded Operating Systems :: Maemo"))
    create_trove_cat((693,315,"limo","LiMo (Linux Mobile)","Operating System :: Handheld/Embedded Operating Systems :: LiMo (Linux Mobile)"))
    create_trove_cat((694,160,"clean","Clean","Programming Language :: Clean"))
    create_trove_cat((695,160,"lasso","Lasso","Programming Language :: Lasso"))
    create_trove_cat((696,160,"turing","Turing","Programming Language :: Turing"))
    create_trove_cat((697,160,"glsl","GLSL (OpenGL Shading Language)","Programming Language :: GLSL (OpenGL Shading Language)"))
    create_trove_cat((698,160,"lazarus","Lazarus","Programming Language :: Lazarus"))
    create_trove_cat((699,160,"freepascal","Free Pascal","Programming Language :: Free Pascal"))
    create_trove_cat((700,160,"scriptol","Scriptol","Programming Language :: Scriptol"))
    create_trove_cat((701,160,"pl-i","PL/I (Programming Language One)","Programming Language :: PL/I (Programming Language One)"))
    create_trove_cat((702,160,"oz","Oz","Programming Language :: Oz"))
    create_trove_cat((703,160,"limbo","Limbo","Programming Language :: Limbo"))
    create_trove_cat((704,160,"scala","Scala","Programming Language :: Scala"))
    create_trove_cat((705,160,"blitzmax","BlitzMax","Programming Language :: BlitzMax"))
    create_trove_cat((706,160,"xbaseclipper","XBase/Clipper","Programming Language :: XBase/Clipper"))
    create_trove_cat((707,160,"curl","Curl","Programming Language :: Curl"))
    create_trove_cat((708,160,"flex","Flex","Programming Language :: Flex"))
    create_trove_cat((709,160,"mathematica","Mathematica","Programming Language :: Mathematica"))
    create_trove_cat((710,160,"visualdataflex","Visual DataFlex","Programming Language :: Visual DataFlex"))
    create_trove_cat((711,160,"fenix","Fenix","Programming Language :: Fenix"))
    create_trove_cat((713,456,"vexi","Vexi","User Interface :: Graphical :: Vexi"))
    create_trove_cat((714,160,"kaya","Kaya","Programming Language :: Kaya"))
    create_trove_cat((715,160,"transcript-revolution","Transcript/Revolution","Programming Language :: Transcript/Revolution"))
    create_trove_cat((716,160,"haXe","haXe","Programming Language :: haXe"))
    create_trove_cat((717,160,"proglangmeta","Project is a programming language","Programming Language :: Project is a programming language"))
    create_trove_cat((718,634,"msxb360","Microsoft Xbox 360","Operating System :: Other Operating Systems :: Console-based Platforms :: Microsoft Xbox 360"))
    create_trove_cat((719,634,"nintendogc","Nintendo GameCube","Operating System :: Other Operating Systems :: Console-based Platforms :: Nintendo GameCube"))
    create_trove_cat((720,634,"nintendowii","Nintendo Wii","Operating System :: Other Operating Systems :: Console-based Platforms :: Nintendo Wii"))
    create_trove_cat((721,634,"sonyps3","Sony PlayStation 3","Operating System :: Other Operating Systems :: Console-based Platforms :: Sony PlayStation 3"))
    create_trove_cat((722,634,"sonypsp","Sony PlayStation Portable (PSP)","Operating System :: Other Operating Systems :: Console-based Platforms :: Sony PlayStation Portable (PSP)"))
    create_trove_cat((723,160,"scilab","Scilab","Programming Language :: Scilab"))
    create_trove_cat((724,160,"scicos","Scicos","Programming Language :: Scicos"))
    create_trove_cat((725,534,"management","Management","Intended Audience :: by End-User Class :: Management"))
    create_trove_cat((726,71,"edadministration","Administration","Topic :: Education :: Administration"))
    create_trove_cat((727,97,"mechcivileng","Mechanical and Civil Engineering","Topic :: Scientific/Engineering :: Mechanical and Civil Engineering"))
    create_trove_cat((729,535,"audienceengineering","Engineering","Intended Audience :: by Industry or Sector :: Engineering"))
    create_trove_cat((730,274,"basque","Basque (Euskara)","Translations :: Basque (Euskara)"))
    create_trove_cat((731,14,"classpath","GNU General Public License with Classpath exception (Classpath::License)","License :: OSI-Approved Open Source :: GNU General Public License with Classpath exception (Classpath::License)"))
    create_trove_cat((732,727,"caddcam","Computer-aided technologies (CADD/CAM/CAE)","Topic :: Scientific/Engineering :: Mechanical and Civil Engineering :: Computer-aided technologies (CADD/CAM/CAE)"))
    create_trove_cat((733,576,"humanresources","Human Resources","Topic :: Office/Business :: Enterprise :: Human Resources"))
    create_trove_cat((734,554,"mcml","Media Center Markup Language (MCML)","Topic :: Formats and Protocols :: Data Formats :: Media Center Markup Language (MCML)"))
    create_trove_cat((735,461,"nsis","Nullsoft Scriptable Install System (NSIS)","User Interface :: Plugins :: Nullsoft Scriptable Install System (NSIS)"))
    create_trove_cat((736,97,"scada","SCADA","Topic :: Scientific/Engineering :: SCADA"))
    create_trove_cat((737,461,"autohotkey","AutoHotkey","User Interface :: Plugins :: AutoHotkey"))
    create_trove_cat((738,160,"autoit","AutoIt","Programming Language :: AutoIt"))
    create_trove_cat((739,132,"humanitarianism","Humanitarianism","Topic :: Religion and Philosophy :: Humanitarianism"))
    create_trove_cat((740,129,"insurance","Insurance","Topic :: Office/Business :: Insurance"))
    create_trove_cat((741,97,"linguistics","Linguistics","Topic :: Scientific/Engineering :: Linguistics"))
    create_trove_cat((742,741,"machinetranslation","Machine Translation","Topic :: Scientific/Engineering :: Linguistics :: Machine Translation"))
    create_trove_cat((743,43,"antispam","Anti-Spam","Topic :: Security :: Anti-Spam"))
    create_trove_cat((744,43,"antivirus","Anti-Virus","Topic :: Security :: Anti-Virus"))
    create_trove_cat((745,43,"antimalware","Anti-Malware","Topic :: Security :: Anti-Malware"))
    create_trove_cat((746,554,"autocaddxf","AutoCAD DXF","Topic :: Formats and Protocols :: Data Formats :: AutoCAD DXF"))
    create_trove_cat((747,75,"billing","Billing","Topic :: Office/Business :: Financial :: Billing"))
    create_trove_cat((748,576,"processmanagement","Business Process Management","Topic :: Office/Business :: Enterprise :: Business Process Management"))
    create_trove_cat((749,136,"embedded","Embedded systems","Topic :: System :: Embedded systems"))
    create_trove_cat((750,456,"magicui","Magic User Interface (MUI)","User Interface :: Graphical :: Magic User Interface (MUI)"))
    create_trove_cat((751,237,"xul","XUL","User Interface :: Web-based :: XUL"))
    create_trove_cat((752,80,"flightsim","Flight simulator","Topic :: Games/Entertainment :: Flight simulator"))
    create_trove_cat((753,63,"vivim","Vi/Vim","Topic :: Text Editors :: Vi/Vim"))
    create_trove_cat((754,45,"sourceanalysis","Source code analysis","Topic :: Software Development :: Source code analysis"))
    create_trove_cat((755,45,"sourcebrowsing","Source code browsing","Topic :: Software Development :: Source code browsing"))
    create_trove_cat((756,576,"plm","Product lifecycle management (PLM)","Topic :: Office/Business :: Enterprise :: Product lifecycle management (PLM)"))
    create_trove_cat((757,274,"breton","Breton","Translations :: Breton"))
    create_trove_cat((758,498,"db4o","db4objects (db4o)","Database Environment :: File-based DBMS :: db4objects (db4o)"))
    create_trove_cat((759,497,"nexusdb","NexusDB","Database Environment :: Network-based DBMS :: NexusDB"))
    create_trove_cat((760,160,"prism","Prism","Programming Language :: Prism"))
    create_trove_cat((761,45,"collaborative","Collaborative development tools","Topic :: Software Development :: Collaborative development tools"))
    create_trove_cat((762,91,"pluginsaddons","Plugins and add-ons","Topic :: Internet :: WWW/HTTP :: Browsers :: Plugins and add-ons"))
    create_trove_cat((763,456,"winaero","Windows Aero","User Interface :: Graphical :: Windows Aero"))
    create_trove_cat((764,45,"agile","Agile development tools","Topic :: Software Development :: Agile development tools"))
    create_trove_cat((765,535,"agriculture","Agriculture","Intended Audience :: by Industry or Sector :: Agriculture"))
    create_trove_cat((766,100,"animation","Animation","Topic :: Multimedia :: Graphics :: Animation"))
    create_trove_cat((767,45,"assemblers","Assemblers","Topic :: Software Development :: Assemblers"))
    create_trove_cat((768,535,"automotive","Automotive","Intended Audience :: by Industry or Sector :: Automotive"))
    create_trove_cat((769,554,"CSV","Comma-separated values (CSV)","Topic :: Formats and Protocols :: Data Formats :: Comma-separated values (CSV)"))
    create_trove_cat((770,45,"softdevlibraries","Libraries","Topic :: Software Development :: Libraries"))
    create_trove_cat((771,45,"sourcereview","Source code review","Topic :: Software Development :: Source code review"))
    create_trove_cat((772,80,"hobbies","Hobbies","Topic :: Games/Entertainment :: Hobbies"))
    create_trove_cat((773,772,"collectionmanage","Collection management","Topic :: Games/Entertainment :: Hobbies :: Collection management"))
    create_trove_cat((774,80,"multiplayer","Multiplayer","Topic :: Games/Entertainment :: Multiplayer"))
    create_trove_cat((775,80,"mmorpg","MMORPG","Topic :: Games/Entertainment :: MMORPG"))
    create_trove_cat((776,97,"mapping","Mapping","Topic :: Scientific/Engineering :: Mapping"))
    create_trove_cat((777,776,"gps","GPS (Global Positioning System)","Topic :: Scientific/Engineering :: Mapping :: GPS (Global Positioning System)"))
    create_trove_cat((778,43,"passwordmanage","Password manager","Topic :: Security :: Password manager"))
    create_trove_cat((779,315,"linksyswrt54g","Linksys WRT54G series","Operating System :: Handheld/Embedded Operating Systems :: Linksys WRT54G series"))
    create_trove_cat((781,576,"medhealth","Medical/Healthcare","Topic :: Office/Business :: Enterprise :: Medical/Healthcare"))
    create_trove_cat((782,45,"bined","Binary editors","Topic :: Software Development :: Binary editors"))
    create_trove_cat((783,99,"mmcatalog","Cataloguing","Topic :: Multimedia :: Cataloguing"))
    create_trove_cat((784,113,"composition","Composition","Topic :: Multimedia :: Sound/Audio :: Composition"))
    create_trove_cat((785,772,"cooking","Cooking","Topic :: Games/Entertainment :: Hobbies :: Cooking"))
    create_trove_cat((786,136,"cron","Cron and scheduling","Topic :: System :: Cron and scheduling"))
    create_trove_cat((787,638,"recovery","Data recovery","Topic :: System :: Storage :: Data recovery"))
    create_trove_cat((788,87,"otherfile","Other file transfer protocol","Topic :: Internet :: Other file transfer protocol"))
    create_trove_cat((789,581,"digpreserve","Digital preservation","Topic :: Education :: Library :: Digital preservation"))
    create_trove_cat((790,251,"directconnect","Direct Connect","Topic :: Communications :: File Sharing :: Direct Connect"))
    create_trove_cat((791,129,"dtp","Desktop Publishing","Topic :: Office/Business :: Desktop Publishing"))
    create_trove_cat((792,580,"etl","ETL","Topic :: Office/Business :: Enterprise :: Data Warehousing :: ETL"))
    create_trove_cat((793,55,"fonts","Fonts","Topic :: Desktop Environment :: Fonts"))
    create_trove_cat((794,80,"gameframeworks","Game development framework","Topic :: Games/Entertainment :: Game development framework"))
    create_trove_cat((795,100,"handrec","Handwriting recognition","Topic :: Multimedia :: Graphics :: Handwriting recognition"))
    create_trove_cat((796,136,"homeauto","Home Automation","Topic :: System :: Home Automation"))
    create_trove_cat((797,63,"translation","Computer Aided Translation (CAT)","Topic :: Text Editors :: Computer Aided Translation (CAT)"))
    create_trove_cat((798,136,"osdistro","OS distribution","Topic :: System :: OS distribution"))
    create_trove_cat((799,798,"livecd","Live CD","Topic :: System :: OS distribution :: Live CD"))
    create_trove_cat((800,497,"lotusnotes","Lotus Notes/Domino","Database Environment :: Network-based DBMS :: Lotus Notes/Domino"))
    create_trove_cat((801,160,"lotusscript","LotusScript","Programming Language :: LotusScript"))
    create_trove_cat((802,133,"machinelearning","Machine Learning","Topic :: Scientific/Engineering :: Artificial Intelligence :: Machine Learning"))
    create_trove_cat((803,106,"metadata","Metadata editors","Topic :: Multimedia :: Graphics :: Editors :: Metadata editors"))
    create_trove_cat((804,236,"riscos","RISC OS","Operating System :: Other Operating Systems :: RISC OS"))
    create_trove_cat((805,282,"politics","Politics","Topic :: Social sciences :: Politics"))
    create_trove_cat((806,80,"sports","Sports","Topic :: Games/Entertainment :: Sports"))
    create_trove_cat((807,282,"psychology","Psychology","Topic :: Social sciences :: Psychology"))
    create_trove_cat((808,458,"ogre3d","Ogre3D","User Interface :: Toolkits/Libraries :: Ogre3D"))
    create_trove_cat((809,45,"orm","ORM (Object-relational mapping)","Topic :: Software Development :: ORM (Object-relational mapping)"))
    create_trove_cat((810,575,"perftest","Performance Testing","Topic :: Software Development :: Testing :: Performance Testing"))
    create_trove_cat((811,75,"personalfinance","Personal finance","Topic :: Office/Business :: Financial :: Personal finance"))
    create_trove_cat((812,499,"pearmdb2","PHP Pear::MDB2","Database Environment :: Database API :: PHP Pear::MDB2"))
    create_trove_cat((813,461,"intellij","IntelliJ","User Interface :: Plugins :: IntelliJ"))
    create_trove_cat((814,554,"postscript","PostScript","Topic :: Formats and Protocols :: Data Formats :: PostScript"))
    create_trove_cat((815,100,"fractals","Fractals and Procedural Generation","Topic :: Multimedia :: Graphics :: Fractals and Procedural Generation"))
    create_trove_cat((816,554,"w3cvoice","W3C Voice","Topic :: Formats and Protocols :: Data Formats :: W3C Voice"))
    create_trove_cat((817,97,"quantumcomp","Quantum Computing","Topic :: Scientific/Engineering :: Quantum Computing"))
    create_trove_cat((818,129,"reportgen","Report Generators","Topic :: Office/Business :: Report Generators"))
    create_trove_cat((819,581,"research","Research","Topic :: Education :: Library :: Research"))
    create_trove_cat((820,87,"ssh","SSH (Secure SHell)","Topic :: Internet :: SSH (Secure SHell)"))
    create_trove_cat((821,554,"semantic","Semantic Web (RDF, OWL, etc.)","Topic :: Formats and Protocols :: Data Formats :: Semantic Web (RDF, OWL, etc.)"))
    create_trove_cat((822,90,"socialbookmarking","Social Bookmarking","Topic :: Internet :: WWW/HTTP :: Social Bookmarking"))
    create_trove_cat((823,20,"synchronization","Synchronization","Topic :: Communications :: Synchronization"))
    create_trove_cat((824,45,"templates","Templates","Topic :: Software Development :: Templates"))
    create_trove_cat((825,97,"testmeasure","Test and Measurement","Topic :: Scientific/Engineering :: Test and Measurement"))
    create_trove_cat((826,98,"statistics","Statistics","Topic :: Scientific/Engineering :: Mathematics :: Statistics"))
    create_trove_cat((827,129,"knowledgemanagement","Knowledge Management","Topic :: Office/Business :: Knowledge Management"))
    create_trove_cat((828,147,"unattended","Unattended","Topic :: System :: Installation/Setup :: Unattended"))
    create_trove_cat((829,457,"emailinterface","Email-based interface","User Interface :: Textual :: Email-based interface"))
    create_trove_cat((830,282,"voting","Voting","Topic :: Social sciences :: Voting"))
    create_trove_cat((831,27,"webconferencing","Web Conferencing","Topic :: Communications :: Conferencing :: Web Conferencing"))
    create_trove_cat((832,27,"videoconferencing","Video Conferencing","Topic :: Communications :: Conferencing :: Video Conferencing"))
    create_trove_cat((833,160,"objectivec2","Objective-C 2.0","Programming Language :: Objective-C 2.0"))
    create_trove_cat((834,274,"georgian","Georgian","Translations :: Georgian"))
    create_trove_cat((835,499,"adonet","ADO.NET","Database Environment :: Database API :: ADO.NET"))
    create_trove_cat((836,554,"xbrl","XBRL","Topic :: Formats and Protocols :: Data Formats :: XBRL"))
    create_trove_cat((837,461,"excel","Excel","User Interface :: Plugins :: Excel"))
    create_trove_cat((838,160,"visualbasicforapplications","Visual Basic for Applications (VBA)","Programming Language :: Visual Basic for Applications (VBA)"))
    create_trove_cat((839,160,"booprogramminglang","Boo","Programming Language :: Boo"))
    create_trove_cat((840,52,"git","Git","Topic :: Software Development :: Version Control :: Git"))
    create_trove_cat((841,52,"mercurial","Mercurial","Topic :: Software Development :: Version Control :: Mercurial"))
    create_trove_cat((842,52,"bazaar","Bazaar","Topic :: Software Development :: Version Control :: Bazaar"))
    create_trove_cat((843,14,"eupublicense","European Union Public License","License :: OSI-Approved Open Source :: European Union Public License"))
    create_trove_cat((844,14,"ipafontlicense","IPA Font License","License :: OSI-Approved Open Source :: IPA Font License"))
    create_trove_cat((845,14,"miroslicense","MirOS License","License :: OSI-Approved Open Source :: MirOS License"))
    create_trove_cat((846,14,"openfontlicense11","Open Font License 1.1 (OFL 1.1)","License :: OSI-Approved Open Source :: Open Font License 1.1 (OFL 1.1)"))
    create_trove_cat((847,80,"realtimetactical","Real Time Tactical","Topic :: Games/Entertainment :: Real Time Tactical"))
    create_trove_cat((848,160,"algol68","ALGOL 68","Programming Language :: ALGOL 68"))
    create_trove_cat((849,92,"groupware","Groupware","Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Groupware"))
    create_trove_cat((850,576,"businesscontinuity","Business Continuity","Topic :: Office/Business :: Enterprise :: Business Continuity"))
    create_trove_cat((852,554,"teiformat","TEI","Topic :: Formats and Protocols :: Data Formats :: TEI"))
    create_trove_cat((853,160,"clarion","Clarion","Programming Language :: Clarion"))
    create_trove_cat((854,576,"sales","Sales","Topic :: Office/Business :: Enterprise :: Sales"))
    create_trove_cat((855,97,"buildingauto","Building Automation","Topic :: Scientific/Engineering :: Building Automation"))
    create_trove_cat((856,129,"businessmodelling","Modelling","Topic :: Office/Business :: Modelling"))
    create_trove_cat((857,150,"routing","Routing","Topic :: System :: Networking :: Routing"))
    create_trove_cat((858,97,"medicalphysics","Medical Physics","Topic :: Scientific/Engineering :: Medical Physics"))
    create_trove_cat((859,71,"edlanguage","Languages","Topic :: Education :: Languages"))
    create_trove_cat((860,97,"molecularmech","Molecular Mechanics","Topic :: Scientific/Engineering :: Molecular Mechanics"))
    create_trove_cat((861,148,"loganalysis","Log Analysis","Topic :: System :: Logging :: Log Analysis"))

    ThreadLocalORMSession.flush_all()
    ThreadLocalORMSession.close_all()

if __name__ == '__main__':
    main()