from django.db import models


class WeatherMeasurement(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    remote_id = models.BigIntegerField(db_column='REMOTE_ID', blank=True, null=True)  # Field name made lowercase.
    ambient_temperature = models.DecimalField(db_column='AMBIENT_TEMPERATURE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    #ground_temperature = models.DecimalField(db_column='GROUND_TEMPERATURE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    #air_quality = models.DecimalField(db_column='AIR_QUALITY', max_digits=6, decimal_places=2)  # Field name made lowercase.
    air_pressure = models.DecimalField(db_column='AIR_PRESSURE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    humidity = models.DecimalField(db_column='HUMIDITY', max_digits=6, decimal_places=2)  # Field name made lowercase.
    wind_direction = models.DecimalField(db_column='WIND_DIRECTION', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wind_speed = models.DecimalField(db_column='WIND_SPEED', max_digits=6, decimal_places=2)  # Field name made lowercase.
    wind_gust_speed = models.DecimalField(db_column='WIND_GUST_SPEED', max_digits=6, decimal_places=2)  # Field name made lowercase.
    rainfall = models.DecimalField(db_column='RAIN_AMOUNT_IN', max_digits=6, decimal_places=2)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'WEATHER_MEASUREMENT'
