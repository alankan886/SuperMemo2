from datetime import date

from .model import SMTwo


def first_review(quality, last_reivew=date.today()):
    smtwo = SMTwo()
    smtwo.calc(quality, 2.5, 1, 1, last_reivew)
    return smtwo


def modify(instance, new_quality=None, new_easiness=None, new_interval=None, new_repetitions=None, new_review_date=None):
    if not(new_quality is not None or new_easiness or new_interval or new_repetitions or new_review_date):
        message = "a new value is not provided for modification"
        raise ValueError(message)

    q, ez, inter, rep, rd = instance.quality, instance.prev.easiness, instance.prev.interval, instance.prev.repetitions, instance.prev.review_date
    if new_quality is not None:
        q = new_quality

    if new_easiness:
        ez = new_easiness

    if new_interval:
        inter = new_interval

    if new_repetitions:
        rep = new_repetitions

    if new_review_date is not None:
        rd = new_review_date

    instance.calc(q, ez, inter, rep, rd)
    return instance


def as_json(instance, **kwargs):
    return instance.json(**kwargs)


def as_dict(instance, **kwargs):
    return instance.dict(**kwargs)
