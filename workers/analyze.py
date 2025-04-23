import asyncio
from bullmq import Job
from config.settings import settings
from config.s3 import s3_client
import uuid

async def analyze_video(job: Job, token=None):
    # fake job progress
    job_duration = 30
    total_steps = 10

    for i in range(total_steps + 1):
        await asyncio.sleep(job_duration / total_steps)
        
        progress = int((i / total_steps) * 100)
        await job.updateProgress(progress)
        print(f"Job progress: {progress}%")

print(uuid.uuid4());