from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField('Отчество', max_length=25, blank=True, null=True)

    number = models.CharField('Номер телефона', max_length=18, null=True)
    date_birth = models.DateField('Дата рождения', max_length=10, blank=True, null=True)

    organization = models.CharField('Организация', max_length=100, blank=True, null=True)
    department = models.TextField('Отдел', blank=True, null=True)


class source(models.Model):
    # our_city_db

    # ВСЕ ДАТЫ ТУТ
    #
    answer_action_date = models.DateField('Дата, указанная в категории действия последнего ответа', blank=True, null=True)
    answer_action_end_date = models.DateField('Дата завершения действия', blank=True, null=True)

    answer_created_at = models.DateField('Дата создания ответа', blank=True, null=True)
    answer_first_assign_date = models.DateField('Дата назначения ответственного', blank=True, null=True)

    answer_moderation_date = models.DateField('Дата поступления ответа на модерацию (последняя)', blank=True, null=True)
    answer_moderation_date_end = models.DateField('Дата завершения модерации ответа (последняя)', blank=True, null=True)

    answer_published_at = models.DateField('Дата публикации ответа', blank=True, null=True)
    old_deadline_changed = models.DateField('Дата первоначального регламентного срока', blank=True, null=True)

    comment_created_date = models.DateField('Дата создания сообщения', blank=True, null=True)
    comment_publish_date = models.DateField('Дата публикации сообщения', blank=True, null=True)

    answer_first_assign_date = models.DateField('Дата назначения ответственного', blank=True, null=True)
    first_assign_date = models.DateField('Дата первого назначения ответственного по сообщению', blank=True, null=True)

    comment_moderation_date = models.DateField('Дата поступления сообщения на модерацию (последняя)', blank=True, null=True)
    comment_moderation_date_end = models.DateField('Дата завершения модерации сообщения (последняя)', blank=True, null=True)

    # ОПРОВЕРЖЕНИЕ
    disprove_comment_publish_date = models.DateField('Дата публикации сообщения-опровержения', blank=True, null=True)

    max_ko_published_at = models.DateField('Дата публикации  ответа КО', blank=True, null=True)
    min_answer_published_at = models.DateField('Дата публикации первичного ответа', blank=True, null=True)

    rec_updated_at = models.DateField('Дата пересчета сообщения в аналитике', blank=True, null=True)
    referee_assign = models.DateField('Дата поступления сообщения в кабинет арбитра', blank=True, null=True)

    # USER DATE
    user_created_at = models.DateField('Дата регистрации пользователя', blank=True, null=True)

    issue_published_at = models.DateField('Дата публикации заявки', blank=True, null=True)

    #
    # Все номера тут
    #
    answer_group_id = models.IntegerField("Номер группы ответа", null=True, blank=True)
    answer_id = models.IntegerField("Номер ответа", null=True, blank=True)

    answer_serial_number = models.IntegerField("Порядковый номер опубликованного ответа", null=True, blank=True)
    second_comment_serial = models.IntegerField("Порядковый номер повторного сообщения", null=True, blank=True)

    initial_comment_id = models.IntegerField("Номер исходного сообщения", null=True, blank=True)
    similar_comment_id = models.IntegerField("Номер основного сообщения", null=True, blank=True)

    comment_id = models.IntegerField("Номер сообщения", null=True, blank=True)
    comment_id_denials = models.IntegerField("Номер сообщения-опровержения", null=True, blank=True)

    ref_issue_id = models.IntegerField("Номер заявки", null=True, blank=True)

    similar_ids = models.TextField("Номера похожих сообщений", null=True, blank=True)

    #
    # Ответственный и все что связано
    #
