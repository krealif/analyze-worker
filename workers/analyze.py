import asyncio
from bullmq import Job
from config.settings import settings
from config.s3 import s3_client
import uuid

async def analyze_video(job: Job, token=None):
    print(f"Processing: {job.name}")
    total_steps = 10

    for i in range(total_steps + 1):
        await asyncio.sleep(5) # Sleep for 5 seconds
        
        progress = int((i / total_steps) * 100)
        await job.updateProgress(progress)
        print(f"Job progress: {progress}%")
        
    print(f"Job {job.name} completed.")

print(uuid.uuid4());
