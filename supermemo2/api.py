from datetime import date

from .model import SMTwo


def first_visit(quality, last_reivew=date.today()):
    smtwo = SMTwo()
    smtwo.calc(quality, 2.5, 1, 1, last_reivew)
    return smtwo


def modify(instance, new_quality=None, new_easiness=None, new_interval=None, new_repetitions=None, new_last_review=None):
    if not(new_quality is not None or new_easiness or new_interval or new_repetitions or new_last_review):
        message = "a new value is not provided for modification"
        raise ValueError(message)

    q, ez, inter, rep, ls = instance.quality, instance.prev.easiness, instance.prev.interval, instance.prev.repetitions, instance.last_review

    if new_quality is not None:
        q = new_quality

    if new_easiness:
        ez = new_easiness

    if new_interval:
        inter = new_interval

    if new_repetitions:
        rep = new_repetitions

    if new_last_review:
        ls = new_last_review

    instance.calc(q, ez, inter, rep, ls)
    return instance


def as_json(instance, **kwargs):
    return instance.json(**kwargs)
