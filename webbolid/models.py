from django.db import models


class Accesszone(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    gindex = models.IntegerField(db_column='GIndex', unique=True)
    config = models.IntegerField(db_column='Config', blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AccessZone'


class Acesspoint(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    computerid = models.IntegerField(db_column='ComputerID')
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)
    comment = models.CharField(db_column='Comment', max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    gindex = models.IntegerField(db_column='GIndex', unique=True)
    gtype = models.IntegerField(db_column='Gtype')
    inkeyid = models.IntegerField(db_column='InKeyID', blank=True, null=True)
    induration = models.IntegerField(db_column='InDuration', blank=True, null=True)
    incommand = models.IntegerField(db_column='InCommand', blank=True, null=True)
    outkeyid = models.IntegerField(db_column='OutKeyID', blank=True, null=True)
    outduration = models.IntegerField(db_column='OutDuration', blank=True, null=True)
    outcommand = models.IntegerField(db_column='OutCommand', blank=True, null=True)
    inkeyid2 = models.IntegerField(db_column='InKeyID2', blank=True, null=True)
    induration2 = models.IntegerField(db_column='InDuration2', blank=True, null=True)
    incommand2 = models.IntegerField(db_column='InCommand2', blank=True, null=True)
    outkeyid2 = models.IntegerField(db_column='OutKeyID2', blank=True, null=True)
    outduration2 = models.IntegerField(db_column='OutDuration2', blank=True, null=True)
    outcommand2 = models.IntegerField(db_column='OutCommand2', blank=True, null=True)
    config = models.IntegerField(db_column='Config', blank=True, null=True)
    indexzone1 = models.IntegerField(db_column='IndexZone1', blank=True, null=True)
    indexzone2 = models.IntegerField(db_column='IndexZone2', blank=True, null=True)
    indexzone3 = models.IntegerField(db_column='IndexZone3', blank=True, null=True)
    indexzone4 = models.IntegerField(db_column='IndexZone4', blank=True, null=True)
    worktimezone1 = models.IntegerField(db_column='WorkTimeZone1', blank=True, null=True)
    worktimezone2 = models.IntegerField(db_column='WorkTimeZone2', blank=True, null=True)
    worktimezone3 = models.IntegerField(db_column='WorkTimeZone3', blank=True, null=True)
    worktimezone4 = models.IntegerField(db_column='WorkTimeZone4', blank=True, null=True)
    mode = models.IntegerField(db_column='Mode', blank=True, null=True)
    weightterminalid = models.IntegerField(db_column='WeightTerminalID', blank=True,
                                           null=True)
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AcessPoint'


class Events(models.Model):
    event = models.IntegerField(db_column='Event', primary_key=True)
    charid = models.CharField(db_column='CharID', max_length=2, db_collation='Cyrillic_General_CI_AS', blank=True,
                              null=True)
    contents = models.CharField(db_column='Contents', max_length=60, db_collation='Cyrillic_General_CI_AS', blank=True,
                                null=True)
    comment = models.CharField(db_column='Comment', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    realevent = models.IntegerField(db_column='RealEvent', blank=True, null=True)
    state = models.IntegerField(db_column='State', blank=True, null=True)
    category = models.IntegerField(db_column='Category', blank=True, null=True)
    formatview = models.IntegerField(db_column='FormatView', blank=True, null=True)
    soundnumber = models.IntegerField(db_column='SoundNumber', blank=True, null=True)
    alarmlevel = models.IntegerField(db_column='AlarmLevel', blank=True, null=True)
    gpevent = models.IntegerField(db_column='GpEvent', blank=True, null=True)
    eventscategoryid = models.IntegerField(db_column='EventsCategoryID', blank=True,
                                           null=True)
    isalarm = models.IntegerField(db_column='IsAlarm', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Events'

    def __str__(self):
        return '{} {}'.format(self.event, self.contents)


class Groups(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    istemplate = models.IntegerField(db_column='isTemplate', blank=True, null=True)
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)
    flags2 = models.IntegerField(db_column='Flags2')

    class Meta:
        managed = False
        db_table = 'Groups'


class Pcompany(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100,
                            db_collation='Cyrillic_General_CI_AS')
    address = models.CharField(db_column='Address', max_length=150, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    phone = models.CharField(db_column='Phone', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True,
                             null=True)
    id_number_company = models.CharField(db_column='Id_Number_Company', max_length=50,
                                         db_collation='Cyrillic_General_CI_AS', blank=True,
                                         null=True)
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    isguest = models.IntegerField(db_column='IsGuest', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PCompany'

    def __str__(self):
        return '{}'.format(self.name)


class Pdivision(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=80,
                            db_collation='Cyrillic_General_CI_AS')
    description = models.CharField(db_column='Description', max_length=100, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)
    shedule = models.IntegerField(db_column='Shedule', blank=True, null=True)
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)
    number = models.IntegerField(db_column='Number', blank=True, null=True)
    pcompany_id = models.IntegerField(db_column='PCompany_ID', blank=True, null=True)
    id_number_division = models.CharField(db_column='ID_Number_Division', max_length=50,
                                          db_collation='Cyrillic_General_CI_AS', blank=True,
                                          null=True)
    id_owner_division = models.IntegerField(db_column='ID_Owner_Division', blank=True,
                                            null=True)
    patterns_id = models.IntegerField(db_column='Patterns_ID', blank=True, null=True)
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)

    class Meta:
        managed = False
        db_table = 'PDivision'


class Ppost(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=80,
                            db_collation='Cyrillic_General_CI_AS')
    number = models.IntegerField(db_column='Number', blank=True, null=True)
    statusmark = models.IntegerField(db_column='StatusMark', blank=True, null=True)
    company_id = models.IntegerField(db_column='Company_ID', blank=True, null=True)
    id_number_ppost = models.CharField(db_column='Id_Number_Ppost', max_length=50,
                                       db_collation='Cyrillic_General_CI_AS', blank=True,
                                       null=True)
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)

    class Meta:
        managed = False
        db_table = 'PPost'

    def __str__(self):
        return '{}'.format(self.name)


class Querylog(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    timeval = models.DateTimeField(db_column='TimeVal', blank=True, null=True)
    ip = models.CharField(db_column='IP', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True,
                          null=True)
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)
    operatorname = models.CharField(db_column='OperatorName', max_length=100, db_collation='Cyrillic_General_CI_AS',
                                    blank=True, null=True)
    programid = models.IntegerField(db_column='ProgramID', blank=True, null=True)
    query = models.CharField(db_column='Query', max_length=2000, blank=True, null=True)
    parameters = models.BinaryField(db_column='Parameters', blank=True, null=True)
    action = models.CharField(db_column='Action', max_length=10, db_collation='Cyrillic_General_CI_AS', blank=True,
                              null=True)
    tablename = models.CharField(db_column='TableName', max_length=30, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QueryLog'

    def __str__(self):
        return '{}'.format(self.query)


class Rslines(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    gindex = models.IntegerField(db_column='GIndex', unique=True)
    comportid = models.IntegerField(db_column='ComPortID')
    pkuid = models.IntegerField(db_column='PKUID')
    glineno = models.IntegerField(db_column='GLineNo')
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True,
                            null=True)
    devicetype = models.IntegerField(db_column='DeviceType', blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)
    broadcast = models.IntegerField(db_column='Broadcast', blank=True, null=True)
    deviceversion = models.IntegerField(db_column='DeviceVersion', blank=True, null=True)
    ipaddress = models.CharField(db_column='IPAddress', max_length=16, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True)
    macaddress = models.CharField(db_column='MACAddress', max_length=18, db_collation='Cyrillic_General_CI_AS',
                                  blank=True, null=True)
    gateway = models.CharField(db_column='GATEWAY', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    submask = models.CharField(db_column='SUBMASK', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True)
    port = models.IntegerField(db_column='Port', blank=True, null=True)
    usedhcp = models.IntegerField(db_column='UseDHCP', blank=True, null=True)
    idcontactname = models.CharField(db_column='IdContactName', max_length=15, db_collation='Cyrillic_General_CI_AS',
                                     blank=True, null=True)
    iddevice = models.IntegerField(db_column='IdDevice', blank=True, null=True)
    deviceinterface = models.IntegerField(db_column='DeviceInterface')
    indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True,
                                            null=True)
    devicetypebio = models.CharField(db_column='DeviceTypeBIO', max_length=8, db_collation='Cyrillic_General_CI_AS',
                                     blank=True, null=True)
    abonenttype = models.IntegerField(db_column='AbonentType', blank=True, null=True)
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                   blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RSLines'
        unique_together = (('comportid', 'pkuid', 'glineno'),)


class Plist(models.Model):
    name = models.CharField(db_column='Name', max_length=25,
                            db_collation='Cyrillic_General_CI_AS', verbose_name='Фамилия')
    firstname = models.CharField(db_column='FirstName', max_length=25,
                                 db_collation='Cyrillic_General_CI_AS', verbose_name='Имя')
    midname = models.CharField(db_column='MidName', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True,
                               null=True, verbose_name='Отчество')
    workphone = models.CharField(db_column='WorkPhone', max_length=25, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True, verbose_name='Дата выдачи')
    homephone = models.CharField(db_column='HomePhone', max_length=25, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True, verbose_name='Дата окончания')
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)
    company = models.ForeignKey(Pcompany, models.DO_NOTHING, db_column='Company', blank=True,
                                null=True, verbose_name='Компания')
    post = models.ForeignKey(Ppost, models.DO_NOTHING, db_column='Post', blank=True,
                             null=True, verbose_name='Должность')
    tabnumber = models.CharField(db_column='TabNumber', max_length=50, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True, verbose_name='Табельный номер')

    class Meta:
        managed = False
        db_table = 'pList'
        # ordering = ['name']

    # def __str__(self):
    #     return '{} {} {}'.format(self.name, self.firstname, self.midname)
    def __str__(self):
        return self.name + " " + self.firstname + " " + self.midname


class Plogdata(models.Model):
    timeval = models.DateTimeField(db_column='TimeVal', verbose_name='Время записи')
    event = models.ForeignKey(Events, models.DO_NOTHING, db_column='Event', db_index=True, verbose_name='Событие')
    hozorgan = models.ForeignKey(Plist, models.DO_NOTHING, db_column='HozOrgan', blank=True,
                                 null=True, db_index=True, verbose_name='Сотрудники')
    remark = models.CharField(db_column='Remark', max_length=65, db_collation='Cyrillic_General_CI_AS', blank=True,
                              null=True, db_index=True, verbose_name='Замечание')
    devicetime = models.DateField(db_column='DeviceTime', blank=True, null=True,
                                  db_index=True, verbose_name='Время устройства')
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)
    doorindex = models.ForeignKey(Acesspoint, models.DO_NOTHING, db_column='DoorIndex', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pLogData'
        # ordering = ['-devicetime']

    def __str__(self):
        return '{}'.format(self.devicetime)


class Pmark(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    # gtype = models.IntegerField(db_column='Gtype')
    # gtypecodeadd = models.IntegerField(db_column='GTypeCodeAdd', blank=True, null=True)
    # config = models.IntegerField(db_column='Config')
    codep = models.CharField(db_column='CodeP', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True,
                             null=True)
    codepadd = models.CharField(db_column='CodePAdd', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True,
                                null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    owner = models.ForeignKey(Plist, models.DO_NOTHING, db_column='Owner')
    ownername = models.CharField(db_column='OwnerName', max_length=30, db_collation='Cyrillic_General_CI_AS',
                                 blank=True, null=True)
    grstatus = models.IntegerField(db_column='GrStatus', blank=True, null=True)
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='GroupID')
    start = models.DateTimeField(db_column='Start', blank=True, null=True)
    finish = models.DateTimeField(db_column='Finish', blank=True, null=True)
    # fingertemplate = models.CharField(max_length=2500, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    # indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True,
    #                                         null=True)
    # comment = models.CharField(db_column='Comment', max_length=250, db_collation='Cyrillic_General_CI_AS', blank=True,
    #                            null=True)
    # login = models.CharField(db_column='Login', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True,
    #                          null=True)
    # operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)
    # workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS',
    #                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pMark'
