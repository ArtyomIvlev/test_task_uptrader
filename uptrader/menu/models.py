from django.db import models
from django.urls import reverse
from django.http import Http404


class Menu (models.Model):

    name = models.CharField(verbose_name='Название меню',
                            max_length=25)
    top_menu = models.ForeignKey('self',
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    url = models.CharField(verbose_name='Ссылка',
                           max_length=256,
                           blank=True,
                           null=True,
                           unique=True)
    named_url = models.CharField(verbose_name='Имя ссылки',
                                 max_length=50,
                                 blank=True,
                                 null=True,
                                 unique=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Проверка имени ссылки и ссылки перед сохранением."""
        if self.named_url:
            named_url_parts = self.named_url.split()
            url_name = named_url_parts[0]
            params = named_url_parts[1:len(named_url_parts)]
            reversed_name_url = reverse(url_name, params)
            if self.url:
                if self.url != reversed_name_url:
                    raise Http404('ccылка не совпадает с именем ссылки')
            else:
                self.url = reversed_name_url
        super(Menu, self).save()

    def __str__(self):
        return self.name

    # def children(self):
    #     return self.
    #
    # def get_elder_ids(self):
    #     if self.parents

    class Meta:

        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ('-id',)
