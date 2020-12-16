import django_tables2 as tables

from places.models.place import Place


class PlaceTable(tables.Table):
    icon = tables.TemplateColumn('<a href="{% url "place details" record.id %}"><i class="fas fa-procedures {{ record.status }}"></i></a>',
                                 verbose_name="Place", orderable=False)
    # city = tables.TemplateColumn(
    #     '<a href="{% url "city details" record.establishment.city.id %}"><i class="fas fa-city"></i>{{ record.establishment.city.name}}</a>',
    #     verbose_name="City", orderable=False)

    class Meta:
        model = Place
        template_name = 'django_tables2/bootstrap4.html'
        sequence = ('icon', 'status', 'room_number', 'floor_number', 'establishment', 'city')
        exclude = ('id',)
