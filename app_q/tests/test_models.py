from django.test import TestCase

from app_q.models import EducationModule


class EducationModuleModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        EducationModule.objects.create(number=1,name='Oleg',content='Тестовый текст')

    def test_number(self):
        educate = EducationModule.objects.get(id=1)
        field_label =educate._meta.get_field('number').verbose_name
        self.assertEquals(field_label,'number')

    def test_name(self):
        educate = EducationModule.objects.get(id=1)
        field_label = educate._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        educate = EducationModule.objects.get(id=1)
        max_length = educate._meta.get_field('name').max_length
        self.assertEquals(max_length,255)

    def test_content(self):
        educate = EducationModule.objects.get(id=1)
        field_label = educate._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_object_name(self):
        educate = EducationModule.objects.get(id=1)
        expected = f'{educate.name}'
        self.assertEquals(expected,str(educate))

    def test_get_absolute_url(self):
        educate = EducationModule.objects.get(id=1)
        self.assertEquals(educate.get_absolute_url(),'/post/1/')
