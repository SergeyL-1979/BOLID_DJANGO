from django.db import models


class Accesszone(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', unique=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccessZone'


class Acesspoint(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', unique=True)  # Field name made lowercase.
    gtype = models.IntegerField(db_column='Gtype')  # Field name made lowercase.
    inkeyid = models.IntegerField(db_column='InKeyID', blank=True, null=True)  # Field name made lowercase.
    induration = models.IntegerField(db_column='InDuration', blank=True, null=True)  # Field name made lowercase.
    incommand = models.IntegerField(db_column='InCommand', blank=True, null=True)  # Field name made lowercase.
    outkeyid = models.IntegerField(db_column='OutKeyID', blank=True, null=True)  # Field name made lowercase.
    outduration = models.IntegerField(db_column='OutDuration', blank=True, null=True)  # Field name made lowercase.
    outcommand = models.IntegerField(db_column='OutCommand', blank=True, null=True)  # Field name made lowercase.
    inkeyid2 = models.IntegerField(db_column='InKeyID2', blank=True, null=True)  # Field name made lowercase.
    induration2 = models.IntegerField(db_column='InDuration2', blank=True, null=True)  # Field name made lowercase.
    incommand2 = models.IntegerField(db_column='InCommand2', blank=True, null=True)  # Field name made lowercase.
    outkeyid2 = models.IntegerField(db_column='OutKeyID2', blank=True, null=True)  # Field name made lowercase.
    outduration2 = models.IntegerField(db_column='OutDuration2', blank=True, null=True)  # Field name made lowercase.
    outcommand2 = models.IntegerField(db_column='OutCommand2', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    indexzone1 = models.IntegerField(db_column='IndexZone1', blank=True, null=True)  # Field name made lowercase.
    indexzone2 = models.IntegerField(db_column='IndexZone2', blank=True, null=True)  # Field name made lowercase.
    indexzone3 = models.IntegerField(db_column='IndexZone3', blank=True, null=True)  # Field name made lowercase.
    indexzone4 = models.IntegerField(db_column='IndexZone4', blank=True, null=True)  # Field name made lowercase.
    worktimezone1 = models.IntegerField(db_column='WorkTimeZone1', blank=True, null=True)  # Field name made lowercase.
    worktimezone2 = models.IntegerField(db_column='WorkTimeZone2', blank=True, null=True)  # Field name made lowercase.
    worktimezone3 = models.IntegerField(db_column='WorkTimeZone3', blank=True, null=True)  # Field name made lowercase.
    worktimezone4 = models.IntegerField(db_column='WorkTimeZone4', blank=True, null=True)  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    weightterminalid = models.IntegerField(db_column='WeightTerminalID', blank=True,
                                           null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcessPoint'


class Events(models.Model):
    event = models.IntegerField(db_column='Event', primary_key=True)  # Field name made lowercase.
    charid = models.CharField(db_column='CharID', max_length=2, db_collation='Cyrillic_General_CI_AS', blank=True,
                              null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='Contents', max_length=60, db_collation='Cyrillic_General_CI_AS', blank=True,
                                null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    realevent = models.IntegerField(db_column='RealEvent', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    formatview = models.IntegerField(db_column='FormatView', blank=True, null=True)  # Field name made lowercase.
    soundnumber = models.IntegerField(db_column='SoundNumber', blank=True, null=True)  # Field name made lowercase.
    alarmlevel = models.IntegerField(db_column='AlarmLevel', blank=True, null=True)  # Field name made lowercase.
    gpevent = models.IntegerField(db_column='GpEvent', blank=True, null=True)  # Field name made lowercase.
    eventscategoryid = models.IntegerField(db_column='EventsCategoryID', blank=True,
                                           null=True)  # Field name made lowercase.
    isalarm = models.IntegerField(db_column='IsAlarm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'

    def __str__(self):
        return '{} {}'.format(self.event, self.contents)


class Groups(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    istemplate = models.IntegerField(db_column='isTemplate', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    flags2 = models.IntegerField(db_column='Flags2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Groups'


class Pcompany(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100,
                            db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True,
                             null=True)  # Field name made lowercase.
    id_number_company = models.CharField(db_column='Id_Number_Company', max_length=50,
                                         db_collation='Cyrillic_General_CI_AS', blank=True,
                                         null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    isguest = models.IntegerField(db_column='IsGuest', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PCompany'

    def __str__(self):
        return '{}'.format(self.name)


class Pdivision(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=80,
                            db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    shedule = models.IntegerField(db_column='Shedule', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    pcompany_id = models.IntegerField(db_column='PCompany_ID', blank=True, null=True)  # Field name made lowercase.
    id_number_division = models.CharField(db_column='ID_Number_Division', max_length=50,
                                          db_collation='Cyrillic_General_CI_AS', blank=True,
                                          null=True)  # Field name made lowercase.
    id_owner_division = models.IntegerField(db_column='ID_Owner_Division', blank=True,
                                            null=True)  # Field name made lowercase.
    patterns_id = models.IntegerField(db_column='Patterns_ID', blank=True, null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PDivision'


class Ppost(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=80,
                            db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    statusmark = models.IntegerField(db_column='StatusMark', blank=True, null=True)  # Field name made lowercase.
    company_id = models.IntegerField(db_column='Company_ID', blank=True, null=True)  # Field name made lowercase.
    id_number_ppost = models.CharField(db_column='Id_Number_Ppost', max_length=50,
                                       db_collation='Cyrillic_General_CI_AS', blank=True,
                                       null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PPost'

    def __str__(self):
        return '{}'.format(self.name)


class Querylog(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    timeval = models.DateTimeField(db_column='TimeVal', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True,
                          null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', max_length=100, db_collation='Cyrillic_General_CI_AS',
                                    blank=True, null=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(db_column='Query', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    parameters = models.BinaryField(db_column='Parameters', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, db_collation='Cyrillic_General_CI_AS', blank=True,
                              null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=30, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QueryLog'

    def __str__(self):
        return '{}'.format(self.query)


class Rslines(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', unique=True)  # Field name made lowercase.
    comportid = models.IntegerField(db_column='ComPortID')  # Field name made lowercase.
    pkuid = models.IntegerField(db_column='PKUID')  # Field name made lowercase.
    glineno = models.IntegerField(db_column='GLineNo')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='DeviceType', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    broadcast = models.IntegerField(db_column='Broadcast', blank=True, null=True)  # Field name made lowercase.
    deviceversion = models.IntegerField(db_column='DeviceVersion', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=16, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=18, db_collation='Cyrillic_General_CI_AS',
                                  blank=True, null=True)  # Field name made lowercase.
    gateway = models.CharField(db_column='GATEWAY', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    submask = models.CharField(db_column='SUBMASK', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    usedhcp = models.IntegerField(db_column='UseDHCP', blank=True, null=True)  # Field name made lowercase.
    idcontactname = models.CharField(db_column='IdContactName', max_length=15, db_collation='Cyrillic_General_CI_AS',
                                     blank=True, null=True)  # Field name made lowercase.
    iddevice = models.IntegerField(db_column='IdDevice', blank=True, null=True)  # Field name made lowercase.
    deviceinterface = models.IntegerField(db_column='DeviceInterface')  # Field name made lowercase.
    indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True,
                                            null=True)  # Field name made lowercase.
    devicetypebio = models.CharField(db_column='DeviceTypeBIO', max_length=8, db_collation='Cyrillic_General_CI_AS',
                                     blank=True, null=True)  # Field name made lowercase.
    abonenttype = models.IntegerField(db_column='AbonentType', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RSLines'
        unique_together = (('comportid', 'pkuid', 'glineno'),)


class Plist(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25,
                            db_collation='Cyrillic_General_CI_AS', verbose_name='Фамилия')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=25,
                                 db_collation='Cyrillic_General_CI_AS', verbose_name='Имя')  # Field name made lowercase.
    midname = models.CharField(db_column='MidName', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True, verbose_name='Отчество')  # Field name made lowercase.
    # status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=25, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True, verbose_name='Дата выдачи')  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=25, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True, verbose_name='Дата окончания')  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.

    # birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    # address = models.CharField(db_column='Address', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
    #                            null=True)  # Field name made lowercase.
    company = models.ForeignKey(Pcompany, models.DO_NOTHING, db_column='Company', blank=True,
                                null=True, verbose_name='Компания')  # Field name made lowercase.
    # section = models.IntegerField(db_column='Section', blank=True, null=True)  # Field name made lowercase.
    post = models.ForeignKey(Ppost, models.DO_NOTHING, db_column='Post', blank=True,
                             null=True, verbose_name='Должность')  # Field name made lowercase.
    # schedule = models.IntegerField(db_column='Schedule', blank=True, null=True)  # Field name made lowercase.
    # avto = models.CharField(db_column='Avto', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
    #                         null=True)  # Field name made lowercase.
    # spack = models.IntegerField(db_column='Spack', blank=True, null=True)  # Field name made lowercase.
    # config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    tabnumber = models.CharField(db_column='TabNumber', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True, verbose_name='Табельный номер')  # Field name made lowercase.
    # grstatus = models.IntegerField(db_column='GrStatus', blank=True, null=True)  # Field name made lowercase.
    # changetime = models.DateTimeField(db_column='ChangeTime', blank=True, null=True)  # Field name made lowercase.
    # indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True,
    #                                         null=True)  # Field name made lowercase.
    # statusrecord = models.IntegerField(db_column='StatusRecord', blank=True, null=True)  # Field name made lowercase.
    # patterns_id = models.IntegerField(db_column='Patterns_ID', blank=True, null=True)  # Field name made lowercase.
    # id_number_list = models.CharField(db_column='ID_Number_List', max_length=50, db_collation='Cyrillic_General_CI_AS',
    #                                   blank=True, null=True)  # Field name made lowercase.
    # weight = models.IntegerField(blank=True, null=True)
    # delta_weight = models.IntegerField(blank=True, null=True)
    # autoid = models.IntegerField(db_column='AutoID', blank=True, null=True)  # Field name made lowercase.
    # guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
    #                            null=True)  # Field name made lowercase.
    # status_list = models.IntegerField(blank=True, null=True)
    # emaillist = models.CharField(db_column='EmailList', max_length=200, db_collation='Cyrillic_General_CI_AS',
    #                              blank=True, null=True)  # Field name made lowercase.
    # fielddelete = models.IntegerField(blank=True, null=True)
    # blacklist = models.IntegerField(db_column='BlackList', blank=True, null=True)  # Field name made lowercase.
    # inn = models.CharField(db_column='INN', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
    #                        null=True)  # Field name made lowercase.
    # reasontoblacklist = models.CharField(db_column='ReasonToBlackList', max_length=200,
    #                                      db_collation='Cyrillic_General_CI_AS', blank=True,
    #                                      null=True)  # Field name made lowercase.
    # typedocum = models.IntegerField(db_column='TypeDocum', blank=True, null=True)  # Field name made lowercase.
    # sexguest = models.IntegerField(db_column='SexGuest', blank=True, null=True)  # Field name made lowercase.
    # dokumseries = models.CharField(db_column='DokumSeries', max_length=50, db_collation='Cyrillic_General_CI_AS',
    #                                blank=True, null=True)  # Field name made lowercase.
    # dokumnumber = models.CharField(db_column='DokumNumber', max_length=50, db_collation='Cyrillic_General_CI_AS',
    #                                blank=True, null=True)  # Field name made lowercase.
    # datedocument = models.DateTimeField(db_column='DateDocument', blank=True, null=True)  # Field name made lowercase.
    # kodpodr = models.CharField(db_column='KodPodr', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True,
    #                            null=True)  # Field name made lowercase.
    # kem = models.CharField(db_column='Kem', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
    #                        null=True)  # Field name made lowercase.
    # datedocumentend = models.DateTimeField(db_column='DateDocumentEnd', blank=True,
    #                                        null=True)  # Field name made lowercase.
    # birthplace = models.CharField(max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    # datetimeinarchive = models.DateTimeField(db_column='DateTimeInArchive', blank=True,
    #                                          null=True)  # Field name made lowercase.
    # firetolist = models.CharField(db_column='FireToList', max_length=200, db_collation='Cyrillic_General_CI_AS',
    #                               blank=True, null=True)  # Field name made lowercase.
    # idscan = models.IntegerField(db_column='IDSCAN', blank=True, null=True)  # Field name made lowercase.
    # idgroupexit = models.IntegerField(db_column='IDGROUPEXIT', blank=True, null=True)  # Field name made lowercase.
    # operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    # workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
    #                                blank=True, null=True)  # Field name made lowercase.
    # roomid = models.IntegerField(db_column='RoomID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pList'
        # ordering = ['name']

    # def __str__(self):
    #     return '{} {} {}'.format(self.name, self.firstname, self.midname)
    def __str__(self):
        return self.name + " " + self.firstname + " " + self.midname


class Plogdata(models.Model):
    timeval = models.DateTimeField(db_column='TimeVal')  # Field name made lowercase.
    numcom = models.IntegerField(db_column='NumCom', blank=True, null=True)  # Field name made lowercase.
    idcomp = models.IntegerField(db_column='IDComp', blank=True, null=True)  # Field name made lowercase.
    par1 = models.IntegerField(db_column='Par1', blank=True, null=True)  # Field name made lowercase.
    par2 = models.IntegerField(db_column='Par2', blank=True, null=True)  # Field name made lowercase.
    par3 = models.IntegerField(db_column='Par3', blank=True, null=True)  # Field name made lowercase.
    par4 = models.IntegerField(db_column='Par4', blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Events, models.DO_NOTHING, db_column='Event', db_index=True)  # Field name made lowercase.
    indexkey = models.IntegerField(db_column='IndexKey', blank=True, null=True)  # Field name made lowercase.
    razdindex = models.IntegerField(db_column='RazdIndex', blank=True, null=True)  # Field name made lowercase.
    hozorgan = models.ForeignKey(Plist, models.DO_NOTHING, db_column='HozOrgan', blank=True,
                                 null=True, db_index=True)  # Field name made lowercase.
    hozguest = models.IntegerField(db_column='HozGuest', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=65, db_collation='Cyrillic_General_CI_AS', blank=True,
                              null=True)  # Field name made lowercase.
    doorindex = models.IntegerField(db_column='DoorIndex', blank=True, null=True)  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    devicetime = models.DateField(db_column='DeviceTime', blank=True, null=True, db_index=True)  # Field name made lowercase.
    vevent = models.IntegerField(db_column='VEvent', blank=True, null=True)  # Field name made lowercase.
    zreserv = models.IntegerField(db_column='ZReserv', blank=True, null=True)  # Field name made lowercase.
    zoneindex = models.IntegerField(db_column='ZoneIndex', blank=True, null=True)  # Field name made lowercase.
    readerindex = models.IntegerField(db_column='ReaderIndex', blank=True, null=True)  # Field name made lowercase.
    sign = models.IntegerField(db_column='Sign', blank=True, null=True)  # Field name made lowercase.
    tprzdindex = models.IntegerField(db_column='tpRzdIndex', blank=True, null=True)  # Field name made lowercase.
    tppar4 = models.IntegerField(db_column='tpPar4', blank=True, null=True)  # Field name made lowercase.
    indexzone = models.IntegerField(db_column='IndexZone', blank=True, null=True)  # Field name made lowercase.
    tpindex = models.IntegerField(db_column='tpIndex', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)  # Field name made lowercase.
    idcomment = models.IntegerField(db_column='IdComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pLogData'
        # ordering = ['-devicetime']

    def __str__(self):
        return '{}'.format(self.devicetime)


class Pmark(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gtype = models.IntegerField(db_column='Gtype')  # Field name made lowercase.
    gtypecodeadd = models.IntegerField(db_column='GTypeCodeAdd', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config')  # Field name made lowercase.
    codep = models.CharField(db_column='CodeP', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True,
                             null=True)  # Field name made lowercase.
    codepadd = models.CharField(db_column='CodePAdd', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True,
                                null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', max_length=30, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    grstatus = models.IntegerField(db_column='GrStatus', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    finish = models.DateTimeField(db_column='Finish', blank=True, null=True)  # Field name made lowercase.
    fingertemplate = models.CharField(max_length=2500, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True,
                                            null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True,
                             null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pMark'
