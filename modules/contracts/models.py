import uuid

from django.db import models

from modules.agents.models import Agent, Face
from modules.products.models import Product, Risk


class Contract(models.Model):
    """
    Модель страхового договора.
    """

    CHOICE_STATUS = [
        ('DRAFT', 'Проект'),
        ('SIGNED', 'Подписан'),
        ('TERMINATED', 'Расторгнут')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name='Агент')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    policy_holder = models.ForeignKey(Face, on_delete=models.CASCADE, related_name='policy_holder_contracts',
                                      verbose_name='Код страхователя')
    insured_person = models.ForeignKey(Face, on_delete=models.CASCADE, related_name='insured_person_contracts',
                                       verbose_name='Код застрахованного лица')
    owner = models.ForeignKey(Face, on_delete=models.CASCADE, related_name='owner_contracts',
                              verbose_name='Код собственника')
    status = models.CharField(max_length=255, choices=CHOICE_STATUS, default='DRAFT', blank=False,
                              verbose_name='Статус договора страхования')
    date_create = models.DateTimeField(blank=False, verbose_name='Дата создания договора')
    date_signet = models.DateTimeField(blank=True, null=True, verbose_name='Дата подписания договора')
    date_begin = models.DateTimeField(blank=True, null=True, verbose_name='Дата начала ответственности')
    date_end = models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания ответственности')
    premium = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Страховая премия')
    insurance_sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Страховая сумма')
    rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Страховая премия')
    commission = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Страховая премия')

    class Meta:
        verbose_name = 'Страховой договор'
        verbose_name_plural = 'Страховые договоры'

    def __str__(self):
        return self.product


class ContractRisk(models.Model):
    """
    Модель рисков по договорам.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Договора страхования')
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, verbose_name='Страховые риски')
    premium = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Страховая премия')
    insurance_sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Страховая сумма')

    class Meta:
        verbose_name = 'Риск по договору'
        verbose_name_plural = 'Рисков по договорам'

    def __str__(self):
        return f'{self.contract} - {self.risk}'
