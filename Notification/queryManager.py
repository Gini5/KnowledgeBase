class Query:
    def __init__(self,frequency=-600):
        self.frequency = frequency

    def genQuery(self,alias):
        """ 
        :type alias: List[str]
        rtype: str
        format email body
        """
        query = """select br.Name as Branch, '<a href=''http://iclqa.intel.com/runboard/Home/Report/' +STR(tr.id)+'''>'+STR(tr.id)+'</a>' as RequestID, td.AliasName,trst.Name as Status, bc.Name as BuildName, CONVERT(varchar(100), bu.DateStamp, 112) as BuildDate, bs.name as BuildStatus, CONVERT(VARCHAR(20), tr.DateCreated, 
        120) as CreatedDate, CONVERT(VARCHAR(20), tr.ExpectedFinishDate, 120) as ExpectedFinishDate,'<a href=''http://iclqa.intel.com/runboard/Home/_Alloy_Info?alloyid='+tt.AlloyId+'''>'+tt.AlloyId+'</a>' as AlloyID,tr.TestingHostid as Host, tt.Scratch
        from testingrun.TestingRequest tr
        join testingrun.TestingDescription td on td.id = tr.TestingDescriptionId
        join config.Branch br on br.id = td.BranchId
        join config.TestingConfig tc on tc.id = td.TestingConfigId
        join builds.Build bu on bu.Id = tr.BuildId
        join config.BuildConfig bc on bc.id = tc.BuildConfigId
        join builds.BuildStatus bs on bs.id = bu.BuildStatusId
        join testingrun.TestingRequestStateType trst on trst.Id = tr.StateId
        left join testingrun.TestingTask tt on tt.TestingRequestId = tr.id
        where 
        tr.ExpectedFinishDate < GETDATE() and CONVERT(VARCHAR(20), tr.ExpectedFinishDate, 120) >= DATEADD(MI,{frequency},GETDATE())
        and tr.StateId <> 'FDOK'
        and td.aliasname in ({aliasList}) 
        group by tr.id, td.AliasName,trst.Name, br.Name, bc.Name, bu.DateStamp, tr.DateCreated,ExpectedFinishDate, AlloyId, bs.name, tr.testinghostid, tt.Scratch
        order by Branch, ExpectedFinishDate"""
        query = query.format(frequency=self.frequency,aliasList=alias)
        return query