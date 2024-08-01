const kue = require('kue');

const queue = kue.createQueue();

const blackList = ['4153518780', '4153518781']

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if(blackList.includes(phoneNumber)) {
    const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
    return done(err);
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
