from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    title = models.CharField("Название", max_length=255)
    image = FilerImageField(
        verbose_name="Картинка",
        on_delete=models.PROTECT,
        related_name="slider_images",
    )
    is_active = models.BooleanField("Активно", default=True)
    order = models.PositiveIntegerField("Порядок", default=0, db_index=True)

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ["order"]

    def __str__(self) -> str:
        return self.title