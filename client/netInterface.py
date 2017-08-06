import network
class CNetInterface:
    def Commit(self, packet):
       CNetWork().Send(self, packet)
    def OnReply(self, packet):
        raise NotImplementedError( "Should have implemented this" )

    
    
    
