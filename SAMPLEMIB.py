# PySNMP SMI module. Autogenerated from smidump -f python SAMPLEMIB
# by libsmi2pysnmp-0.1.3 at Sun Sep 21 00:22:28 2014,
# Python version sys.version_info(major=2, minor=7, micro=5, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, experimental, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "experimental")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

sampleOrg = MibIdentifier((1, 3, 6, 1, 3, 2222))
sampleMIB = ModuleIdentity((1, 3, 6, 1, 3, 2222, 1)).setRevisions(("2014-09-20 00:00",))
if mibBuilder.loadTexts: sampleMIB.setOrganization("None")
if mibBuilder.loadTexts: sampleMIB.setContactInfo("https://github.com/juneedahamed/pysnmp_sample")
if mibBuilder.loadTexts: sampleMIB.setDescription("This is an sample mib to learn how to use pysnmp")
sampleAgent = MibIdentifier((1, 3, 6, 1, 3, 2222, 1, 1))
sampleNotifications = MibIdentifier((1, 3, 6, 1, 3, 2222, 1, 1, 0))
sampleNotificationObjects = MibIdentifier((1, 3, 6, 1, 3, 2222, 1, 1, 0, 1))
sampleNotificationDisplayAttr = MibScalar((1, 3, 6, 1, 3, 2222, 1, 1, 0, 1, 2), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: sampleNotificationDisplayAttr.setDescription("A sample attribute to be associated with the notification")
sampleNotificationNumericAttr = MibScalar((1, 3, 6, 1, 3, 2222, 1, 1, 0, 1, 5), Integer32()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: sampleNotificationNumericAttr.setDescription("A sample attribute to be associated with the notification")
sampleAttrs = MibIdentifier((1, 3, 6, 1, 3, 2222, 1, 1, 1))
sampleReadAttr = MibScalar((1, 3, 6, 1, 3, 2222, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sampleReadAttr.setDescription("A sample read only attribute")
sampleReadWriteAttr = MibScalar((1, 3, 6, 1, 3, 2222, 1, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sampleReadWriteAttr.setDescription("A sample read write attribute")
sampleMIBConformances = MibIdentifier((1, 3, 6, 1, 3, 2222, 1, 1, 2))

# Augmentions

# Notifications

sampleNotification = NotificationType((1, 3, 6, 1, 3, 2222, 1, 1, 0, 2)).setObjects(*(("SAMPLEMIB", "sampleNotificationNumericAttr"), ("SAMPLEMIB", "sampleNotificationDisplayAttr"), ) )
if mibBuilder.loadTexts: sampleNotification.setDescription("A sample Notification")

# Groups

sampleGetOrSetObjectsGroup = ObjectGroup((1, 3, 6, 1, 3, 2222, 1, 1, 2, 2)).setObjects(*(("SAMPLEMIB", "sampleReadAttr"), ("SAMPLEMIB", "sampleReadWriteAttr"), ) )
if mibBuilder.loadTexts: sampleGetOrSetObjectsGroup.setDescription("Attrs that can be get or set on this agent")
sampleNotificationObjectsGroup = NotificationGroup((1, 3, 6, 1, 3, 2222, 1, 1, 2, 3)).setObjects(*(("SAMPLEMIB", "sampleNotificationNumericAttr"), ("SAMPLEMIB", "sampleNotificationDisplayAttr"), ) )
if mibBuilder.loadTexts: sampleNotificationObjectsGroup.setDescription("Objects associated with notifications")
sampleNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 2222, 1, 1, 2, 4)).setObjects(*(("SAMPLEMIB", "sampleNotification"), ) )
if mibBuilder.loadTexts: sampleNotificationGroup.setDescription("All Notifications sent by this agent")

# Compliances

sampleMIBConformance = ModuleCompliance((1, 3, 6, 1, 3, 2222, 1, 1, 2, 1)).setObjects(*(("SAMPLEMIB", "sampleGetOrSetObjectsGroup"), ("SAMPLEMIB", "sampleNotificationObjectsGroup"), ("SAMPLEMIB", "sampleNotificationGroup"), ) )
if mibBuilder.loadTexts: sampleMIBConformance.setDescription("Compliance statement for this MIB")

# Exports

# Module identity
mibBuilder.exportSymbols("SAMPLEMIB", PYSNMP_MODULE_ID=sampleMIB)

# Objects
mibBuilder.exportSymbols("SAMPLEMIB", sampleOrg=sampleOrg, sampleMIB=sampleMIB, sampleAgent=sampleAgent, sampleNotifications=sampleNotifications, sampleNotificationObjects=sampleNotificationObjects, sampleNotificationDisplayAttr=sampleNotificationDisplayAttr, sampleNotificationNumericAttr=sampleNotificationNumericAttr, sampleAttrs=sampleAttrs, sampleReadAttr=sampleReadAttr, sampleReadWriteAttr=sampleReadWriteAttr, sampleMIBConformances=sampleMIBConformances)

# Notifications
mibBuilder.exportSymbols("SAMPLEMIB", sampleNotification=sampleNotification)

# Groups
mibBuilder.exportSymbols("SAMPLEMIB", sampleGetOrSetObjectsGroup=sampleGetOrSetObjectsGroup, sampleNotificationObjectsGroup=sampleNotificationObjectsGroup, sampleNotificationGroup=sampleNotificationGroup)

# Compliances
mibBuilder.exportSymbols("SAMPLEMIB", sampleMIBConformance=sampleMIBConformance)
