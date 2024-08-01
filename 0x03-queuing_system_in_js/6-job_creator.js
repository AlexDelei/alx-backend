const kue = require('kue');
const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
    phoneNumber: '01999467992',
    message: 'Hello there, welcome to my talk',
});

job
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on('completed', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });

job.save();
