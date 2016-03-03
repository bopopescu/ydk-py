""" DIAL_CONTROL_MIB 

The MIB module to describe peer information for
demand access and possibly other kinds of interfaces.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ianaiftype.IANAifType_MIB import IANAifType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class DIALCONTROLMIB(object):
    """
    
    
    .. attribute:: callactivetable
    
    	A table containing information about active calls to a specific destination
    	**type**\: :py:class:`CallActiveTable <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallActiveTable>`
    
    .. attribute:: callhistory
    
    	
    	**type**\: :py:class:`CallHistory <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallHistory>`
    
    .. attribute:: callhistorytable
    
    	A table containing information about specific calls to a specific destination
    	**type**\: :py:class:`CallHistoryTable <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallHistoryTable>`
    
    .. attribute:: dialctlconfiguration
    
    	
    	**type**\: :py:class:`DialCtlConfiguration <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.DialCtlConfiguration>`
    
    .. attribute:: dialctlpeercfgtable
    
    	The list of peers from which the managed device will accept calls or to which it will place them
    	**type**\: :py:class:`DialCtlPeerCfgTable <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.DialCtlPeerCfgTable>`
    
    

    """

    _prefix = 'dial-control'
    _revision = '1996-09-23'

    def __init__(self):
        self.callactivetable = DIALCONTROLMIB.CallActiveTable()
        self.callactivetable.parent = self
        self.callhistory = DIALCONTROLMIB.CallHistory()
        self.callhistory.parent = self
        self.callhistorytable = DIALCONTROLMIB.CallHistoryTable()
        self.callhistorytable.parent = self
        self.dialctlconfiguration = DIALCONTROLMIB.DialCtlConfiguration()
        self.dialctlconfiguration.parent = self
        self.dialctlpeercfgtable = DIALCONTROLMIB.DialCtlPeerCfgTable()
        self.dialctlpeercfgtable.parent = self


    class CallActiveTable(object):
        """
        A table containing information about active
        calls to a specific destination.
        
        .. attribute:: callactiveentry
        
        	The information regarding a single active Connection. An entry in this table will be created when a call is started. An entry in this table will be deleted when an active call clears
        	**type**\: list of :py:class:`CallActiveEntry <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallActiveTable.CallActiveEntry>`
        
        

        """

        _prefix = 'dial-control'
        _revision = '1996-09-23'

        def __init__(self):
            self.parent = None
            self.callactiveentry = YList()
            self.callactiveentry.parent = self
            self.callactiveentry.name = 'callactiveentry'


        class CallActiveEntry(object):
            """
            The information regarding a single active Connection.
            An entry in this table will be created when a call is
            started. An entry in this table will be deleted when
            an active call clears.
            
            .. attribute:: callactiveindex
            
            	Small index variable to distinguish calls that start in the same hundredth of a second
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: callactivesetuptime
            
            	The value of sysUpTime when the call associated to this entry was started. This will be useful for an NMS to retrieve all calls after a specific time. Also, this object can be useful in finding large delays between the time the call was started and the time the call was connected. For ISDN media, this will be the time when the setup message was received from or sent to the network
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivecallorigin
            
            	The call origin
            	**type**\: :py:class:`CallActiveCallOrigin_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallActiveTable.CallActiveEntry.CallActiveCallOrigin_Enum>`
            
            .. attribute:: callactivecallstate
            
            	The current call state. unknown(1)     \- The call state is unknown. connecting(2)  \- A connection attempt (outgoing call)                  is being made. connected(3)   \- An incoming call is in the process                  of validation. active(4)      \- The call is active
            	**type**\: :py:class:`CallActiveCallState_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallActiveTable.CallActiveEntry.CallActiveCallState_Enum>`
            
            .. attribute:: callactivechargedunits
            
            	The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactiveconnecttime
            
            	The value of sysUpTime when the call was connected. If the call is not connected, this object will have a value of zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactiveinfotype
            
            	The information type for this call
            	**type**\: :py:class:`CallActiveInfoType_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallActiveTable.CallActiveEntry.CallActiveInfoType_Enum>`
            
            .. attribute:: callactivelogicalifindex
            
            	This is the ifIndex value of the logical interface through which this call was made. For ISDN media, this would be the ifIndex of the B channel which was used for this call. If the ifIndex value is unknown, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactivepeeraddress
            
            	The number this call is connected to. If the number is not available, then it will have a length of zero
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: callactivepeerid
            
            	This is the Id value of the peer table entry to which this call was made. If a peer table entry for this call does not exist or is unknown, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactivepeerifindex
            
            	This is the ifIndex value of the peer table entry to which this call was made. If a peer table entry for this call does not exist or is unknown, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callactivepeersubaddress
            
            	The subaddress this call is connected to. If the subaddress is undefined or not available, this will be a zero length string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: callactivereceivebytes
            
            	The number of bytes which were received for this call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivereceivepackets
            
            	The number of packets which were received for this call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivetransmitbytes
            
            	The number of bytes which were transmitted for this call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callactivetransmitpackets
            
            	The number of packets which were transmitted for this call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'dial-control'
            _revision = '1996-09-23'

            def __init__(self):
                self.parent = None
                self.callactiveindex = None
                self.callactivesetuptime = None
                self.callactivecallorigin = None
                self.callactivecallstate = None
                self.callactivechargedunits = None
                self.callactiveconnecttime = None
                self.callactiveinfotype = None
                self.callactivelogicalifindex = None
                self.callactivepeeraddress = None
                self.callactivepeerid = None
                self.callactivepeerifindex = None
                self.callactivepeersubaddress = None
                self.callactivereceivebytes = None
                self.callactivereceivepackets = None
                self.callactivetransmitbytes = None
                self.callactivetransmitpackets = None

            class CallActiveCallOrigin_Enum(Enum):
                """
                CallActiveCallOrigin_Enum

                The call origin.

                """

                ORIGINATE = 1

                ANSWER = 2

                CALLBACK = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DIALCONTROLMIB.CallActiveTable.CallActiveEntry.CallActiveCallOrigin_Enum']


            class CallActiveCallState_Enum(Enum):
                """
                CallActiveCallState_Enum

                The current call state.
                unknown(1)     \- The call state is unknown.
                connecting(2)  \- A connection attempt (outgoing call)
                                 is being made.
                connected(3)   \- An incoming call is in the process
                                 of validation.
                active(4)      \- The call is active.

                """

                UNKNOWN = 1

                CONNECTING = 2

                CONNECTED = 3

                ACTIVE = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DIALCONTROLMIB.CallActiveTable.CallActiveEntry.CallActiveCallState_Enum']


            class CallActiveInfoType_Enum(Enum):
                """
                CallActiveInfoType_Enum

                The information type for this call.

                """

                OTHER = 1

                SPEECH = 2

                UNRESTRICTEDDIGITAL = 3

                UNRESTRICTEDDIGITAL56 = 4

                RESTRICTEDDIGITAL = 5

                AUDIO31 = 6

                AUDIO7 = 7

                VIDEO = 8

                PACKETSWITCHED = 9

                FAX = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DIALCONTROLMIB.CallActiveTable.CallActiveEntry.CallActiveInfoType_Enum']


            @property
            def _common_path(self):
                if self.callactiveindex is None:
                    raise YPYDataValidationError('Key property callactiveindex is None')
                if self.callactivesetuptime is None:
                    raise YPYDataValidationError('Key property callactivesetuptime is None')

                return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callActiveTable/DIAL-CONTROL-MIB:callActiveEntry[DIAL-CONTROL-MIB:callActiveIndex = ' + str(self.callactiveindex) + '][DIAL-CONTROL-MIB:callActiveSetupTime = ' + str(self.callactivesetuptime) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.callactiveindex is not None:
                    return True

                if self.callactivesetuptime is not None:
                    return True

                if self.callactivecallorigin is not None:
                    return True

                if self.callactivecallstate is not None:
                    return True

                if self.callactivechargedunits is not None:
                    return True

                if self.callactiveconnecttime is not None:
                    return True

                if self.callactiveinfotype is not None:
                    return True

                if self.callactivelogicalifindex is not None:
                    return True

                if self.callactivepeeraddress is not None:
                    return True

                if self.callactivepeerid is not None:
                    return True

                if self.callactivepeerifindex is not None:
                    return True

                if self.callactivepeersubaddress is not None:
                    return True

                if self.callactivereceivebytes is not None:
                    return True

                if self.callactivereceivepackets is not None:
                    return True

                if self.callactivetransmitbytes is not None:
                    return True

                if self.callactivetransmitpackets is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DIALCONTROLMIB.CallActiveTable.CallActiveEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callActiveTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.callactiveentry is not None:
                for child_ref in self.callactiveentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DIALCONTROLMIB.CallActiveTable']['meta_info']


    class CallHistory(object):
        """
        
        
        .. attribute:: callhistoryretaintimer
        
        	The minimum amount of time that an callHistoryEntry will be maintained before being deleted. A value of 0 will prevent any history from being retained in the callHistoryTable, but will neither prevent callCompletion traps being generated nor affect other tables
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: callhistorytablemaxlength
        
        	The upper limit on the number of entries that the callHistoryTable may contain.  A value of 0 will prevent any history from being retained. When this table is full, the oldest entry will be deleted and the new one will be created
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'dial-control'
        _revision = '1996-09-23'

        def __init__(self):
            self.parent = None
            self.callhistoryretaintimer = None
            self.callhistorytablemaxlength = None

        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callHistory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.callhistoryretaintimer is not None:
                return True

            if self.callhistorytablemaxlength is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DIALCONTROLMIB.CallHistory']['meta_info']


    class CallHistoryTable(object):
        """
        A table containing information about specific
        calls to a specific destination.
        
        .. attribute:: callhistoryentry
        
        	The information regarding a single Connection
        	**type**\: list of :py:class:`CallHistoryEntry <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallHistoryTable.CallHistoryEntry>`
        
        

        """

        _prefix = 'dial-control'
        _revision = '1996-09-23'

        def __init__(self):
            self.parent = None
            self.callhistoryentry = YList()
            self.callhistoryentry.parent = self
            self.callhistoryentry.name = 'callhistoryentry'


        class CallHistoryEntry(object):
            """
            The information regarding a single Connection.
            
            .. attribute:: callactiveindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: callactivesetuptime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorycallorigin
            
            	The call origin
            	**type**\: :py:class:`CallHistoryCallOrigin_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallHistoryTable.CallHistoryEntry.CallHistoryCallOrigin_Enum>`
            
            .. attribute:: callhistorychargedunits
            
            	The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryconnecttime
            
            	The value of sysUpTime when the call was connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorydisconnectcause
            
            	The encoded network cause value associated with this call.  The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below
            	**type**\: str
            
            	**range:** 0..4
            
            .. attribute:: callhistorydisconnecttext
            
            	ASCII text describing the reason for call termination.  This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of dialCtlPeerStatsLastDisconnectCause
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: callhistorydisconnecttime
            
            	The value of sysUpTime when the call was disconnected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryinfotype
            
            	The information type for this call
            	**type**\: :py:class:`CallHistoryInfoType_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.CallHistoryTable.CallHistoryEntry.CallHistoryInfoType_Enum>`
            
            .. attribute:: callhistorylogicalifindex
            
            	This is the ifIndex value of the logical interface through which this call was made. For ISDN media, this would be the ifIndex of the B channel which was used for this call
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: callhistorypeeraddress
            
            	The number this call was connected to. If the number is not available, then it will have a length of zero
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: callhistorypeerid
            
            	This is the Id value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callhistorypeerifindex
            
            	This is the ifIndex value of the peer table entry to which this call was made. If a peer table entry for this call does not exist, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: callhistorypeersubaddress
            
            	The subaddress this call was connected to. If the subaddress is undefined or not available, this will be a zero length string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: callhistoryreceivebytes
            
            	The number of bytes which were received while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistoryreceivepackets
            
            	The number of packets which were received while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorytransmitbytes
            
            	The number of bytes which were transmitted while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: callhistorytransmitpackets
            
            	The number of packets which were transmitted while this call was active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'dial-control'
            _revision = '1996-09-23'

            def __init__(self):
                self.parent = None
                self.callactiveindex = None
                self.callactivesetuptime = None
                self.callhistorycallorigin = None
                self.callhistorychargedunits = None
                self.callhistoryconnecttime = None
                self.callhistorydisconnectcause = None
                self.callhistorydisconnecttext = None
                self.callhistorydisconnecttime = None
                self.callhistoryinfotype = None
                self.callhistorylogicalifindex = None
                self.callhistorypeeraddress = None
                self.callhistorypeerid = None
                self.callhistorypeerifindex = None
                self.callhistorypeersubaddress = None
                self.callhistoryreceivebytes = None
                self.callhistoryreceivepackets = None
                self.callhistorytransmitbytes = None
                self.callhistorytransmitpackets = None

            class CallHistoryCallOrigin_Enum(Enum):
                """
                CallHistoryCallOrigin_Enum

                The call origin.

                """

                ORIGINATE = 1

                ANSWER = 2

                CALLBACK = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DIALCONTROLMIB.CallHistoryTable.CallHistoryEntry.CallHistoryCallOrigin_Enum']


            class CallHistoryInfoType_Enum(Enum):
                """
                CallHistoryInfoType_Enum

                The information type for this call.

                """

                OTHER = 1

                SPEECH = 2

                UNRESTRICTEDDIGITAL = 3

                UNRESTRICTEDDIGITAL56 = 4

                RESTRICTEDDIGITAL = 5

                AUDIO31 = 6

                AUDIO7 = 7

                VIDEO = 8

                PACKETSWITCHED = 9

                FAX = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DIALCONTROLMIB.CallHistoryTable.CallHistoryEntry.CallHistoryInfoType_Enum']


            @property
            def _common_path(self):
                if self.callactiveindex is None:
                    raise YPYDataValidationError('Key property callactiveindex is None')
                if self.callactivesetuptime is None:
                    raise YPYDataValidationError('Key property callactivesetuptime is None')

                return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callHistoryTable/DIAL-CONTROL-MIB:callHistoryEntry[DIAL-CONTROL-MIB:callActiveIndex = ' + str(self.callactiveindex) + '][DIAL-CONTROL-MIB:callActiveSetupTime = ' + str(self.callactivesetuptime) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.callactiveindex is not None:
                    return True

                if self.callactivesetuptime is not None:
                    return True

                if self.callhistorycallorigin is not None:
                    return True

                if self.callhistorychargedunits is not None:
                    return True

                if self.callhistoryconnecttime is not None:
                    return True

                if self.callhistorydisconnectcause is not None:
                    return True

                if self.callhistorydisconnecttext is not None:
                    return True

                if self.callhistorydisconnecttime is not None:
                    return True

                if self.callhistoryinfotype is not None:
                    return True

                if self.callhistorylogicalifindex is not None:
                    return True

                if self.callhistorypeeraddress is not None:
                    return True

                if self.callhistorypeerid is not None:
                    return True

                if self.callhistorypeerifindex is not None:
                    return True

                if self.callhistorypeersubaddress is not None:
                    return True

                if self.callhistoryreceivebytes is not None:
                    return True

                if self.callhistoryreceivepackets is not None:
                    return True

                if self.callhistorytransmitbytes is not None:
                    return True

                if self.callhistorytransmitpackets is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DIALCONTROLMIB.CallHistoryTable.CallHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:callHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.callhistoryentry is not None:
                for child_ref in self.callhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DIALCONTROLMIB.CallHistoryTable']['meta_info']


    class DialCtlConfiguration(object):
        """
        
        
        .. attribute:: dialctlacceptmode
        
        	The security level for acceptance of incoming calls. acceptNone(1)  \- incoming calls will not be accepted acceptAll(2)   \- incoming calls will be accepted,                  even if there is no matching entry                  in the dialCtlPeerCfgTable acceptKnown(3) \- incoming calls will be accepted only                  if there is a matching entry in the                  dialCtlPeerCfgTable
        	**type**\: :py:class:`DialCtlAcceptMode_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.DialCtlConfiguration.DialCtlAcceptMode_Enum>`
        
        .. attribute:: dialctltrapenable
        
        	This object indicates whether dialCtlPeerCallInformation and dialCtlPeerCallSetup traps should be generated for all peers. If the value of this object is enabled(1), traps will be generated for all peers. If the value of this object is disabled(2), traps will be generated only for peers having dialCtlPeerCfgTrapEnable set to enabled(1)
        	**type**\: :py:class:`DialCtlTrapEnable_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.DialCtlConfiguration.DialCtlTrapEnable_Enum>`
        
        

        """

        _prefix = 'dial-control'
        _revision = '1996-09-23'

        def __init__(self):
            self.parent = None
            self.dialctlacceptmode = None
            self.dialctltrapenable = None

        class DialCtlAcceptMode_Enum(Enum):
            """
            DialCtlAcceptMode_Enum

            The security level for acceptance of incoming calls.
            acceptNone(1)  \- incoming calls will not be accepted
            acceptAll(2)   \- incoming calls will be accepted,
                             even if there is no matching entry
                             in the dialCtlPeerCfgTable
            acceptKnown(3) \- incoming calls will be accepted only
                             if there is a matching entry in the
                             dialCtlPeerCfgTable

            """

            ACCEPTNONE = 1

            ACCEPTALL = 2

            ACCEPTKNOWN = 3


            @staticmethod
            def _meta_info():
                from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DIALCONTROLMIB.DialCtlConfiguration.DialCtlAcceptMode_Enum']


        class DialCtlTrapEnable_Enum(Enum):
            """
            DialCtlTrapEnable_Enum

            This object indicates whether dialCtlPeerCallInformation
            and dialCtlPeerCallSetup traps should be generated for
            all peers. If the value of this object is enabled(1),
            traps will be generated for all peers. If the value
            of this object is disabled(2), traps will be generated
            only for peers having dialCtlPeerCfgTrapEnable set
            to enabled(1).

            """

            ENABLED = 1

            DISABLED = 2


            @staticmethod
            def _meta_info():
                from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DIALCONTROLMIB.DialCtlConfiguration.DialCtlTrapEnable_Enum']


        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:dialCtlConfiguration'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dialctlacceptmode is not None:
                return True

            if self.dialctltrapenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DIALCONTROLMIB.DialCtlConfiguration']['meta_info']


    class DialCtlPeerCfgTable(object):
        """
        The list of peers from which the managed device
        will accept calls or to which it will place them.
        
        .. attribute:: dialctlpeercfgentry
        
        	Configuration data for a single Peer. This entry is effectively permanent, and contains information to identify the peer, how to connect to the peer, how to identify the peer and its permissions. The value of dialCtlPeerCfgOriginateAddress must be specified before a new row in this table can become active(1). Any writeable parameters in an existing entry can be modified while the entry is active. The modification will take effect when the peer in question will be called the next time. An entry in this table can only be created if the associated ifEntry already exists
        	**type**\: list of :py:class:`DialCtlPeerCfgEntry <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.DialCtlPeerCfgTable.DialCtlPeerCfgEntry>`
        
        

        """

        _prefix = 'dial-control'
        _revision = '1996-09-23'

        def __init__(self):
            self.parent = None
            self.dialctlpeercfgentry = YList()
            self.dialctlpeercfgentry.parent = self
            self.dialctlpeercfgentry.name = 'dialctlpeercfgentry'


        class DialCtlPeerCfgEntry(object):
            """
            Configuration data for a single Peer. This entry is
            effectively permanent, and contains information
            to identify the peer, how to connect to the peer,
            how to identify the peer and its permissions.
            The value of dialCtlPeerCfgOriginateAddress must be
            specified before a new row in this table can become
            active(1). Any writeable parameters in an existing entry
            can be modified while the entry is active. The modification
            will take effect when the peer in question will be
            called the next time.
            An entry in this table can only be created if the
            associated ifEntry already exists.
            
            .. attribute:: dialctlpeercfgid
            
            	This object identifies a single peer. There may be several entries in this table for one peer, defining different ways of reaching this peer. Thus, there may be several entries in this table with the same value of dialCtlPeerCfgId. Multiple entries for one peer may be used to support multilink as well as backup lines. A single peer will be identified by a unique value of this object. Several entries for one peer MUST have the same value of dialCtlPeerCfgId, but different ifEntries and thus different values of ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dialctlpeercfgansweraddress
            
            	Calling Party Number information element, as for example passed in an ISDN SETUP message by a PBX or switch, for incoming calls. This address can be used to identify the peer. If this address is either unknown or identical to dialCtlPeerCfgOriginateAddress, this object will be a zero length string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: dialctlpeercfgcallretries
            
            	The number of calls to a non\-responding address that may be made. A retry count of zero means there is no bound. The intent is to bound the number of successive calls to an address which is inaccessible, or which refuses those calls.  Some countries regulate the number of call retries to a given peer that can be made
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgcarrierdelay
            
            	The call timeout time in seconds. The default value of zero means that the call timeout as specified for the media in question will apply
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgclosedusergroup
            
            	Closed User Group at which the peer will be called. If the Closed User Group is undefined for the given media or unused, this is a zero length string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: dialctlpeercfgfailuredelay
            
            	The time in seconds after which call attempts are to be placed again after a peer has been noticed to be unreachable, i.e. after dialCtlPeerCfgCallRetries unsuccessful call attempts. A value of zero means that a peer will not be called again after dialCtlPeerCfgCallRetries unsuccessful call attempts
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgiftype
            
            	The interface type to be used for calling this peer. In case of ISDN, the value of isdn(63) is to be used
            	**type**\: :py:class:`IANAifType_Enum <ydk.models.ianaiftype.IANAifType_MIB.IANAifType_Enum>`
            
            .. attribute:: dialctlpeercfginactivitytimer
            
            	The connection will be automatically disconnected if no longer carrying useful data for a time period, in seconds, specified in this object. Useful data in this context refers to forwarding packets, including routing information; it excludes the encapsulator maintenance frames. A value of zero means the connection will not be automatically taken down due to inactivity, which implies that it is a dedicated circuit
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfginfotype
            
            	The Information Transfer Capability to be used when calling this peer.  speech(2) refers to a non\-data connection, whereas audio31(6) and audio7(7) refer to data mode connections
            	**type**\: :py:class:`DialCtlPeerCfgInfoType_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.DialCtlPeerCfgTable.DialCtlPeerCfgEntry.DialCtlPeerCfgInfoType_Enum>`
            
            .. attribute:: dialctlpeercfglowerif
            
            	ifIndex value of an interface the peer will have to be called on. For example, on an ISDN interface, this can be the ifIndex value of a D channel or the ifIndex value of a B channel, whatever is appropriate for a given peer. As an example, for Basic Rate leased lines it will be necessary to specify a B channel ifIndex, while for     semi\-permanent connections the D channel ifIndex has to be specified. If the interface can be dynamically assigned, this object has a value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgmaxduration
            
            	Maximum call duration in seconds. Zero means 'unlimited'
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgminduration
            
            	Minimum duration of a call in seconds, starting from the time the call is connected until the call is disconnected. This is to accomplish the fact that in most countries charging applies to units of time, which should be matched as closely as possible
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgoriginateaddress
            
            	Call Address at which the peer will be called. Think of this as the set of characters following 'ATDT ' or the 'phone number' included in a D channel call request.  The structure of this information will be switch type specific. If there is no address information required for reaching the peer, i.e., for leased lines, this object will be a zero length string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: dialctlpeercfgpermission
            
            	Applicable permissions. callback(4) either rejects the call and then calls back, or uses the 'Reverse charging' information element if it is available. Note that callback(4) is supposed to control charging, not security, and applies to callback prior to accepting a call. Callback for security reasons can be handled using PPP callback
            	**type**\: :py:class:`DialCtlPeerCfgPermission_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.DialCtlPeerCfgTable.DialCtlPeerCfgEntry.DialCtlPeerCfgPermission_Enum>`
            
            .. attribute:: dialctlpeercfgretrydelay
            
            	The time in seconds between call retries if a peer cannot be reached. A value of zero means that call retries may be done without any delay
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgspeed
            
            	The desired information transfer speed in bits/second when calling this peer. The detailed media specific information, e.g. information type and information transfer rate for ISDN circuits, has to be extracted from this object. If the transfer speed to be used is unknown or the default speed for this type of interfaces, the value of this object may be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dialctlpeercfgstatus
            
            	Status of one row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: dialctlpeercfgsubaddress
            
            	Subaddress at which the peer will be called. If the subaddress is undefined for the given media or unused, this is a zero length string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: dialctlpeercfgtrapenable
            
            	This object indicates whether dialCtlPeerCallInformation and dialCtlPeerCallSetup traps should be generated for this peer
            	**type**\: :py:class:`DialCtlPeerCfgTrapEnable_Enum <ydk.models.dial.DIAL_CONTROL_MIB.DIALCONTROLMIB.DialCtlPeerCfgTable.DialCtlPeerCfgEntry.DialCtlPeerCfgTrapEnable_Enum>`
            
            .. attribute:: dialctlpeerstatsacceptcalls
            
            	Number of calls from this peer accepted since system startup
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatschargedunits
            
            	The total number of charging units applying to this peer since system startup. Only the charging units applying to the local interface, i.e. for originated calls or for calls with 'Reverse charging' being active, will be counted here
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatsconnecttime
            
            	Accumulated connect time to the peer since system startup. This is the total connect time, i.e. the connect time for outgoing calls plus the time for incoming calls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatsfailcalls
            
            	Number of failed call attempts to this peer since system startup
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatslastdisconnectcause
            
            	The encoded network cause value associated with the last call. This object will be updated whenever a call is started or cleared. The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. Some references for possible cause values are given below
            	**type**\: str
            
            	**range:** 0..4
            
            .. attribute:: dialctlpeerstatslastdisconnecttext
            
            	ASCII text describing the reason for the last call termination.  This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of dialCtlPeerStatsLastDisconnectCause.  This object will be updated whenever a call is started or cleared
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: dialctlpeerstatslastsetuptime
            
            	The value of sysUpTime when the last call to this peer was started. For ISDN media, this will be the time when the setup message was received from or sent to the network. This object will be updated whenever a call is started or cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatsrefusecalls
            
            	Number of calls from this peer refused since system startup
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dialctlpeerstatssuccesscalls
            
            	Number of completed calls to this peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'dial-control'
            _revision = '1996-09-23'

            def __init__(self):
                self.parent = None
                self.dialctlpeercfgid = None
                self.ifindex = None
                self.dialctlpeercfgansweraddress = None
                self.dialctlpeercfgcallretries = None
                self.dialctlpeercfgcarrierdelay = None
                self.dialctlpeercfgclosedusergroup = None
                self.dialctlpeercfgfailuredelay = None
                self.dialctlpeercfgiftype = None
                self.dialctlpeercfginactivitytimer = None
                self.dialctlpeercfginfotype = None
                self.dialctlpeercfglowerif = None
                self.dialctlpeercfgmaxduration = None
                self.dialctlpeercfgminduration = None
                self.dialctlpeercfgoriginateaddress = None
                self.dialctlpeercfgpermission = None
                self.dialctlpeercfgretrydelay = None
                self.dialctlpeercfgspeed = None
                self.dialctlpeercfgstatus = None
                self.dialctlpeercfgsubaddress = None
                self.dialctlpeercfgtrapenable = None
                self.dialctlpeerstatsacceptcalls = None
                self.dialctlpeerstatschargedunits = None
                self.dialctlpeerstatsconnecttime = None
                self.dialctlpeerstatsfailcalls = None
                self.dialctlpeerstatslastdisconnectcause = None
                self.dialctlpeerstatslastdisconnecttext = None
                self.dialctlpeerstatslastsetuptime = None
                self.dialctlpeerstatsrefusecalls = None
                self.dialctlpeerstatssuccesscalls = None

            class DialCtlPeerCfgInfoType_Enum(Enum):
                """
                DialCtlPeerCfgInfoType_Enum

                The Information Transfer Capability to be used when
                calling this peer.
                
                speech(2) refers to a non\-data connection, whereas
                audio31(6) and audio7(7) refer to data mode
                connections.

                """

                OTHER = 1

                SPEECH = 2

                UNRESTRICTEDDIGITAL = 3

                UNRESTRICTEDDIGITAL56 = 4

                RESTRICTEDDIGITAL = 5

                AUDIO31 = 6

                AUDIO7 = 7

                VIDEO = 8

                PACKETSWITCHED = 9

                FAX = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DIALCONTROLMIB.DialCtlPeerCfgTable.DialCtlPeerCfgEntry.DialCtlPeerCfgInfoType_Enum']


            class DialCtlPeerCfgPermission_Enum(Enum):
                """
                DialCtlPeerCfgPermission_Enum

                Applicable permissions. callback(4) either rejects the
                call and then calls back, or uses the 'Reverse charging'
                information element if it is available.
                Note that callback(4) is supposed to control charging, not
                security, and applies to callback prior to accepting a
                call. Callback for security reasons can be handled using
                PPP callback.

                """

                ORIGINATE = 1

                ANSWER = 2

                BOTH = 3

                CALLBACK = 4

                NONE = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DIALCONTROLMIB.DialCtlPeerCfgTable.DialCtlPeerCfgEntry.DialCtlPeerCfgPermission_Enum']


            class DialCtlPeerCfgTrapEnable_Enum(Enum):
                """
                DialCtlPeerCfgTrapEnable_Enum

                This object indicates whether dialCtlPeerCallInformation
                and dialCtlPeerCallSetup traps should be generated for
                this peer.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                    return meta._meta_table['DIALCONTROLMIB.DialCtlPeerCfgTable.DialCtlPeerCfgEntry.DialCtlPeerCfgTrapEnable_Enum']


            @property
            def _common_path(self):
                if self.dialctlpeercfgid is None:
                    raise YPYDataValidationError('Key property dialctlpeercfgid is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:dialCtlPeerCfgTable/DIAL-CONTROL-MIB:dialCtlPeerCfgEntry[DIAL-CONTROL-MIB:dialCtlPeerCfgId = ' + str(self.dialctlpeercfgid) + '][DIAL-CONTROL-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dialctlpeercfgid is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.dialctlpeercfgansweraddress is not None:
                    return True

                if self.dialctlpeercfgcallretries is not None:
                    return True

                if self.dialctlpeercfgcarrierdelay is not None:
                    return True

                if self.dialctlpeercfgclosedusergroup is not None:
                    return True

                if self.dialctlpeercfgfailuredelay is not None:
                    return True

                if self.dialctlpeercfgiftype is not None:
                    return True

                if self.dialctlpeercfginactivitytimer is not None:
                    return True

                if self.dialctlpeercfginfotype is not None:
                    return True

                if self.dialctlpeercfglowerif is not None:
                    return True

                if self.dialctlpeercfgmaxduration is not None:
                    return True

                if self.dialctlpeercfgminduration is not None:
                    return True

                if self.dialctlpeercfgoriginateaddress is not None:
                    return True

                if self.dialctlpeercfgpermission is not None:
                    return True

                if self.dialctlpeercfgretrydelay is not None:
                    return True

                if self.dialctlpeercfgspeed is not None:
                    return True

                if self.dialctlpeercfgstatus is not None:
                    return True

                if self.dialctlpeercfgsubaddress is not None:
                    return True

                if self.dialctlpeercfgtrapenable is not None:
                    return True

                if self.dialctlpeerstatsacceptcalls is not None:
                    return True

                if self.dialctlpeerstatschargedunits is not None:
                    return True

                if self.dialctlpeerstatsconnecttime is not None:
                    return True

                if self.dialctlpeerstatsfailcalls is not None:
                    return True

                if self.dialctlpeerstatslastdisconnectcause is not None:
                    return True

                if self.dialctlpeerstatslastdisconnecttext is not None:
                    return True

                if self.dialctlpeerstatslastsetuptime is not None:
                    return True

                if self.dialctlpeerstatsrefusecalls is not None:
                    return True

                if self.dialctlpeerstatssuccesscalls is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
                return meta._meta_table['DIALCONTROLMIB.DialCtlPeerCfgTable.DialCtlPeerCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB/DIAL-CONTROL-MIB:dialCtlPeerCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dialctlpeercfgentry is not None:
                for child_ref in self.dialctlpeercfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
            return meta._meta_table['DIALCONTROLMIB.DialCtlPeerCfgTable']['meta_info']

    @property
    def _common_path(self):

        return '/DIAL-CONTROL-MIB:DIAL-CONTROL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.callactivetable is not None and self.callactivetable._has_data():
            return True

        if self.callactivetable is not None and self.callactivetable.is_presence():
            return True

        if self.callhistory is not None and self.callhistory._has_data():
            return True

        if self.callhistory is not None and self.callhistory.is_presence():
            return True

        if self.callhistorytable is not None and self.callhistorytable._has_data():
            return True

        if self.callhistorytable is not None and self.callhistorytable.is_presence():
            return True

        if self.dialctlconfiguration is not None and self.dialctlconfiguration._has_data():
            return True

        if self.dialctlconfiguration is not None and self.dialctlconfiguration.is_presence():
            return True

        if self.dialctlpeercfgtable is not None and self.dialctlpeercfgtable._has_data():
            return True

        if self.dialctlpeercfgtable is not None and self.dialctlpeercfgtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.dial._meta import _DIAL_CONTROL_MIB as meta
        return meta._meta_table['DIALCONTROLMIB']['meta_info']

