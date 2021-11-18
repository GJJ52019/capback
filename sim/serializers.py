from rest_framework import serializers
from .models import Day

class DaySerializer(serializers.HyperlinkedModelSerializer):

    day_url = serializers.ModelSerializer.serializer_url_field(
        view_name='day_detail')
 
    class Meta:
        model = Day
        fields = ('id','day_number', 'oxygen', 'propane', 'copper_raw', 'copper_rings_raw', 'copper_tubing', 'berylium_raw', 'brass_raw', 'silver_solder', 'grinding_wheels', 'machine_tools', 'copper_first_op', 'copper_second_op',  'copper_third_op', 'copper_first_inspection', 'copper_second_inspection', 'copper_third_inspection', 'copper_first_op', 'copper_second_op', 'copper_third_op', 'copper_first_inspection', 'copper_second_inspection', 'copper_third_inspection', 'copper_prebrightdip', 'copper_postbrightdip', 'brass_first_op', 'brass_second_op', 'brass_prebrightdip', 'brass_postbrightdip', 'berylium_first_op', 'berylium_second_op', 'berylium_third_op', 'berylium_first_inspection', 'berylium_second_inspection', 'berylium_third_inspection', 'berylium_prebrightdip', 'berylium_postbrightdip', 'copper_rings_op', 'copper_rings_prebrightdip', 'copper_rings_postbrightdip', 'silver_solder_firstop', 'first_grinding_op', 'silver_solder_secondop', 'second_grinding', 'finish_machining_firstop', 'finish_maching_secondop', 'deburr', 'finishing','day_url')