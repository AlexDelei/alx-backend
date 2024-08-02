import { expect } from "chai";
import sinon from "sinon";
import { createQueue } from 'kue';
import createPushNotificationsJobs from "./8-job";

describe('test for job creation', () => {
  const spy = sinon.spy(console);
  const queue = createQueue({ name: 'push_notification_test' });

  before(() => {
    queue.testMode.enter(true);
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  afterEach(() => {
    spy.log.resetHistory();
  });

  it('display an error message if jobs is not an array', () => {
    expect(
        createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, queue)
    ).to.throw('Jobs is not an array');
  });

  it('adds job to the queue with the correct type', (done) => {
    expect(queue.testMode.jobs.length).to.equal(0);

    const testJobs = [
        {
            phoneNumber: '808139083231',
            message: 'Use the code 0012 to verify your account',
        },
        {
            phoneNumber: '891097830988',
            message: 'Use the code 6789 to verify your account',
        },
    ];

    createPushNotificationsJobs(testJobs, queue);
    expect(queue.testMode.jobs[0].data).to.deep.equal(testJobs[0]);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    queue.process('push_notification_code_3', () => {
        expect(
            spy.log.calledWith(`Notification job created: ${queue.testMode.jobs[0].id}`)
        ).to.be.true;
        done();
    });
  });

  it('registeres the progress event handler for a job', (done) => {
    queue.testMode.jobs[0].addListener('progress', () => {
        expect(
            spy.log.calledWith(`Notification job ${queue.testMode.jobs[0].id} 25% complete`)
        ).to.be.true;
        done();
    });
    queue.testMode.jobs[0].emit('progress', 25);
  });

  it('registers a failed event handler for a job', (done) => {
    queue.testMode.jobs[0].addListener('failed', (error) => {
      const actual = spy.log.getCalls().map(call => call.args[0]);
      const expectedMessage = `Notification job ${queue.testMode.jobs[0].id} failed: ${error.message}`;

      expect(actual).to.include(expectedMessage);
      done();
    });
    queue.testMode.jobs[0].emit('failed', new Error('Failed to send'));
  });

  it('registers the complete event handler', (done) => {
    queue.testMode.jobs[0].addListener('completed', () => {
        expect(
            spy.log.calledWith(`Notification job ${queue.testMode.jobs[0].id} completed`)
        ).to.be.true;
        done();
    });
    queue.testMode.jobs[0].emit('completed');
  });

});
