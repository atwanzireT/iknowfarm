# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExGroupWorkers(models.Model):
    group = models.ForeignKey('ExGroups', models.DO_NOTHING)
    district = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    designation = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=100)
    operation_area = models.CharField(max_length=100)
    module = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'ex_group_workers'


class ExGroups(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ex_groups'


class FarmerDistrict(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_district'


class FarmerFarmer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=255)
    codesent = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()
    group = models.ForeignKey('FarmerFarmergroup', models.DO_NOTHING, blank=True, null=True)
    recommender = models.ForeignKey('FarmerRecomender', models.DO_NOTHING, blank=True, null=True)
    village = models.ForeignKey('FarmerVillage', models.DO_NOTHING, blank=True, null=True)
    farmer_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_farmer'


class FarmerFarmerfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_farmerfile'


class FarmerFarmergroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()
    village = models.ForeignKey('FarmerVillage', models.DO_NOTHING, blank=True, null=True)
    female_farmers = models.IntegerField()
    group_type = models.CharField(max_length=20)
    male_farmers = models.IntegerField()
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=10)
    recommender = models.ForeignKey('FarmerRecomender', models.DO_NOTHING, blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_farmergroup'


class FarmerRecomender(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()
    village = models.ForeignKey('FarmerVillage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_recomender'


class FarmerVillage(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()
    districtid = models.ForeignKey(FarmerDistrict, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'farmer_village'


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


class FeedbackFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    ratingtitle = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    audiofile = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    createdby = models.ForeignKey(FarmerFarmer, models.DO_NOTHING, db_column='createdby')

    class Meta:
        managed = False
        db_table = 'feedback_feedback'


class HomeCrop(models.Model):
    id = models.BigAutoField(primary_key=True)
    english = models.CharField(max_length=255, blank=True, null=True)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'home_crop'


class HomeLivestock(models.Model):
    id = models.BigAutoField(primary_key=True)
    english = models.CharField(max_length=255, blank=True, null=True)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'home_livestock'


class HomeUnregistreduser(models.Model):
    id = models.BigAutoField(primary_key=True)
    deviceid = models.CharField(max_length=255)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'home_unregistreduser'


class TranslationManual(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    english = models.TextField(blank=True, null=True)
    arabic = models.TextField(blank=True, null=True)
    lugbara = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()
    cropid = models.ForeignKey(HomeCrop, models.DO_NOTHING, blank=True, null=True)
    livestockid = models.ForeignKey(HomeLivestock, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    arabic_audio = models.CharField(max_length=100, blank=True, null=True)
    english_audio = models.CharField(max_length=100, blank=True, null=True)
    lugbara_audio = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'translation_manual'


class UploadVideo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    english = models.CharField(max_length=100, blank=True, null=True)
    arabic = models.CharField(max_length=100, blank=True, null=True)
    lugbara = models.CharField(max_length=100, blank=True, null=True)
    createdat = models.DateTimeField()
    updatedat = models.DateTimeField()
    cropid = models.ForeignKey(HomeCrop, models.DO_NOTHING)
    livestockid = models.ForeignKey(HomeLivestock, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_video'


class Villages(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    districtid = models.IntegerField(db_column='districtId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'villages'
