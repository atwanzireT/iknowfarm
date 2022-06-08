# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActiveDevices(models.Model):
    deviceid = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    farmerid = models.ForeignKey('Farmers', models.DO_NOTHING, db_column='farmerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active_devices'


class AgroinputDealers(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    services = models.TextField(blank=True, null=True)
    products = models.TextField(blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    farmerid = models.ForeignKey('Farmers', models.DO_NOTHING, db_column='farmerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agroinput_dealers'


class Audios(models.Model):
    title = models.CharField(max_length=255)
    english = models.CharField(max_length=255)
    arabic = models.IntegerField(blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'audios'


class Contacts(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    subcounty = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contacts'


class CropManuals(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    cropid = models.OneToOneField('Crops', models.DO_NOTHING, db_column='cropId', primary_key=True)  # Field name made lowercase.
    manualid = models.ForeignKey('Manual', models.DO_NOTHING, db_column='manualId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crop_manuals'
        unique_together = (('cropid', 'manualid'),)


class Crops(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crops'


class Districts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'districts'


class Farmers(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    pin = models.CharField(max_length=255)
    grouptype = models.CharField(max_length=255, blank=True, null=True)
    registrationtype = models.IntegerField(blank=True, null=True)
    femalefarmers = models.CharField(max_length=255, blank=True, null=True)
    malefarmers = models.CharField(max_length=255, blank=True, null=True)
    codesent = models.IntegerField(blank=True, null=True)
    sponsor = models.CharField(max_length=255, blank=True, null=True)
    farmertype = models.CharField(max_length=255, blank=True, null=True)
    village = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    status = models.IntegerField()
    expiry = models.DateTimeField()
    recommender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmers'


class Feedback(models.Model):
    rating = models.CharField(max_length=255, blank=True, null=True)
    ratingtitle = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    audiofile = models.CharField(max_length=255, blank=True, null=True)
    createdby = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'


class Generalvideos(models.Model):
    title = models.CharField(max_length=255)
    english = models.CharField(max_length=255)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'generalvideos'


class GroupCodes(models.Model):
    code = models.CharField(max_length=255)
    limit = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group_codes'


class Livestock(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'livestock'


class LivestockManuals(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    livestockid = models.OneToOneField(Livestock, models.DO_NOTHING, db_column='livestockId', primary_key=True)  # Field name made lowercase.
    manualid = models.ForeignKey('Manual', models.DO_NOTHING, db_column='manualId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'livestock_manuals'
        unique_together = (('livestockid', 'manualid'),)


class Manual(models.Model):
    description = models.TextField(blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    audio = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manual'


class MarketPrices(models.Model):
    commodity = models.CharField(max_length=255, blank=True, null=True)
    variety = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    retailprice = models.CharField(max_length=255, blank=True, null=True)
    wholesaleprice = models.CharField(max_length=255, blank=True, null=True)
    market = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'market_prices'


class MarketVisits(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    deviceid = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'market_visits'


class ModuleViews(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    deviceid = models.CharField(max_length=255, blank=True, null=True)
    cropid = models.CharField(db_column='cropId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    livestockid = models.CharField(db_column='livestockId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'module_views'


class ProductSale(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    variety = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    unitprice = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    farmerid = models.ForeignKey(Farmers, models.DO_NOTHING, db_column='farmerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_sale'


class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'


class Sequelizemeta(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'sequelizemeta'


class Translations(models.Model):
    type = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    english = models.TextField(blank=True, null=True)
    arabic = models.TextField(blank=True, null=True)
    lugbara = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'translations'


class UnregistredUsers(models.Model):
    deviceid = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unregistred_users'


class UserRoles(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    roleid = models.OneToOneField(Roles, models.DO_NOTHING, db_column='roleId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_roles'
        unique_together = (('roleid', 'userid'),)


class Users(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class Videos(models.Model):
    title = models.CharField(max_length=255)
    english = models.CharField(max_length=255)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    cropid = models.ForeignKey(Crops, models.DO_NOTHING, db_column='cropId', blank=True, null=True)  # Field name made lowercase.
    livestockid = models.ForeignKey(Livestock, models.DO_NOTHING, db_column='livestockId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'videos'


class Villages(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    districtid = models.ForeignKey(Districts, models.DO_NOTHING, db_column='districtId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'villages'
