# from django.utils.encoding import force_str
# from django_countries import force_str, force_str
# from rest_framework.metadata import SimpleMetadata
# from rest_framework.relations import ManyRelatedField, RelatedField


# # implementation from https://stackoverflow.com/a/50989115/12930482
# class ManyToManyMetaData(SimpleMetadata):

#     def get_field_info(self, field):
#         field_info = super(ManyToManyMetaData, self).get_field_info(field)
        
#         # adding choice for read_only fields
#         if (field_info.get('read_only') and
#             not isinstance(field, (RelatedField, ManyRelatedField)) and
#                 hasattr(field, 'choices')):
#             field_info['choices'] = [
#                 {
#                     'value': choice_value,
#                     'display_name': force_str(choice_name, strings_only=True)
#                 }
#                 for choice_value, choice_name in field.choices.items()
#             ]

#         if isinstance(field, (RelatedField, ManyRelatedField)):
#             field_info['type'] = 'choice'
#             field_info['choices'] = [
#                 {
#                     'value': choice_value,
#                     'display_name': force_str(choice_name, strings_only=True)
#                 }
#                 for choice_value, choice_name in field.get_choices().items()
#             ]
#         return field_info
