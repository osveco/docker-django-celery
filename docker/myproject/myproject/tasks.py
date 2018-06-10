from functools import wraps

from myproject.celeryconf import app
from .models import Job


def update_job(fn):
    @wraps(fn)
    def wrapper(job_id, *args, **kwargs):
        job = Job.objects.get(id=job_id)
        job.status = 'started'
        job.save()
        try:
            result = fn(*args, **kwargs)
            job.result = result
            job.status = 'finished'
            job.save()
        except:
            job.result = None
            job.status = 'failed'
            job.save()
    return wrapper

@app.task
@update_job
def analyze(n):
    return n**2

@app.task
@update_job
def enhance(n):
    return 0

TASK_MAPPING = {
    'analyze': analyze,
    'enhance': enhance
}
