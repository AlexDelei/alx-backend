function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }

  jobs.forEach(obj => {
    const job = queue.create('push_notification_code_3', {
        phoneNumber: obj.phoneNumber,
        message: obj.message,
    });

    job
      .on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      })
      .on('completed', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (error) => {
        console.log(`Notification job ${job.id} failed: ${error}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });

    job.save();
  });
}

export default createPushNotificationsJobs;
