from rest_framework import serializers
from .models import Vaga


class VagaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vaga
        fields = ('titulo', 'atividades', 'requisitos', 'destaques')


    def to_representation(self, data):
        ret = super(VagaSerializer, self).to_internal_value(data)
        if ret['atividades']:
            ret['atividades'] = ret['atividades'].split(';')
        if ret['requisitos']:
            ret['requisitos'] = ret['requisitos'].split(';')
        if ret['destaques']:
            ret['destaques'] = ret['destaques'].split(';')

        return ret
