from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import BaseModel, UserProfile, TeamMember, Customer

class CallCategory(BaseModel):
    name = models.CharField(
        verbose_name = "Nom",
        max_length = 200,
        )
    urgent_level = models.PositiveSmallIntegerField(
        verbose_name = "Niveau d'urgence",
        help_text = "Entre 0 (bas niveau d'urgence) et 10 (urgence critique)",
        default=3,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )

    def __str__(self):
        return "%s(%d)" % (self.name, self.urgent_level)

    class Meta:
        verbose_name = "Catégorie d'appel"
        verbose_name_plural = "Catégories d'appels"

class CallTag(BaseModel):
    name = models.CharField(
        verbose_name = "Nom",
        max_length = 100,
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag d'appel"
        verbose_name_plural = "Tags d'appels"

class Call(BaseModel):

    title = models.CharField(
        verbose_name="Titre",
        max_length=200,
        )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        verbose_name = "Client",
        db_index=True,
        null=True,
        blank=True,
        default=None,
        )

    teammember = models.ForeignKey(
        "users.TeamMember",
        on_delete=models.SET_NULL,
        verbose_name = "Membre d'équipe",
        db_index=True,
        null=True,
        blank=True,
        default=None,
        )

    tags = models.ManyToManyField(
        "CallTag",
        verbose_name="Tags",
        )

    content = models.TextField(
        verbose_name="Contenu de l'appel",
        )

    solved = models.BooleanField(
        verbose_name = "Résolu",
        default=False,
        db_index=True,
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Appel"
        verbose_name_plural = "Appels"
